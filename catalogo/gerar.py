# Gera catalogo.html e mensagens-whatsapp.txt a partir da lista de produtos.
P = [
 ("2-per-day (Multivitamínico)","Life Extension","Importado","120 cápsulas","60 doses","231,77","3,86","15 dias úteis","Multivitamínico completo: 2 cápsulas por dia para energia, imunidade e bem-estar."),
 ("Gold C® Vitamina C 1.000 mg","California Gold Nutrition","Importado","240 cápsulas","240 doses","190,09","0,79","16 dias úteis","Vitamina C grau USP para reforçar a imunidade e ação antioxidante."),
 ("Metil B-12 1.000 mcg","NOW Foods","Importado","250 pastilhas","250 doses","209,21","0,84","17 dias úteis","Vitamina B12 na forma ativa (metilcobalamina) para energia e sistema nervoso."),
 ("NAC 600 mg","NOW Foods","Importado","250 cápsulas","250 doses","294,61","1,18","18 dias úteis","N-Acetil Cisteína: apoio antioxidante e saúde respiratória e do fígado."),
 ("Omegafor Plus","Vitafor","Nacional","240 cápsulas","120 doses","255,17","2,13","5 dias úteis","Ômega 3 de alta concentração para coração, cérebro e articulações."),
 ("Bio Synergy D3 2000 UI + K2 MK7 20 mcg (A, D, E e K) – Limão","Bigens","Nacional","20 ml (kit c/ 3)","150 doses","65,33","0,44","5 dias úteis","Vitaminas A, D, E e K em gotas, sabor limão: ossos, imunidade e saúde geral."),
 ("Ferro Quelato Plus com Vitamina C","Vitafor","Nacional","30 cápsulas","30 doses","40,25","1,34","10 dias úteis","Ferro quelato com vitamina C para melhor absorção e mais disposição."),
 ("Creatina Monohidratada 250 g","Growth Supplements","Nacional","250 g","83 doses","45,89","0,55","5 dias úteis","Creatina pura para força, desempenho e ganho de massa muscular."),
 ("Shampoo Natural Antiqueda Hidratante 90 g – Linha Capilar","Senhor Saboeiro","Nacional","90 g","—","28,64","—","10 dias úteis","Shampoo natural que ajuda a reduzir a queda e hidrata os fios."),
 ("Condicionador Natural Hidratação Capilar Pitaia Vegano","Senhor Saboeiro","Nacional","90 g","—","28,69","—","10 dias úteis","Condicionador vegano com pitaia para fios macios e hidratados."),
 ("Creme Dental Ultra Mint Xilitol Vegano s/ Flúor","Dentil","Nacional","70 g","—","3,35","—","10 dias úteis","Creme dental vegano com xilitol, sem flúor, hálito fresco ultra mint."),
]
import html as H
GR=[("Suplementos Importados","Seleção internacional das marcas mais reconhecidas",[0,1,2,3]),
    ("Suplementos Nacionais","Qualidade nacional com entrega rápida",[4,5,6,7]),
    ("Cuidados Pessoais","Higiene e beleza com ingredientes naturais e veganos",[8,9,10])]
def card(i):
    n,m,o,e,d,p,pd,pr,desc=P[i]
    rows=f'<tr><td>Embalagem</td><td>{e}</td></tr>'
    if d!="—": rows+=f'<tr><td>Rendimento</td><td>{d}</td></tr>'
    rows+=f'<tr><td>Origem</td><td>{o}</td></tr><tr><td>Entrega</td><td>{pr}</td></tr>'
    dose=f'<div class="dose">R$ {pd} por dose</div>' if pd!="—" else '<div class="dose">&nbsp;</div>'
    return f"""<div class="card"><div class="cod">{i+1:02d}</div><div class="marca">{m}</div>
<h3>{H.escape(n)}</h3><p>{desc}</p><table class="spec">{rows}</table>
<div class="price"><div><span class="rs">R$</span>{p}</div>{dose}</div></div>"""
def hdr(t): return f'<div class="hdr"><span class="brand">DO REI <i>Saúde &amp; Suplementos</i></span><span>{t}</span></div>'
def ftr(n): return f'<div class="ftr"><span>Catálogo Outubro 2026</span><span>{n:02d}</span></div>'
secoes=""
for k,(t,sub,ids) in enumerate(GR):
    secoes+=f'<div class="page">{hdr("Catálogo de Produtos")}<div class="sec"><div class="secn">0{k+1}</div><h2>{t}</h2><div class="secsub">{sub}</div></div><div class="grid">'+"".join(card(i) for i in ids)+f'</div>{ftr(k+2)}</div>'
