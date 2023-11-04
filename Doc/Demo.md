# DEMO.MD

이 문서는 노드MCU를 이용해 IoT 시스템을 구축하는 방법에 대해 설명합니다. 이 프로젝트에서는 온도, 습도, 빛 센서를 이용하며, LED와 USB LED를 제어하는 기능을 포함하고 있습니다.

## 필요한 장비
- 노드MCU
- DHT22 온도 및 습도 센서
- 빛 센서
- LED
- USB LED
- 릴레이 모듈

## 코드 설명

### 라이브러리 및 전역 변수 설정

```c
#include "EspMQTTClient.h"
#include "DHTesp.h"
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
```

위 코드는 이 프로젝트에서 필요한 라이브러리를 불러오는 부분입니다. MQTT 클라이언트, DHT 센서, SPI, I2C, 그래픽 라이브러리, OLED 디스플레이 라이브러리를 사용합니다.

```c
#define D0 16 // LED
#define D3 0  // 온습도센서 연결핀
#define D1 5 // Relay 
#define D4 2 // USBLED
#define D5 14
#define D6 12
#define D7 13
#define D8 15
```

노드MCU의 GPIO 핀을 설정하는 부분입니다. LED, 온습도 센서, 릴레이, USB LED가 연결된 핀을 정의합니다.

### 센서 및 액츄에이터 설정

```c
#define DHTTYPE DHT22
#define LED_ON HIGH
#define LED_OFF LOW
#define RELAY_ON LOW
#define RELAY_OFF HIGH
```

사용하는 센서의 타입과, LED 및 릴레이의 ON/OFF 상태를 정의하는 부분입니다.

### MQTT 설정

```c
const char *mqtt_topic = "iot/21800677";
```

MQTT 메시지를 송수신할 토픽을 설정합니다.

### 세팅 및 루프 함수

```c
void setup() {
  ...
}

void loop() {
  ...
}
```

`setup()` 함수에서는 시스템 초기 설정을 하고, `loop()` 함수에서는 주기적으로 센서 값을 읽어서 MQTT로 전송하고, MQTT 메시지를 받아서 액츄에이터를 제어하는 작업을 수행합니다.

## 사용방법

필요한 장비를 노드MCU에 연결한 후, 위의 코드를 노드MCU에 업로드합니다. 이후 MQTT 브로커에 메시지를 보내서 LED 및 USB LED를 제어하거나, 센서 값을 받아볼 수 있습니다.

## 실행 예시

### 웹페이지

#### Main View
<img width="1282" alt="KakaoTalk_20231104_204219329_06" src="https://github.com/DolmaengC/IoT_server/assets/100391405/b634693e-fbc0-4d4f-9f74-21f826adf193">

#### Easy View
<img width="1282" alt="KakaoTalk_20231104_204219329_05" src="https://github.com/DolmaengC/IoT_server/assets/100391405/91421dbd-892d-43bd-9a67-1278fac882a3">


### 반응형 HTML
<img width="539" alt="KakaoTalk_20231104_204207740" src="https://github.com/DolmaengC/IoT_server/assets/100391405/ebd4297c-8cc0-42f1-84ee-41d66a120c15">

#### 404 Handling
<img width="1159" alt="KakaoTalk_20231104_204219329_04" src="https://github.com/DolmaengC/IoT_server/assets/100391405/aa450353-6ed2-4dd7-898e-0976109361c8">

### OLED
![KakaoTalk_20231104_204219329_01](https://github.com/DolmaengC/IoT_server/assets/100391405/743b57ff-cd86-4c64-9c84-e20ed43f3a09)

### Relay/USBLED ON/OFF
![KakaoTalk_20231104_203815904](https://github.com/DolmaengC/IoT_server/assets/100391405/93d83ddb-6572-4ff2-ad03-6b09323b75c3)
![KakaoTalk_20231104_203815904_01](https://github.com/DolmaengC/IoT_server/assets/100391405/1e4c76fa-a0aa-41d3-8ef7-fccae0eb4e77)

### LED ON/OFF
![KakaoTalk_20231104_203815904_02](https://github.com/DolmaengC/IoT_server/assets/100391405/36d3241f-feff-4141-bacb-b0444aab814d)
![KakaoTalk_20231104_203815904_03](https://github.com/DolmaengC/IoT_server/assets/100391405/3620687b-a40b-4e6d-9ca6-f5a9df51ecbf)

