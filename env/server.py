from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
from pydantic import BaseModel
import json
import time

app = FastAPI()

@app.get("/")
def read_root():
    jsonD = 'data.json'
    with open(jsonD,'r') as file:
        dataForex=json.load(file)
    return dataForex