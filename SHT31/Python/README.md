# Raspberry-PI_SHT31_Firebase
  In this project I am going to post the real time data of temperature and humidity sensor to the Firebase database.
  I am using SHT31 Sensor to communicate with raspberry pi using I2C connection adapters

## Setup for the Devices used in project 

  - ## Raspberry Pi 3 Model B
      ### Installation and Image Configuration

       - Install OS Raspbian [imagefile](https://www.raspberrypi.org/downloads/)
       - Make the bootable SD card containing using software "Win32 Disk Imager" or "Power ISO"
       - Insert Bootable SD card in Raspberry Pi SD slot
    Give power to Raspberry pi through micro USB port and connect keybopard, mouse, HDMI port of Diplay Screen with

    ***Enable the VNC settings so that it will be easily connected to VNC viewer in Laptop or Desktop*** 

      ### For Connecting the Raspberry pi via Laptop using LAN Port
  
       - Power Up the RPI through micro USB port
       - Connect the LAN port with Laptop
       - open cmd prompt
       - Write "ipconfig"
       - In Ethernet Adapter option it will show Raspberry PI the default local IP (copy and save it in notepad)
       - Install VNCviewer
       - After installation, Open VNC viewer -> File -> New Connection
       - Type the default Ip copied before, Give Friendly name to raspberry pi(If user want)
       - Write the default Username = "pi" and Password = "raspberry" (if no user id password changed by the user)
  
      ### You will able to see the Raspbian OS system
  
      - Open CLI of Raspbian
      - Write the commands
        - sudo apt-upgrade
        - sudo apt-update
     
      ### For Python
      Download and install smbus library on Raspberry pi. Steps to install smbus are provided at:

        https://pypi.python.org/pypi/smbus-cffi/0.5.1
       
  
  
  - [SHT31](https://store.ncd.io/product/sht31-humidity-and-temperature-sensor-%C2%B12rh-%C2%B10-3c-i2c-mini-module/) I2C mini module sensor
   
   ![alt text](https://github.com/varul29/Raspberry-PI-/blob/master/Firebase_Python/SHT31%20I2CS.png)
   
  - Raspberry Pi [I2C adapter](https://store.ncd.io/product/i2c-shield-for-raspberry-pi-3-pi2-with-inward-facing-i2c-port/)
  
  ![alt text](https://github.com/varul29/Raspberry-PI-/blob/master/Firebase_Python/I2C%20adapter.png)
  
  - I2C cable
  
***Connect the Raspberry Pi GPIO pins with I2C adapter***

***Using I2C cable, connect SHT31 sensor 'IN' port (available on sensor) with I2C adapter***

### First Step after Physical connections 

  After Physical connection between SHT31(Temperature and humidity sensor) and Raspberry Pi:
    
   - Check the LED status which shows the power Connection in I2C adapter(connected with GPIO pins of RPI3) as well as in SHT31
   - After power connection open CLI of Raspberry Pi 
   - Configure all the general commands which are mentioned above for RPI setup
   - detect I2C register of sensor using comman i2cdetect -y 1
   - configure firebase using "sudo pip install python-firebase"
   
# Firebase Console browser Setup
  
   Log in to firebase console.
  
   - Click on "Add Project"
  
   ![alt text](https://github.com/varul29/Raspberry-PI-/blob/master/Add%20project.PNG)
  
   - Write Project name. 
  
   - Accept controller-controller terms.
    
   ![alt text](https://github.com/varul29/Raspberry-PI-/blob/master/Project%20name.PNG)
  
   - Click "create project".
  
   - Click "Database" (mentioned in left handside).
  
   ![alt text](https://github.com/varul29/Raspberry-PI-/blob/master/Database.PNG)
  
   - Click on "Create Database".
  
   ![alt text](https://github.com/varul29/Raspberry-PI-/blob/master/Create%20databse.PNG)
  
   - According to newwer version - you can choose either locked version or unlocked version and press Ok.
  
   - Choose Realtime Database(mentioned in the image).
  
   ![alt text](https://github.com/varul29/Raspberry-PI-/blob/master/Real%20time%20database.PNG)
  
   - Click on "Rules".
  
   ![alt text](https://github.com/varul29/Raspberry-PI-/blob/master/Rules.PNG)
  
   ### If in default security rules code is mentioned like below
      
        {
          "rules": { 
            "read": "auth != null"
            "write": "auth != null"
            }
         }
   ### Then change "auth != null" into "true"
  
        {
              "rules": { 
                "read": "true"
               "write": "true"
                }
         }
         
   - click on "Publish".
  
   ![alt text](https://github.com/varul29/Raspberry-PI-/blob/master/ruels%20change.PNG)
  
   - While creating code, we have to use the Host Id "https://tahsensor.firebase.com/" (which will be different for every users)
  
   ![alt text](https://github.com/varul29/Raspberry-PI-/blob/master/hostid.PNG)
  
     
## How to use firebase after installing Firebase package in RPI3

   Perform all the setup for firebase as mentioned above.
  
   This code should be used with every script that you will be using to connect to the Firebase database.
       
    from firebase import firebase
    
   ### How to post the data in Firebase database
   
   - Store the Host ID(provided in firebase database) in variable.  
    
    firebase= firebase.FirebaseApplication('host id mentioned in databse of firebase')

   - Store the real time readings in variable and convert the readings into string
   - The string conversion real time data of sensor will be post to database using "firebase.post" 
       
    result = firebase.post('host id mentioned', {'cTemp':str(cTemp),'ftemp':str(fTemp), 'humidity':str(humidity)})
    print(result)
   
 Download (or git pull) the code in pi. Run the program.
      
      $> python SHT31.py
 
 After executing the file,
 
 The output readings of SHT31 sensor in Firebase database will be appear as mentioned below in snap.
 
  ![alt text](https://github.com/varul29/Raspberry-PI-/blob/master/Sample%20Data.PNG)
 

 
 
 ### Note: This code is to post the Temeprature and humidiy sensor data for only one go.  
