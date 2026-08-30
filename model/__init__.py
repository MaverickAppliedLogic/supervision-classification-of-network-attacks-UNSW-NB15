from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from model import splitting as sp

def train_and_evaluate(X, y, y_multi, scaler, le):
    X_train, X_val, X_test, y_train, y_val, y_test = sp.get_splits(X, y)

    print("Entrenando Random Forest...")
    model = RandomForestClassifier(
        n_estimators=100,
        class_weight='balanced',
        random_state=42,
        n_jobs=-1  # usa todos los cores disponibles
    )

    model.fit(X_train, y_train)

    print("\n=== VALIDACIÓN ===")
    y_pred_val = model.predict(X_val)
    print(classification_report(y_val, y_pred_val, target_names=['Normal', 'Ataque']))
    print("Matriz de confusión:")
    print(confusion_matrix(y_val, y_pred_val))

    print("\n=== TEST ===")
    y_pred_test = model.predict(X_test)
    print(classification_report(y_test, y_pred_test, target_names=['Normal', 'Ataque']))
    print("Matriz de confusión:")
    print(confusion_matrix(y_test, y_pred_test))

    return model