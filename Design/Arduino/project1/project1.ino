#include "EspMQTTClient.h"
#include "DHTesp.h"
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>


// GPIO Pin mapping 부분, nodemcu와 아두이노 간 pin이 달라서 초기 설정 필요
#define D0 16 // LED
#define D3 0  // 온습도센서 연결핀
#define D1 5 // Relay 
#define D4 2 // USBLED
#define D5 14
#define D6 12
#define D7 13
#define D8 15


#define LED_PIN D0
#define DHT_PIN D3
#define USBLED_PIN D4
#define CDS_PIN A0

// Sensors and Actuators
#define DHTTYPE DHT22
#define LED_ON HIGH
#define LED_OFF LOW
#define RELAY_ON LOW
#define RELAY_OFF HIGH

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels

#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define LOGO_HEIGHT   16
#define LOGO_WIDTH    16
static const unsigned char PROGMEM logo_bmp[] =
{ 0b00000000, 0b11000000,
  0b00000001, 0b11000000,
  0b00000001, 0b11000000,
  0b00000011, 0b11100000,
  0b11110011, 0b11100000,
  0b11111110, 0b11111000,
  0b01111110, 0b11111111,
  0b00110011, 0b10011111,
  0b00011111, 0b11111100,
  0b00001101, 0b01110000,
  0b00011011, 0b10100000,
  0b00111111, 0b11100000,
  0b00111111, 0b11110000,
  0b01111100, 0b11110000,
  0b01110000, 0b01110000,
  0b00000000, 0b00110000 };

// MQTT topics to be subscribed and messages to be handled
// iot/[id]/{led, dht22, cds}
const char *mqtt_topic = "iot/21800677";

DHTesp dht;
int lightValue;
float temperature, humidity;
// String msgString;
char pub_data[200];


// nonblocking procedure
unsigned long previousMillis_sensor = 0;
unsigned long previousMillis_publish = 0;
unsigned long light_Timer = 0;
const long interval_OneSecond = 1000;
const long interval_TenSecond = 10000;

int led_state, usbled_state;

bool dark_flag = false;
bool bright_flag = false;

//Wifi
const char *WifiSSID = "*****"; // wifi SSID 및 password 변경 필요
const char *WifiPassword = "******";


// MQTT
#define mqtt_broker "sweetdream.iptime.org"
#define mqtt_clientname "21800677"
#define MQTTUsername "iot"
#define MQTTPassword "********"

EspMQTTClient mqtt_client(
  WifiSSID,
  WifiPassword,
  mqtt_broker,
  MQTTUsername,
  MQTTPassword,
  mqtt_clientname,
  1883
);

void setup() {
  Serial.begin(115200);
  Serial.println("serial port baud rate: 115200");
  
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LED_OFF); // LED off

  pinMode(USBLED_PIN, OUTPUT);
  digitalWrite(USBLED_PIN, RELAY_OFF); // USBLED off

  dht.setup(DHT_PIN, DHTesp::DHT22);
  
  // OLED
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }
  // Show initial display buffer contents on the screen --
  // the library initializes this with an Adafruit splash screen.
  display.display();
  delay(2000); // Pause for 2 seconds

  // Clear the buffer
  display.clearDisplay();
}

void onConnectionEstablished() {
  // Subscribe to "iot/21800677" and display received message to Serial
  mqtt_client.subscribe("iot/21800677", [](const String &payload) {
    Serial.println(payload);
    
    if (payload == "led") {
      // LED 토글 로직
      led_state = !led_state;
      digitalWrite(LED_PIN, led_state);
      Serial.println("Switching LED");
    } else if (payload == "ledon") {
      // LED on 로직
      led_state = LED_ON;
      digitalWrite(LED_PIN, led_state);
      Serial.println("Switching LED");
    } else if (payload == "ledoff") {
      // LED off 로직
      led_state = LED_OFF;
      digitalWrite(LED_PIN, led_state);
      Serial.println("Switching LED");
    } 
    
    else if (payload == "usbled") {
      // LED 토글 로직
      if (!bright_flag || !dark_flag) {  // event 동작상태에서는 toggle 작동 x
        usbled_state = !usbled_state;
        if(usbled_state == RELAY_ON) {
          bright_flag = false;
        }
        digitalWrite(USBLED_PIN, usbled_state);
        Serial.println("Switching USBLED");
      }
    } else if (payload == "usbledon") {
      // LED on 로직
      usbled_state = RELAY_ON;
      digitalWrite(USBLED_PIN, usbled_state);
      Serial.println("Switching USBLED");
    } else if (payload == "usbledoff") {
      // LED off 로직
      //off 버튼이 눌려지면 강제로 off, 이후 이벤트 발생하면 이벤트 동작
      bright_flag = false; // 이벤트 확인 플레그들 초기화
      dark_flag = false;
      usbled_state = RELAY_OFF;
      digitalWrite(USBLED_PIN, usbled_state);
      Serial.println("Switching USBLED");
    }
  });

  // Publish a message to mqtt_topic
  mqtt_client.publish(mqtt_topic, "This is a message frome NodeMCU when mqtt is publish");
}


