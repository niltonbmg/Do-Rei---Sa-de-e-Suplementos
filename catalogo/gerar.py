# Gera catalogo.html e mensagens-whatsapp.txt a partir da lista de produtos.
P = [
 ("Two-Per-Day Multivitamínico · 120 tabletes","Life Extension","Importado","120 tabletes","60 doses","207,90","3,47","15 dias úteis","Multivitamínico e multimineral em 2 tabletes ao dia."),
 ("Gold C® Vitamina C 1.000 mg · 240 cápsulas","California Gold Nutrition","Importado","240 cápsulas","240 doses","142,90","0,60","16 dias úteis","Vitamina C grau USP em cápsula vegetal."),
 ("Methyl B-12 1.000 mcg · 250 pastilhas","NOW Foods","Importado","250 pastilhas","250 doses","169,90","0,68","17 dias úteis","Vitamina B12 na forma metilcobalamina, em pastilha."),
 ("NAC 600 mg · 250 cápsulas","NOW Foods","Importado","250 cápsulas","250 doses","291,90","1,17","18 dias úteis","N-Acetil L-Cisteína em cápsula vegetal."),
 ("Omegafor Plus · 240 cápsulas","Vitafor","Nacional","240 cápsulas","80 doses","255,90","3,20","5 dias úteis","Ômega 3 ultraconcentrado em EPA e DHA, certificado IFOS."),
 ("Bio Synergy D3 + K2 MK-7 · 20 ml","Bigens","Nacional","20 ml","150 doses","61,90","0,41","5 dias úteis","Vitaminas A, D3, E e K2 em gotas, sabor limão, zero açúcares."),
 ("Ferro Plus · 30 cápsulas","Vitafor","Nacional","30 cápsulas","30 doses","39,90","1,33","10 dias úteis","Ferro quelato com vitamina C."),
 ("Creatina Monohidratada · 250 g","Growth Supplements","Nacional","250 g","83 doses","45,90","0,55","5 dias úteis","Creatina monohidratada pura, sem sabor."),
 ("Shampoo em Barra Aloe Vera · 90 g","Senhor Saboeiro","Nacional","Barra 90 g","—","27,90","—","10 dias úteis","Shampoo sólido natural com aloe vera, para cabelos normais e oleosos."),
 ("Condicionador em Barra Pitaia Rosa · 55 g","Senhor Saboeiro","Nacional","Barra 55 g","—","EM FALTA","—","10 dias úteis","Condicionador sólido vegano com extrato de pitaia."),
 ("Creme Dental Ultra Mint · 70 g","Dentil","Nacional","70 g","—","4,90","—","10 dias úteis","Creme dental com xilitol, sem flúor, sabor menta."),
]
import html as H
GR=[("Suplementos Importados","Seleção internacional das marcas mais reconhecidas",[0,1,2,3]),
    ("Suplementos Nacionais","Qualidade nacional com entrega rápida",[4,5,6,7]),
    ("Cuidados Pessoais","Higiene e beleza com ingredientes naturais e veganos",[8,9,10])]
from dados import D
def hdr(t): return f'<div class="hdr"><span class="brand"><img class="hlogo" src="logo.png"><i>Saúde &amp; Suplementos</i></span><span>{t}</span></div>'
def ftr(n): return f'<div class="ftr"><span>Catálogo Outubro 2026</span><span>{n:02d}</span></div>'
CAT=[g[0] for g in GR for _ in g[2]]
import os
def foto(i):
    for ext in ("jpg",):
        f=f"fotos_std/{i+1:02d}.{ext}"
        if os.path.exists(f): return f'<img class="foto" src="{f}">'
    return ""
EXTRA={0:["Sem glúten"],2:["Vegano"],4:["Sem glúten","IFOS"],5:["Zero açúcar"],8:["Vegano"],9:["Vegano"],10:["Vegano"]}
def selos(i):
    o=P[i][2]; t=[("Importado","g")] if o=="Importado" else [("Pronta entrega","g")]
    t+= [(x,"") for x in EXTRA.get(i,[])]
    return '<div class="selos">'+"".join(f'<span class="selo {c}">{x}</span>' for x,c in t)+'</div>'
