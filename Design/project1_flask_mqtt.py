from flask import Flask, render_template
from flask_mqtt import Mqtt
import time # library for time delay
import json

app = Flask(__name__)

app.config['MQTT_BROKER_URL'] = 'sweetdream.iptime.org'
app.config['MQTT_BROKER_PORT'] = 1883 
app.config['MQTT_USERNAME'] = 'iot'
app.config['MQTT_PASSWORD'] = 'csee1414'
'''
app.config['MQTT_BROKER_URL'] = '192.168.0.123'
app.config['MQTT_BROKER_PORT'] = 1883 
app.config['MQTT_USERNAME'] = 'junhyeok'
app.config['MQTT_PASSWORD'] = 'jun102030'
'''

mqtt = Mqtt(app)

# 21900764
pub_topic_21900764 = 'iot/21900764' # iot/{student id}
sub_topic_dht22_21900764 = 'iot/21900764/dht22'
sub_topic_dht22_h_21900764 = 'iot/21900764/dht22_h'
sub_topic_dht22_t_21900764 = 'iot/21900764/dht22_t'
sub_topic_cds_21900764 = 'iot/21900764/cds'
# 22100768
pub_topic_22100768 = 'iot/22100768' # iot/{student id}
sub_topic_dht22_22100768 = 'iot/22100768/dht22'
sub_topic_dht22_h_22100768 = 'iot/22100768/dht22_h'
sub_topic_dht22_t_22100768 = 'iot/22100768/dht22_t'
sub_topic_cds_22100768 = 'iot/22100768/cds'
#21800677
pub_topic_21800677 = 'iot/21800677' # iot/{student id}
sub_topic_dht22_21800677 = 'iot/21800677/dht22'
sub_topic_dht22_h_21800677 = 'iot/21800677/dht22_h'
sub_topic_dht22_t_21800677 = 'iot/21800677/dht22_t'
sub_topic_cds_21800677 = 'iot/21800677/cds'
# nth405
pub_topic_nth405 = 'iot/nth405' # iot/{student id}
sub_topic_dht22_nth405 = 'iot/nth405/dht22'
sub_topic_dht22_h_nth405 = 'iot/nth405/dht22_h'
sub_topic_dht22_t_nth405 = 'iot/nth405/dht22_t'
sub_topic_cds_nth405 = 'iot/nth405/cds'

# global varuable for messge payload
mqtt_message = ''
view_mode = 0
json_data = {
    "temperature_21900764" : '',
    "humidity_21900764" : '',
    "light_intensity_21900764" : '',
    "temperature_22100768" : '',
    "humidity_22100768" : '',
    "light_intensity_22100768" : '', 
    "temperature_21800677" : '', 
    "humidity_21800677" : '',
    "light_intensity_21800677" : '' ,
    "temperature_nth405" : '', 
    "humidity_nth405" : '',
    "light_intensity_nth405" : '' 
}

print('@@ Use URL:/iot/21900764/{led,ledon,ledoff,dht22,cds}')

# cmd = {led, ledon, ledoff, usbled, usbledon, usbledoff}
@app.route('/iot/21900764/<cmd>') 
def get_command_21900764(cmd):
    global mqtt_message
    global view_mode
    if cmd == 'led':
        mqtt.publish(pub_topic_21900764, 'led')
    elif cmd == 'ledon':
        mqtt.publish(pub_topic_21900764, 'ledon')
    elif cmd == 'ledoff':
        mqtt.publish(pub_topic_21900764, 'ledoff')

    elif cmd == 'usbled':
        mqtt.publish(pub_topic_21900764, 'usbled')
    elif cmd == 'usbledon':
        mqtt.publish(pub_topic_21900764, 'usbledon')
    elif cmd == 'usbledoff':
        mqtt.publish(pub_topic_21900764, 'usbledoff')
    elif cmd == 'change_mode':
        if view_mode == 1:
            view_mode = 0
        else:
            view_mode = 1

    if view_mode == 0:
        return render_template('index.html', json_data=json_data)
    else :
        return render_template('index_easy_view.html', json_data=json_data)

# cmd = {led, ledon, ledoff, usbled, usbledon, usbledoff}
@app.route('/iot/22100768/<cmd>') 
def get_command_22100768(cmd):
	global mqtt_message
    
	if cmd == 'led':
		mqtt.publish(pub_topic_22100768, 'led')
	elif cmd == 'ledon':
		mqtt.publish(pub_topic_22100768, 'ledon')
	elif cmd == 'ledoff':
		mqtt.publish(pub_topic_22100768, 'ledoff')

	elif cmd == 'usbled':
		mqtt.publish(pub_topic_22100768, 'usbled')
	elif cmd == 'usbledon':
		mqtt.publish(pub_topic_22100768, 'usbledon')
	elif cmd == 'usbledoff':
		mqtt.publish(pub_topic_22100768, 'usbledoff')
	return render_template('index.html', json_data=json_data) 

