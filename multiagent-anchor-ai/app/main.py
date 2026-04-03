from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.planner import plan
from app.executor import execute
from app.db import get_dashboard
app=FastAPI()
class Input(BaseModel): message:str
@app.get('/')
def ui(): return FileResponse('frontend/index.html')
@app.post('/chat')
def chat(i:Input): steps=plan(i.message);res=execute(steps);mood,tasks,streak=get_dashboard(); return {'message':'\n\n'.join([r['msg'] for r in res]),'agents':[s['tool'] for s in steps],'dashboard':{'mood':mood,'tasks':tasks,'streak':streak}}