void loop() {
  mqtt_client.loop();
  unsigned long currentMillis = millis(); 
  
  //Sensing temperature and humidity every second for stable data
  if (currentMillis - previousMillis_sensor >= interval_OneSecond) {
    previousMillis_sensor = currentMillis;
    lightValue = analogRead(CDS_PIN);
    Serial.print("lightValue: ");
    Serial.println(lightValue);

    // read temperature and humidity
    float tmp_temperature = dht.getTemperature();
    float tmp_humidity = dht.getHumidity();
  
    // print temperature and humidity to serial monitor
    if ( !isnan(tmp_humidity) && !isnan(tmp_temperature) ) {
      Serial.print("Temperature = ");
      Serial.print(temperature);
      Serial.print(" Humidity = ");
      Serial.println(humidity);
      humidity = tmp_humidity;
      temperature = tmp_temperature;

      OLED_Print_text(humidity, temperature, lightValue);
    }

    // USBLED turn on 상태일 때는 밝아진 상태에서 어두워져도 USBLED 상태에 영향을 주지 않음
    if (usbled_state == RELAY_ON) {
      // USBLED turn on 상태이면 밝아짐 확인 플래그와 어두워짐 확인 플래그 모두 초기화
      dark_flag = false;
      bright_flag = false;
    }
    else {
      // 밝은 상태에서 어두워지는 이벤트 발생 여부 확인
      if (dark_flag && bright_flag) {

        // 10초 경과
        if (currentMillis - light_Timer >= 10000) {
          digitalWrite(USBLED_PIN, RELAY_OFF);
          dark_flag = false;
          bright_flag = false;
        } 
      } 
      else {
        if (lightValue < 500 && bright_flag) { // 밝은 상태에서 어두워지는 이벤트 발생
          digitalWrite(USBLED_PIN, RELAY_ON);
          light_Timer = currentMillis;
          dark_flag = true;
        } else if (lightValue > 600) { // 밝아지는 이벤트 발생
          bright_flag = true;
        }
      }  
    }
  }

  //Publish every 10 second
  if (currentMillis - previousMillis_publish >= interval_TenSecond) {
    previousMillis_publish = currentMillis;
    
    sprintf(pub_data, "{\"temperature\" : %3.2f, \"humidity\" : %3.2f}", temperature, humidity);
    Serial.println(pub_data);
    mqtt_client.publish("iot/21800677/dht22", pub_data);
    sprintf(pub_data, "%3.2f", temperature);
    mqtt_client.publish("iot/21800677/dht22_t", pub_data);
    sprintf(pub_data, "%3.2f", humidity);
    mqtt_client.publish("iot/21800677/dht22_h", pub_data);
  
    sprintf(pub_data, "%d", lightValue);
    mqtt_client.publish("iot/21800677/cds", pub_data);
  }
}

void OLED_Print_text(float humidity, float temperature, float light_value) {
  display.clearDisplay();

  display.setTextSize(2); // Draw 1.5X-scale text
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.print(F("T: "));
  display.print(temperature);
  display.drawCircle(display.width()/4*3+6, 3, 3, SSD1306_WHITE);
  display.println(F(" C"));
  display.print(F("H: "));
  display.print(humidity);
  display.println(F("%"));
  display.display();      // Show initial text
  delay(100);
}
