from fastapi import FastAPI, File, UploadFile
import json
from datetime import datetime,date
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI(debug=True)
with open('plot.json','r') as f:
    fileData= json.load(f)

origins = [
    "http://localhost:3000",
    # Add more origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/range/{start}/{end}')

async def xrange(start: str, end:str):
    start=datetime.fromisoformat(start)
    end=datetime.fromisoformat(end)
    x= fileData["X"]
    y= fileData["Y"]
    X_list=[]
    Y_list=[]
    for i in range(len(x)):
        datetime_obj = datetime.fromisoformat(x[i])  # Convert string to datetime object
        if start <= datetime_obj <= end:
            X_list.append(x[i])
            Y_list.append(y[i])
    return {"X":X_list, "Y":Y_list}



