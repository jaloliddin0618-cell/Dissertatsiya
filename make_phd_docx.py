"""
PhD dissertatsiya DOCX generator
- Times New Roman 14pt
- 1.5 qator interval
- Sahifa raqamlari (pastda o'rtada)
- Chegaralar: chap 3 sm, o'ng 1.5 sm, yuqori/past 2 sm
- Sarlavhalar qalin (bold), 14pt
- Paragraflar ichi oraliq 1.25 sm
"""
import zipfile
import os
import re

# =================== YORDAMCHI FUNKSIYALAR ===================

def esc(text):
    text = str(text)
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    text = text.replace('"', '&quot;')
    return text

def clean(text):
    """Markdown belgilarini tozalash"""
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    return text

# =================== PARAGRAPH XML QOLIPLARI ===================

TNR = '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'

def p_title(text):
    """Muqova sarlavhasi — qalin, 16pt, markaz"""
    return f'''<w:p>
  <w:pPr><w:jc w:val="center"/><w:spacing w:line="360" w:lineRule="auto"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:sz w:val="32"/><w:szCs w:val="32"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_subtitle(text):
    """Muqova kichik sarlavha"""
    return f'''<w:p>
  <w:pPr><w:jc w:val="center"/><w:spacing w:after="200"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_h1(text):
    """1-darajali sarlavha — bob nomi, qalin, 14pt, markaz, yangi sahifa"""
    return f'''<w:p>
  <w:pPr>
    <w:pageBreakBefore/>
    <w:jc w:val="center"/>
    <w:spacing w:before="240" w:after="240" w:line="360" w:lineRule="auto"/>
  </w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_h2(text):
    """2-darajali sarlavha — paragraf, qalin, 14pt, chap"""
    return f'''<w:p>
  <w:pPr>
    <w:spacing w:before="240" w:after="120" w:line="360" w:lineRule="auto"/>
  </w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_h3(text):
    """3-darajali sarlavha — kichik bo'lim, qalin, 14pt"""
    return f'''<w:p>
  <w:pPr>
    <w:spacing w:before="200" w:after="100" w:line="360" w:lineRule="auto"/>
  </w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_h4(text):
    """4-darajali sarlavha — kursiv, 14pt"""
    return f'''<w:p>
  <w:pPr>
    <w:spacing w:before="160" w:after="80" w:line="360" w:lineRule="auto"/>
  </w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:i/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_body(text):
    """Asosiy matn — TNR 14pt, 1.5 interval, birinchi qator 1.25 sm chekinish"""
    return f'''<w:p>
  <w:pPr>
    <w:ind w:firstLine="709"/>
    <w:spacing w:line="360" w:lineRule="auto" w:after="0"/>
    <w:jc w:val="both"/>
  </w:pPr>
  <w:r><w:rPr>{TNR}<w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_bullet(text):
    """Ro'yxat — 14pt, 1.5 interval"""
    return f'''<w:p>
  <w:pPr>
    <w:ind w:left="720" w:hanging="360"/>
    <w:spacing w:line="360" w:lineRule="auto" w:after="0"/>
  </w:pPr>
  <w:r><w:rPr>{TNR}<w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_table_row(text):
    """Jadval satri — kichik shrift, monospace"""
    return f'''<w:p>
  <w:pPr>
    <w:ind w:left="360"/>
    <w:spacing w:line="280" w:lineRule="auto" w:after="0"/>
  </w:pPr>
  <w:r><w:rPr>
    <w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/>
    <w:sz w:val="20"/><w:szCs w:val="20"/>
  </w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_empty():
    return '<w:p><w:pPr><w:spacing w:after="0"/></w:pPr><w:r><w:t></w:t></w:r></w:p>'

# =================== MARKDOWN PARSER ===================

def parse_md(md_text):
    """Markdown ni paragraflar ro'yxatiga o'tkazish"""
    items = []
    lines = md_text.split('\n')
    in_code = False

    for line in lines:
        raw = line.rstrip()
        stripped = raw.strip()

        # Kod bloki
        if stripped.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue

        # Bo'sh qator
        if not stripped:
            continue

        # Jadval satri
        if stripped.startswith('|'):
            cells = [c.strip() for c in stripped.split('|') if c.strip()]
            if cells and not all(set(c) <= set('-: ') for c in cells):
                items.append(('table', '  |  '.join(cells)))
            continue

        # Sarlavhalar
        if stripped.startswith('#### '):
            items.append(('h4', clean(stripped[5:])))
        elif stripped.startswith('### '):
            items.append(('h3', clean(stripped[4:])))
        elif stripped.startswith('## '):
            items.append(('h2', clean(stripped[3:])))
        elif stripped.startswith('# '):
            items.append(('h1', clean(stripped[2:])))
        elif stripped.startswith(('- ', '* ')):
            items.append(('bullet', '• ' + clean(stripped[2:])))
        elif stripped.startswith('---'):
            items.append(('empty', ''))
        elif stripped.startswith(tuple('0123456789')) and '. ' in stripped[:5]:
            items.append(('bullet', clean(stripped)))
        else:
            items.append(('body', clean(stripped)))

    return items

def render(ptype, text):
    if ptype == 'h1':   return p_h1(text)
    if ptype == 'h2':   return p_h2(text)
    if ptype == 'h3':   return p_h3(text)
    if ptype == 'h4':   return p_h4(text)
    if ptype == 'bullet': return p_bullet(text)
    if ptype == 'table':  return p_table_row(text)
    if ptype == 'empty':  return p_empty()
    return p_body(text)

# =================== ASOSIY FUNKSIYA ===================

def build_phd_docx(output_path):
    base = '/projects/sandbox/Dissertatsiya'
    sections = [
        'kirish.md',
        '1-bob.md',
        '2-bob.md',
        '3-bob.md',
        'adabiyotlar.md',
    ]

    all_xml = []

    # Muqova
    all_xml.append(p_empty())
    all_xml.append(p_empty())
    all_xml.append(p_title("O'ZBEKISTON RESPUBLIKASI"))
    all_xml.append(p_title("TOSHKENT DAVLAT AGRAR UNIVERSITETI"))
    all_xml.append(p_empty())
    all_xml.append(p_subtitle("Dissertatsiya"))
    all_xml.append(p_empty())
    all_xml.append(p_title("SUG'ORILADIGAN YERLAR DEGRADATSIYASINI"))
    all_xml.append(p_title("HISOBINI YURITISHNI GAT TEXNOLOGIYALARI"))
    all_xml.append(p_title("ASOSIDA TAKOMILLASHTIRISH"))
    all_xml.append(p_empty())
    all_xml.append(p_subtitle("(Sirdaryo viloyati misolida)"))
    all_xml.append(p_empty())
    all_xml.append(p_empty())
    all_xml.append(p_subtitle("Ilmiy daraja: Falsafa doktori (PhD)"))
    all_xml.append(p_empty())
    all_xml.append(p_empty())
    all_xml.append(p_subtitle("Toshkent — 2025"))

    # Boblar
    for fname in sections:
        fpath = os.path.join(base, fname)
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            items = parse_md(content)
            for ptype, text in items:
                all_xml.append(render(ptype, text))
        all_xml.append(p_empty())

    body_xml = '\n'.join(all_xml)

    # =================== DOCX FAYL YARATISH ===================

    # Sahifa raqami footer
    footer_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:p>
    <w:pPr><w:jc w:val="center"/></w:pPr>
    <w:fldSimple w:instr=" PAGE ">
      <w:r><w:rPr>
        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
        <w:sz w:val="28"/>
      </w:rPr><w:t>1</w:t></w:r>
    </w:fldSimple>
  </w:p>
</w:ftr>'''

    document_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
            xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
            xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">
  <w:body>
{body_xml}
    <w:sectPr>
      <!-- A4: 210x297 mm = 11906x16838 twips -->
      <w:pgSz w:w="11906" w:h="16838"/>
      <!-- Chap 3sm=1701, o'ng 1.5sm=851, yuqori/past 2sm=1134 -->
      <w:pgMar w:top="1134" w:right="851" w:bottom="1134" w:left="1701" w:header="709" w:footer="709"/>
      <w:footerReference w:type="default" r:id="rId2"/>
    </w:sectPr>
  </w:body>
</w:document>'''

    styles_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
        <w:sz w:val="28"/>
        <w:szCs w:val="28"/>
        <w:lang w:val="uz-UZ"/>
      </w:rPr>
    </w:rPrDefault>
    <w:pPrDefault>
      <w:pPr>
        <w:spacing w:line="360" w:lineRule="auto"/>
        <w:jc w:val="both"/>
      </w:pPr>
    </w:pPrDefault>
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
    print(f"✅ PhD DOCX yaratildi: {output_path}")
    print(f"   Hajmi: {size:,} bayt  ({size // 1024} KB)")

if __name__ == '__main__':
    out = '/projects/sandbox/Dissertatsiya/Dissertatsiya_GAT_Sugoriladigan_Yerlar.docx'
    build_phd_docx(out)
