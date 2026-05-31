"""
Q2 maqola DOCX generator — jurnal formati
- Times New Roman 12pt (jurnal standarti)
- 1.0 qator oraliq (jurnal standarti)
- Sarlavhalar qalin, 12pt
- Abstract, Keywords alohida formatda
- Adabiyotlar raqamlangan
- A4, chegaralar: har tomondan 2.5 sm
"""
import zipfile
import os
import re

TNR = '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'

def esc(text):
    text = str(text)
    for a, b in [('&','&amp;'),('<','&lt;'),('>','&gt;'),('"','&quot;')]:
        text = text.replace(a, b)
    return text

def clean(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    text = re.sub(r'\$\$.+?\$\$', '[formula]', text)
    return text

# === XML PARAGRAPH QOLIPLARI ===

def p_article_title(text):
    return f'''<w:p>
  <w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="240"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_author(text):
    return f'''<w:p>
  <w:pPr><w:jc w:val="center"/><w:spacing w:after="80"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:i/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_section(text):
    """Bo'lim sarlavhasi — qalin, 12pt, katta harflar"""
    return f'''<w:p>
  <w:pPr><w:spacing w:before="240" w:after="120"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>
    <w:t xml:space="preserve">{esc(text.upper())}</w:t></w:r>
</w:p>'''

def p_subsection(text):
    """Kichik bo'lim — qalin, 12pt"""
    return f'''<w:p>
  <w:pPr><w:spacing w:before="160" w:after="80"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_subsubsection(text):
    """3-daraja — qalin, kursiv"""
    return f'''<w:p>
  <w:pPr><w:spacing w:before="120" w:after="60"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:i/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_abstract_label():
    return f'''<w:p>
  <w:pPr><w:spacing w:before="200" w:after="80"/></w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:sz w:val="24"/></w:rPr>
    <w:t>ABSTRACT</w:t></w:r>
</w:p>'''

def p_abstract_text(text):
    return f'''<w:p>
  <w:pPr>
    <w:ind w:left="720" w:right="720"/>
    <w:spacing w:line="240" w:lineRule="auto" w:after="0"/>
    <w:jc w:val="both"/>
  </w:pPr>
  <w:r><w:rPr>{TNR}<w:i/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_keywords(text):
    return f'''<w:p>
  <w:pPr>
    <w:ind w:left="720" w:right="720"/>
    <w:spacing w:after="200"/>
    <w:jc w:val="both"/>
  </w:pPr>
  <w:r><w:rPr>{TNR}<w:b/><w:i/><w:sz w:val="22"/></w:rPr><w:t xml:space="preserve">Keywords: </w:t></w:r>
  <w:r><w:rPr>{TNR}<w:i/><w:sz w:val="22"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_body(text):
    return f'''<w:p>
  <w:pPr>
    <w:ind w:firstLine="709"/>
    <w:spacing w:line="240" w:lineRule="auto" w:after="0"/>
    <w:jc w:val="both"/>
  </w:pPr>
  <w:r><w:rPr>{TNR}<w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_bullet(text):
    return f'''<w:p>
  <w:pPr>
    <w:ind w:left="720" w:hanging="360"/>
    <w:spacing w:line="240" w:lineRule="auto" w:after="0"/>
  </w:pPr>
  <w:r><w:rPr>{TNR}<w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_table_row(text):
    return f'''<w:p>
  <w:pPr>
    <w:ind w:left="360"/>
    <w:spacing w:line="220" w:lineRule="auto" w:after="0"/>
  </w:pPr>
  <w:r><w:rPr>
    <w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/>
    <w:sz w:val="18"/><w:szCs w:val="18"/>
  </w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_ref(text):
    return f'''<w:p>
  <w:pPr>
    <w:ind w:left="720" w:hanging="720"/>
    <w:spacing w:line="240" w:lineRule="auto" w:after="60"/>
    <w:jc w:val="both"/>
  </w:pPr>
  <w:r><w:rPr>{TNR}<w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr>
    <w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>'''

def p_empty():
    return '<w:p><w:pPr><w:spacing w:after="0"/></w:pPr><w:r><w:t></w:t></w:r></w:p>'

def p_line():
    return '<w:p><w:r><w:t>────────────────────────────────────────────────</w:t></w:r></w:p>'

# === MARKDOWN PARSER ===

def parse_md(md_text):
    items = []
    lines = md_text.split('\n')
    in_code = False
    in_abstract = False
    in_keywords = False
    in_references = False
    abstract_lines = []
    keywords_text = ''

    for line in lines:
        stripped = line.strip()

        if stripped.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        if not stripped:
            if in_abstract and abstract_lines:
                items.append(('abstract', ' '.join(abstract_lines)))
                abstract_lines = []
                in_abstract = False
            continue

        # Jadval
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
            text = clean(stripped[3:])
            items.append(('h2', text))
            in_references = 'REFERENCES' in text.upper() or 'ADABIYOT' in text.upper()
        elif stripped.startswith('# '):
            items.append(('h1', clean(stripped[2:])))
        elif stripped.startswith(('- ', '* ')):
            items.append(('bullet', '• ' + clean(stripped[2:])))
        elif stripped.startswith('**Keywords') or stripped.startswith('**Kalit'):
            kw = re.sub(r'\*\*Keywords?\*\*:?\s*', '', stripped)
            kw = re.sub(r'\*\*Kalit so\'zlar\*\*:?\s*', '', kw)
            kw = clean(kw)
            items.append(('keywords', kw))
        elif stripped.startswith('**Author') or stripped.startswith('**Muallif') or stripped.startswith('**Affiliation') or stripped.startswith('**Tashkilot') or stripped.startswith('**Email') or stripped.startswith('**Corresponding'):
            items.append(('author', clean(stripped.replace('**', ''))))
        elif stripped == '---':
            items.append(('line', ''))
        else:
            text = clean(stripped)
            if in_references:
                items.append(('ref', text))
            else:
                items.append(('body', text))

    return items

def render(ptype, text):
    if ptype == 'h1':       return p_article_title(text)
    if ptype == 'h2':       return p_section(text)
    if ptype == 'h3':       return p_subsection(text)
    if ptype == 'h4':       return p_subsubsection(text)
    if ptype == 'author':   return p_author(text)
    if ptype == 'abstract': return p_abstract_text(text)
    if ptype == 'keywords': return p_keywords(text)
    if ptype == 'bullet':   return p_bullet(text)
    if ptype == 'table':    return p_table_row(text)
    if ptype == 'ref':      return p_ref(text)
    if ptype == 'line':     return p_line()
    return p_body(text)

# === ASOSIY FUNKSIYA ===

def build_article_docx(output_path):
    base = '/projects/sandbox/Dissertatsiya'
    fpath = os.path.join(base, 'article_q2_english.md')

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    items = parse_md(content)

    all_xml = []
    for ptype, text in items:
        all_xml.append(render(ptype, text))

    body_xml = '\n'.join(all_xml)

    # Footer — sahifa raqami
    footer_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:p>
    <w:pPr><w:jc w:val="center"/></w:pPr>
    <w:fldSimple w:instr=" PAGE ">
      <w:r><w:rPr>
        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
        <w:sz w:val="24"/>
      </w:rPr><w:t>1</w:t></w:r>
    </w:fldSimple>
  </w:p>
</w:ftr>'''

    document_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
            xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <w:body>
{body_xml}
    <w:sectPr>
      <w:pgSz w:w="11906" w:h="16838"/>
      <!-- 2.5 sm = 1418 twips har tomondan -->
      <w:pgMar w:top="1418" w:right="1418" w:bottom="1418" w:left="1418" w:header="709" w:footer="709"/>
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
        <w:sz w:val="24"/><w:szCs w:val="24"/>
        <w:lang w:val="en-US"/>
      </w:rPr>
    </w:rPrDefault>
    <w:pPrDefault>
      <w:pPr>
        <w:spacing w:line="240" w:lineRule="auto"/>
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
    print(f"✅ Maqola DOCX yaratildi: {output_path}")
    print(f"   Hajmi: {size:,} bayt  ({size // 1024} KB)")

if __name__ == '__main__':
    out = '/projects/sandbox/Dissertatsiya/Article_Q2_Syrdarya_Land_Degradation.docx'
    build_article_docx(out)
