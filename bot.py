import javascript,random

mineflayer = javascript.require("mineflayer")
server = str(input("Enter the server address: "))
port = int(input("Enter the server port: (Default port is 25565)\n"))
version = str(input("Enter the server version: "))
username = f"Rorschach{random.randint(0,4395837309458)}"
bot = mineflayer.createBot({"host":server,"port":port,"username":username,"version:":version,"hideErrors":False})

@javascript.On(bot,"spawn")
def login(this):
    print("We did that!")
