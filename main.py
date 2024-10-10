from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import pandas as pd
import json
from pydantic import BaseModel
app = FastAPI()
df = pd.read_excel('static/info.xlsx', dtype=str)
user_str_data = df.to_json(orient='records', force_ascii=False)
user_data = json.loads(user_str_data)
class User(BaseModel):
    classData: str
    numberData: str
    username: str
@app.post("/login")
def login(user: User):
    for item in user_data:
        if item["classData"] == user.classData and item["numberData"] == user.numberData and item["username"] == user.username:
            return {"code": 200, "user": item}
    return {"code":401, "user": {}}
@app.get("/examination")
def exam():
    paths = []
    for i in range(1, 21):
        paths.append("static/chooseQuestions/" + str(i) + ".png")
    for i in range(21, 31):
        paths.append("static/judgeQuestions/" + str(i) + ".png")
    return [FileResponse(path) for path in paths]
    # return FileResponse("static/chooseQuestions/1.png")
# 允许所有来源的跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)