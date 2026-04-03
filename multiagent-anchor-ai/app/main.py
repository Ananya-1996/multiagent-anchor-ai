
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.planner import plan
from app.executor import execute

app=FastAPI()

class Input(BaseModel):
    message:str

@app.get("/")
def ui():
    return FileResponse("frontend/index.html")

@app.post("/chat")
def chat(i:Input):
    steps=plan(i.message)
    res=execute(steps)
    return {"message":" ".join([r["msg"] for r in res])}
