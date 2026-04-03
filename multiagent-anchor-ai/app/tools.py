
import re, random
from app.db import save_event,get_events,save_memory,get_last_memory

def extract_time(t):
    m=re.search(r'\b(\d{1,2}(?:AM|PM|am|pm))\b',t)
    return m.group(1).upper() if m else "10AM"

def support(x):
    save_memory(x)
    last=get_last_memory()
    return {"msg":f"💙 I remember you said: '{last}'. Let's take one small step together."}

def weather(x):
    return {"msg":"🌤️ Today looks calm. Take things gently."}

def calendar(x):
    t=extract_time(x)
    if any(t in str(e) for e in get_events()):
        return {"msg":"💙 That time is full. Want to try another?"}
    save_event(x,t)
    return {"msg":f"✨ Scheduled for {t}. You're making progress."}

def task(x):
    return {"msg":"✅ Small step added. One thing at a time."}

def notes(x):
    return {"msg":"📝 Noted. You're organizing your thoughts."}

def routine(x):
    return {"msg":"🌿 Here's a simple routine: Morning: 1 task, Afternoon: learn something, Evening: rest."}

def suggestion(x):
    return {"msg":"💡 Would you like me to add a reminder or break this into smaller steps?"}

def general(x):
    return {"msg":"💙 I'm here with you. What would you like to do next?"}
