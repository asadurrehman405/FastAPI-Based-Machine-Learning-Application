import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import pandas as pd
import numpy as np

def df_preprocess(df):
    save_dir = "preprocessed_datasets"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        print(f"Directory '{save_dir}' created successfully.")
    else:
        print(f"Directory '{save_dir}' already exists.")
    df=df.drop("Loan_ID",axis=1)
    df.drop_duplicates(inplace=True)
    df.dropna(axis=0, inplace=True)
    le = LabelEncoder()
    columns_to_encode = ['Loan_Status', 'Self_Employed', 'Married', 'Education', 'Gender']
    for col in columns_to_encode:
        df[col] = le.fit_transform(df[col])
    ohe = OneHotEncoder(drop='first', sparse_output=False, dtype=np.int32)
    df2 = ohe.fit_transform(df[['Property_Area']])
    df3 = ohe.transform(df[['Property_Area']])
    ohe = OneHotEncoder(drop='first', sparse_output=False, dtype=np.int32)
    df2 = ohe.fit_transform(df[['Property_Area']])
    ohe_columns = ohe.get_feature_names_out(['Property_Area'])
    df2 = pd.DataFrame(df2, columns=ohe_columns, index=df.index)
    df = pd.concat([df, df2], axis=1)
    df=df.drop(['Property_Area'],axis=1)
    x = df.drop('Loan_Status', axis=1)
    y = df['Loan_Status']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


    joblib.dump(x_train, os.path.join(save_dir, "x_train.pkl"))
    joblib.dump(x_test, os.path.join(save_dir, "x_test.pkl"))
    joblib.dump(y_train, os.path.join(save_dir, "y_train.pkl"))
    joblib.dump(y_test, os.path.join(save_dir, "y_test.pkl"))

    return "Datasets are saved"