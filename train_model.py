from sklearn.neighbors import KNeighborsClassifier
import joblib
import os
import pickle

def model_train():
    save_dir = "preprocessed_datasets"
    model_save = "model_save"
    if not os.path.exists(model_save):
        os.makedirs(model_save)
        print(f"Directory '{model_save}' created successfully.")
    else:
        print(f"Directory '{model_save}' already exists.")
    lr = KNeighborsClassifier()

    x_train = joblib.load(os.path.join(save_dir, "x_train.pkl"))
    y_train = joblib.load(os.path.join(save_dir, "y_train.pkl"))

    lr.fit(x_train, y_train)

    with open(f'{model_save}/model.pkl', 'wb') as file:
        pickle.dump(lr, file)

    return "Model is saved"
