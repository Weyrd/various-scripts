import requests
import asyncio
import os
# console clear lambda
clear = lambda : os.system('cls')
# getting application id
app_id = input("Application ID ?\n")
clear()
# getting bot token for headers authorization
bot_token = input("Bot Token ?\n")
clear()
headers = {
    "Authorization": f"Bot {bot_token}"
}
# guild or global commands
suite = False
while suite == False:
    guild_or_global = input("Serveur (s) ou global (g) ?\n")
    clear()
    # guild commands
    if guild_or_global == "s":
        suite = True
        guild_id = input("Guild ID ?\n")
        clear()
        url_get = f"https://discord.com/api/v8/applications/{app_id}/guilds/{guild_id}/commands"
    # global commands
    elif guild_or_global == "g":
        suite = True
        url_get = f"https://discord.com/api/v8/applications/{app_id}/commands"
    else:
        input("Please, enter s for serveur command or g for global command.")
# getting commands name and id
msg = ""
with requests.get(url_get, headers=headers) as r:
    re = r.json()
    for i in re:
        re_name = i["name"]
        re_id = i["id"]
        msg += f"{re_name} : {re_id}\n"
        
    if msg == "":
        print("Seems there is no command known for what you asked.")
    else:
        print(msg)
# input command id to delete it (loop : stopped when ctrl+c)
try:
    while True:
        identi = input("Command id ? (ctrl+c to exit)\n")
        url_delete = f"{url_get}/{identi}"
        # requests delete the command
        rd = requests.delete(url_delete, headers=headers)
        if rd.status_code == 204:
            print("Command perfectly deleted!")
        elif rd.status_code == 404:
            print("Command id unknow.")
except KeyboardInterrupt:
    pass