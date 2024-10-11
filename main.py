from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import pandas as pd
import json
import random
from pydantic import BaseModel
app = FastAPI()
df = pd.read_excel('static/info.xlsx', dtype=str)
user_str_data = df.to_json(orient='records', force_ascii=False)
user_data = json.loads(user_str_data)
df1 = pd.read_excel('static/questions.xlsx', sheet_name="Sheet1", dtype=str)
choose_question_str_data = df1.to_json(orient='records', force_ascii=False)
choose_questions_data = json.loads(choose_question_str_data)
df2 = pd.read_excel('static/questions.xlsx', sheet_name="Sheet2", dtype=str)
judge_question_str_data = df2.to_json(orient='records', force_ascii=False)
judge_questions_data = json.loads(judge_question_str_data)
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
    res = random.sample(choose_questions_data, 20) + random.sample(judge_questions_data, 10)
    return res
@app.get("/chooseQuestions/{filename}")
def get_choose_pic(filename:str):
    return FileResponse("static/chooseQuestions/" + filename, media_type="image/png")
@app.get("/judgeQuestions/{filename}")
def get_judge_pic(filename:str):
    return FileResponse("static/judgeQuestions/" + filename, media_type="image/png")
# 允许所有来源的跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)