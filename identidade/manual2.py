pages=[]; n=[0]
def P(title_k,title,body,dark=False,num=True):
    n[0]+=1
    hd=f'<div class="hd"><img src="{"logo-do-rei-negativo.svg" if dark else "logo-do-rei-horizontal.svg"}" class="{"hld" if dark else "hl"}"><span>MANUAL DE MARCA</span><span>{title_k}</span></div>'
    ft=f'<div class="ft"><span>Do Rei · Saúde &amp; Suplementos</span><span>Manual de Marca · 2026</span><span>{n[0]:02d}</span></div>' if num else ""
    pages.append(f'<div class="page{" dark" if dark else ""}">{hd}<h1>{title}</h1>{body}{ft}</div>')
# capa
n[0]+=1
pages.append('''<div class="page cover"><div class="cv-top">MANUAL DE IDENTIDADE VISUAL · EDIÇÃO 2026</div><img class="cv-logo" src="logo-do-rei-negativo.svg"><div class="cv-line"></div>
<div class="cv-t">Manual de <em>Marca.</em></div><div class="cv-s">Como usar a marca Do Rei, em todos os lugares, sempre do mesmo jeito.</div>
<div class="cv-bot"><span>Versão 1.0</span><span>Outubro 2026</span><span>Uso interno e fornecedores</span></div></div>''')
sec=[("01","Conceito","A coroa que serve"),("02","Anatomia","As partes da logo"),("03","Versões","Qual logo usar"),("04","Mapa de aplicação","Onde usar cada versão"),("05","Proteção e tamanho","Respiro e mínimos"),("06","Cores","Paleta e proporção"),("07","Tipografia","Fontes e hierarquia"),("08","Fundos","Onde a logo pode ficar"),("09","Usos incorretos","O que nunca fazer"),("10","Aplicações","A marca no mundo real"),("11","Tom de voz","Como falamos"),("12","Arquivos","Qual arquivo usar")]
P("SUMÁRIO","Sumário",'<div class="toc">'+"".join(f'<div class="tr"><span class="tn">{a}</span><b>{b}</b><em>{c}</em><span class="tp">{int(a)+2:02d}</span></div>' for a,b,c in sec)+'</div>')
P("01 · CONCEITO","A coroa <em>que serve.</em>",'''<div class="hero"><img src="logo-do-rei.svg"></div>
<div class="two"><div><div class="k">O SÍMBOLO</div><p>Uma <b>coroa</b> e uma <b>mão aberta que oferece</b>, num único traço. À primeira vista, a pessoa vê uma coroa elegante. Num segundo olhar, percebe a mão que serve e cuida.</p></div>
<div><div class="k">O ENIGMA</div><p>O Rei da marca não se apresenta pela logo. As pessoas o descobrem pela experiência: verdade no que dizemos, cuidado com quem compra e serviço com excelência.</p></div></div>
<div class="quote">“Cuidado com o corpo, <em>feito com verdade e serviço.</em>”</div>
<div class="vals"><div><b>Confiável</b><p>Informação honesta, preço justo, promessa cumprida.</p></div><div><b>Premium</b><p>Produtos selecionados e acabamento impecável.</p></div><div><b>Próxima</b><p>Atendimento de quem conhece o cliente pelo nome.</p></div><div><b>Serviço</b><p>O interesse do cliente vem primeiro.</p></div></div>''')
P("02 · ANATOMIA","As partes <em>da logo.</em>",'''<div class="anat"><img src="logo-do-rei.svg"><div class="lb l1"><span>1</span>Símbolo</div><div class="lb l2"><span>2</span>Nome</div><div class="lb l3"><span>3</span>Assinatura</div></div>
<table class="tb"><tr><th>Parte</th><th>O que é</th><th>Regra</th></tr>
<tr><td><b>1 · Símbolo</b></td><td>Coroa + mão que serve, em linha dourada uniforme</td><td>Pode ser usado sozinho (ícone, lacre, bordado). Nunca redesenhar.</td></tr>
<tr><td><b>2 · Nome</b></td><td>"DO REI" em Montserrat Medium, azul-marinho</td><td>Nunca trocar a fonte, nunca escrever em outra cor que não as oficiais.</td></tr>
<tr><td><b>3 · Assinatura</b></td><td>"SAÚDE &amp; SUPLEMENTOS" em Montserrat Light espaçada, mesma largura do nome</td><td>Some quando a logo ficar menor que 25 mm; aí use a versão sem assinatura ou o ícone.</td></tr></table>
<p class="sm">A logo é sempre usada a partir dos arquivos oficiais (página 14). Nunca recrie a logo digitando o nome ou desenhando a coroa.</p>''')
V=[("logo-do-rei.svg","","Vertical colorida","Versão principal. Catálogo, materiais impressos, posts, documentos. Sempre que houver espaço em altura."),
("logo-do-rei-horizontal.svg","","Horizontal","Espaços largos e baixos: cabeçalho de site, assinatura de e-mail, fachada, rodapé de documentos."),
("logo-do-rei-negativo.svg","nv","Negativo","Fundos azul-marinho ou fotos escuras: capa do catálogo, stories, cartão (frente), fachada."),
("icone-do-rei.svg","","Ícone","Espaços pequenos e quadrados: foto de perfil (WhatsApp, Instagram), favicon, lacre, bordado."),
("logo-do-rei-azul.svg","","Uma cor · azul","Impressão em 1 cor: etiqueta, carimbo, sacola kraft, nota fiscal, fax/fotocópia."),
("logo-do-rei-branca.svg","nv","Uma cor · branca","Sobre fotos e fundos coloridos escuros, gravação a laser, bordado claro em tecido escuro.")]
P("03 · VERSÕES","Qual logo <em>usar.</em>",'<div class="vg">'+"".join(f'<div class="vc"><div class="vb {c}"><img src="{f}"></div><b>{t}</b><p>{d}</p></div>' for f,c,t,d in V)+'</div>')
M=[("WhatsApp · foto de perfil","Ícone","Arquivo pronto 640 × 640 px"),("WhatsApp · foto do grupo","Vertical colorida, fundo branco","foto-grupo-whatsapp.png (640 px)"),
("Instagram · perfil","Ícone","1080 × 1080 px"),("Instagram · posts","Horizontal ou ícone no canto","Marca d'água: 8–10% da largura"),
("Instagram · stories","Negativo","Topo ou rodapé, longe das bordas"),("Etiqueta do produto","Azul 1 cor ou ícone","Mínimo 25 mm (logo) / 12 mm (ícone)"),
("Lacre de embalagem","Ícone dourado","Adesivo redondo de 3 a 4 cm"),("Sacola","Azul 1 cor (kraft) ou negativo (sacola azul)","Logo com 30–40% da largura"),
("Fachada / placa","Horizontal ou negativo","Letras douradas em relevo sobre azul-marinho"),("Cartão de visita","Frente: negativo · Verso: vertical colorida","Logo com 45–55 mm de largura"),
("Catálogo","Capa: negativo · Páginas: horizontal no cabeçalho","Cabeçalho com 8–10 mm de altura"),("Site","Horizontal no topo · Ícone como favicon","Altura de 40–56 px no topo"),
("Assinatura de e-mail","Horizontal","180–220 px de largura"),("Uniforme / camiseta","Ícone bordado no peito","Dourado em tecido azul; 7–9 cm"),
("Carimbo / nota","Azul 1 cor","Sem a assinatura se < 25 mm")]
P("04 · MAPA DE APLICAÇÃO","Onde usar <em>cada versão.</em>",'<table class="tb map"><tr><th>Onde</th><th>Versão</th><th>Tamanho / observação</th></tr>'+"".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>" for a,b,c in M)+'</table>')
P("05 · PROTEÇÃO E TAMANHO","Respiro e <em>tamanho mínimo.</em>",'''<div class="safe"><div class="sz"><img src="logo-do-rei.svg"></div><div class="x xt">x</div><div class="x xl">x</div></div>
<p><b>Área de proteção:</b> ao redor da logo, mantenha livre um espaço igual a <b>x</b> = a altura do losango central da coroa × 2. Nada de texto, borda ou imagem dentro dessa área.</p>
<div class="mins"><div><div class="mb"><img src="logo-do-rei.svg" style="width:25mm"></div><b>Vertical</b><p>Mínimo 25 mm impresso / 120 px tela</p></div>
<div><div class="mb"><img src="logo-do-rei-horizontal.svg" style="width:40mm"></div><b>Horizontal</b><p>Mínimo 40 mm / 180 px</p></div>
<div><div class="mb"><img src="icone-do-rei.svg" style="width:10mm"></div><b>Ícone</b><p>Mínimo 10 mm / 32 px</p></div></div>''')
P("06 · CORES","Paleta <em>oficial.</em>",'''<div class="pal"><div class="sw" style="background:#0B2A5B;color:#fff;flex:6"><b>Azul-marinho</b><span>60%</span></div><div class="sw" style="background:#fff;color:#0B2A5B;flex:3;border:1px solid #E1E7F0"><b>Branco</b><span>30%</span></div><div class="sw" style="background:#D4A72C;color:#0B2A5B;flex:1"><b>Dourado</b><span>10%</span></div></div>
<p class="sm">Proporção de uso: o azul domina, o branco dá respiro e o dourado é só detalhe (símbolo, preços, filetes, selos). Dourado nunca vira fundo de grandes áreas.</p>
<table class="tb"><tr><th>Cor</th><th>HEX</th><th>RGB</th><th>CMYK (aprox.)</th><th>Uso</th></tr>
<tr><td><i class="dot" style="background:#0B2A5B"></i><b>Azul-marinho</b></td><td>#0B2A5B</td><td>11 42 91</td><td>88 54 0 64</td><td>Nome, títulos, fundos</td></tr>
<tr><td><i class="dot" style="background:#D4A72C"></i><b>Dourado</b></td><td>#D4A72C</td><td>212 167 44</td><td>0 21 79 17</td><td>Símbolo, preços, detalhes</td></tr>
<tr><td><i class="dot" style="background:#1F4FA3"></i><b>Azul royal</b></td><td>#1F4FA3</td><td>31 79 163</td><td>81 52 0 36</td><td>Links, botões, destaques</td></tr>
<tr><td><i class="dot" style="background:#EAF1FB"></i><b>Azul-gelo</b></td><td>#EAF1FB</td><td>234 241 251</td><td>7 4 0 2</td><td>Fundos de seção</td></tr>
<tr><td><i class="dot" style="background:#14213D"></i><b>Texto</b></td><td>#14213D</td><td>20 33 61</td><td>67 46 0 76</td><td>Textos corridos</td></tr></table>
<p class="sm">Gráfica: peça sempre uma prova de cor. Para placa e brinde, o dourado pode ser metalizado (hot stamping, latão escovado).</p>''')
P("07 · TIPOGRAFIA","Fontes e <em>hierarquia.</em>",'''<div class="ty"><div class="tl">MONTSERRAT · MEDIUM / LIGHT</div><div style="font:500 40px Montserrat;letter-spacing:3px;color:#0B2A5B">DO REI</div><div style="font:300 15px Montserrat;letter-spacing:6px;color:#0B2A5B">SAÚDE &amp; SUPLEMENTOS</div><p>Marca, títulos de site e redes sociais, chamadas curtas.</p></div>
<div class="ty"><div class="tl">CORMORANT GARAMOND · EDITORIAL</div><div style="font:400 38px 'Cormorant Garamond';color:#0B2A5B">Cuidado com o corpo, <em style="color:#1F4FA3">feito com verdade.</em></div><p>Títulos do catálogo, nomes de produto, frases de impacto. Segunda parte sempre em itálico.</p></div>
<div class="ty"><div class="tl">INTER · TEXTO</div><div style="font:400 15px Inter;color:#14213D">Auxilia na formação das células vermelhas do sangue.</div><p>Textos corridos, tabelas, preços, mensagens.</p></div>
<div class="ty"><div class="tl">JETBRAINS MONO · RÓTULOS</div><div style="font:600 12px 'JetBrains Mono';letter-spacing:3px;color:#1F4FA3">FICHA 05 · NACIONAL</div><p>Rótulos, numeração, legendas técnicas, em maiúsculas espaçadas.</p></div>
<p class="sm">Todas gratuitas no Google Fonts. No celular e no Canva, se não houver a fonte, use Montserrat para tudo.</p>''')
F=[("#fff","logo-do-rei.svg","Branco","✓"),("#EAF1FB","logo-do-rei.svg","Azul-gelo","✓"),("#0B2A5B","logo-do-rei-negativo.svg","Azul-marinho","✓"),("linear-gradient(135deg,#1b2433,#3a4658)","logo-do-rei-branca.svg","Foto escura","✓"),("#D4A72C","logo-do-rei.svg","Dourado","✕"),("#7A3B3B","logo-do-rei.svg","Cores fora da paleta","✕")]
P("08 · FUNDOS","Onde a logo <em>pode ficar.</em>",'<div class="vg">'+"".join(f'<div class="vc"><div class="vb" style="background:{b}"><img src="{l}"></div><b>{"<span class=ok>✓</span>" if o=="✓" else "<span class=no>✕</span>"} {t}</b></div>' for b,l,t,o in F)+'</div><p class="sm">Regra simples: fundo claro → versão colorida ou azul. Fundo escuro → negativo ou branca. Fundo colorido ou foto clara → evite; se precisar, use uma faixa branca ou azul atrás da logo.</p>')
W=[("transform:scaleX(1.4)","Não esticar ou achatar"),("filter:hue-rotate(140deg)","Não trocar as cores"),("filter:drop-shadow(3mm 3mm 2mm rgba(0,0,0,.5))","Não aplicar sombra, brilho ou 3D"),("transform:rotate(-14deg)","Não girar"),("opacity:.35","Não usar transparente/apagada"),("outline:3px solid #0B2A5B;outline-offset:2mm","Não colocar moldura ou caixa")]
P("09 · USOS INCORRETOS","O que <em>nunca fazer.</em>",'<div class="vg">'+"".join(f'<div class="vc"><div class="vb bad"><img src="logo-do-rei.svg" style="{s}"></div><b><span class=no>✕</span> {t}</b></div>' for s,t in W)+'</div><p class="sm">Também não: trocar a fonte, separar a coroa e mudar a posição dela, adicionar elementos (folhas, estrelas, cruz), usar a coroa antiga ou imagens geradas por IA no lugar da logo oficial.</p>')
P("10 · APLICAÇÕES","A marca no <em>mundo real.</em>",'''<div class="apps">
<div class="ap"><div class="card f"><img src="logo-do-rei-negativo.svg"></div><div class="card b"><img src="logo-do-rei-horizontal.svg"><span>(00) 00000-0000 · @dorei</span></div><b>Cartão de visita</b></div>
<div class="ap"><div class="phone"><div class="av"><img src="icone-do-rei.svg"></div><b>Do Rei</b><span>Saúde &amp; Suplementos</span></div><b>Perfil WhatsApp / Instagram</b></div>
<div class="ap"><div class="bag"><div class="handle"></div><img src="logo-do-rei-azul.svg"></div><b>Sacola kraft</b></div>
<div class="ap"><div class="jar"><div class="lid"></div><div class="lab"><img src="icone-do-rei.svg"><span>DO REI</span></div></div><b>Lacre / etiqueta</b></div>
<div class="ap wide"><div class="wall"><img src="logo-do-rei-horizontal.svg" style="filter:brightness(0) saturate(100%) invert(72%) sepia(52%) saturate(600%) hue-rotate(5deg)"></div><b>Fachada · letras douradas sobre azul</b></div></div>''')
P("11 · TOM DE VOZ","Como <em>falamos.</em>",'''<div class="two"><div><div class="k">SOMOS</div><ul><li>Próximos: falamos como quem conhece o cliente.</li><li>Verdadeiros: dizemos para quem o produto é e para quem não é.</li><li>Simples: frases curtas, sem jargão.</li><li>Cuidadosos: benefício sempre com a alegação permitida ("auxilia na…").</li></ul></div>
<div><div class="k">NÃO SOMOS</div><ul><li>Exagerados: nada de "milagroso", "cura", "emagrece rápido".</li><li>Insistentes: não empurramos produto.</li><li>Religiosos na comunicação: a fé aparece no serviço, não no anúncio.</li><li>Informais demais: sem gírias e excesso de emoji.</li></ul></div></div>
<div class="k">FRASES DA MARCA</div><div class="quote sm2">“Cuidado com o corpo, <em>feito com verdade e serviço.</em>”</div>
<table class="tb"><tr><th>Em vez de</th><th>Diga</th></tr><tr><td>"Compre já, últimas unidades!!!"</td><td>"Fechamos os pedidos na sexta, às 18 h."</td></tr><tr><td>"Acaba com o cansaço"</td><td>"Auxilia no metabolismo energético"</td></tr><tr><td>"O melhor preço do Brasil"</td><td>"Preço justo, produto original e entrega combinada"</td></tr></table>''')
FL=[("logo-do-rei.svg / .png","Vertical colorida","Uso geral"),("logo-do-rei-horizontal.svg / .png","Horizontal","Site, e-mail, fachada"),("logo-do-rei-negativo.svg / .png","Negativo","Fundos azuis e escuros"),("logo-do-rei-azul.svg / .png","Uma cor azul","Etiqueta, carimbo, sacola"),("logo-do-rei-branca.svg / .png","Uma cor branca","Fotos escuras, laser"),("icone-do-rei.svg / .png","Ícone","Perfis, favicon, lacre"),("foto-grupo-whatsapp.png","Foto do grupo","Grupo de WhatsApp")]
P("12 · ARQUIVOS","Qual arquivo <em>usar.</em>",'<table class="tb"><tr><th>Arquivo</th><th>Versão</th><th>Para</th></tr>'+"".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>" for a,b,c in FL)+'</table><div class="two" style="margin-top:8mm"><div><div class="k">SVG</div><p>Vetor: para gráfica, fachada, brinde, site. Pode ampliar sem perder qualidade.</p></div><div><div class="k">PNG</div><p>Imagem com fundo transparente: para WhatsApp, Instagram, Canva, documentos.</p></div></div><p class="sm">Todos os arquivos estão na pasta <b>identidade/</b>. Dúvida sobre uso? Na dúvida, use a vertical colorida em fundo branco.</p>')
CSS='''@page{size:A4;margin:0}*{box-sizing:border-box}body{margin:0;font-family:Inter,sans-serif;color:#14213D;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;padding:13mm 16mm;position:relative;overflow:hidden;page-break-after:always;background:#fff}
.hd{display:grid;grid-template-columns:auto 1fr auto;gap:6mm;align-items:center;font:500 8px 'JetBrains Mono',monospace;letter-spacing:2.2px;color:#1F4FA3;padding-bottom:4mm;border-bottom:1px solid #E1E7F0}.hd span:nth-child(3){color:#5B6B82}.hl{height:8mm}
.ft{position:absolute;left:16mm;right:16mm;bottom:9mm;display:flex;justify-content:space-between;font:500 7.5px 'JetBrains Mono',monospace;letter-spacing:1.5px;color:#5B6B82;text-transform:uppercase}
h1{font:400 44px/1.05 'Cormorant Garamond',serif;color:#0B2A5B;margin:12mm 0 8mm}h1 em{color:#1F4FA3}
.k{font:600 8.5px 'JetBrains Mono',monospace;letter-spacing:2.5px;color:#1F4FA3;margin:6mm 0 2mm}p{font-size:11.5px;line-height:1.65;margin:0 0 3mm}.sm{font-size:10px;color:#5B6B82;margin-top:5mm}
.cover{background:#0B2A5B;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}.cv-top{position:absolute;top:16mm;font:500 8.5px 'JetBrains Mono';letter-spacing:3px;color:#D4A72C}
.cv-logo{width:85mm}.cv-line{width:16mm;height:1.5px;background:#D4A72C;margin:12mm 0}.cv-t{font:400 46px 'Cormorant Garamond'}.cv-t em{color:#D4A72C}.cv-s{font-size:12px;color:#B9C6DD;margin-top:4mm}
.cv-bot{position:absolute;bottom:14mm;left:16mm;right:16mm;display:flex;justify-content:space-between;font:500 7.5px 'JetBrains Mono';letter-spacing:2px;color:#B9C6DD;text-transform:uppercase}
.toc{border-top:1px solid #E1E7F0}.tr{display:flex;align-items:baseline;gap:5mm;padding:4mm 0;border-bottom:1px solid #E1E7F0}.tn{font:600 9px 'JetBrains Mono';color:#D4A72C;width:8mm}.tr b{font:400 22px 'Cormorant Garamond';color:#0B2A5B;width:70mm}.tr em{font-size:11px;color:#5B6B82;font-style:normal;flex:1}.tp{font:500 9px 'JetBrains Mono';color:#5B6B82}
.hero{height:70mm;display:flex;align-items:center;justify-content:center;background:#F4F6F9;margin-bottom:6mm}.hero img{height:58mm}
.two{display:grid;grid-template-columns:1fr 1fr;gap:9mm}.two ul{margin:0;padding-left:4mm}.two li{font-size:11px;line-height:1.55;margin-bottom:1.5mm}
.quote{font:400 26px/1.3 'Cormorant Garamond';color:#0B2A5B;margin:8mm 0;border-left:2px solid #D4A72C;padding-left:6mm}.quote em{color:#1F4FA3}.quote.sm2{font-size:22px;margin:3mm 0 6mm}
.vals{display:grid;grid-template-columns:repeat(4,1fr);gap:4mm}.vals div{border-top:2px solid #D4A72C;padding-top:3mm}.vals b{color:#0B2A5B;font-size:12px}.vals p{font-size:10px;color:#5B6B82;margin-top:1mm}
.anat{position:relative;height:95mm;background:#F4F6F9;display:flex;align-items:center;justify-content:center;margin-bottom:6mm}.anat img{height:80mm}
.lb{position:absolute;right:12mm;font:600 9px 'JetBrains Mono';letter-spacing:2px;color:#0B2A5B;display:flex;align-items:center;gap:2mm}.lb span{width:6mm;height:6mm;border-radius:50%;background:#D4A72C;color:#fff;display:flex;align-items:center;justify-content:center}
.l1{top:22mm}.l2{top:60mm}.l3{top:76mm}
.tb{width:100%;border-collapse:collapse;font-size:10.5px}.tb th{text-align:left;font:600 7.5px 'JetBrains Mono';letter-spacing:2px;color:#1F4FA3;padding:2mm;border-bottom:1.5px solid #0B2A5B}.tb td{padding:2.4mm 2mm;border-bottom:1px solid #E1E7F0;vertical-align:top}.tb td b{color:#0B2A5B}
.map{font-size:12px}.map td{padding:3.6mm 2mm}
.vg{display:grid;grid-template-columns:1fr 1fr;gap:6mm 7mm}.vc b{font-size:12px;color:#0B2A5B;display:block;margin-top:2mm}.vc p{font-size:10px;color:#5B6B82;margin-top:1mm}
.vb{height:44mm;border:1px solid #E1E7F0;display:flex;align-items:center;justify-content:center;background:#fff}.vb img{max-height:36mm;max-width:70mm}.vb.nv{background:#0B2A5B;border-color:#0B2A5B}.vb.bad{position:relative}
.ok{color:#2E8B57}.no{color:#C0392B}
.safe{position:relative;height:80mm;display:flex;align-items:center;justify-content:center;background:#F4F6F9;margin-bottom:6mm}.sz{outline:1.5px dashed #D4A72C;outline-offset:9mm;background:#fff}.sz img{height:50mm;display:block}.x{position:absolute;font:600 10px 'JetBrains Mono';color:#D4A72C}.xt{top:9mm;left:50%}.xl{left:46mm;top:50%}
.mins{display:grid;grid-template-columns:repeat(3,1fr);gap:6mm;margin-top:6mm}.mb{height:30mm;border:1px solid #E1E7F0;display:flex;align-items:center;justify-content:center}.mins b{font-size:12px;color:#0B2A5B;display:block;margin-top:2mm}.mins p{font-size:10px;color:#5B6B82}
.pal{display:flex;height:34mm;margin-bottom:2mm}.sw{display:flex;flex-direction:column;justify-content:flex-end;padding:3mm;font-size:11px}.sw span{font:500 9px 'JetBrains Mono'}
.dot{display:inline-block;width:3.5mm;height:3.5mm;border-radius:50%;margin-right:2mm;vertical-align:middle;border:1px solid #E1E7F0}
.ty{border-bottom:1px solid #E1E7F0;padding:4mm 0}.tl{font:600 8px 'JetBrains Mono';letter-spacing:2.5px;color:#D4A72C;margin-bottom:2mm}.ty p{font-size:10px;color:#5B6B82;margin:2mm 0 0}
.apps{display:grid;grid-template-columns:1fr 1fr;gap:7mm}.ap>b{display:block;font-size:11px;color:#0B2A5B;margin-top:2mm}.ap.wide{grid-column:1/3}
.card{width:72mm;height:40mm;display:flex;align-items:center;justify-content:center;box-shadow:0 2mm 4mm rgba(0,0,0,.18);border-radius:1.5mm}.card.f{background:#0B2A5B}.card.f img{height:30mm}.card.b{background:#fff;flex-direction:column;margin:-12mm 0 0 14mm;position:relative}.card.b img{width:52mm}.card.b span{font-size:7px;color:#5B6B82;margin-top:2mm}
.phone{width:60mm;height:62mm;border-radius:6mm;background:#F4F6F9;border:5px solid #14213D;display:flex;flex-direction:column;align-items:center;justify-content:center}.av img{width:26mm;border-radius:50%}.phone b{font-size:13px;margin-top:3mm;color:#14213D}.phone span{font-size:9px;color:#5B6B82}
.bag{width:52mm;height:62mm;background:#C8A27A;position:relative;display:flex;align-items:center;justify-content:center;margin-left:8mm}.bag img{width:34mm;filter:brightness(.6)}.handle{position:absolute;top:-10mm;width:22mm;height:14mm;border:2.5px solid #8C6A45;border-bottom:0;border-radius:12mm 12mm 0 0}
.jar{width:46mm;height:62mm;background:#fff;border:1px solid #D6DEE9;border-radius:4mm;position:relative;display:flex;align-items:center;justify-content:center;margin-left:10mm}.lid{position:absolute;top:-8mm;width:40mm;height:10mm;background:#0B2A5B;border-radius:2mm}.lab{width:34mm;height:34mm;border-radius:50%;background:#0B2A5B;display:flex;flex-direction:column;align-items:center;justify-content:center}.lab img{width:22mm}.lab span{font:500 8px Montserrat;letter-spacing:2px;color:#fff;margin-top:-2mm}
.wall{height:46mm;background:radial-gradient(circle at 50% 30%,#16376E,#06142E);display:flex;align-items:center;justify-content:center}.wall img{height:24mm}'''
html=f'''<!doctype html><html lang="pt-br"><meta charset="utf-8"><title>Manual de Marca Do Rei</title><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;1,400&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;600&family=Montserrat:wght@300;500&display=block" rel="stylesheet"><style>{CSS}</style><body>{"".join(pages)}</body></html>'''
open("manual.html","w").write(html)