idx="".join(f'<tr><td class="c">{j+1:02d}</td><td><b>{H.escape(x[0])}</b><br><span>{x[1]}</span></td><td>{x[4] if x[4]!="—" else x[3]}</td><td>{x[7]}</td><td class="r">R$ {x[5]}</td></tr>' for j,x in enumerate(P))
html=f"""<!doctype html><html lang="pt-br"><meta charset="utf-8"><title>Catálogo Do Rei</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
@page{{size:A4;margin:0}} *{{box-sizing:border-box}}
:root{{--g:#0f7a4a;--gd:#0b5c38;--gl:#e8f4ee;--t:#1b1f1d;--m:#6b756f;--b:#e3e8e5}}
body{{margin:0;background:#fff;font-family:Inter,Arial,sans-serif;color:var(--t);-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:210mm;height:297mm;padding:14mm 16mm;position:relative;overflow:hidden;page-break-after:always}}
.cover{{padding:0;display:flex}}
.cl{{width:62%;padding:22mm 16mm;display:flex;flex-direction:column}} .cr{{width:38%;background:var(--g)}}
.mark{{font-size:11px;font-weight:700;letter-spacing:4px;color:var(--g)}}
.cover h1{{font-size:64px;line-height:1;font-weight:800;margin:auto 0 6mm;letter-spacing:-2px}}
.cover h1 span{{color:var(--g)}} .cover .lead{{font-size:15px;color:var(--m);font-weight:300;line-height:1.6;max-width:110mm}}
.cover .bar{{width:18mm;height:3px;background:var(--g);margin:10mm 0}}
.cover .meta{{font-size:11px;color:var(--m);letter-spacing:2px;text-transform:uppercase;margin-top:auto}}
.cover .meta b{{display:block;color:var(--t);font-size:13px;letter-spacing:1px;margin-bottom:1mm}}
.logo{{max-width:50mm;max-height:30mm}}
.hdr{{display:flex;justify-content:space-between;font-size:9px;letter-spacing:2px;text-transform:uppercase;color:var(--m);padding-bottom:4mm;border-bottom:1px solid var(--b)}}
.brand{{color:var(--g);font-weight:800}} .brand i{{font-style:normal;font-weight:400;color:var(--m);margin-left:2mm}}
.ftr{{position:absolute;left:16mm;right:16mm;bottom:10mm;display:flex;justify-content:space-between;font-size:9px;color:var(--m);letter-spacing:1px;border-top:1px solid var(--b);padding-top:3mm}}
.sec{{margin:9mm 0 7mm}} .secn{{font-size:11px;font-weight:700;color:var(--g);letter-spacing:3px}}
h2{{font-size:28px;font-weight:800;margin:1mm 0 1mm;letter-spacing:-.5px}} .secsub{{font-size:12px;color:var(--m)}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:6mm}}
.card{{border:1px solid var(--b);border-top:3px solid var(--g);border-radius:2mm;padding:6mm;display:flex;flex-direction:column;position:relative;min-height:98mm}}
.cod{{position:absolute;top:5mm;right:6mm;font-size:10px;color:#b7c2bc;font-weight:600}}
.marca{{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--g)}}
h3{{font-size:15px;line-height:1.3;font-weight:700;margin:2mm 0 2mm}}
p{{font-size:10.5px;color:var(--m);line-height:1.5;margin:0 0 4mm}}
.spec{{width:100%;border-collapse:collapse;font-size:10px;margin-bottom:4mm}} .spec td{{padding:1.6mm 0;border-bottom:1px solid var(--b)}}
.spec td:first-child{{color:var(--m)}} .spec td:last-child{{text-align:right;font-weight:600}}
.price{{margin-top:auto;background:var(--gl);border-radius:1.5mm;padding:3mm 4mm;display:flex;justify-content:space-between;align-items:center}}
.price>div:first-child{{font-size:22px;font-weight:800;color:var(--gd)}} .rs{{font-size:11px;font-weight:600;margin-right:1mm}}
.dose{{font-size:9.5px;color:var(--gd);font-weight:500}}
.tab{{width:100%;border-collapse:collapse;font-size:10px;margin-top:2mm}}
.tab th{{text-align:left;font-size:8.5px;letter-spacing:1.5px;text-transform:uppercase;color:var(--m);font-weight:600;padding:2.5mm 2mm;border-bottom:2px solid var(--g)}}
.tab td{{padding:2.6mm 2mm;border-bottom:1px solid var(--b);vertical-align:middle}} .tab td span{{color:var(--m);font-size:9px}}
.c{{color:#b7c2bc;font-weight:600}} .r{{text-align:right;font-weight:700;color:var(--gd);white-space:nowrap}}
.cta{{margin-top:8mm;background:var(--g);color:#fff;border-radius:2mm;padding:8mm;display:flex;justify-content:space-between;align-items:center}}
.cta h4{{margin:0;font-size:20px;font-weight:800}} .cta div{{font-size:11px;opacity:.9;line-height:1.6}}
.note{{font-size:8.5px;color:var(--m);margin-top:6mm;line-height:1.6}}
</style><body>
<div class="page cover"><div class="cl"><img class="logo" src="logo.png" onerror="this.outerHTML='<div class=mark>DO REI</div>'">
<h1>Saúde &amp;<br><span>Suplementos</span></h1><div class="lead">Suplementos importados e nacionais selecionados, com qualidade garantida e atendimento personalizado.</div>
<div class="bar"></div><div class="meta"><b>Catálogo de Produtos</b>Outubro 2026</div></div><div class="cr"></div></div>
{secoes}
<div class="page">{hdr("Tabela de Preços")}<div class="sec"><div class="secn">RESUMO</div><h2>Tabela de Preços</h2><div class="secsub">Todos os produtos em uma visão rápida</div></div>
<table class="tab"><tr><th>Cód.</th><th>Produto</th><th>Rend.</th><th>Entrega</th><th class="r">Preço</th></tr>{idx}</table>
<div class="cta"><div><h4>Faça seu pedido</h4><div>Atendimento direto pelo WhatsApp.</div></div><div style="text-align:right">Informe o código do produto<br>e a quantidade desejada.</div></div>
<div class="note">Preços válidos para outubro de 2026, sujeitos a alteração sem aviso prévio. Prazos de entrega contados em dias úteis após a confirmação do pedido. Suplementos alimentares não substituem uma alimentação equilibrada; consulte um profissional de saúde.</div>{ftr(5)}</div>
</body></html>"""
open("catalogo.html","w").write(html)
msg = "MENSAGENS PARA AS FOTOS DOS PRODUTOS NO WHATSAPP\n(copie e cole como legenda de cada foto)\n\n"
for n,m,o,e,d,p,pd,pr,desc in P:
    msg += f"━━━━━━━━━━━━━━━━\n👑 *Do Rei – Saúde e Suplementos*\n\n✨ *{n}*\n🏷️ {m} ({o.lower()})\n\n{desc}\n\n📦 {e}" + (f" – {d}" if d!="—" else "") + f"\n💰 *R$ {p}*" + (f" (apenas R$ {pd} por dose!)" if pd!="—" else "") + f"\n🚚 Entrega em {pr}\n\n📲 Peça já o seu! Responda esta mensagem.\n\n"
open("mensagens-whatsapp.txt","w").write(msg)
