#!/usr/bin/env python
import datetime
import time
import requests
from influxdb import InfluxDBClient

influx_host = '127.0.0.1'
influx_port = 8086
influx_user = 'root'
influx_passwd = 'root'

influx_dbname = 'temperatures'
log_interval = 1

influx_client = InfluxDBClient(influx_host, influx_port, influx_user, influx_passwd, influx_dbname)
influx_client.create_database(influx_dbname)

sensorlist = ow.Sensor('/').sensorList()

ow_url = 'http://localhost:2121/text/uncached/'

def get_sensors(sensor_type='DS18B20'):
	device_list = requests.get(ow_url).content.split('\r\n')
	device_dict = {}
	for device in device_list:
		if not device:
			continue
		name, name2, entry_type = device.split()
		device_details = requests.get(ow_url+name).content.split('\r\n')
		sensor_dict = {}
		for dd in device_details:
			if not dd:
				continue
			l = dd.split()
			if len(l) == 2:
				sensor_dict[l[0]] = l[1]
			elif len(l) == 1:
				sensor_dict[l[0]] = ""
			else:
				pass
			sensor_dict["time"] = datetime.datetime.utcnow().isoformat() + 'Z'
		if 'type' in sensor_dict and sensor_dict['type'] == sensor_type:
			device_dict[name] = sensor_dict

	return device_dict
		
				



try:
	while True:
		json_body = []
		sensors = get_sensors()
		for name, sensor in sensors.items():
			json_body.append(
				{
					"measurement": "temperature",
					"tags": {
						"sensorid": sensor['id'],
						"alias": sensor['alias'] if sensor['alias'] else sensor['id']
						},
					"time": sensor['time'],
					"fields": {
						"value": float(sensor['temperature'])
						}
				}
			)
			
		print(json_body)

		influx_client.write_points(json_body)

		time.sleep(log_interval)

except KeyboardInterrupt:
	print('Exiting')

