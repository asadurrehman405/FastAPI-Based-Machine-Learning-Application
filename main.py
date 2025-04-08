import pandas as pd
from fastapi import FastAPI, Depends,File, UploadFile
from sqlalchemy.orm import Session
import joblib
import numpy as np
from database import get_db
from database import Base
from train_model import model_train
from schemas import LoanData, PredictionOut
from database import engine, SessionLocal
from crud import create_prediction, get_predictions
import preprocessing
import io
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        return {"error": "Only CSV files are allowed"}
    # Read the file content
    contents = await file.read()

    # Use io.BytesIO to turn the bytes into a file-like object
    df = pd.read_csv(io.BytesIO(contents))
    message = preprocessing.df_preprocess(df)
    return {"message": message}

@app.post("/train")
def train_model():
    response = model_train()
    return {"response": response}


ml_model = joblib.load(os.path.join(os.path.dirname(__file__), "model/model.pkl"))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/predict")
def predict(data: LoanData):
    input_array = np.array([list(data.dict().values())])
    prediction = ml_model.predict(input_array)[0]
    return {"prediction": int(prediction)}

@app.post("/store_prediction", response_model=PredictionOut)
def store_prediction(data: LoanData, db: Session = Depends(get_db)):
    input_array = np.array([list(data.dict().values())])
    prediction = ml_model.predict(input_array)[0]
    db_pred = create_prediction(db, data, int(prediction))
    return db_pred



@app.get("/get_predictions")
def read_predictions(db: Session = Depends(get_db)):
    return get_predictions(db)