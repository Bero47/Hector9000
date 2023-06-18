import RPi.GPIO as GPIO
import time

# Pinbelegung (angepasst an deine Konfiguration)
DIR = 13  # Richtungs-Pin
STEP = 26  # Schritt-Pin
ENABLE = 17  # Aktivierungs-Pin

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(ENABLE, GPIO.OUT)
GPIO.output(DIR, GPIO.HIGH)  # Richtung (LOW = vorwärts, HIGH = rückwärts)
GPIO.output(ENABLE, GPIO.HIGH)  # Aktivierung (LOW = aktiviert, HIGH = deaktiviert)

# Schrittfunktion
def step():
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(0.005)  # Wartezeit zwischen den Schritten anpassen (falls erforderlich)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(0.005)  # Wartezeit zwischen den Schritten anpassen (falls erforderlich)

# Schritte ausführen
try:
    while True:
        # Führe 200 Schritte in eine Richtung aus
        for _ in range(200):
            step()

        # Warte für 2 Sekunden
        time.sleep(2)
        print('hallo')

        # Ändere die Richtung
        GPIO.output(DIR, not GPIO.input(DIR))  # Invertiere die aktuelle Richtung

except KeyboardInterrupt:
    # Beim Abbruch durch den Benutzer aufräumen
    GPIO.cleanup()
