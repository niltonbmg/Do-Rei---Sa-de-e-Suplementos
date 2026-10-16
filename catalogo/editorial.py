# Catálogo editorial Do Rei — gera catalogo.html, PDF e mensagens de WhatsApp.
import html as H, os
src=open("gerar.py").read(); ns={}
exec(src[:src.index("import html as H")],ns); P=ns["P"]
from dados import D
from labs import LABS
from guia import GUIA
T=[("Multivitamínico","2 por dia"),("Vitamina C","1.000 mg"),("Vitamina B12","metilcobalamina"),("N-acetilcisteína","600 mg"),("Ômega 3","concentrado"),("Vitamina D3 + K2","em gotas"),("Ferro quelato","+ vitamina C"),("Creatina","monohidratada"),("Shampoo em barra","aloe vera"),("Condicionador em barra","pitaia rosa"),("Creme dental","menta, sem flúor")]
PN=["Two-Per-Day","Gold C®","Methyl B-12","NAC 600 mg","Omegafor Plus","Bio Synergy D3 + K2 MK-7","Ferro Plus","Creatina Monohidratada","Shampoo Sólido Aloe Vera","Condicionador Sólido Pitaia Rosa","Ultra Mint Flex"]
SV=["Completa as vitaminas e minerais do dia a dia","Auxilia na imunidade e na formação do colágeno","Auxilia na energia e no sistema nervoso","Antioxidante que auxilia na proteção das células","Auxilia na manutenção de triglicerídeos saudáveis","Auxilia na saúde dos ossos, dentes e na imunidade","Auxilia na formação das células vermelhas do sangue","Auxilia no desempenho em treinos intensos","Limpa com suavidade e controla a oleosidade","Hidrata e amacia sem pesar os fios","Higiene bucal com xilitol, sem flúor"]
K=["Multivitamínico + multimineral","Vitamina C · 1.000 mg","Vitamina B12 · 1.000 mcg","N-acetil L-cisteína · 600 mg","Ômega 3 · EPA + DHA","Vitaminas A, D3, E e K2 · gotas","Ferro quelato + vitamina C","Creatina · 3 g por dose","Shampoo sólido em barra","Condicionador sólido em barra","Creme dental com xilitol"]
Q=["Para adultos que querem uma base nutricional completa no dia a dia, com a praticidade de apenas 2 tabletes.",
"Para quem quer reforçar a ingestão de vitamina C com uma fonte pura, de padrão farmacêutico.",
"Para vegetarianos, veganos, pessoas acima de 50 anos e quem busca B12 na forma ativa.",
"Para adultos que buscam suplementação de NAC, com orientação de um profissional de saúde.",
"Para quem consome pouco peixe e quer um ômega 3 concentrado e certificado em pureza.",
"Para quem toma pouco sol ou quer vitamina D3 com K2 em gotas fáceis de dosar.",
"Para quem precisa complementar o ferro da alimentação, com orientação profissional.",
"Para quem treina e busca mais desempenho em exercícios intensos e repetidos.",
"Para cabelos normais e oleosos, e para quem prefere cosméticos naturais e sem plástico.",
"Para cabelos finos ou frágeis que precisam de hidratação leve.",
"Para quem prefere um creme dental sem flúor, com xilitol e fórmula vegana."]
DARK={0,3}
TAG={0:"CARRO-CHEFE",3:"RECOMENDADO"}
EXTRA={0:["Sem glúten"],2:["Vegano"],4:["Sem glúten","IFOS"],5:["Zero açúcar"],8:["Vegano"],9:["Vegano"],10:["Vegano"]}
GR=[("Suplementos","importados.","Seleção internacional das marcas mais reconhecidas do mundo, sem que você precise importar.",[0,1,2,3]),
    ("Suplementos","nacionais.","Marcas brasileiras de confiança, com pronta entrega.",[4,5,6,7]),
    ("Cuidados","naturais.","Higiene e beleza com ingredientes naturais e veganos.",[8,9,10])]
def foto(i):
    f=f"fotos_std/{i+1:02d}.jpg"; return f'<img class="ph" src="{f}">' if os.path.exists(f) else ""
