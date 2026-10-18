# Ícones duotone da marca (48x48): círculo azul-marinho, símbolo dourado, mini coroa no topo
G='#D4A72C'; N='#0B2A5B'; W='#FFFFFF'
CROWN=f'<path d="M18 9l2.2 2.4L24 7.5l3.8 3.9L30 9l-1 5H19z" fill="{G}"/>'
def ic(sym): return f'<svg viewBox="0 0 48 48"><circle cx="24" cy="26" r="21" fill="{N}"/>{CROWN}<g transform="translate(0,3)">{sym}</g></svg>'
ICO=[
ic(f'<path d="M14 33c0-10 6.5-16 20-17-1 13-7.5 19-20 17z" fill="{G}"/><path d="M15 32l11-10" stroke="{N}" stroke-width="1.8" stroke-linecap="round"/>'),
ic(f'<path d="M26 12L15 27h8l-2 11 12-16h-8z" fill="{G}"/>'),
ic(f'<path d="M24 12l10 4v7c0 7-4.5 11-10 13-5.5-2-10-6-10-13v-7z" fill="{G}"/><path d="M19.5 24l3.2 3.2 6-6" fill="none" stroke="{N}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'),
ic(f'<circle cx="24" cy="25" r="6.5" fill="{G}"/><g stroke="{G}" stroke-width="2.4" stroke-linecap="round"><path d="M24 12v3M24 35v3M11 25h3M34 25h3M14.8 15.8l2.1 2.1M31.1 32.1l2.1 2.1M14.8 34.2l2.1-2.1M31.1 17.9l2.1-2.1"/></g>'),
ic(f'<path d="M24 36s-11-6.5-11-14.5A6 6 0 0124 18a6 6 0 0111 3.5C35 29.5 24 36 24 36z" fill="{G}"/><path d="M16 25h4l2-3 3 6 2-3h5" fill="none" stroke="{N}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'),
ic(f'<g fill="{G}"><rect x="11" y="20" width="4" height="10" rx="1.5"/><rect x="15.5" y="17" width="4" height="16" rx="1.5"/><rect x="28.5" y="17" width="4" height="16" rx="1.5"/><rect x="33" y="20" width="4" height="10" rx="1.5"/><rect x="19" y="23.5" width="10" height="3" rx="1"/></g>'),
ic(f'<path d="M24 37V25" stroke="{G}" stroke-width="2.4" stroke-linecap="round"/><path d="M24 25c0-6-4.5-10-11-10 0 6.5 4.5 10 11 10z" fill="{G}"/><path d="M24 29c0-5 4-8.5 10-8.5 0 5-4 8.5-10 8.5z" fill="{G}"/>'),
ic(f'<g fill="{G}"><circle cx="19" cy="22" r="4"/><circle cx="27" cy="20" r="4"/><circle cx="23" cy="28" r="4"/><circle cx="31" cy="27" r="3.5"/><circle cx="16" cy="30" r="3.2"/></g><path d="M27 16c1-2 3-3 5-3" stroke="{G}" stroke-width="1.8" fill="none" stroke-linecap="round"/>'),
ic(f'<path d="M24 12s9 9.5 9 16a9 9 0 01-18 0c0-6.5 9-16 9-16z" fill="{G}"/><path d="M19.5 29a4.5 4.5 0 004.5 4.5" fill="none" stroke="{N}" stroke-width="2" stroke-linecap="round"/>'),
]
