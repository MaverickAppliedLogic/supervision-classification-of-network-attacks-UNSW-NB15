import pandas as pd
from pandas import DataFrame
from sklearn.preprocessing import StandardScaler, LabelEncoder

_cache = None

def get_features(df: DataFrame):
    global _cache
    if _cache is not None:
        return _cache


    le = LabelEncoder()
    y = df['label']
    y_multiclass = le.fit_transform(df['attack_cat'])
    X = df.drop(columns=['attack_cat', 'label'])

    ohe_cols = ['proto', 'state', 'service', 'vt_country']
    X = pd.get_dummies(X, columns=ohe_cols, drop_first=True)

    numeric_cols = X.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    X[numeric_cols] = scaler.fit_transform(X[numeric_cols])

    print(f"Features shape: {X.shape}")
    print(f"Target shape: {y.shape}")
    print(f"Columnas tras OHE: {X.shape[1]}")
    print(f"Categorías attack_cat:\n{dict(zip(le.classes_, le.transform(le.classes_)))}")

    _cache = (X, y, y_multiclass, scaler, le)
    return _cache