import smbus
import time

# I2C-Busnummer (normalerweise 1 für den Raspberry Pi)
bus_number = 1

# I2C-Adresse
i2c_address = 0x40

# Erzeuge ein I2C-Busobjekt
i2c_bus = smbus.SMBus(bus_number)

# Kontinuierlich Werte lesen
try:
    while True:
        # Lese einen Wert vom I2C-Bus
        value = i2c_bus.read_byte(i2c_address)
        print(f"Gelesener Wert: {value}")

        # Warte für 1 Sekunde, bevor der nächste Lesevorgang stattfindet
        time.sleep(1)

# Beenden der Schleife mit Strg+C
except KeyboardInterrupt:
    pass

# Schließe den I2C-Bus
i2c_bus.close()
