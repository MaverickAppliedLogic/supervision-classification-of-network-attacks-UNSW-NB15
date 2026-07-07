import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv('ABUSEIPDB_API_KEY')
url = "https://api.abuseipdb.com/api/v2/check"

def check_ip_abuseipdb(ip)->json:
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }

    response = requests.request(method='GET', url= url, headers=headers, params=querystring)
    return json.loads(response.text)