def li(x): return "".join(f"<li>{v}</li>" for v in x)
def hdr(l,r,dark=False):
    return f'<div class="hd"><img src="{"logo-do-rei-negativo.svg" if dark else "logo-do-rei-horizontal.svg"}" class="hl{" d" if dark else ""}"><span>{l}</span><span>{r}</span></div>'
def ftr(n,dark=False): return f'<div class="ft"><span>Do Rei · Saúde &amp; Suplementos</span><span>Catálogo · Outubro 2026</span><span>{n:02d}</span></div>'
pages=[]; pg=1
# capa
pages.append('''<div class="page cover"><div class="cv-top">CATÁLOGO DE PRODUTOS · EDIÇÃO OUTUBRO 2026</div>
<img class="cv-logo" src="logo-do-rei-negativo.svg"><div class="cv-line"></div>
<div class="cv-t">Cuidado com o corpo,<br><em>feito com verdade e serviço.</em></div>
<div class="cv-bot"><span>11 produtos</span><span>Importados · Nacionais · Naturais</span><span>Preços de 15/10/2026</span></div></div>'''); pg+=1

def feature():
    a=P[0]; b=P[3]
    return f'''<div class="page feat">{hdr("DESTAQUE DA CASA","02",True)}
<div class="fk">NOSSO CARRO-CHEFE</div>
<div class="fg"><div><h2>{T[0][0]}<br><em>{T[0][1]}</em></h2><div class="fm">{a[1]} · {PN[0]} · {a[3]}</div>
<p class="fp">Fabricado pela <b>Life Extension</b> (EUA), referência mundial em suplementação baseada em ciência desde 1980. A base de tudo. Vitaminas e minerais essenciais em apenas 2 tabletes por dia, com doses generosas e formas de alta qualidade. Se você vai começar por um produto, comece por este.</p>
<ul class="fb">{li(D[0]["ben"])}</ul>
<div class="fpr"><small>R$</small>{a[5]}<span>R$ {a[6]} por dose · {a[4]}</span></div></div>
<div class="fph"><img src="fotos_std/01.jpg"></div></div>
<div class="rec"><div class="rk">INDICAMOS TAMBÉM</div><div class="rg"><img src="fotos_std/04.jpg"><div><h4>{T[3][0]} <em>{T[3][1]}</em></h4><p>{SV[3]}. {Q[3]}</p></div><div class="rp"><small>R$</small>{b[5]}<span>Ficha 04</span></div></div></div>
{ftr(2,True)}</div>'''
pages.append(feature()); pg+=1
# manifesto + sumario
pstart=7; idx=""; p=pstart
for k,(a,b,d,ids) in enumerate(GR):
    p+=1
    items="".join(f'<div class="ii"><span>{i+1:02d}</span>{T[i][0]} <em>{T[i][1]}</em><b>p. {p+n:02d}</b></div>' for n,i in enumerate(ids))
    idx+=f'<div class="ix"><div class="ixh"><span class="ixn">0{k+1}</span>{a} <em>{b}</em></div>{items}</div>'
    p+=len(ids)
