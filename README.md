# IoT Server Project 1

이 프로젝트는 NodeMCU를 이용하여 온도/습도/조도 센서의 데이터를 수집하고, 수집된 데이터를 MQTT 프로토콜을 통해 웹 서버에 전송합니다. 또한, 웹 브라우저를 통해 LED와 USB LED의 상태를 제어할 수 있습니다.

## 1. NodeMCU 코드

NodeMCU 코드는 센서 데이터를 수집하고, MQTT 프토콜을 통해 이를 웹 서버에 전송하는 역할을 합니다. 또한, 웹 서버로부터 받은 명령을 통해 LED와 USB LED의 상태를 제어합니다. 동시에, 수집한 센서 데이터는 OLED display를 통해 출력됩니다 

[NodeMCU 코드](Design/Arduino/project1/project1.ino)

## 2. 웹 서버 코드 

웹 서버는 Flask 기반으로 작성되었습니다. 웹 서버는 MQTT를 통해 NodeMCU로부터 받은 센서 데이터를 저장하고, 웹 페이지를 통해 이를 사용자에게 표시합니다. 또한, 웹 페이지를 통해 사용자의 명령을 받아 MQTT를 통해 NodeMCU에 전달하여 LED와 USB LED의 상태를 제어합니다. 

[웹 서버 코드](https://github.com/DolmaengC/IoT_server/blob/caca4eda117c139555ffdad51d6faab500827d9a/Design/templates/index.html)

## 3. 웹 페이지 코드

웹 페이지는 Bootstrap을 이용하여 제작되었습니다. 웹 페이지는 웹 서버로부터 받은 센서 데이터를 표시하고, 사용자의 명령을 웹 서버에 전달하는 인터페이스를 제공합니다.   
전송받은 센서 데이터와 LED, USBLED의 상태를 제어하는(ON, OFF, Toggle) Detail View 페이지와 전송받은 센서 데이터와 USLED, LED의 Toggle 버튼만 제공하는 Easy View 페이지가 있습니다.

[웹 페이지 코드(Detail view)](Design/templates/index.html)   
[웹 페이지 코드(Easy view)](Design/templates/index_easy_view.html)

## 사용 방법

1. NodeMCU와 센서들을 연결합니다.
2. NodeMCU 코드를 NodeMCU에 업로드합니다.
3. 웹 서버 코드를 실행합니다.
4. 웹 페이지를 통해 센서 데이터를 확인하고, LED와 USB LED의 상태를 제어합니다.

## 필요 사항

- NodeMCU(ESP8266)
- 온도 센서 (DHT22)
- 습도 센서 (DHT22)
- 빛 센서 (CDS)
- LED
- USB LED
- Relay
- OLED display(Adafriut SSD1306 0.96" 128x32 I2C)
- MQTT 브로커 서버
- Python Flask 웹 서버

## 주의 사항

- NodeMCU 코드의 Wi-Fi SSID, 비밀번호, MQTT 브로커 주소, 사용자 이름, 비밀번호 등을 실제 환경에 맞게 변경해야 합니다.
- NodeMCU와 센서들이 올바르게 연결되어 있어야 합니다.
- MQTT 브로커 서버가 실행 중이어야 합니다.
- 웹 서버 코드를 실행하기 전에 필요한 파이썬 라이브러리를 설치해야 합니다.
