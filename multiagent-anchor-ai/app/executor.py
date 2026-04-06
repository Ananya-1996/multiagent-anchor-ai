from app.tools import support, weather, calendar, notes, routine, suggestion, general

def execute(steps):
    out = []

    for s in steps:
        tool = s["tool"]

        if tool == "support":
            res = support(s["input"])

        elif tool == "weather":
            res = weather(s["input"])

        elif tool == "calendar":
            res = calendar(s["input"])

        elif tool == "notes":
            res = notes(s["input"])

        elif tool == "routine":
            res = routine(s["input"])

        elif tool == "suggestion":
            res = suggestion(s["input"])

        else:
            res = general(s["input"])

        out.append(res)

    return out
