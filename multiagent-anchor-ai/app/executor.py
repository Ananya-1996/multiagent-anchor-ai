
from app.tools import support,weather,calendar,task,notes,general,routine,suggestion

MAP={"support":support,"weather":weather,"calendar":calendar,"task":task,"notes":notes,"general":general,"routine":routine,"suggestion":suggestion}

def execute(steps):
    res=[]
    ok=False

    for s in steps:
        if s.get("condition")=="after_calendar" and not ok:
            continue

        r=MAP[s["tool"]](s["input"])
        res.append(r)

        if s["tool"]=="calendar" and "scheduled" in r["msg"].lower():
            ok=True

    return res
