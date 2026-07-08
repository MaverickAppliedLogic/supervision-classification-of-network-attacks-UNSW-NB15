import ipaddress
import pandas as pd
from pandas import DataFrame
from data import csv_repository as csvr
from data import apis_repository as apir

ENRICHMENT_COLUMNS = {
    'vt_malicious': None, 'vt_suspicious': None, 'vt_reputation': None,
    'vt_country': None, 'vt_votes_malicious': None,
    'ab_score': None, 'ab_total_reports': None, 'ab_distinct_users': None,
    'ab_is_tor': None, 'ab_is_whitelisted': None, 'ab_last_reported': None
}


def is_private_ip(ip) -> bool:
    try:
        return ipaddress.ip_address(ip).is_private
    except ValueError:
        return False


def get_data() -> DataFrame:
    df = csvr.get_data()

    unique_ip = df['srcip'].unique()

    results = []
    for ip in unique_ip:
        row = {'srcip': ip}

        if is_private_ip(ip):
            row.update(ENRICHMENT_COLUMNS)
            results.append(row)
            continue

        try:
            vt_data = apir.get_virustotal_reputation(ip)
            row['vt_malicious'] = vt_data['data']['attributes']['last_analysis_stats']['malicious']
            row['vt_suspicious'] = vt_data['data']['attributes']['last_analysis_stats']['suspicious']
            row['vt_reputation'] = vt_data['data']['attributes']['reputation']
            row['vt_country'] = vt_data['data']['attributes']['country']
            row['vt_votes_malicious'] = vt_data['data']['attributes']['total_votes']['malicious']
        except Exception as e:
            print(f"VirusTotal error para {ip}: {e}")
            row.update({'vt_malicious': None, 'vt_suspicious': None,
                        'vt_reputation': None, 'vt_country': None,
                        'vt_votes_malicious': None})

        try:
            ab_data = apir.get_abuseipdb_reputation(ip)
            row['ab_score'] = ab_data['data']['abuseConfidenceScore']
            row['ab_total_reports'] = ab_data['data']['totalReports']
            row['ab_distinct_users'] = ab_data['data']['numDistinctUsers']
            row['ab_is_tor'] = ab_data['data']['isTor']
            row['ab_is_whitelisted'] = ab_data['data']['isWhitelisted']
            row['ab_last_reported'] = ab_data['data']['lastReportedAt']
        except Exception as e:
            print(f"AbuseIPDB error para {ip}: {e}")
            row.update({'ab_score': None, 'ab_total_reports': None,
                        'ab_distinct_users': None, 'ab_is_tor': None,
                        'ab_is_whitelisted': None, 'ab_last_reported': None})

        results.append(row)

    df_enriched = pd.DataFrame(results)
    df_final = df.merge(df_enriched, on='srcip', how='left')

    return df_final