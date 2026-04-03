from app.tools import support,weather,calendar,task,notes,routine,suggestion,general
MAP={'support':support,'weather':weather,'calendar':calendar,'task':task,'notes':notes,'routine':routine,'suggestion':suggestion,'general':general}
def execute(steps): return [MAP[s['tool']](s['input']) for s in steps]
