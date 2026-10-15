import json, sys
sys.path.insert(0,"../catalogo")
src=open("../catalogo/gerar.py").read(); ns={}; exec(src[:src.index("import html as H")],ns); P=ns["P"]
ed=open("../catalogo/editorial.py").read(); ns2={}
exec(ed[ed.index("T=["):ed.index("DARK=")],ns2)
from dados import D
prods=[]
for i,(nm,m,o,e,d,p,pd,pr,desc) in enumerate(P):
    prods.append(dict(id=f"{i+1:02d}",t1=ns2["T"][i][0],t2=ns2["T"][i][1],kick=ns2["K"][i],marca=m,origem=o,emb=e,doses=d,
      preco=None if p=="EM FALTA" else float(p.replace(".","").replace(",",".")),dose=pd,prazo=pr,para=ns2["Q"][i],
      ben=D[i]["ben"],uso=D[i]["uso"],porcao=D[i]["porcao"],nut=D[i]["nut"],con=D[i]["con"],cat=0 if i<4 else (1 if i<8 else 2)))
html=open("template.html").read().replace("/*PRODUTOS*/",json.dumps(prods,ensure_ascii=False))
open("index.html","w").write(html)
print(len(prods))
