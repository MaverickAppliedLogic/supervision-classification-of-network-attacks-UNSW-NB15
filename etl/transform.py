import pandas as pd
from etl import extraction as ext

_df = None

def _get_df():
    global _df
    if _df is None:
        _df = ext.get_data()
    return _df


def get_network_conn_info():
    df = _get_df()
    nci = {
        'srcIP': df.iloc[:, 0],
        'srcPort': df.iloc[:, 1],
        'dstIP': df.iloc[:, 2],
        'dstPort': df.iloc[:, 3],
        'protocol': df.iloc[:, 4],
        'state': df.iloc[:, 5],
        'dur': df.iloc[:, 6]
    }
    return pd.DataFrame(nci)

def get_ip_reputation():
    df = _get_df()
    rep = {
        'srcIP': df['srcip'],
        'malicious': df['vt_malicious'],
        'suspicious': df['vt_suspicious'],
        'reputation': df['vt_reputation'],
        'country': df['vt_country'],
        'votes_malicious': df['vt_votes_malicious'],
        'score': df['ab_score'],
        'total_reports': df['ab_total_reports'],
        'distinct_users': df['ab_distinct_users'],
        'is_tor': df['ab_is_tor'],
        'is_whitelisted': df['ab_is_whitelisted'],
        'last_reported': df['ab_last_reported']
    }
    return pd.DataFrame(rep)

def get_traffic_stats():
    df = _get_df()
    ts = {
        'srcBytes': df.iloc[:, 7],
        'dstBytes': df.iloc[:, 8],
        'sttl': df.iloc[:, 9],
        'dttl': df.iloc[:, 10],
        'srcLoss': df.iloc[:, 11],
        'destLoss': df.iloc[:, 12],
        'srcBitsPS': df.iloc[:, 14],
        'destBitsPS': df.iloc[:,15],
        'srcPkts': df.iloc[:, 16],
        'destPkts': df.iloc[:, 17]
    }
    return pd.DataFrame(ts)


def get_tcp_info():
    df = _get_df()
    tcp = {
        'swin': df.iloc[:, 18],
        'dwin': df.iloc[:, 19],
        'stcpb': df.iloc[:, 20],
        'dtcpb': df.iloc[:, 21],
        'tcprtt': df.iloc[:, 32],
        'synack': df.iloc[:, 33],
        'ackdat': df.iloc[:, 34]
    }
    return pd.DataFrame(tcp)


def get_flow_features():
    df = _get_df()
    ff = {
        'srcMeansz': df.iloc[:, 22],
        'destMeansz': df.iloc[:, 23],
        'trans_depth': df.iloc[:, 24],
        'res_bdy_len': df.iloc[:, 25],
        'sjit': df.iloc[:, 26],
        'djit': df.iloc[:, 27],
        'sintpkt': df.iloc[:, 30],
        'dintpkt': df.iloc[:, 31]
    }
    return pd.DataFrame(ff)


def get_timestamps():
    df = _get_df()
    ts = {
        'startTime': df.iloc[:, 28],
        'lastTime': df.iloc[:, 29]
    }
    return pd.DataFrame(ts)


def get_connection_counts():
    df = _get_df()
    cc = {
        'ct_state_ttl': df.iloc[:, 36],
        'ct_flw_http_mthd': df.iloc[:, 37],
        'ct_ftp_cmd': df.iloc[:, 39],
        'ct_srv_src': df.iloc[:, 40],
        'ct_srv_dst': df.iloc[:, 41],
        'ct_dst_ltm': df.iloc[:, 42],
        'ct_src_ltm': df.iloc[:, 43],
        'ct_src_dport_ltm': df.iloc[:, 44],
        'ct_dst_sport_ltm': df.iloc[:, 45],
        'ct_dst_src_ltm': df.iloc[:, 46]
    }
    return pd.DataFrame(cc)


def get_labels():
    df = _get_df()
    labels = {
        'service': df.iloc[:, 13],
        'is_sm_ips_ports': df.iloc[:, 35],
        'is_ftp_login': df.iloc[:, 38],
        'attack_cat': df.iloc[:, 47],
        'label': df.iloc[:, 48]
    }
    return pd.DataFrame(labels)