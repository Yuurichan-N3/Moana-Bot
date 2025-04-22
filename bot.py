import requests
import random
import string
from web3 import Web3
from colorama import init, Fore, Style

# Initialize colorama for colored output
init()

# Banner
print(Fore.BLUE + """
╔══════════════════════════════════════════════╗
║       🌟 MOANA AGENT BOT - Automation        ║
║ Automate user registration for AgentMoana!   ║
║  Developed by: https://t.me/sentineldiscus   ║
╚══════════════════════════════════════════════╝
""" + Style.RESET_ALL)

# Endpoint URL
url = "https://moana-y43h.onrender.com/user"

# Headers 
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "id-ID,id;q=0.9,ja-ID;q=0.8,ja;q=0.7,en-ID;q=0.6,en;q=0.5,en-US;q=0.4",
    "content-type": "application/json",
    "origin": "https://agentmoana.xyz",
    "priority": "u=1, i",
    "referer": "https://agentmoana.xyz/",
    "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

# Function to generate a random Twitter-like username
def generate_random_twitter_username():
    length = random.randint(5, 15)
    characters = string.ascii_lowercase + string.digits + "_."
    username = ''.join(random.choice(characters) for _ in range(length))
    return username + ".fx"  # Append .fx to mimic the provided example

# Function to generate a new Ethereum wallet address
def generate_wallet_address():
    w3 = Web3()
    account = w3.eth.account.create()
    return account.address

# Function to send a single POST request
def send_request(invite_code, request_number):
    try:
        # Generate payload
        payload = {
            "wallet": generate_wallet_address(),
            "twitter": generate_random_twitter_username(),
            "invite": invite_code
        }

        # Send POST request
        response = requests.post(url, json=payload, headers=headers)

        # Colored output
        print(Fore.BLUE + f"Request #{request_number}" + Style.RESET_ALL)
        print(f"Status: {response.status_code}")
        print(f"Wallet: {payload['wallet']}")
        print(f"Twitter: {payload['twitter']}")
        print(f"Invite Code: {payload['invite']}")
        
        # Check if request was successful
        if response.status_code == 201:
            print(Fore.GREEN + "Result: Success" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Result: Failed" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"Request #{request_number} - Error: {str(e)}" + Style.RESET_ALL)

# Get number of requests from user
try:
    num_requests = int(input("Enter the number of requests to send: "))
    if num_requests <= 0:
        print(Fore.RED + "Number of requests must be positive." + Style.RESET_ALL)
        exit()
except ValueError:
    print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)
    exit()

# Get invite code from user input (with default)
invite_code = input("Enter the invite code (press Enter for default 'y19YjY4U'): ").strip()
if not invite_code:
    invite_code = "y19YjY4U"
    print(Fore.BLUE + f"Using default invite code: {invite_code}" + Style.RESET_ALL)

# Send requests sequentially with request counter
for i in range(num_requests):
    send_request(invite_code, i + 1)

print(Fore.BLUE + f"Completed sending {num_requests} requests." + Style.RESET_ALL)
