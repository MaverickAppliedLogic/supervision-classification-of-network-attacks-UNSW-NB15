import etl
import model

def gen_model():
    X, y, y_multi, scaler, le = etl.get_data()
    model.train_and_evaluate(X, y, y_multi, scaler, le)