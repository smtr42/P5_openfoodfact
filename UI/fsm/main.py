from machine import Machine

print("""\
   ____                   ______              _  __           _
  / __ \                 |  ____|            | |/ _|         | |
 | |  | |_ __   ___ _ __ | |__ ___   ___   __| | |_ __ _  ___| |_
 | |  | | '_ \ / _ \ '_ \|  __/ _ \ / _ \ / _` |  _/ _` |/ __| __|
 | |__| | |_) |  __/ | | | | | (_) | (_) | (_| | || (_| | (__| |_
  \____/| .__/ \___|_| |_|_|  \___/ \___/ \__,_|_| \__,_|\___|\__|
        | |
        |_|
      """
      "\n"
      "Welcome, write down a number to access the desired line \n"
      "\n"
      "To QUIT the program write 'q', to GO BACK to the last menu write 'r'"
      "\n"
      "")

device = Machine()
while True:
    device.show()
    event = device.input_checker()
    device.on_event(event)
