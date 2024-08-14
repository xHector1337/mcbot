import javascript,random,json
mineflayer = javascript.require("mineflayer")

usernames = ["OyunPortall","Einshine","Herobrine","Homelander","SaulGoodman","Luna","Locked","SoldierBoy","TheDeep","ArthurMorgan","Dexter","PokerFace","0x","Rorschach","TerryDavis","KingTerry","Builderman","PunkGirl","Adrian","Umut","Hector","TheGood","TheBad","TheUgly","MindHunter","RustCohle","BenTennyson","GwenStacy","Caroline","HateMyLife","NietzscheFan","Ubermensch","FlowerLover","BillyButcher","KarolKarol"]
words = ["apple","destiny","butcher","good","evil","punish","arrest","put","look","gamble","Deep the peak","dogs","cats","bird","sky","moon","love","sun","come","fun","what","hate","keep","want","cancel","me","I","you","we","womp womp womp","candy","meow :3","nyaa :3","shop","skibidi","toilet","worth","deserve","lune","Walter White","Pinkman","Ozymandias","dance","nothing"]

def setup():
    file = open("settings.json","r")
    data = json.load(file)
    server = data["address"].split()
    port = data["port"]
    version = data["version"]
    username = f"{random.choice(usernames)}{random.randint(0,99)}"
    if len(data["username"]) > 1:
        username = data["username"]
    mode = data["mode"]
    password = data["password"]    
    bot = mineflayer.createBot({"host":server,"port":port,"username":username,"version":version,"hideErrors":False,"verbose":True})
    if data["keepJump"]:
        bot.setControlState("jump",True)

    @javascript.On(bot,"spawn")
    def login(this):
        bot.chat(random.choice(words))
    @javascript.On(bot,"login")
    def oopsie(this):
        if mode == "login":
            bot.chat(f"/login {password}")
        elif mode == "register":
            bot.chat(f"/register {password} {password}")
        else:
            pass       
    
    @javascript.On(bot,"kicked")
    def connectback(this,reason,loggedIn):
        setup()
           

setup()
