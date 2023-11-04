# DEMO.MD

이 문서에서는 Flask와 MQTT를 이용하여 IoT 디바이스를 제어하고, 디바이스의 센서 데이터를 수집하는 프로그램의 사용 방법을 설명합니다.

## 1. 프로그램 설정

먼저, 프로그램의 설정을 확인합니다. 이 설정은 MQTT 브로커의 정보를 포함하고 있습니다.

```python
app.config['MQTT_BROKER_URL'] = 'sweetdream.iptime.org'
app.config['MQTT_BROKER_PORT'] = 1883 
app.config['MQTT_USERNAME'] = 'iot'
app.config['MQTT_PASSWORD'] = 'csee1414'
```

## 2. IoT 디바이스 제어

각 IoT 디바이스를 제어하려면, 웹 브라우저에서 다음 형식의 URL을 입력합니다.

```
http://your_server_address/iot/{student_id}/{command}
```

여기서,
- `{student_id}`는 제어하려는 IoT 디바이스의 학생 ID를 나타냅니다.
- `{command}`는 실행할 명령어를 나타냅니다. 명령어는 'led', 'ledon', 'ledoff', 'usbled', 'usbledon', 'usbledoff' 중 하나입니다.

예를 들어, 학생 ID가 '21900764'인 디바이스의 LED를 켜려면 다음 URL을 사용합니다.

```
http://your_server_address/iot/21900764/ledon
```

## 3. 센서 데이터 확인

센서 데이터는 웹 페이지에 실시간으로 표시됩니다. 이 데이터는 전역 변수 `json_data`에 저장되며, 웹 페이지를 새로 고침하면 최신 데이터를 확인할 수 있습니다.

## 4. 프로그램 실행

이 애플리케이션은 모든 네트워크 인터페이스의 80 포트에서 실행됩니다. 디버그 모드는 비활성화되어 있습니다.

```python
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=False)
```
리눅스 환경에서 아래 명령어를 통해 프로그램을 실행할 수 있습니다.
```
sudo pyhton3 project1_flask_mqtt.py
```

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

