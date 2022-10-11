import os
from re import M
import time
import socket
import paho.mqtt.client as mqtt
import numpy as np
from termcolor import colored
import random
from helpers.running_mean import running_mean
from helpers.MeasurementType import MeasurementType , averageMeasurament, MaxMeasurament


MOSQUITO_CLIENT_NAME = socket.gethostname() + '_cpu_temperature_mqtt_' + str(random.randint(1,10000))

MQTT_SERVER_ADD = '192.168.123.16'
MQTT_PORT = 1883
MQTT_TOPIC = 'MQTT TOPIC'
MQTT_USERNAME = ''
MQTT_PASSWORD = ''

# NUMBER OF SAMPLES TO TAKE BEFORE SENDING TO THE MQTT SERVER
REPETITIONS = 6

# TIME BETWEEN REPETITIONS
REPETITIONS_SLEEP_TIME_SECS = 10

# LENGTH OF THE MOVING AVERAGE ARRAY
TEMPERATURE_ARRAY_MAX_POSITIONS = 6


# N cores
N_CORES = 1

# AVERAGE MEASUREMENT OR MAX
TYPE_MEASUREMENT = MeasurementType.AVERAGE


client = mqtt.Client(MOSQUITO_CLIENT_NAME, clean_session=True)
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
not_connected = True
while not_connected:
  try:
    client.connect(MQTT_SERVER_ADD, port = MQTT_PORT)
    not_connected = False
  except:
    print('failed connection')
    time.sleep(10)
client.loop_start()

TEMPERATURE_ARRAY = []

for _ in range(TEMPERATURE_ARRAY_MAX_POSITIONS):
  temperature = float(os.popen('sysctl dev.cpu.0.temperature').read()[23:27])
  TEMPERATURE_ARRAY.append(temperature)



while True:
  try:
    cpu_temp_avg = 0
    for _ in range(REPETITIONS):
      if TYPE_MEASUREMENT == MeasurementType.AVERAGE:
        cpu_temp = averageMeasurament(N_CORES)
      else:
        cpu_temp = MaxMeasurament(N_CORES)
      cpu_temp_avg = running_mean(cpu_temp, TEMPERATURE_ARRAY_MAX_POSITIONS, TEMPERATURE_ARRAY)
      time.sleep(REPETITIONS_SLEEP_TIME_SECS)
      
    
    client.publish(MQTT_TOPIC, "{:.1f}". format(cpu_temp_avg))
    print(colored(cpu_temp_avg, 'green'))
  except Exception as e:
    print(colored(e, 'red'))



 
