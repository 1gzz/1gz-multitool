import requests
from colorama import Fore
from utilities.Settings.common import getheaders

def DmDeleter(token, channels):
    """
    Deletes a list of DM channels for the given user token.

    Parameters:
    - token (str): Discord user token.
    - channels (list): List of channel objects to delete.
    """
    for channel in channels:
        try:
            channel_id = channel.get('id')
            if not channel_id:
                print(f"[{Fore.YELLOW}!{Fore.RESET}] Invalid channel data: {channel}")
                continue
            
            response = requests.delete(
                f'https://discord.com/api/v9/channels/{channel_id}',
                headers=getheaders(token)
            )

            if response.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted DM: {Fore.WHITE}{channel_id}{Fore.RESET}")
            else:
                print(f"[{Fore.RED}!{Fore.RESET}] Failed to delete DM: {Fore.WHITE}{channel_id}{Fore.RESET} "
                      f"(Status: {response.status_code})")
        except Exception as e:
            print(f"[{Fore.RED}ERROR{Fore.RESET}] An error occurred: {e}")