def li(x): return "".join(f"<li>{v}</li>" for v in x)
def prod(i,pg):
    n,m,o,e,d,p,pd,pr,desc=P[i]; x=D[i]
    sup=x["porcao"] is not None
    tit="Informação Nutricional" if sup else "Características"
    cab=f'<tr><th>Porção: {x["porcao"]}</th><th class="r">Quantidade</th></tr>' if sup else '<tr><th colspan=2>Produto</th></tr>'
    rows="".join(f'<tr><td>{k}</td><td class="r">{v}</td></tr>' for k,v in x["nut"])
    dose=f'<div class="dose">R$ {pd} por dose</div>' if pd!="—" else ""
    rend=f"<div><span>Rendimento</span><b>{d}</b></div>" if d!="—" else ""
    return f"""<div class="page">{hdr(CAT[i])}
<div class="ph">{foto(i)}<div class="phl"><div class="cod">PRODUTO {i+1:02d} · {o.upper()}</div><div class="marca">{m}</div><h2 class="pn">{H.escape(n)}</h2><p class="desc">{desc}</p>{selos(i)}</div>
{"<div class=\"pbox falta\"><div class=\"lbl\">Disponibilidade</div><div class=\"big\">Em falta</div><div class=\"dose\">Consulte reposição</div></div>" if p=="EM FALTA" else f"<div class=\"pbox\"><div class=\"lbl\">Preço</div><div class=\"big\"><span class=\"rs\">R$</span>{p}</div>{dose}</div>"}</div>
<div class="facts"><div><span>Embalagem</span><b>{e}</b></div>{rend}<div><span>Origem</span><b>{o}</b></div><div><span>Entrega</span><b>{pr}</b></div></div>
<div class="cols"><div><h4>Benefícios</h4><ul class="ben">{li(x["ben"])}</ul>
<h4>Modo de uso</h4><p class="uso">{x["uso"]}</p></div>
<div><h4>{tit}</h4><table class="nut">{cab}{rows}</table>{'<div class="obs">Valores por porção conforme rótulo do fabricante.</div>' if sup else ''}</div></div>
<div class="con"><h4>Contraindicações e precauções</h4><ul>{li(x["con"])}</ul></div>
{ftr(pg)}</div>"""
secoes=""; pg=3
for k,(t,sub,ids) in enumerate(GR):
    for i in ids: secoes+=prod(i,pg); pg+=1
sumario=""; p0=3
for k,(t,sub,ids) in enumerate(GR):
    sumario+=f'<div class="si"><span class="sn">0{k+1}</span><div><b>{t}</b><br><span>{sub}</span></div><span class="sp">p. {p0:02d}</span></div>'
    p0+=len(ids)
