import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('VIRUSTOTAL_API_KEY')

def check_ip_virustotal(ip)->json:
    url = "https://www.virustotal.com/api/v3/ip_addresses/" + ip
    headers = {
        "accept": "application/json",
        "x-apikey": api_key
    }
    response = requests.get(url, headers=headers)
    return json.loads(response.text)