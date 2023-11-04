# HowToRun.md

이 문서는 NodeMCU 기반 IoT 시스템을 실행하는 방법에 대해 설명합니다.

## 필요 사항

- NodeMCU
- 온도 센서 (DHT22)
- 습도 센서 (DHT22)
- 조도 센서 (CDS)
- LED
- USB LED
- MQTT 브로커 서버
- Python Flask 웹 서버

## 1단계: NodeMCU와 센서 연결

먼저 NodeMCU와 센서들을 아래와 같이 연결합니다.

- DHT22 (온도, 습도 센서): NodeMCU의 D3 핀에 연결
- CDS (조도 센서): NodeMCU의 A0 핀에 연결
- LED: NodeMCU의 D0 핀에 연결
- USB LED: NodeMCU의 D4 핀에 연결

## 2단계: NodeMCU 코드 업로드

NodeMCU 코드를 Arduino IDE 등의 개발 환경을 이용해 NodeMCU에 업로드합니다. 코드 내의 Wi-Fi SSID, 비밀번호, MQTT 브로커 주소, 사용자 이름, 비밀번호 등을 실제 환경에 맞게 변경해야 합니다.

## 3단계: 웹 서버 실행

리눅스 환경에서 아래 코드를 사용하여 Python3 Flask 웹 서버 코드를 실행합니다.

```
sudo python3 project1_flask_mqtt.py
```

## 4단계: 웹 페이지 사용

웹 브라우저를 열고 웹 서버의 주소를 입력해 웹 페이지를 엽니다. 웹 페이지를 통해 센서에서 측정한 데이터를 확인하고, LED와 USB LED의 상태를 제어할 수 있습니다. 

이제 NodeMCU 기반 IoT 시스템이 정상적으로 작동합니다. 문제가 발생하면 각 단계를 다시 확인하고 필요한 경우 문제를 해결합니다.
