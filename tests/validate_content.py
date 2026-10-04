import json, pathlib, sys
R=pathlib.Path(__file__).resolve().parents[1]
def j(n):
    with open(R/n,encoding="utf-8") as f:return json.load(f)
def main():
    v=j("vocab.json"); q=j("quizzes.json"); e=j("explanations.json"); t=j("trilingual.json")
    assert len(v)==978
    assert len(q)==2550
    assert sum(len(x["questions"]) for x in q)==25500
    assert all(len(x["options"])==5 for z in q for x in z["questions"])
    assert len(e)>=20 and len(t)>=2000
    print("VALID",len(v),len(q),len(e),len(t))
if __name__=="__main__":
    try:main()
    except Exception as e:print("INVALID",e);sys.exit(1)