# cmd = {led, ledon, ledoff, usbled, usbledon, usbledoff}
@app.route('/iot/21800677/<cmd>') 
def get_command_21800677(cmd):
	global mqtt_message
    
	if cmd == 'led':
		mqtt.publish(pub_topic_21800677, 'led')
	elif cmd == 'ledon':
		mqtt.publish(pub_topic_21800677, 'ledon')
	elif cmd == 'ledoff':
		mqtt.publish(pub_topic_21800677, 'ledoff')

	elif cmd == 'usbled':
		mqtt.publish(pub_topic_21800677, 'usbled')
	elif cmd == 'usbledon':
		mqtt.publish(pub_topic_21800677, 'usbledon')
	elif cmd == 'usbledoff':
		mqtt.publish(pub_topic_21800677, 'usbledoff')
	return render_template('index.html', json_data=json_data) 

# cmd = {led, ledon, ledoff, usbled, usbledon, usbledoff}
@app.route('/iot/nth405/<cmd>') 
def get_command_nth405(cmd):
    global mqtt_message
    
    if cmd == 'led':
        mqtt.publish(pub_topic_nth405, 'led')
    elif cmd == 'ledon':
        mqtt.publish(pub_topic_nth405, 'ledon')
    elif cmd == 'ledoff':
        mqtt.publish(pub_topic_nth405, 'ledoff')
    elif cmd == 'usbled':
        mqtt.publish(pub_topic_nth405, 'usbled')
    elif cmd == 'usbledon':
        mqtt.publish(pub_topic_nth405, 'usbledon')
    elif cmd == 'usbledoff':
        mqtt.publish(pub_topic_nth405, 'usbledoff')

    if view_mode == 0:
        return render_template('index.html', json_data=json_data)
    else :
        return remder_template('index_easy_view.html', json_data=json_data)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('index.html', json_data=json_data)

# When mqtt is connected, subscribe to following topics
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe(sub_topic_dht22_21900764)
    mqtt.subscribe(sub_topic_dht22_t_21900764)
    mqtt.subscribe(sub_topic_dht22_h_21900764)
    mqtt.subscribe(sub_topic_cds_21900764)

    mqtt.subscribe(pub_topic_22100768)
    mqtt.subscribe(sub_topic_dht22_22100768)
    mqtt.subscribe(sub_topic_dht22_t_22100768)
    mqtt.subscribe(sub_topic_dht22_h_22100768)
    mqtt.subscribe(sub_topic_cds_22100768)
    
    mqtt.subscribe(pub_topic_21800677)
    mqtt.subscribe(sub_topic_dht22_21800677)
    mqtt.subscribe(sub_topic_dht22_t_21800677)
    mqtt.subscribe(sub_topic_dht22_h_21800677)
    mqtt.subscribe(sub_topic_cds_21800677)

    mqtt.subscribe(pub_topic_nth405)
    mqtt.subscribe(sub_topic_dht22_nth405)
    mqtt.subscribe(sub_topic_dht22_t_nth405)
    mqtt.subscribe(sub_topic_dht22_h_nth405)
    mqtt.subscribe(sub_topic_cds_nth405)

# When mqtt receives message from subscribed topic
@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    global mqtt_message
    
    global json_data

    topic = message.topic
    payload = message.payload
    payload = payload.decode('utf-8')
    topic = str(message.topic)
    payload = str(message.payload)[2:-1]

    if topic == sub_topic_dht22_21900764:
        payload = json.loads(payload)
        json_data['humidity_21900764'] = payload["humidity"]
        json_data['temperature_21900764'] = payload["temperature"]
    elif topic == sub_topic_cds_21900764:
        json_data['light_intensity_21900764'] = payload 

    elif topic == sub_topic_dht22_22100768:
        payload = json.loads(payload)
        json_data['humidity_22100768'] = payload["humidity"]
        json_data['temperature_22100768'] = payload["temperature"]
    elif topic == sub_topic_cds_22100768:
        json_data['light_intensity_22100768'] = payload 

    elif topic == sub_topic_dht22_21800677:
        payload = json.loads(payload)
        json_data['humidity_21800677'] = payload["humidity"]
        json_data['temperature_21800677'] = payload["temperature"]
    elif topic == sub_topic_cds_21800677:
        json_data['light_intensity_21800677'] = payload 

    elif topic == sub_topic_dht22_t_nth405:
        json_data['temperature_nth405'] = payload
    elif topic == sub_topic_dht22_h_nth405:
        json_data['humidity_nth405'] = payload
    elif topic == sub_topic_cds_nth405:
        json_data['light_intensity_nth405'] = payload 
    
    

    mqtt_message = payload
    print("Topic: " + topic , end="")
    print(" message: ", end="")
    print(mqtt_message)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=False)
