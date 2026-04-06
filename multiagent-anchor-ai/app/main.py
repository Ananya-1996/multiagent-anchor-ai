from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.planner import plan
from app.executor import execute
from app.db import get_dashboard

app = FastAPI()

class Input(BaseModel):
    message: str


@app.get("/")
def ui():
    return FileResponse("frontend/index.html")


@app.post("/chat")
def chat(i: Input):
    steps = plan(i.message)
    res = execute(steps)

    agent_map = {
        "support": "💙 Support Agent",
        "weather": "🌤 Weather Agent",
        "calendar": "📅 Calendar Agent",
        "notes": "📝 Notes Agent",
        "routine": "🌿 Routine Agent",
        "suggestion": "💡 Suggestion Agent",
        "general": "🤖 Assistant"
    }

    message_blocks = []
    for s, r in zip(steps, res):
        agent_name = agent_map.get(s["tool"], "Agent")
        message_blocks.append(f"{agent_name}\n{r['msg']}")

    mood, tasks_done, streak = get_dashboard()

    return {
        "message": "\n\n".join(message_blocks),
        "agents": [agent_map.get(s["tool"], s["tool"]) for s in steps],
        "dashboard": {
            "mood": mood,
            "tasks": tasks_done,
            "streak": streak
        }
    }
