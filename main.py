import os
from apidata.requester import RequestData
from dbmanagement import main_manager
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
      "Welcome \n"
      "\n"
      "You must have a functional database and put your credentials into the configuration file in  configuration/constant.py"
      "\n"
      "For mor information you are strongly advised to read the readme"
      "\n"
      "")

this_folder = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(this_folder, 'apidata/products_fr.json')
if not os.path.exists(data_file):
    print("IT SEEMS DATA IS MISSING - YOU MUST LET THE APPLICATION DOWNLOAD")


answer =input("Do you want to transfert data from the API ? It's MANDATORY for your first utilisation and good program execution"
      "\n"
      "Press 'y' to do so, otherwise press any other key to continue")

if answer == 'y':
    rd = RequestData()
    rd.fetch_category()
    rd.fetch_products()
else:
    main_manager.run()

