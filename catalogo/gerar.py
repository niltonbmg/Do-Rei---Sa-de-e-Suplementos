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
cards = ""
for n,m,o,e,d,p,pd,pr,desc in P:
    dose = f'<div class="dose">R$ {pd} por dose</div>' if pd!="—" else ""
    info = e + (f" · {d}" if d!="—" else "")
    cards += f'''<div class="card"><div class="tag {o.lower()}">{o}</div>
<h3>{n}</h3><div class="marca">{m}</div><p>{desc}</p>
<div class="info">{info}</div><div class="pr">R$ {p}</div>{dose}
<div class="prazo">🚚 Entrega: {pr}</div></div>'''
html = f'''<!doctype html><html lang="pt-br"><meta charset="utf-8"><title>Catálogo Do Rei</title>
<style>
@page{{size:A4;margin:12mm}} body{{font-family:Arial,Helvetica,sans-serif;color:#222;margin:0}}
header{{text-align:center;border-bottom:4px solid #c9a227;padding-bottom:10px;margin-bottom:14px}}
.logo{{height:90px}} h1{{margin:6px 0 2px;color:#1d5c3a;font-size:28px}} .sub{{color:#666}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}
.card{{border:1px solid #ddd;border-radius:10px;padding:10px 12px;break-inside:avoid;position:relative}}
.card h3{{margin:0 70px 2px 0;font-size:14px;color:#1d5c3a}} .marca{{font-size:12px;color:#888}}
.card p{{font-size:12px;margin:6px 0}} .info{{font-size:11px;color:#555}}
.pr{{font-size:22px;font-weight:bold;color:#c0392b;margin-top:4px}} .dose{{font-size:11px;color:#555}}
.prazo{{font-size:11px;margin-top:4px}}
.tag{{position:absolute;top:8px;right:8px;font-size:10px;padding:2px 6px;border-radius:8px;color:#fff}}
.importado{{background:#2c6fbb}} .nacional{{background:#1d8a4a}}
footer{{margin-top:14px;text-align:center;font-size:13px;background:#1d5c3a;color:#fff;padding:10px;border-radius:8px}}
</style><body><header>
<img class="logo" src="logo.png" onerror="this.style.display='none'">
<h1>👑 Do Rei – Saúde e Suplementos</h1><div class="sub">Catálogo de Produtos · Outubro 2026</div></header>
<div class="grid">{cards}</div>
<footer>📲 Faça seu pedido pelo WhatsApp! · Preços sujeitos a alteração · Prazos de entrega em dias úteis</footer>
</body></html>'''
open("catalogo.html","w").write(html)
msg = "MENSAGENS PARA AS FOTOS DOS PRODUTOS NO WHATSAPP\n(copie e cole como legenda de cada foto)\n\n"
for n,m,o,e,d,p,pd,pr,desc in P:
    msg += f"━━━━━━━━━━━━━━━━\n👑 *Do Rei – Saúde e Suplementos*\n\n✨ *{n}*\n🏷️ {m} ({o.lower()})\n\n{desc}\n\n📦 {e}" + (f" – {d}" if d!="—" else "") + f"\n💰 *R$ {p}*" + (f" (apenas R$ {pd} por dose!)" if pd!="—" else "") + f"\n🚚 Entrega em {pr}\n\n📲 Peça já o seu! Responda esta mensagem.\n\n"
open("mensagens-whatsapp.txt","w").write(msg)
