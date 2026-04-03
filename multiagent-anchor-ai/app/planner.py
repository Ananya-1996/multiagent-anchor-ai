def plan(text): t=text.lower();steps=[]
 if any(w in t for w in ['sad','stress','overwhelmed']): steps.append({'tool':'support','input':text})
 if any(w in t for w in ['schedule','meeting']): steps+=[{'tool':'weather','input':text},{'tool':'calendar','input':text},{'tool':'suggestion','input':text}]
 elif any(x in text.upper() for x in ['AM','PM']): steps.append({'tool':'calendar','input':text})
 if 'note' in t: steps.append({'tool':'notes','input':text})
 if 'task' in t: steps.append({'tool':'task','input':text})
 if 'routine' in t: steps.append({'tool':'routine','input':text})
 return steps or [{'tool':'general','input':text}]