sumario+=f'<div class="si"><span class="sn">04</span><div><b>Tabela de Preços</b><br><span>Todos os produtos em uma página</span></div><span class="sp">p. {p0:02d}</span></div>'
passos=[("Escolha","Veja os produtos e anote o código de cada um (ex.: 05)."),("Peça","Envie pelo WhatsApp os códigos e as quantidades."),("Pague","Confirmamos o total e você paga por Pix."),("Receba","Nacionais em 5 a 10 dias úteis; importados em 15 a 18 dias úteis.")]
como="".join(f'<div class="st"><div class="stn">{j+1}</div><b>{a}</b><p>{b}</p></div>' for j,(a,b) in enumerate(passos))
pagina2=f"""<div class="page">{hdr("Bem-vindo")}<div class="sec"><div class="secn">SUMÁRIO</div><h2>Nosso catálogo</h2></div><div class="sum">{sumario}</div>
<div class="sec" style="margin-top:12mm"><div class="secn">COMO COMPRAR</div><h2>Simples e seguro</h2></div><div class="steps">{como}</div>
<div class="pol"><div><b>Pagamento</b><br>Pix antecipado</div><div><b>Pedidos</b><br>fecham toda sexta, 18 h</div><div><b>Validade</b><br>mínimo de 6 meses</div><div><b>Trocas</b><br>defeito ou avaria</div></div>{ftr(2)}</div>"""
idx="".join(f'<tr><td class="c">{j+1:02d}</td><td><b>{H.escape(x[0])}</b><br><span>{x[1]}</span></td><td>{x[4] if x[4]!="—" else x[3]}</td><td>{x[7]}</td><td class="r">{"Em falta" if x[5]=="EM FALTA" else "R$ "+x[5]}</td></tr>' for j,x in enumerate(P))
html=f"""<!doctype html><html lang="pt-br"><meta charset="utf-8"><title>Catálogo Do Rei</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
@page{{size:A4;margin:0}} *{{box-sizing:border-box}}
:root{{--g:#0B2A5B;--gd:#0B2A5B;--gl:#EAF1FB;--t:#14213D;--m:#5B6B82;--b:#E1E7F0;--a:#D4A72C;--r:#1F4FA3}}
body{{margin:0;background:#fff;font-family:Inter,Arial,sans-serif;color:var(--t);-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:210mm;height:297mm;padding:14mm 16mm;position:relative;overflow:hidden;page-break-after:always}}
.cover{{padding:0;display:flex}}
.cl{{width:62%;padding:22mm 16mm;display:flex;flex-direction:column}} .cr{{width:38%;background:var(--g);border-left:4px solid var(--a)}}
.mark{{font-size:11px;font-weight:700;letter-spacing:4px;color:var(--g)}}
.cover h1{{font-size:54px;line-height:1;font-weight:800;margin:auto 0 6mm;letter-spacing:-2px}}
.cover h1 span{{color:var(--r)}} .cover .lead{{font-size:15px;color:var(--m);font-weight:300;line-height:1.6;max-width:110mm}}
.cover .bar{{width:18mm;height:3px;background:var(--a);margin:10mm 0}}
.cover .meta{{font-size:11px;color:var(--m);letter-spacing:2px;text-transform:uppercase;margin-top:auto}}
.cover .meta b{{display:block;color:var(--t);font-size:13px;letter-spacing:1px;margin-bottom:1mm}}
.logo{{width:105mm}} .hlogo{{height:7mm;vertical-align:middle;margin-right:2mm}} .hdr{{align-items:center}}
.hdr{{display:flex;justify-content:space-between;font-size:9px;letter-spacing:2px;text-transform:uppercase;color:var(--m);padding-bottom:4mm;border-bottom:1px solid var(--b)}}
.brand{{color:var(--g);font-weight:800}} .brand i{{font-style:normal;font-weight:400;color:var(--m);margin-left:2mm}}
.ftr{{position:absolute;left:16mm;right:16mm;bottom:10mm;display:flex;justify-content:space-between;font-size:9px;color:var(--m);letter-spacing:1px;border-top:1px solid var(--b);padding-top:3mm}}
.sec{{margin:9mm 0 7mm}} .secn{{font-size:11px;font-weight:700;color:var(--g);letter-spacing:3px}}
h2{{font-size:28px;font-weight:800;margin:1mm 0 1mm;letter-spacing:-.5px}} .secsub{{font-size:12px;color:var(--m)}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:6mm}}
.card{{border:1px solid var(--b);border-top:3px solid var(--g);border-radius:2mm;padding:6mm;display:flex;flex-direction:column;position:relative;min-height:98mm}}
.cod{{position:absolute;top:5mm;right:6mm;font-size:10px;color:#B5C0D0;font-weight:600}}
.marca{{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--g)}}
h3{{font-size:15px;line-height:1.3;font-weight:700;margin:2mm 0 2mm}}
p{{font-size:10.5px;color:var(--m);line-height:1.5;margin:0 0 4mm}}
.spec{{width:100%;border-collapse:collapse;font-size:10px;margin-bottom:4mm}} .spec td{{padding:1.6mm 0;border-bottom:1px solid var(--b)}}
.spec td:first-child{{color:var(--m)}} .spec td:last-child{{text-align:right;font-weight:600}}
.price{{margin-top:auto;background:var(--gl);border-radius:1.5mm;padding:3mm 4mm;display:flex;justify-content:space-between;align-items:center}}
.price>div:first-child{{font-size:22px;font-weight:800;color:var(--gd)}} .rs{{font-size:11px;font-weight:600;margin-right:1mm}}
.dose{{font-size:9.5px;color:var(--gd);font-weight:500}}
.ph .cod{{position:static}} .foto{{width:52mm;height:52mm;object-fit:contain;border:1px solid var(--b);border-radius:3mm;background:#fff;box-shadow:0 1.5mm 4mm rgba(11,42,91,.10)}} .selos{{display:flex;gap:1.5mm;flex-wrap:wrap;margin-top:3mm}} .selo{{font-size:8px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;padding:1mm 2.5mm;border-radius:10px;border:1px solid var(--r);color:var(--r)}} .selo.g{{border-color:var(--a);color:#9A7412}} .ph{{display:flex;justify-content:space-between;gap:8mm;margin:6mm 0 5mm}} .phl{{flex:1}}
.cod{{font-size:9px;letter-spacing:2.5px;color:#8A97AD;font-weight:600}} .ph .marca{{margin-top:4mm;font-size:10px}}
.pn{{font-size:30px;line-height:1.15;margin:2mm 0 3mm}} .desc{{font-size:13px;color:var(--m);line-height:1.6;margin:0}}
.pbox{{background:var(--g);border-bottom:3px solid var(--a);color:#fff;border-radius:2mm;padding:6mm 7mm;min-width:55mm;align-self:flex-start}}
.falta{{background:#8A97AD}} .pbox .lbl{{color:var(--a);opacity:1 !important;font-size:9px;letter-spacing:2px;text-transform:uppercase;opacity:.8}} .big{{font-size:34px;font-weight:800;margin:1mm 0}} .pbox .dose{{color:#fff;opacity:.9}}
.facts{{display:flex;border:1px solid var(--b);border-radius:2mm;margin-bottom:5mm}} .facts div{{flex:1;padding:4mm 5mm;border-right:1px solid var(--b)}} .facts div:last-child{{border:0}}
.facts span{{display:block;font-size:8.5px;letter-spacing:1.5px;text-transform:uppercase;color:var(--m);margin-bottom:1mm}} .facts b{{font-size:12px}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:10mm}}
h4{{font-size:10px;letter-spacing:2px;text-transform:uppercase;color:var(--g);margin:0 0 3mm;padding-bottom:2mm;border-bottom:2px solid var(--a)}}
.ben{{list-style:none;padding:0;margin:0 0 7mm}} .ben li{{font-size:11.5px;padding:2mm 0 2mm 6mm;position:relative;line-height:1.45;border-bottom:1px solid var(--b)}}
.ben li:before{{content:"";position:absolute;left:0;top:3.4mm;width:2.2mm;height:2.2mm;border-radius:50%;background:var(--a)}}
.uso{{font-size:11.5px;line-height:1.6;margin:0}}
.nut{{width:100%;border-collapse:collapse;font-size:10.5px;border:1.5px solid var(--t)}} .nut th{{text-align:left;background:var(--t);color:#fff;padding:2.2mm 3mm;font-size:10px}}
.nut td{{padding:1.4mm 3mm;border-bottom:1px solid #D6DEE9}} .nut .r{{text-align:right;font-weight:600}} .obs{{font-size:8.5px;color:var(--m);margin-top:2mm}}
.con{{margin-top:5mm;background:#fff7f5;border-left:3px solid #c0392b;border-radius:1.5mm;padding:5mm 6mm}} .con h4{{color:#c0392b;border-color:#f0c9c2}}
.con ul{{margin:0;padding-left:5mm}} .con li{{font-size:11px;line-height:1.5;margin-bottom:1mm}}
.sum{{border-top:1px solid var(--b)}} .si{{display:flex;align-items:center;gap:6mm;padding:4mm 0;border-bottom:1px solid var(--b)}} .sn{{font-size:22px;font-weight:800;color:var(--a);width:12mm}} .si div{{flex:1;font-size:13px}} .si span{{color:var(--m);font-size:10.5px}} .sp{{font-weight:600}}
.steps{{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm}} .st{{background:var(--gl);border-radius:2mm;padding:5mm}} .stn{{width:8mm;height:8mm;border-radius:50%;background:var(--g);color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center;margin-bottom:3mm;font-size:12px}} .st b{{font-size:13px}} .st p{{font-size:10.5px;margin:1.5mm 0 0}}
.pol{{display:grid;grid-template-columns:repeat(4,1fr);margin-top:8mm;border:1px solid var(--b);border-radius:2mm}} .pol div{{padding:4mm 5mm;font-size:10.5px;color:var(--m);border-right:1px solid var(--b)}} .pol div:last-child{{border:0}} .pol b{{color:var(--t);font-size:11px}}
.back{{background:var(--g);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#fff}} .blogo{{width:110mm;background:#fff;padding:8mm 10mm;border-radius:3mm}} .bline{{width:20mm;height:3px;background:var(--a);margin:12mm 0}} .btxt{{font-size:16px;line-height:1.8}} .btxt b{{font-size:20px}} .bsm{{position:absolute;bottom:16mm;font-size:10px;letter-spacing:2px;text-transform:uppercase;opacity:.8}}
.tab{{width:100%;border-collapse:collapse;font-size:10px;margin-top:2mm}}
.tab th{{text-align:left;font-size:8.5px;letter-spacing:1.5px;text-transform:uppercase;color:var(--m);font-weight:600;padding:2.5mm 2mm;border-bottom:2px solid var(--a)}}
.tab td{{padding:2.6mm 2mm;border-bottom:1px solid var(--b);vertical-align:middle}} .tab td span{{color:var(--m);font-size:9px}}
.c{{color:#B5C0D0;font-weight:600}} .r{{text-align:right;font-weight:700;color:var(--gd);white-space:nowrap}}
.cta{{margin-top:8mm;background:var(--g);color:#fff;border-radius:2mm;padding:8mm;display:flex;justify-content:space-between;align-items:center}}
.cta h4{{margin:0;font-size:20px;font-weight:800;color:#fff;border:0;padding:0;letter-spacing:0;text-transform:none}} .cta div{{font-size:11px;opacity:.9;line-height:1.6}}
.note{{font-size:8.5px;color:var(--m);margin-top:6mm;line-height:1.6}}
</style><body>
<div class="page cover"><div class="cl"><img class="logo" src="logo.png" onerror="this.outerHTML='<div class=mark>DO REI</div>'">
<h1>Saúde &amp;<br><span>Suplementos</span></h1><div class="lead">Suplementos importados e nacionais selecionados, com qualidade garantida e atendimento personalizado.</div>
<div class="bar"></div><div class="meta"><b>Catálogo de Produtos</b>Preços de 15/10/2026</div></div><div class="cr"></div></div>
{pagina2}
{secoes}
<div class="page">{hdr("Tabela de Preços")}<div class="sec"><div class="secn">RESUMO</div><h2>Tabela de Preços</h2><div class="secsub">Todos os produtos em uma visão rápida</div></div>
<table class="tab"><tr><th>Cód.</th><th>Produto</th><th>Rend.</th><th>Entrega</th><th class="r">Preço</th></tr>{idx}</table>
<div class="cta"><div><h4>Faça seu pedido</h4><div>Atendimento direto pelo WhatsApp.</div></div><div style="text-align:right">Informe o código do produto<br>e a quantidade desejada.</div></div>
<div class="note">Preços atualizados em 15/10/2026, sujeitos a alteração sem aviso prévio. Prazos de entrega contados em dias úteis após a confirmação do pedido. As informações nutricionais seguem os rótulos dos fabricantes e podem variar entre lotes. Suplementos alimentares não substituem uma alimentação equilibrada; consulte um profissional de saúde.</div>{ftr(pg)}</div>
<div class="page back"><img class="blogo" src="logo.png"><div class="bline"></div><div class="btxt">Faça seu pedido pelo WhatsApp<br><b>Do Rei · Saúde &amp; Suplementos</b></div><div class="bsm">Suplementos importados e nacionais selecionados · Cuidados naturais</div></div>
</body></html>"""
open("catalogo.html","w").write(html)
msg = "MENSAGENS PARA AS FOTOS DOS PRODUTOS NO WHATSAPP\n(copie e cole como legenda de cada foto)\n\n"
for n,m,o,e,d,p,pd,pr,desc in P:
    if p=="EM FALTA": continue
    msg += f"━━━━━━━━━━━━━━━━\n👑 *Do Rei – Saúde e Suplementos*\n\n✨ *{n}*\n🏷️ {m} ({o.lower()})\n\n{desc}\n\n📦 {e}" + (f" – {d}" if d!="—" else "") + f"\n💰 *R$ {p}*" + (f" (apenas R$ {pd} por dose!)" if pd!="—" else "") + f"\n🚚 Entrega em {pr}\n\n📲 Peça já o seu! Responda esta mensagem.\n\n"
open("mensagens-whatsapp.txt","w").write(msg)
