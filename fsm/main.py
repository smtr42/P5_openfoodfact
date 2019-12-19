from machine import Machine

print("Bienvenue, rentre le numéro de ligne que tu veux exécuter \n"
      "\n"
      "")



device = Machine()
while True:
    device.show()
    event = device.input_checker()
    device.on_event(event)