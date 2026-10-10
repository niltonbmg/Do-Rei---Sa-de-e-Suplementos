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
def icon(kind):
    if kind=="frasco": return '<svg viewBox="0 0 60 80"><rect x="18" y="4" width="24" height="10" rx="2" fill="#c9a227"/><rect x="10" y="14" width="40" height="62" rx="8" fill="#1d5c3a"/><rect x="14" y="32" width="32" height="26" rx="3" fill="#f6efd9"/><text x="30" y="49" font-size="10" text-anchor="middle" fill="#1d5c3a" font-weight="bold">♛</text></svg>'
    if kind=="gotas": return '<svg viewBox="0 0 60 80"><rect x="24" y="2" width="12" height="16" rx="3" fill="#c9a227"/><rect x="16" y="18" width="28" height="58" rx="6" fill="#1d5c3a"/><rect x="20" y="36" width="20" height="24" rx="3" fill="#f6efd9"/><text x="30" y="52" font-size="9" text-anchor="middle" fill="#1d5c3a">♛</text></svg>'
    if kind=="pote": return '<svg viewBox="0 0 60 80"><rect x="8" y="12" width="44" height="10" rx="3" fill="#c9a227"/><rect x="6" y="22" width="48" height="52" rx="6" fill="#1d5c3a"/><rect x="12" y="36" width="36" height="24" rx="3" fill="#f6efd9"/><text x="30" y="52" font-size="9" text-anchor="middle" fill="#1d5c3a">♛</text></svg>'
    return '<svg viewBox="0 0 60 80"><rect x="20" y="4" width="20" height="12" rx="3" fill="#c9a227"/><path d="M14 16h32l4 58H10z" fill="#1d5c3a"/><rect x="16" y="34" width="28" height="22" rx="3" fill="#f6efd9"/><text x="30" y="49" font-size="9" text-anchor="middle" fill="#1d5c3a">♛</text></svg>'
KIND=["frasco","frasco","frasco","frasco","frasco","gotas","frasco","pote","tubo","tubo","tubo"]
GR=[("Suplementos Importados","Qualidade internacional selecionada",[0,1,2,3]),
    ("Suplementos Nacionais","Entrega rápida, marcas de confiança",[4,5,6,7]),
    ("Cuidados Pessoais Naturais","Higiene e beleza veganas",[8,9,10])]
def card(i):
    n,m,o,e,d,p,pd,pr,desc=P[i]
    dose=f'<span class="dose">R$ {pd} / dose</span>' if pd!="—" else ""
    info=e+(f" · {d}" if d!="—" else "")
    return f'''<div class="card"><div class="img">{icon(KIND[i])}</div><div class="body">
<div class="top"><span class="marca">{m}</span><span class="tag {o.lower()}">{o}</span></div>
<h3>{H.escape(n)}</h3><p>{desc}</p><div class="info">{info}</div>
<div class="bottom"><div><span class="rs">R$</span><span class="pr">{p}</span>{dose}</div><div class="prazo">Entrega<br><b>{pr}</b></div></div></div></div>'''
secoes=""
for t,sub,ids in GR:
    secoes+=f'<div class="page"><div class="hdr"><b>♛ Do Rei</b><span>Catálogo · Outubro 2026</span></div><section><div class="sec"><span class="num">{GR.index((t,sub,ids))+1:02d}</span><div><h2>{t}</h2><div class="secsub">{sub}</div></div></div>'+"".join(card(i) for i in ids)+'</section></div>'
