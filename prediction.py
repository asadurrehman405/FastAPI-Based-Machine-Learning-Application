import joblib
import os
import pandas as pd

def pred():
    save_dir = "preprocessed_datasets"
    model_save = "model_save"

    loaded_model = joblib.load(f'{model_save}/model.pkl')
    x_test = joblib.load(os.path.join(save_dir, "x_test.pkl"))
    y_test = joblib.load(os.path.join(save_dir, "y_test.pkl"))

    predictions = loaded_model.predict(x_test)
    results_df = pd.DataFrame({
        'Actual': y_test.values,
        'Predicted': predictions
    })

    return results_df