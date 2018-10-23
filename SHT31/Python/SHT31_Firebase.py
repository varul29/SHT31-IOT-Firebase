#We are using Python code to send the real time data of SHT31(temperature and humidity sensor) I2C module to Firebase
#Importing I2C, Time, Firebase library in python code.
import smbus
import time
from firebase import firebase

# Get I2C bus
bus = smbus.SMBus(1) #If I2C library detects the pull up then initialize the register using sensors

# SHT31 address, 0x44(68)
# Send measurement command, 0x2C(44)
#		0x06(06)	High repeatability measurement
bus.write_i2c_block_data(0x44, 0x2C, [0x06])

time.sleep(0.5)

# SHT31 address, 0x44(68)
#6 bytes -> 
#0,1-> 2 bytes for MSB and LSB for Temperature, 2 -> 1 byte for CRC , 3,4-> 2 byte for MSB and LSB for humidity, 5 -> 1byte for CRC. 
# Temp MSB, Temp LSB, Temp CRC, Humidity MSB, Humidity LSB, Humidity CRC

# Read data back from 0x00(00), 6 bytes 
data = bus.read_i2c_block_data(0x44, 0x00, 6)

# Convert the data
temp = data[0] * 256 + data[1] #shifting data[0] to left side and adding data[1] xisting in right side
cTemp = -45 + (175 * temp / 65535.0) #formula mentioned in datasheet
fTemp = -49 + (315 * temp / 65535.0) #formula mentioned in datasheet
humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

# Print the readings and show it RPI OS CLI
print "Temperature in Celsius is : %.2f C" %cTemp
print "Temperature in Fahrenheit is : %.2f F" %fTemp
print "Relative Humidity is : %.2f %%RH" %humidity

time.sleep(5) #5milliseconds

#store the Host ID(provided in firebase database) in variable where you want to send the real time sensor data.  
firebase= firebase.FirebaseApplication('HOST ID')

#store the readings in variable and convert it into string and using firbase.post then data will be posted to databse of firebase 
result = firebase.post('Project Name', {'cTemp':str(cTemp),'ftemp':str(fTemp), 'humidity':str(humidity)})
print(result)
