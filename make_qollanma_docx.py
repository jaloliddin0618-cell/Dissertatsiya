"""
Yo'l qurilishi o'quv qo'llanma DOCX generator
- Barcha 12 mavzu bitta faylga
- Times New Roman 12pt
- A4, chegaralar 2.5sm
- Bo'lim sarlavhalari, formulalar, jadvallar
"""
import zipfile, os, re, glob

TNR = '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'

def esc(t):
    t = str(t)
    for a, b in [('&','&amp;'),('<','&lt;'),('>','&gt;'),('"','&quot;')]:
        t = t.replace(a, b)
    return t

def clean(t):
    t = re.sub(r'\*\*(.+?)\*\*', r'\1', t)
    t = re.sub(r'\*(.+?)\*', r'\1', t)
    t = re.sub(r'`(.+?)`', r'\1', t)
    t = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', t)
    t = re.sub(r'\$\$.+?\$\$', '[formula]', t)
    t = re.sub(r'\$[^\$]+\$', '[formula]', t)
    return t.strip()


# === PARAGRAPH FUNKSIYALARI ===

def p_cover_title(t):
    return f'''<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="1440" w:after="240"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:sz w:val="36"/><w:szCs w:val="36"/></w:rPr>
    <w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:p>'''

def p_cover_sub(t):
    return f'''<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:after="120"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:sz w:val="26"/><w:szCs w:val="26"/></w:rPr>
    <w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:p>'''

def p_h1(t):
    """Mavzu sarlavhasi — katta, qalin, markazda"""
    return f'''<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="480" w:after="240"/>
    <w:pBdr><w:bottom w:val="single" w:sz="6" w:space="4" w:color="2E74B5"/></w:pBdr></w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:sz w:val="30"/><w:szCs w:val="30"/><w:color w:val="1F3864"/></w:rPr>
    <w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:p>'''

def p_h2(t):
    """Bo'lim sarlavhasi"""
    return f'''<w:p><w:pPr><w:spacing w:before="360" w:after="120"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:sz w:val="26"/><w:szCs w:val="26"/><w:color w:val="2E74B5"/></w:rPr>
    <w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:p>'''

def p_h3(t):
    """Kichik bo'lim"""
    return f'''<w:p><w:pPr><w:spacing w:before="240" w:after="80"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>
    <w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:p>'''

def p_h4(t):
    return f'''<w:p><w:pPr><w:spacing w:before="160" w:after="60"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:i/><w:sz w:val="24"/></w:rPr>
    <w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:p>'''


def p_body(t):
    return f'''<w:p><w:pPr>
    <w:ind w:firstLine="709"/>
    <w:spacing w:line="276" w:lineRule="auto" w:after="80"/>
    <w:jc w:val="both"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>
    <w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:p>'''

def p_bullet(t):
    return f'''<w:p><w:pPr>
    <w:ind w:left="720" w:hanging="360"/>
    <w:spacing w:line="260" w:lineRule="auto" w:after="60"/>
    <w:jc w:val="both"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>
    <w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:p>'''

def p_numbered(t):
    return f'''<w:p><w:pPr>
    <w:ind w:left="720" w:hanging="360"/>
    <w:spacing w:line="260" w:lineRule="auto" w:after="60"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:sz w:val="24"/></w:rPr>
    <w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:p>'''

def p_table(t):
    return f'''<w:p><w:pPr>
    <w:ind w:left="360"/>
    <w:spacing w:line="220" w:lineRule="auto" w:after="40"/></w:pPr>
  <w:r><w:rPr>
    <w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/>
    <w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr>
    <w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:p>'''

def p_formula(t):
    return f'''<w:p><w:pPr><w:jc w:val="center"/>
    <w:spacing w:before="120" w:after="120"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:i/><w:sz w:val="24"/></w:rPr>
    <w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:p>'''

def p_note(t):
    """Formuladagi izoh — kichikroq, chap indent"""
    return f'''<w:p><w:pPr>
    <w:ind w:left="720"/>
    <w:spacing w:line="220" w:lineRule="auto" w:after="40"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:sz w:val="22"/><w:szCs w:val="22"/><w:color w:val="404040"/></w:rPr>
    <w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:p>'''

def p_empty():
    return '<w:p><w:pPr><w:spacing w:after="80"/></w:pPr><w:r><w:t></w:t></w:r></w:p>'

def p_page_break():
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

def p_separator():
    return f'''<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="120" w:after="120"/></w:pPr>
  <w:r><w:rPr><w:color w:val="AAAAAA"/></w:rPr>
    <w:t>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</w:t></w:r></w:p>'''


# === MARKDOWN PARSER ===