idx+=f'<div class="ix"><div class="ixh"><span class="ixn">04</span>Tabela de <em>preços.</em><b>p. {p:02d}</b></div></div>'
pages.append(f'''<div class="page">{hdr("MANIFESTO","03")}
<div class="mf"><div class="mq">“</div><h1>Cuidado com o corpo,<br><em>feito com verdade<br>e serviço.</em></h1>
<p>Este catálogo existe para ajudar você a escolher, não para empurrar. Cada ficha diz o que o produto é, para quem serve e quando não é para você. Vendemos só o que compraríamos para a nossa própria família, com preço justo e atendimento de quem conhece você pelo nome.</p></div>
<div class="kk">ÍNDICE</div><div class="idx">{idx}</div>{ftr(3)}</div>'''); pg+=1
# como comprar
steps=[("Escolha","Veja as fichas e anote o número de cada produto."),("Peça","Envie pelo WhatsApp <a href=\"https://wa.me/5575991832734\" style=\"color:var(--r)\">(75) 99183-2734</a> os números e as quantidades."),("Pague","Pix (melhor preço) ou cartão de crédito com link de pagamento."),("Receba","Nacionais em 5 a 10 dias úteis; importados em 15 a 18 dias úteis.")]
pages.append(f'''<div class="page">{hdr("COMO COMPRAR","04")}
<h2 class="big">Simples, <em>transparente</em><br>e seguro.</h2>
<div class="steps">{"".join(f'<div class="st"><div class="stn">0{j+1}</div><b>{a}</b><p>{b}</p></div>' for j,(a,b) in enumerate(steps))}</div>
<div class="kk" style="margin-top:14mm">NOSSOS COMPROMISSOS</div>
<div class="cm"><div><b>Pagamento</b><p>Pix com o melhor preço, ou cartão de crédito (+5%, à vista ou parcelado). Pedidos fecham toda sexta, às 12 h.</p></div><div><b>Validade</b><p>Entregamos só produtos com no mínimo 6 meses de validade.</p></div><div><b>Originalidade</b><p>Produtos lacrados, comprados de fornecedores confiáveis.</p></div><div><b>Trocas</b><p>Defeito ou avaria: trocamos ou devolvemos o valor.</p></div></div>
<div class="sel-leg"><span class="selo g">Importado</span> chega em 15–18 dias úteis &nbsp; <span class="selo g">Pronta entrega</span> chega em 5–10 dias úteis</div>{ftr(4)}</div>''')
labp=f'''<div class="page">{hdr("LABORATÓRIOS","05")}<h2 class="big">Laboratórios <em>de confiança.</em></h2>
<div class="labhero"><div class="lk">DESTAQUE</div><h3>Life Extension</h3><div class="lo">{LABS["Life Extension"][0]}</div><p>{LABS["Life Extension"][1]}</p><p class="lp">Na Do Rei: <b>Multivitamínico 2 por dia</b> (Two-Per-Day), nosso carro-chefe.</p></div>
<div class="labs">{"".join(f'<div><b>{k}</b><span>{v[0]}</span><p>{v[1]}</p></div>' for k,v in LABS.items() if not v[2])}</div>{ftr(5)}</div>'''
pages.append(labp)
rows_g="".join(f'<div class="gr"><div class="gq">{q}</div><div class="gp"><b>{int(a):02d}</b> {T[int(a)-1][0]} <em>{T[int(a)-1][1]}</em><span>+ {int(b):02d} {T[int(b)-1][0]} {T[int(b)-1][1]}</span></div><p>{w}</p></div>' for q,a,b,w in GUIA)
pages.append(f'''<div class="page">{hdr("GUIA RÁPIDO","06")}<h2 class="big">Qual é o seu <em>objetivo?</em></h2><p class="gi">Encontre seu objetivo, veja a indicação principal e o complemento. Os números levam às fichas.</p><div class="guia">{rows_g}</div><p class="note">Orientação geral, não substitui avaliação profissional. Gestantes, lactantes, crianças e pessoas em tratamento devem consultar um profissional de saúde. Ferro: use apenas com orientação.</p>{ftr(6)}</div>'''); pg=7
def product(i,n):
    nm,m,o,e,d,p,pd,pr,desc=P[i]; x=D[i]; dk=i in DARK
    sup=x["porcao"] is not None
    rows="".join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a,b in x["nut"])
    comp=f'COMPOSIÇÃO · {x["porcao"].upper()}' if sup else "CARACTERÍSTICAS"
    sel=[("Importado","g")] if o=="Importado" else [("Pronta entrega","g")]
    sel+=[(s,"") for s in EXTRA.get(i,[])]
    sels="".join(f'<span class="selo {c}">{s}</span>' for s,c in sel)
    if p=="EM FALTA": price='<div class="pr"><div class="pv out">Em falta</div><div class="pd">Consulte a reposição</div></div>'
    else: price=f'<div class="pr"><div class="pl">PREÇO</div><div class="pv"><small>R$</small>{p}</div>{f"<div class=pd>R$ {pd} por dose</div>" if pd!="—" else ""}</div>'
    info=e+(f" · {d}" if d!="—" else "")
    CT=f'<div class="ct"><div class="kk r">CONTRAINDICAÇÕES E PRECAUÇÕES</div><ul>{li(x["con"])}</ul></div>'
    return f'''<div class="page{" dark" if dk else ""}">{hdr(f"FICHA {i+1:02d} · "+TAG.get(i,o.upper()),K[i].upper(),dk)}
<div class="top"><div class="num">{i+1:02d}</div><div class="tt"><div class="kc">{K[i].upper()}</div><h3>{T[i][0]}<br><em>{T[i][1]}</em></h3><div class="mk"><b class="lab">{m}</b> · {LABS[m][0]}<br>{PN[i]} · {info}</div><div class="sv"><span>PARA QUE SERVE</span>{SV[i]}</div></div><div class="phb">{foto(i)}</div></div>
<div class="bar">{price}<div class="bi"><div>{sels}</div><div class="en">Entrega em <b>{pr}</b></div></div></div>
<div class="cols"><div><div class="kk">PARA QUEM É</div><p class="pq">{Q[i]}</p>
<div class="kk">BENEFÍCIOS</div><ul class="bn">{li(x["ben"])}</ul>
<div class="kk">MODO DE USO</div><p class="pq">{x["uso"]}</p>{CT if len(x["nut"])>16 else ""}</div>
<div><div class="cb{" dense" if len(x["nut"])>8 else ""}"><div class="kk m">{comp}</div>{"<div class=nut2>"+"".join(f"<div><span>{a}</span><b>{b}</b></div>" for a,b in x["nut"])+"</div>" if len(x["nut"])>16 else "<table>"+rows+"</table>"}{'<div class=ob>Valores conforme rótulo do fabricante.</div>' if sup else ''}</div>
{"" if len(x["nut"])>16 else CT}</div></div>{ftr(n,dk)}</div>'''
for k,(a,b,d,ids) in enumerate(GR):
    lst="".join(f'<div class="oi"><span>{i+1:02d}</span>{T[i][0]} <em>{T[i][1]}</em></div>' for i in ids)
    pages.append(f'''<div class="page opener"><div class="op-l"><div class="op-k">PARTE 0{k+1}</div><h2>{a}<br><em>{b}</em></h2><p>{d}</p><div class="ol">{lst}</div></div><div class="op-r"><img src="icone-do-rei.svg"></div><div class="ft"><span>Do Rei · Saúde &amp; Suplementos</span><span></span><span>{pg:02d}</span></div></div>'''); pg+=1
    for i in ids: pages.append(product(i,pg)); pg+=1
