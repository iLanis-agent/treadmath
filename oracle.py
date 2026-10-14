import json, math

def pos(x): return isinstance(x,(int,float)) and math.isfinite(x) and x>0
def jround(x): return math.floor(x+0.5)
def jsnum(x):
    if isinstance(x,float) and x==int(x): return str(int(x))
    return str(x)
def r1(x): return jround(x*10)/10

def motor_plan(peakHp):
    if not pos(peakHp): return {"error":"the peak horsepower must be above zero"}
    chp=peakHp*0.5
    if chp<1.5: verdict="walking territory"
    elif chp<2.5: verdict="jogging is fine, running is borrowed"
    else: verdict="a runner's motor"
    return {"chp":r1(chp),"verdict":verdict}

def render_motor(r,peakHp):
    return "The "+jsnum(peakHp)+" peak HP sticker figures about "+jsnum(r["chp"])+" continuous HP - "+r["verdict"]+"."

def deck_plan(heightIn,use):
    if not pos(heightIn): return {"error":"your height must be above zero"}
    base={"walk":50,"jog":54,"run":58}.get(use)
    width={"walk":18,"jog":20,"run":22}.get(use)
    if base is None: return {"error":"pick walk, jog or run"}
    return {"length":base+(2 if heightIn>74 else 0),"width":width}

def render_deck(r,heightIn,use):
    return ("At "+jsnum(heightIn)+" in planning to "+use+" you want about a "+jsnum(r["length"])+" in x "
            +jsnum(r["width"])+" in deck - anything shorter borrows your stride.")

def pace_plan(mph):
    if not pos(mph): return {"error":"the speed must be above zero"}
    secMile=jround(3600/mph)
    secKm=jround(3600/(mph*1.609344))
    def fmt(s): return f"{s//60}:{s%60:02d}"
    return {"mile":fmt(secMile),"km":fmt(secKm)}

def render_pace(r,mph):
    return "The belt at "+jsnum(mph)+" mph is "+r["mile"]+" per mile and "+r["km"]+" per km."

cases=[]
def add(tool,args):
    if tool=="motor": r=motor_plan(*args); fn=render_motor
    elif tool=="deck": r=deck_plan(*args); fn=render_deck
    else: r=pace_plan(*args); fn=render_pace
    case={"tool":tool,"args":args,"result":r}
    if "error" not in r: case["render"]=fn(r,*args)
    cases.append(case)

for a in [(3.0,),(2.5,),(4.0,),(1.5,),(5.0,),(2.0,),(4.75,),(6.0,)]:
    add("motor",a)
for a in [(71,"run"),(66,"walk"),(70,"jog"),(75,"run"),(78,"run"),(64,"walk"),(72,"jog"),(76,"walk")]:
    add("deck",a)
for a in [(6.0,),(6.2,),(5.0,),(7.5,),(4.0,),(10.0,),(3.5,),(8.6,)]:
    add("pace",a)
add("motor",[0]); add("deck",[0,"run"]); add("deck",[70,"sprint"]); add("pace",[0])

json.dump(cases,open("expected.json","w"),separators=(",",":"))
print(len(cases),"cases")
