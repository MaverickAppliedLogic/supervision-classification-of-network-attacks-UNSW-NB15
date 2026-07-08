import services.virustotal_conn as vtc
import services.abuseipdb_conn as aic
import json

def get_virustotal_reputation(ip)->json:
    return vtc.check_ip_virustotal(ip)

def get_abuseipdb_reputation(ip)->json:
    return aic.check_ip_abuseipdb(ip)