idx="".join(f'<tr><td>{H.escape(x[0])}</td><td>{x[1]}</td><td>{x[7]}</td><td class="r">R$ {x[5]}</td></tr>' for x in P)
html=f'''<!doctype html><html lang="pt-br"><meta charset="utf-8"><title>Catálogo Do Rei</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;800&family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet">
<style>
@page{{size:A4;margin:0}} *{{box-sizing:border-box}} body{{margin:0;font-family:Montserrat,Arial,sans-serif;color:#1f2a24;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:210mm;height:297mm;overflow:hidden;padding:16mm 15mm 14mm;position:relative;page-break-after:always}}
.cover{{background:radial-gradient(circle at 50% 35%,#24704a,#0f3522 75%);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;height:297mm}}
.cover .logo{{max-height:60mm;margin-bottom:8mm}} .crown{{font-size:70px;color:#e2c15a}}
.cover h1{{font-family:'Playfair Display',serif;font-size:54px;margin:4mm 0 0;letter-spacing:1px}}
.cover .tg{{color:#e2c15a;letter-spacing:6px;font-size:14px;text-transform:uppercase;margin-top:3mm}}
.cover .line{{width:60mm;height:2px;background:#e2c15a;margin:12mm auto}}
.cover .ed{{font-family:'Playfair Display',serif;font-size:26px}} .cover .ed2{{font-size:13px;opacity:.8;margin-top:3mm;letter-spacing:2px}}
.cover .foot{{position:absolute;bottom:16mm;font-size:12px;opacity:.85;letter-spacing:1px}}
.hdr{{display:flex;justify-content:space-between;align-items:center;border-bottom:1.5px solid #c9a227;padding-bottom:3mm;margin-bottom:6mm;font-size:10px;color:#1d5c3a;letter-spacing:2px;text-transform:uppercase}}
.hdr b{{font-family:'Playfair Display',serif;font-size:15px;letter-spacing:0;text-transform:none}}
section{{break-inside:auto}}
.sec{{display:flex;gap:4mm;align-items:center;margin:2mm 0 5mm;break-after:avoid}} .num{{font-family:'Playfair Display';font-size:34px;color:#c9a227;font-weight:800}}
h2{{font-family:'Playfair Display',serif;font-size:24px;margin:0;color:#14452c}} .secsub{{font-size:11px;color:#7a857f;letter-spacing:1px}}
.card{{display:flex;border-radius:4mm;background:#fbf8ef;margin-bottom:6mm;min-height:52mm;overflow:hidden;break-inside:avoid;border:1px solid #ece3c6}}
.img{{width:38mm;background:linear-gradient(160deg,#f3e9c8,#e6d7a6);display:flex;align-items:center;justify-content:center}} .img svg{{width:26mm;height:36mm}}
.body{{flex:1;padding:4mm 5mm}} .top{{display:flex;justify-content:space-between;align-items:center}}
.marca{{font-size:9.5px;letter-spacing:2px;text-transform:uppercase;color:#9a7b16;font-weight:700}}
.tag{{font-size:8.5px;padding:1mm 2.5mm;border-radius:10px;color:#fff;letter-spacing:1px;text-transform:uppercase}} .importado{{background:#2b5d8f}} .nacional{{background:#1d8a4a}}
h3{{font-family:'Playfair Display',serif;font-size:17px;margin:1.5mm 0 1mm;color:#14452c}}
p{{font-size:11px;margin:0 0 1.5mm;color:#45524b;line-height:1.4}} .info{{font-size:10px;color:#7a857f}}
.bottom{{display:flex;justify-content:space-between;align-items:flex-end;margin-top:2mm;border-top:1px dashed #d8cba0;padding-top:2mm}}
.rs{{font-size:12px;font-weight:700;color:#14452c;margin-right:1mm}} .pr{{font-size:24px;font-weight:700;color:#14452c}}
.dose{{display:inline-block;margin-left:3mm;font-size:9.5px;background:#14452c;color:#e2c15a;padding:1mm 2.5mm;border-radius:10px}}
.prazo{{text-align:right;font-size:9px;color:#7a857f;text-transform:uppercase;letter-spacing:1px}} .prazo b{{color:#14452c;font-size:11px;text-transform:none;letter-spacing:0}}
table{{width:100%;border-collapse:collapse;font-size:11px}} th{{background:#14452c;color:#e2c15a;text-align:left;padding:2.5mm;font-weight:600;letter-spacing:1px}}
td{{padding:2.3mm 2.5mm;border-bottom:1px solid #ece3c6}} tr:nth-child(even) td{{background:#fbf8ef}} .r{{text-align:right;font-weight:700;white-space:nowrap}}
.cta{{margin-top:8mm;background:#14452c;color:#fff;border-radius:4mm;padding:7mm;text-align:center}}
.cta h2{{color:#e2c15a;font-size:22px}} .cta div{{font-size:12px;margin-top:2mm;line-height:1.6}}
.note{{font-size:9px;color:#7a857f;margin-top:5mm;text-align:center}}
</style><body>
<div class="page cover"><img class="logo" src="logo.png" onerror="this.outerHTML='<div class=crown>♛</div>'">
<h1>Do Rei</h1><div class="tg">Saúde &amp; Suplementos</div><div class="line"></div>
<div class="ed">Catálogo de Produtos</div><div class="ed2">OUTUBRO · 2026</div>
<div class="foot">Suplementos importados e nacionais · Cuidados naturais</div></div>
{secoes}
<div class="page"><div class="hdr"><b>♛ Do Rei</b><span>Tabela de preços</span></div>
<h2 style="margin-bottom:5mm">Tabela de Preços Resumida</h2>
<table><tr><th>Produto</th><th>Marca</th><th>Entrega</th><th class="r">Preço</th></tr>{idx}</table>
<div class="cta"><h2>Faça seu pedido!</h2><div>Chame a gente no WhatsApp e garanta o seu.<br>Atendimento personalizado da equipe Do Rei.</div></div>
<div class="note">Preços válidos para outubro/2026, sujeitos a alteração sem aviso prévio. Prazos de entrega em dias úteis após a confirmação do pedido.<br>Suplementos não substituem uma alimentação equilibrada. Consulte um profissional de saúde.</div></div>
</body></html>'''
open("catalogo.html","w").write(html)
msg = "MENSAGENS PARA AS FOTOS DOS PRODUTOS NO WHATSAPP\n(copie e cole como legenda de cada foto)\n\n"
for n,m,o,e,d,p,pd,pr,desc in P:
    msg += f"━━━━━━━━━━━━━━━━\n👑 *Do Rei – Saúde e Suplementos*\n\n✨ *{n}*\n🏷️ {m} ({o.lower()})\n\n{desc}\n\n📦 {e}" + (f" – {d}" if d!="—" else "") + f"\n💰 *R$ {p}*" + (f" (apenas R$ {pd} por dose!)" if pd!="—" else "") + f"\n🚚 Entrega em {pr}\n\n📲 Peça já o seu! Responda esta mensagem.\n\n"
open("mensagens-whatsapp.txt","w").write(msg)
