import re
from app.db import save_event, get_events, update_dashboard

AVAILABLE_SLOTS = ["9AM", "10AM", "11AM", "2PM", "3PM", "4PM"]


def extract_time(text):
    match = re.search(r'\b(\d{1,2}(AM|PM|am|pm))\b', text)
    return match.group(1).upper() if match else "10AM"


# 💙 SUPPORT AGENT
def support(x):
    text = x.lower()

    if "happy" in text:
        mood = "😊 happy"

    elif any(w in text for w in ["sad", "down", "low"]):
        mood = "😔 sad"

    elif any(w in text for w in ["stress", "overwhelmed", "anxious", "failed"]):
        mood = "😟 stressed"

    else:
        mood = "🙂 okay"

    update_dashboard(mood=mood)

    return {
        "msg": f"""💙 Thanks for sharing.

I sense you're feeling {mood}.

👉 Want help planning your next step or creating a routine?"""
    }


# 🌤 WEATHER AGENT
def weather(x):
    return {
        "msg": """🌤️ **Today's Outlook**
• Calm weather  
• Good time for focus  
• Take things gently"""
    }


# 📅 CALENDAR AGENT
def calendar(x):
    t = extract_time(x)
    booked = [e[2] for e in get_events()]

    if t in booked:
        free = [s for s in AVAILABLE_SLOTS if s not in booked]
        return {
            "msg": f"💙 {t} is already booked.\n👉 Try: {', '.join(free[:3])}"
        }

    save_event(x, t)

    update_dashboard(task_increment=1)

    return {
        "msg": f"""✨ **Meeting Confirmed**

🕒 {t}  
📍 Google Meet  

🔗 https://meet.google.com/{t.lower()}-demo  

📅 Invite sent successfully"""
    }


# 📝 NOTES AGENT
def notes(x):
    update_dashboard(task_increment=1)

    return {
        "msg": """📝 **Notes Created**

🔗 https://docs.google.com/document/d/demo-notes  

📂 Saved in Personal Workspace"""
    }


# ✅ TASK AGENT
def task(x):
    update_dashboard(task_increment=1)

    return {
        "msg": "✅ Task added. One step at a time."
    }


# 🌿 ROUTINE AGENT (🔥 UPGRADED)
def routine(x):
    return {
        "msg": """🌿 **A Gentle Reset Plan for Today**

💙 I’m really sorry about the interview. That’s tough — but this is not the end of your journey.

---

🌅 **Morning (Start Soft)**
• Take a short walk or sit in fresh air  
• Write down 1 thing you did well in the interview  
• Do ONE small task (update resume / apply to 1 job)

---

☀️ **Afternoon (Build Momentum)**
• Learn or revise one key skill (30–60 mins)  
• Practice 2–3 interview questions  
• Reach out to 1 connection / recruiter  

---

🌙 **Evening (Reset & Recharge)**
• Do something relaxing (music, journaling, light walk)  
• Avoid overthinking — today was enough  
• Sleep early — your energy matters  

---

✨ **Reminder**
This is a phase, not your final outcome.  
You’re still moving forward — one step at a time.

💙 I’m here with you. Want help preparing for your next interview?"""
    }


# 💡 SUGGESTION AGENT
def suggestion(x):
    return {
        "msg": """💡 **Next Step**
• Add reminder  
• Break into smaller steps  
• Stay consistent"""
    }


# 🤖 GENERAL AGENT
def general(x):
    return {
        "msg": "💙 I'm here with you. What would you like to do next?"
    }
