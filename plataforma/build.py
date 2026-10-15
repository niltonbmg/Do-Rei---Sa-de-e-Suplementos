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
import base64
from PIL import Image
import io
def uri(path,fmt=None):
    if path.endswith(".svg"): return "data:image/svg+xml;base64,"+base64.b64encode(open(path,"rb").read()).decode()
    im=Image.open(path).convert("RGB"); im.thumbnail((600,600)); b=io.BytesIO(); im.save(b,"JPEG",quality=82); return "data:image/jpeg;base64,"+base64.b64encode(b.getvalue()).decode()
html=html.replace('src="logo-horizontal-branca.svg"','src="'+uri("logo-horizontal-branca.svg")+'"')
fotos={p["id"]:uri(f"fotos/{p['id']}.jpg") for p in prods}
html=html.replace("const PRODUTOS=","const FOTOS="+json.dumps(fotos)+";\nconst PRODUTOS=")
html=html.replace('src="fotos/${p.id}.jpg"','src="${FOTOS[p.id]}"')
open("index.html","w").write(html)
print(len(prods))