def parse_md(text):
    items = []
    lines = text.split('\n')
    in_code = False
    for line in lines:
        s = line.strip()
        if s.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            if s:
                items.append(('table', s))
            continue
        if not s:
            continue
        if s.startswith('# '):
            items.append(('h1', clean(s[2:])))
        elif s.startswith('## '):
            items.append(('h2', clean(s[3:])))
        elif s.startswith('### '):
            items.append(('h3', clean(s[4:])))
        elif s.startswith('#### '):
            items.append(('h4', clean(s[5:])))
        elif s.startswith('|'):
            cells = [c.strip() for c in s.split('|') if c.strip()]
            if cells and not all(set(c) <= set('-:| ') for c in cells):
                items.append(('table', '  |  '.join(cells)))
        elif re.match(r'^[-*] ', s):
            items.append(('bullet', '• ' + clean(s[2:])))
        elif re.match(r'^\d+\. ', s):
            items.append(('numbered', clean(re.sub(r'^\d+\. ', '', s))))
        elif s == '---':
            items.append(('sep', ''))
        elif s.startswith('Bu yerda:') or s.startswith('- **'):
            items.append(('note', clean(s)))
        else:
            items.append(('body', clean(s)))
    return items

def render(ptype, text):
    if ptype == 'h1':       return p_h1(text)
    if ptype == 'h2':       return p_h2(text)
    if ptype == 'h3':       return p_h3(text)
    if ptype == 'h4':       return p_h4(text)
    if ptype == 'bullet':   return p_bullet(text)
    if ptype == 'numbered': return p_numbered(text)
    if ptype == 'table':    return p_table(text)
    if ptype == 'note':     return p_note(text)
    if ptype == 'sep':      return p_separator()
    return p_body(text)


# === DOCX QURISH ===

def build_docx(output_path):
    base = '/projects/sandbox/Dissertatsiya/yol_qollanma'
    files = sorted(glob.glob(os.path.join(base, 'mavzu_*.md')))

    all_xml = []

    # Muqova sahifasi
    all_xml.append(p_cover_title("YO'L QURILISHI VA LOYIHALASH"))
    all_xml.append(p_cover_sub("O'quv Qo'llanma — Universitet Talabalari Uchun"))
    all_xml.append(p_empty())
    all_xml.append(p_cover_sub("Barcha mavzular: 1–12"))
    all_xml.append(p_cover_sub("2026-yil"))
    all_xml.append(p_page_break())

    # Har bir mavzu
    for i, fpath in enumerate(files):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        items = parse_md(content)
        for ptype, text in items:
            all_xml.append(render(ptype, text))
        # Mavzular orasida sahifa uzish
        if i < len(files) - 1:
            all_xml.append(p_page_break())

    body_xml = '\n'.join(all_xml)

    document_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
            xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <w:body>
{body_xml}
    <w:sectPr>
      <w:pgSz w:w="11906" w:h="16838"/>
      <w:pgMar w:top="1418" w:right="1418" w:bottom="1418" w:left="1701" w:header="709" w:footer="709"/>
      <w:footerReference w:type="default" r:id="rId2"/>
    </w:sectPr>
  </w:body>
</w:document>'''

    footer_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:p><w:pPr><w:jc w:val="center"/></w:pPr>
    <w:fldSimple w:instr=" PAGE ">
      <w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
        <w:sz w:val="22"/></w:rPr><w:t>1</w:t></w:r>
    </w:fldSimple>
  </w:p>
</w:ftr>'''

    styles_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault><w:rPr>
      <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
      <w:sz w:val="24"/><w:szCs w:val="24"/>
      <w:lang w:val="uz-UZ"/>
    </w:rPr></w:rPrDefault>
    <w:pPrDefault><w:pPr>
      <w:spacing w:line="276" w:lineRule="auto"/>
      <w:jc w:val="both"/>
    </w:pPr></w:pPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
  </w:style>
</w:styles>'''

    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml"
    ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml"
    ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/footer1.xml"
    ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
</Types>'''

    rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1"
    Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"
    Target="word/document.xml"/>
</Relationships>'''

    word_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1"
    Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles"
    Target="styles.xml"/>
  <Relationship Id="rId2"
    Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer"
    Target="footer1.xml"/>
</Relationships>'''

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('[Content_Types].xml', content_types)
        zf.writestr('_rels/.rels', rels)
        zf.writestr('word/_rels/document.xml.rels', word_rels)
        zf.writestr('word/styles.xml', styles_xml)
        zf.writestr('word/footer1.xml', footer_xml)
        zf.writestr('word/document.xml', document_xml.encode('utf-8'))

    size = os.path.getsize(output_path)
    print(f"✅ DOCX yaratildi: {output_path}")
    print(f"   Hajmi: {size:,} bayt ({size//1024} KB)")
    print(f"   Mavzular: {len(files)} ta")

if __name__ == '__main__':
    out = '/projects/sandbox/Dissertatsiya/Yol_Qurilishi_Qollanma.docx'
    build_docx(out)
