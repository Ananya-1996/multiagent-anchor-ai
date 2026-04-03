
def plan(text):
    t=text.lower()
    steps=[]

    if any(w in t for w in ["sad","stress","anxious","lost","overwhelmed"]):
        steps.append({"tool":"support","input":text})

    if "routine" in t:
        steps.append({"tool":"routine","input":text})

    if any(w in t for w in ["schedule","meeting"]):
        steps.append({"tool":"weather","input":text})
        steps.append({"tool":"calendar","input":text})
        steps.append({"tool":"suggestion","input":text})

    if "task" in t:
        steps.append({"tool":"task","input":text})

    if "note" in t or "notes" in t:
        steps.append({"tool":"notes","input":text,"condition":"after_calendar"})

    if not steps:
        steps=[{"tool":"general","input":text}]

    return steps
