import RPi.GPIO as GPIO
from hx711 import HX711

# Initialisierung der GPIO-Pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Definieren Sie die Pins für den HX711
HX711_DATAPIN = 6
HX711_SCLKPIN = 5

# Erstellen Sie eine Instanz des HX711-Sensors
hx711 = HX711(HX711_DATAPIN, HX711_SCLKPIN)

# Kalibrierungsfaktoren
CALIBRATION_FACTOR = 1

# Einstellungen für den HX711
hx711.set_reading_format("MSB")
hx711.set_reference_unit(1)
hx711.reset()

# TARA-Gewicht einstellen (optionale Schritt, um Nullpunkt zu setzen)
hx711.tare()

# Schleife zum kontinuierlichen Auslesen des Gewichts
while True:
    try:
        # Gewicht auslesen
        weight = hx711.get_weight() / CALIBRATION_FACTOR

        # Gewicht auf der Konsole anzeigen
        print("Gewicht: %.2f" % weight)

    except (KeyboardInterrupt, SystemExit):
        GPIO.cleanup()
        break
