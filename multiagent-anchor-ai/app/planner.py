def plan(user_input):
    text = user_input.lower()

    steps = []

    if "schedule" in text or "meeting" in text:
        steps.append({"tool": "calendar", "input": user_input})

    elif "note" in text:
        steps.append({"tool": "notes", "input": user_input})

    elif "routine" in text:
        steps.append({"tool": "routine", "input": user_input})

    elif "weather" in text:
        steps.append({"tool": "weather", "input": user_input})

    elif "stress" in text or "happy" in text:
        steps.append({"tool": "support", "input": user_input})

    else:
        steps.append({"tool": "general", "input": user_input})

    return steps
