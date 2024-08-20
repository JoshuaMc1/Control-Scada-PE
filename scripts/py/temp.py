import subprocess
import Adafruit_DHT
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 26 
GPIO.setup(DHT_PIN, GPIO.IN)

num = 0
last_temp = None
last_hum = None

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        
        if humidity is not None and temperature is not None:
            print(f"Temperatura={temperature:.1f}C  Humedad={humidity:.1f}%")
            
            if last_temp is None or temperature != last_temp or humidity != last_hum:
                num += 1
                print(f"Cambio detectado en la temperatura o humedad {num}")
                last_temp = temperature
                last_hum = humidity
                
                with open("/home/sps/examen/status/temp.txt", "w") as temp_file:
                    temp_file.write(f"{temperature:.1f}\n")
                
                with open("/home/sps/examen/status/hum.txt", "w") as hum_file:
                    hum_file.write(f"{humidity:.1f}\n")
                
            if temperature >= 20.0:
                subprocess.call("/home/sps/examen/scripts/sh/Bzzon.sh")
                time.sleep(1)
                subprocess.call("/home/sps/examen/scripts/sh/Bzzoff.sh")
                
            time.sleep(1)
        else:
            print("Fallo al obtener lectura del sensor DHT11")
            subprocess.call("/home/sps/examen/scripts/sh/Bzzoff.sh")
            time.sleep(2)

except KeyboardInterrupt:
    print("Detenido por el usuario")
    GPIO.cleanup()
