from pandas import DataFrame
from sklearn.model_selection import train_test_split

from etl import feature_engineering as fe


_cache = None

def get_splits( X, y):

    global _cache
    if _cache is not None:
        return _cache

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y,
        test_size=0.15,
        random_state=42,
        stratify=y
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val,
        test_size=0.176,
        random_state=42,
        stratify=y_train_val
    )

    print(f"Train:      {X_train.shape} — {y_train.sum()} ataques")
    print(f"Validation: {X_val.shape} — {y_val.sum()} ataques")
    print(f"Test:       {X_test.shape} — {y_test.sum()} ataques")

    _cache = (X_train, X_val, X_test, y_train, y_val, y_test)
    return _cache
