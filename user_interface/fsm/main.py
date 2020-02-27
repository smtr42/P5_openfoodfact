import colorful as cf

from .machine import Machine

"""Instanciate the Machine class and has the start menu print output"""

print(cf.green(r"""
   ____                   ______              _  __           _
  / __ \                 |  ____|            | |/ _|         | |
 | |  | |_ __   ___ _ __ | |__ ___   ___   __| | |_ __ _  ___| |_
 | |  | | '_ \ / _ \ '_ \|  __/ _ \ / _ \ / _` |  _/ _` |/ __| __|
 | |__| | |_) |  __/ | | | | | (_) | (_) | (_| | || (_| | (__| |_
  \____/| .__/ \___|_| |_|_|  \___/ \___/ \__,_|_| \__,_|\___|\__|
        | |
        |_|
      """))
print(
    "\n Welcome \n \n"
    "You must have a functional database and put your credentials into the "
    "configuration file in configuration/constant.py before using this script"
    "\n For mor information you are strongly advised to read the readme")
print(cf.green("\n"
               "Write down a number to access the desired line \n"
               "\n"))

device = Machine()