rows="".join(f'<tr><td class="n">{i+1:02d}</td><td><b>{T[i][0]} {T[i][1]}</b><br><span>{x[1]} · {x[3]}</span></td><td>{x[2]}</td><td>{x[7]}</td><td class="p">{"Em falta" if x[5]=="EM FALTA" else "R$ "+x[5]}</td></tr>' for i,x in enumerate(P))
pages.append(f'''<div class="page">{hdr("TABELA DE PREÇOS",f"{pg:02d}")}<h2 class="big">Tabela de <em>preços.</em></h2>
<table class="tp"><tr><th></th><th>Produto</th><th>Origem</th><th>Entrega</th><th class="p">Preço</th></tr>{rows}</table>
<a class="fale" href="https://wa.me/5575991832734"><span>💬</span><div><b>Fale conosco</b>WhatsApp (75) 99183-2734 · toque para abrir a conversa</div></a><div class="note">Preços de 15/10/2026 para pagamento no Pix; no cartão de crédito, +5%. Sujeitos a alteração. Prazos em dias úteis após a confirmação do pagamento. As informações nutricionais seguem os rótulos dos fabricantes. Suplementos alimentares não substituem uma alimentação equilibrada; consulte um profissional de saúde.</div>{ftr(pg)}</div>'''); pg+=1
pages.append('''<div class="page back"><img class="bk-logo" src="logo-do-rei-negativo.svg"><div class="cv-line"></div><div class="bk-t">Faça seu pedido pelo WhatsApp<br><a class="wa" href="https://wa.me/5575991832734">(75) 99183-2734</a><br><em>Atendimento de quem conhece você pelo nome.</em></div><div class="cv-bot"><span>Do Rei · Saúde &amp; Suplementos</span><span>Cuidado com o corpo, feito com verdade e serviço.</span></div></div>''')
CSS='''@page{size:A4;margin:0}*{box-sizing:border-box}
:root{--n:#0B2A5B;--nn:#071B3D;--r:#1F4FA3;--a:#D4A72C;--l:#EAF1FB;--t:#14213D;--m:#5B6B82;--b:#E1E7F0;--g:#F4F6F9}
body{margin:0;font-family:Inter,Arial,sans-serif;color:var(--t);-webkit-print-color-adjust:exact;print-color-adjust:exact}
em{font-style:italic}
.page{width:210mm;height:297mm;padding:13mm 16mm;position:relative;overflow:hidden;page-break-after:always;background:#fff}
.hd{display:grid;grid-template-columns:auto 1fr auto;gap:6mm;align-items:center;font:500 8px 'JetBrains Mono',monospace;letter-spacing:2.2px;color:var(--r);padding-bottom:4mm;border-bottom:1px solid var(--b)}
.hd span:nth-child(3){text-align:right;color:var(--m)} .hl{height:8mm} .hl.d{height:11mm}
.ft{position:absolute;left:16mm;right:16mm;bottom:9mm;display:flex;justify-content:space-between;font:500 7.5px 'JetBrains Mono',monospace;letter-spacing:1.5px;color:var(--m);text-transform:uppercase}
.kk{font:600 9px 'JetBrains Mono',monospace;letter-spacing:2.5px;color:var(--r);margin:8mm 0 3mm}
.cover,.back{background:var(--n);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.cv-top{position:absolute;top:16mm;font:500 8.5px 'JetBrains Mono',monospace;letter-spacing:3px;color:var(--a)}
.cv-logo{width:92mm} .cv-line{width:16mm;height:1.5px;background:var(--a);margin:12mm 0}
.cv-t,.bk-t{font:400 30px/1.25 'Cormorant Garamond',serif} .cv-t em,.bk-t em{color:var(--a)}
.cv-bot{position:absolute;bottom:14mm;left:16mm;right:16mm;display:flex;justify-content:space-between;font:500 7.5px 'JetBrains Mono',monospace;letter-spacing:2px;color:#B9C6DD;text-transform:uppercase}
.bk-logo{width:80mm} .wa{text-decoration:none;display:inline-block;font:600 26px Montserrat,sans-serif;letter-spacing:1px;color:#fff;margin:4mm 0} .bk-t{font-size:24px}
.mf{margin:16mm 0 8mm} .mq{font:400 90px/0.6 'Cormorant Garamond',serif;color:var(--a)}
.mf h1{font:400 44px/1.12 'Cormorant Garamond',serif;margin:4mm 0 6mm;color:var(--n)} .mf h1 em{color:var(--r)}
.mf p{font-size:12px;line-height:1.7;color:var(--m);max-width:135mm}
.idx{border-top:1px solid var(--b)} .ix{padding:3.5mm 0;border-bottom:1px solid var(--b)}
.ixh{font:400 22px 'Cormorant Garamond',serif;color:var(--n);display:flex;align-items:baseline;gap:4mm} .ixh em{color:var(--r)} .ixh b{margin-left:auto;font:500 9px 'JetBrains Mono',monospace;color:var(--m)}
.ixn{font:600 9px 'JetBrains Mono',monospace;color:var(--a);letter-spacing:2px}
.ii{display:flex;gap:3mm;font:400 14px 'Cormorant Garamond',serif;padding:0.8mm 0 0.8mm 12mm;color:var(--t)} .ii span{font:500 8.5px 'JetBrains Mono',monospace;color:var(--a);padding-top:1mm} .ii em{color:var(--r)} .ii b{margin-left:auto;font:500 8.5px 'JetBrains Mono',monospace;color:var(--m);font-weight:500}
.big{font:400 46px/1.1 'Cormorant Garamond',serif;color:var(--n);margin:14mm 0 10mm} .big em{color:var(--r)}
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:4mm} .st{border-top:2px solid var(--a);padding-top:4mm} .stn{font:400 34px 'Cormorant Garamond',serif;color:var(--a)} .st b{font-size:13px;color:var(--n)} .st p{font-size:10.5px;color:var(--m);line-height:1.55}
.cm{display:grid;grid-template-columns:1fr 1fr;gap:5mm 10mm} .cm b{font-size:12px;color:var(--n)} .cm p{font-size:10.5px;color:var(--m);margin:1mm 0 0;line-height:1.55}
.sel-leg{margin-top:12mm;font-size:10px;color:var(--m)}
.selo{display:inline-block;font:600 7.5px 'JetBrains Mono',monospace;letter-spacing:1.5px;text-transform:uppercase;padding:1.2mm 2.5mm;border:1px solid var(--r);color:var(--r);margin:0 1.5mm 1.5mm 0}
.selo.g{border-color:var(--a);color:#9A7412;background:#FBF5E4}
.top{display:grid;grid-template-columns:40mm 1fr 62mm;gap:5mm;margin-top:9mm;align-items:start}
.num{font:300 110px/0.85 'Cormorant Garamond',serif;color:var(--a)}
.kc{font:500 8px 'JetBrains Mono',monospace;letter-spacing:2px;color:var(--m)}
h3{font:500 46px/1.02 'Cormorant Garamond',serif;color:var(--n);margin:2mm 0 3mm} h3 em{color:var(--r);font-weight:400}
.sv{margin-top:4mm;font-size:13px;color:var(--ink);line-height:1.45}.sv span{display:block;font:600 8px 'JetBrains Mono',monospace;letter-spacing:2px;color:var(--a);margin-bottom:1mm}.dark .sv{color:#fff}
.lab{color:var(--n);font-weight:600}.dark .lab{color:#fff}
.labhero{background:var(--n);color:#fff;padding:9mm 10mm;border-left:4px solid var(--a);margin-bottom:8mm}.labhero h3{color:#fff;font-size:44px;margin:1mm 0}.lk{font:600 8.5px 'JetBrains Mono',monospace;letter-spacing:3px;color:var(--a)}.lo{font:500 9px 'JetBrains Mono',monospace;letter-spacing:2px;color:#B9C6DD;text-transform:uppercase}.labhero p{font-size:12.5px;line-height:1.7;color:#E8EDF5;margin:4mm 0 0}.lp b{color:var(--a)}
.labs{display:grid;grid-template-columns:1fr 1fr;gap:6mm 9mm}.labs b{font:500 20px 'Cormorant Garamond',serif;color:var(--n)}.labs span{display:block;font:500 8px 'JetBrains Mono',monospace;letter-spacing:2px;color:var(--a);text-transform:uppercase;margin:1mm 0}.labs p{font-size:10.5px;color:var(--m);line-height:1.55;margin:0}
.mk{font-size:11.5px;color:var(--m)}
.phb{border:1px solid var(--b);background:#fff;height:62mm;display:flex;align-items:center;justify-content:center} .ph{width:61mm;height:61mm;object-fit:contain}
.bar{display:flex;gap:8mm;align-items:center;margin:10mm 0 2mm;padding:4mm 6mm;background:var(--l);border-left:3px solid var(--a)}
.pl{font:600 7.5px 'JetBrains Mono',monospace;letter-spacing:2px;color:var(--m)} .pv{font:600 30px 'Montserrat',sans-serif;color:var(--n);line-height:1.1} .pv small{font-size:13px;margin-right:1mm} .pv.out{font-size:22px;color:var(--m)}
.pd{font-size:9.5px;color:var(--m)} .bi{flex:1;display:flex;flex-direction:column;align-items:flex-end;gap:1mm} .en{font-size:10px;color:var(--m)} .en b{color:var(--n)}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:9mm}
.pq{font-size:12.5px;line-height:1.65;margin:0} .bn{margin:0;padding-left:4.5mm} .bn li{font-size:12.5px;line-height:1.55;margin-bottom:2.5mm} .bn li::marker{color:var(--a)}
.cb{background:var(--g);padding:1mm 5mm 4mm;margin-top:4mm} .kk.m{margin-top:4mm}
.cb table{width:100%;border-collapse:collapse;font:400 10.5px 'JetBrains Mono',monospace} .cb td{padding:1.8mm 0;border-bottom:1px dotted #C5CEDB} .cb td:last-child{text-align:right;font-weight:600}
.dense table{font-size:9px} .dense td{padding:0.7mm 0 !important} .nut2{display:grid;grid-template-columns:1fr;font:400 8.6px 'JetBrains Mono',monospace}.nut2 div{display:flex;justify-content:space-between;gap:2mm;padding:0.55mm 0;border-bottom:1px dotted #2A4777}.nut2 b{font-weight:600;white-space:nowrap}
.ob{font-size:8px;color:var(--m);margin-top:2mm}
.ct{margin-top:5mm;border-left:2px solid #B4483C;padding:0 0 0 4mm} .kk.r{color:#B4483C;margin-top:1mm} .ct ul{margin:0;padding-left:4mm} .ct li{font-size:11px;line-height:1.5;color:var(--t);margin-bottom:1mm}
.dark{background:var(--nn);color:#E8EDF5} .dark .hd{border-color:#22406F;color:var(--a)} .dark h3{color:#fff} .dark h3 em{color:var(--a)} .dark .kk{color:var(--a)} .dark .mk,.dark .kc,.dark .pd,.dark .en,.dark .ft,.dark .ob{color:#9FB0CC}
.dark .bar{background:#0F2A55} .dark .pv{color:#fff} .dark .en b{color:#fff} .dark .cb{background:#0F2A55} .dark .cb td{border-color:#2A4777} .dark .ct li,.dark .pq,.dark .bn li{color:#E8EDF5} .dark .kk.r{color:#E59A8F} .dark .ct{border-color:#E59A8F}
.dark .phb{border-color:#22406F} .dark .selo{border-color:#8FB0E6;color:#8FB0E6} .dark .selo.g{background:transparent;border-color:var(--a);color:var(--a)}
.opener{padding:0;display:flex;background:var(--n);color:#fff}
.op-l{width:62%;padding:30mm 16mm} .op-k{font:500 9px 'JetBrains Mono',monospace;letter-spacing:3px;color:var(--a)}
.op-l h2{font:400 64px/1.0 'Cormorant Garamond',serif;margin:8mm 0 8mm} .op-l h2 em{color:var(--a)} .op-l p{font-size:12px;line-height:1.7;color:#B9C6DD;max-width:100mm}
.ol{margin-top:14mm;border-top:1px solid #2A4777} .oi{font:400 18px 'Cormorant Garamond',serif;padding:2.5mm 0;border-bottom:1px solid #2A4777;display:flex;gap:4mm;align-items:baseline} .oi span{font:500 9px 'JetBrains Mono',monospace;color:var(--a)} .oi em{color:#8FB0E6}
.op-r{width:38%;background:var(--nn);display:flex;align-items:center;justify-content:center} .op-r img{width:52mm;opacity:.95}
.opener .ft{color:#9FB0CC}
.feat{background:var(--nn);color:#E8EDF5}.feat .hd{border-color:#22406F;color:var(--a)}
.fk{font:600 9px 'JetBrains Mono',monospace;letter-spacing:3px;color:var(--a);margin:12mm 0 4mm}
.fg{display:grid;grid-template-columns:minmax(0,1fr) 72mm;gap:8mm;align-items:center}
.feat h2{font:400 58px/1.0 'Cormorant Garamond',serif;color:#fff;margin:0 0 4mm}.feat h2 em{color:var(--a)}
.fm{font-size:11px;color:#9FB0CC}.fp{font-size:13px;line-height:1.7;margin:6mm 0}.fb{margin:0;padding-left:5mm}.fb li{font-size:12px;line-height:1.55;margin-bottom:2mm}.fb li::marker{color:var(--a)}
.fpr{font:600 40px Montserrat,sans-serif;color:#fff;margin-top:6mm}.fpr small{font-size:16px;margin-right:2mm}.fpr span{display:block;font:400 11px Inter,sans-serif;color:#9FB0CC;margin-top:1mm}
.fph{background:#fff;height:90mm;display:flex;align-items:center;justify-content:center}.fph img{width:66mm;height:80mm;object-fit:contain}
.rec{position:absolute;left:16mm;right:16mm;bottom:22mm;border-top:1px solid #2A4777;padding-top:6mm}.rk{font:600 8.5px 'JetBrains Mono',monospace;letter-spacing:2.5px;color:var(--a);margin-bottom:4mm}
.rg{display:grid;grid-template-columns:30mm 1fr auto;gap:6mm;align-items:center}.rg img{width:30mm;height:30mm;object-fit:contain;background:#fff}
.rg h4{font:400 26px 'Cormorant Garamond',serif;color:#fff;margin:0 0 2mm}.rg h4 em{color:var(--a)}.rg p{font-size:11px;color:#B9C6DD;margin:0;line-height:1.55}
.rp{font:600 24px Montserrat,sans-serif;color:#fff;text-align:right}.rp small{font-size:12px;margin-right:1mm}.rp span{display:block;font:500 8px 'JetBrains Mono',monospace;letter-spacing:2px;color:var(--a)}
.fale{display:flex;gap:4mm;align-items:center;margin-top:8mm;background:var(--n);color:#fff;text-decoration:none;padding:5mm 6mm;border-left:3px solid var(--a)}.fale span{font-size:22px}.fale b{display:block;font-size:14px;color:var(--a)}.fale div{font-size:11px}
.gi{font-size:12px;color:var(--m);margin:-6mm 0 6mm}.guia{border-top:1.5px solid var(--n)}.gr{display:grid;grid-template-columns:52mm 1fr;gap:1mm 6mm;padding:3.2mm 0;border-bottom:1px solid var(--b)}.gq{font:500 17px/1.2 'Cormorant Garamond',serif;color:var(--n);grid-row:span 2}.gp{font-size:12px}.gp b{font:600 9px 'JetBrains Mono',monospace;color:var(--a)}.gp em{color:var(--r)}.gp span{display:block;font-size:10.5px;color:var(--m);margin-top:0.5mm}.gr p{font-size:10px;color:var(--m);margin:0}
.tp{width:100%;border-collapse:collapse;font-size:10px} .tp th{text-align:left;font:600 7.5px 'JetBrains Mono',monospace;letter-spacing:2px;color:var(--r);padding:2mm;border-bottom:1.5px solid var(--n)}
.tp td{padding:2.2mm 2mm;border-bottom:1px solid var(--b)} .tp td span{color:var(--m);font-size:9px} .tp .n{font:500 9px 'JetBrains Mono',monospace;color:var(--a)} .tp .p{text-align:right;font-weight:700;color:var(--n);white-space:nowrap}
.note{font-size:8.5px;color:var(--m);margin-top:6mm;line-height:1.6}'''
html=f'''<!doctype html><html lang="pt-br"><meta charset="utf-8"><title>Catálogo Do Rei</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,400;1,500&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;600&family=Montserrat:wght@600&display=block" rel="stylesheet">
<style>{CSS}</style><body>{"".join(pages)}</body></html>'''
open("catalogo.html","w").write(html)
msg="MENSAGENS PARA AS FOTOS DOS PRODUTOS NO WHATSAPP\n(copie e cole como legenda de cada foto)\n\n"
for i,(nm,m,o,e,d,p,pd,pr,desc) in enumerate(P):
    if p=="EM FALTA": continue
    msg+=f"━━━━━━━━━━━━━━━━\n👑 *Do Rei · Saúde & Suplementos*\n\n*{i+1:02d} · {T[i][0]} {T[i][1]}*\n{m} · {PN[i]} · {e}\n\n*Para que serve:* {SV[i]}\n\n💰 *R$ {p}*"+(f" (R$ {pd} por dose)" if pd!="—" else "")+f"\n🚚 Entrega em {pr}\n\n📲 Peça pelo número do produto: *{i+1:02d}*\nWhatsApp: (75) 99183-2734 · Pix ou cartão\n_Cuidado com o corpo, feito com verdade e serviço._\n\n"
open("mensagens-whatsapp.txt","w").write(msg)
