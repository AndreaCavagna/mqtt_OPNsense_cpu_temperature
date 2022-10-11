from enum import Enum
import os

MeasurementType = Enum('MeasurementType', 'AVERAGE MAXIMUM')


def averageMeasurament(N_CORES: int):
  cpu_temp = 0
  for i in range(N_CORES):
    cpu_temp = float(os.popen('sysctl dev.cpu.'+ str(i)+'.temperature').read()[23:27])
  return cpu_temp/ float(N_CORES) 


def MaxMeasurament(N_CORES: int):
  max_temp = 0  
  for i in range(N_CORES):
    cpu_temp = float(os.popen('sysctl dev.cpu.'+ str(i)+'.temperature').read()[23:27])
    if cpu_temp > max_temp:
        max_temp = cpu_temp
  return max_temp