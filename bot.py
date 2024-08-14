import javascript,random,json
mineflayer = javascript.require("mineflayer")

usernames = ["OyunPortall","Einshine","Herobrine","Homelander","SaulGoodman","Locked","SoldierBoy","TheDeep","ArthurMorgan","Dexter","PokerFace","0x","Rorschach","TerryDavis","KingTerry","Builderman","PunkGirl","Adrian","Umut","Hector","TheGood","TheBad","TheUgly"]
words = ["apple","destiny","butcher","Deep the peak","dogs","cats","bird","sky","moon","sun","come","fun",""]

def setup():
    file = open("settings.json","rb")
    data = json.load(file)
    server = data["address"].split()
    port = data["port"]
    version = data["version"]
    username = f"{random.choice(usernames)}{random.randint(0,99)}"
    if len(data["username"]) > 1:
        username = data["username"]
    bot = mineflayer.createBot({"host":server,"port":port,"username":username,"version":version,"hideErrors":False,"verbose":True})
    bot.setControlState("jump",True)

    @javascript.On(bot,"spawn")
    def login(this):
        bot.chat(random.choice(words))
    
    @javascript.On(bot,"kicked")
    def connectback(this,reason,loggedIn):
        setup()
           

setup()

