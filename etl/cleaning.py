# etl/cleaning.py
import pandas as pd
from pandas import DataFrame


_clean_df = None

def get_clean_data(df: DataFrame) -> pd.DataFrame:
    global _clean_df
    if _clean_df is not None:
        return _clean_df

    # 1. Eliminar duplicados
    before = len(df)
    df = df.drop_duplicates()
    print(f"Duplicados eliminados: {before - len(df)}")

    # 2. Rellenar attack_cat nulos con Normal y limpiar espacios
    df['attack_cat'] = df['attack_cat'].fillna('Normal').str.strip()

    # 3. Eliminar columnas AbuseIPDB — sin señal en dataset de laboratorio
    cols_drop = [
        'ab_score', 'ab_total_reports', 'ab_distinct_users',
        'ab_is_tor', 'ab_is_whitelisted', 'ab_last_reported'
    ]
    df = df.drop(columns=cols_drop)

    # 4. Convertir sport y dsport a numérico — tienen valores mixtos
    df['sport'] = pd.to_numeric(df['sport'], errors='coerce')
    df['dsport'] = pd.to_numeric(df['dsport'], errors='coerce')

    # 5. Rellenar nulos de sport y dsport con mediana
    df['sport'] = df['sport'].fillna(df['sport'].median())
    df['dsport'] = df['dsport'].fillna(df['dsport'].median())

    # 6. Rellenar nulos de columnas VT con 0
    vt_cols = ['vt_malicious', 'vt_suspicious', 'vt_reputation', 'vt_votes_malicious']
    df[vt_cols] = df[vt_cols].fillna(0)

    # 7. vt_country nulo rellenar con Unknown
    df['vt_country'] = df['vt_country'].fillna('Unknown')

    # 8. Eliminar IPs — no son features útiles para ML
    df = df.drop(columns=['srcip', 'dstip'])

    # 9. Convertir Stime y Ltime a datetime y extraer features útiles
    df['Stime'] = pd.to_datetime(df['Stime'], unit='s')
    df['Ltime'] = pd.to_datetime(df['Ltime'], unit='s')
    df['hour'] = df['Stime'].dt.hour
    df['day_of_week'] = df['Stime'].dt.dayofweek
    df = df.drop(columns=['Stime', 'Ltime'])

    print(f"Dataset limpio: {df.shape}")
    print(f"Nulos restantes:\n{df.isnull().sum()[df.isnull().sum() > 0]}")
    print(f"\nDistribución label:\n{df['label'].value_counts()}")
    print(f"\nCategorías attack_cat:\n{df['attack_cat'].value_counts()}")

    _clean_df = df
    return _clean_df