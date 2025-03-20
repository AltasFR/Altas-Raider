import requests
import time
from colorama import Fore, Style

ascii_art = f"""{Fore.MAGENTA}
 ▄████████  ▄█           ███        ▄████████    ▄████████ 
  ███    ███ ███       ▀█████████▄   ███    ███   ███    ███ 
  ███    ███ ███          ▀███▀▀██   ███    ███   ███    █▀  
  ███    ███ ███           ███   ▀   ███    ███   ███        
▀███████████ ███           ███     ▀███████████ ▀███████████ 
  ███    ███ ███           ███       ███    ███          ███ 
  ███    ███ ███▌    ▄     ███       ███    ███    ▄█    ███ 
  ███    █▀  █████▄▄██    ▄████▀     ███    █▀   ▄████████▀   
{Style.RESET_ALL}"""

def spam_webhook(webhook_url, message):
    payload = {"content": message}
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            print(f"{Fore.GREEN}[!] Message successful.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[!] Message failed. Status code: {response.status_code}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Message failed. Error: {e}{Style.RESET_ALL}")

def main():
    print(ascii_art)

    file_path = input(f"{Fore.MAGENTA}Enter the path to the txt file with webhook URLs: {Style.RESET_ALL}")

    try:
        with open(file_path, "r") as file:
            webhook_urls = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"{Fore.RED}File not found. Please check the file path.{Style.RESET_ALL}")
        return

    message = input(f"{Fore.MAGENTA}Enter the message to spam: {Style.RESET_ALL}")
    
    try:
        times = int(input(f"{Fore.MAGENTA}Enter the number of times to spam: {Style.RESET_ALL}"))
        delay = float(input(f"{Fore.MAGENTA}Enter delay between messages (in seconds): {Style.RESET_ALL}"))
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter numbers only.{Style.RESET_ALL}")
        return

    for i in range(times):
        print(f"{Fore.MAGENTA}Spam cycle {i+1}/{times}{Style.RESET_ALL}")
        for webhook_url in webhook_urls:
            spam_webhook(webhook_url, message)
        time.sleep(delay)

if __name__ == "__main__":
    main()
