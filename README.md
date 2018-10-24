# Raspberry-PI_SHT31_Firebase
  
  In this project I am going to post the real time data of temperature and humidity sensor to the Firebase database.
  I am using SHT31 Sensor to communicate with raspberry pi using I2C connection adapters

## Important Features:

  - The Firebase Realtime Database is a cloud-hosted database.
  - Single client sensor data is Collaborate with cross-platform apps like IOS, Android, and JavaScript SDKs as well as many IoT hardware with ease.
  - With the help of I2C protocol we will be able to extract the precised, calibrated and linear data.
  - Data of sensor stores with specified key-value pairs to change the behavior and appearance of your app without requiring any download an update.

## Devices Used in project 

  - Raspberry Pi 3 Model B ([Setup and Insatallation procedure for Newbie](https://github.com/varul29/Raspberry-PI-/blob/master/README.md))
  - [SHT31](https://store.ncd.io/product/sht31-humidity-and-temperature-sensor-%C2%B12rh-%C2%B10-3c-i2c-mini-module/) I2C mini module sensor
  ![alt text](https://github.com/varul29/Raspberry-PI-/blob/master/Firebase_Python/SHT31%20I2CS.png)
   
  - Raspberry Pi [I2C adapter](https://store.ncd.io/product/i2c-shield-for-raspberry-pi-3-pi2-with-inward-facing-i2c-port/)
  
  ![alt text](https://github.com/varul29/Raspberry-PI-/blob/master/Firebase_Python/I2C%20adapter.png)
  
  - I2C cable
     
***Connect the Raspberry Pi GPIO pins with I2C adapter***

***Using I2C cable, connect SHT31 sensor 'IN' port (available on sensor) with I2C adapter***

## Working Of Code

  - We are importing the the libraries packages of I2C, Firebase in starting.
          
          import smbus
          import time
          from firebase import firebase
          
  - Detects the pull up then initialize the I2C register, measurement commands, repeatability measurement and write the I2C data 
      
          bus = smbus.SMBus(1)
          bus.write_i2c_block_data(0x44, 0x2C, [0x06])
  
  - Read data from 8 Bit I2C frame using speidfied address registers  
      
          data = bus.read_i2c_block_data(0x44, 0x00, 6)   
          
  -  Combine the 2 Bytes data (MSB & LSB available) by using shift register value
  
          temp = data[0] * 256 + data[1]
          
  - With help of SHT31 datasheet, calclate the temperature in celcius as well as in Farenhiet divided by the resolutin specified by user, subtrcted 1.
  
          temp = data[0] * 256 + data[1] #shifting data[0] 
          cTemp = -45 + (175 * temp / 65535.0) 
          fTemp = -49 + (315 * temp / 65535.0) 
          humidity = 100 * (data[3] * 256 + data[4]) / 65535.0 
          
  - Finally print the data after the conversion
  
          print "Temperature in Celsius is : %.2f C" %cTemp
          print "Temperature in Fahrenheit is : %.2f F" %fTemp
          print "Relative Humidity is : %.2f %%RH" %humidity
 
    ### Post the data in Firebase 
 
    We are syncing the real time database for JSON data. Data will be stored in form JSON object and synchronized in realtime to every connected client. For creating project for storing sensor data in console database, check the [documentation](https://github.com/varul29/Raspberry-PI-/blob/master/Firebase_Python/README.md)
   
   - Connecting to the Host ID(provided in firebase database)  
    
          firebase= firebase.FirebaseApplication('host id mentioned in databse of firebase')
      
   ![alt text](https://github.com/varul29/Raspberry-PI-/blob/master/hostid.PNG)

   - Posting real time readings in form of JSON data to the host ID used for storing the values of sensor 
   - The JSON data of sensor will be posted to database using "firebase.post" also called JSON post method
       
          result = firebase.post('host id mentioned', {'cTemp':str(cTemp),'ftemp':str(fTemp), 'humidity':str(humidity)})
            
  Secured random authentication value will be printed while using the command
   
          print(result)
   
Now Download (or git pull) the code in pi. Run the program.
      
      $> python SHT31.py
 
 After executing the Program,
 
 ### Output in Firebase
 
 Output readings of SHT31 sensor in database will be appear in form of Parent, Child name and its value 
 
       temperature-sensor-bb4bd (PARENT)
           {
             LGeJ3JC2jj9O8tM6FI6 (Secured Random Authentication Value)
                 cTemp: "26.8371862364"  (CHILD NAME)
                 ftemp: "80.3069352255"  (CHILD NAME)
                 humidity: "38.1216144045" (CHILD NAME)
           }   
 
  ![alt text](https://github.com/varul29/Raspberry-PI-/blob/master/Sample%20Data.PNG)
 

 ## Limitation
 
 You can only send the JSON Object in Firebase 
 
 # Reference
 
  1. SHT 31: https://github.com/ControlEverythingCommunity/SHT31/blob/master/Arduino/SHT31.ino
  2. Raspberry Pi: http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
  3. Firebase: https://www.youtube.com/watch?v=BJfVoaifnzc&t=240s
  4. JSON Post method: https://www.geeksforgeeks.org/get-post-requests-using-python/
  
  # Future Enhancement
  
   - The stored sensor data in JSON object will be useful with any application - Android, Python, Java, IOS SDKs
   - We are trying to display the sensor data on Dashboard 
   - Further it will be helpful in streamline analytics of environment status in industries, home automation and many different places
   - Data will be easily accessed and analyzed by smartphones in apps via internet
   - The data will be greatlyused in Online Envrionment monitoring system of Underground stores, Refridging Stores any many other automation departments
   
