import RPi.GPIO as GPIO
import time

# Festlegen des zu lesenden GPIO-Pins
GPIO_PIN = 6

# GPIO initialisieren
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

# Schleife, um den Status des Pins jede Sekunde auszulesen und in der Konsole auszugeben
while True:
    pin_status = GPIO.input(GPIO_PIN)
    print(f"GPIO Pin {GPIO_PIN} Status: {pin_status}")
    time.sleep(1)
