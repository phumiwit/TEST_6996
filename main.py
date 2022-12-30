from fastapi import FastAPI
import uvicorn
from key import Keyword_Spotting_Service
from pydantic import BaseModel
import json
app = FastAPI()

class File(BaseModel):
    file: str
    
class File1(BaseModel):
    file:str
    
@app.get('/')
def Hello():
    return {'Hello':'Hello'}

@app.post('/predict')
def predict(path:File):
    input_data = path.json()
    input_dict = json.loads(input_data)
    PATH = input_dict['file']
    kss = Keyword_Spotting_Service()
    keyword1,keyword2= kss.prediction(PATH)
    return keyword1

@app.post('/value')
def value(path:File1):
    input_data = path.json()
    input_dict = json.loads(input_data)
    PATH = input_dict['file']
    kss = Keyword_Spotting_Service()
    keyword1,keyword2 = kss.prediction(PATH)
    return keyword2


if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port=8000)