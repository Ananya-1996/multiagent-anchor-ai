import re
from app.db import save_event,get_events,save_dashboard
AVAILABLE_SLOTS=['9AM','10AM','11AM','2PM','3PM','4PM']
def extract_time(t): m=re.search(r'\b(\d{1,2}(AM|PM|am|pm))\b',t); return m.group(1).upper() if m else '10AM'
def support(x): save_dashboard('😔 stressed' if 'stress' in x or 'overwhelmed' in x else '🙂 okay'); return {'msg':'💙 It sounds like things feel heavy. Let’s take one small step.'}
def weather(x): return {'msg':'🌤️ Today looks calm. Take things gently.'}
def calendar(x): t=extract_time(x); booked=[e[2] for e in get_events()];
 if t in booked: return {'msg':f'💙 {t} is booked. Try another slot.'}
 save_event(x,t); return {'msg':f'✨ Meeting at {t}\n🔗 https://meet.google.com/{t.lower()}-demo'}
def notes(x): return {'msg':'📝 Notes saved\n🔗 https://docs.google.com/document/d/demo'}
def task(x): return {'msg':'✅ Task added'}
def routine(x): return {'msg':'🌿 Morning task | Afternoon learn | Evening rest'}
def suggestion(x): return {'msg':'💡 Add reminder or break tasks'}
def general(x): return {'msg':'💙 I’m here with you'}
