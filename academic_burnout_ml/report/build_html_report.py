import os
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
md_path = os.path.join(base_dir, "report", "Thesis_Early_Detection_Academic_Burnout.md")
html_path = os.path.join(base_dir, "report", "Thesis_Early_Detection_Academic_Burnout.html")

with open(md_path, 'r', encoding='utf-8') as f:
    md_text = f.read()

# Replace local file paths in img tags with relative paths for browser rendering
md_text = md_text.replace(
    'file:///d:/user%20files/New%20folder/Downloads/learner/learner/academic_burnout_ml/figures/',
    '../figures/'
)

css = """
<style>
  @page {
    size: A4;
    margin: 20mm;
  }
  body {
    font-family: 'Times New Roman', Times, Georgia, serif;
    font-size: 11.5pt;
    line-height: 1.6;
    color: #1a1a1a;
    background: #f8f9fa;
    margin: 0;
    padding: 20px;
  }
  .paper-container {
    background: #ffffff;
    max-width: 900px;
    margin: 0 auto;
    padding: 60px 70px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    border-radius: 4px;
  }
  h1 {
    font-size: 20pt;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 40px;
    margin-bottom: 25px;
    border-top: 2px solid #2c3e50;
    border-bottom: 2px solid #2c3e50;
    padding: 15px 0;
  }
  h2 {
    font-size: 15pt;
    color: #2c3e50;
    border-bottom: 1px solid #bdc3c7;
    padding-bottom: 6px;
    margin-top: 35px;
    page-break-after: avoid;
  }
  h3 {
    font-size: 13pt;
    color: #34495e;
    margin-top: 25px;
    page-break-after: avoid;
  }
  p {
    text-align: justify;
    margin-bottom: 14px;
    text-indent: 0;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 25px 0;
    font-size: 10.5pt;
    page-break-inside: avoid;
  }
  th, td {
    border: 1px solid #7f8c8d;
    padding: 8px 12px;
    text-align: left;
  }
  th {
    background-color: #ecf0f1;
    font-weight: bold;
    color: #2c3e50;
  }
  tr:nth-child(even) {
    background-color: #fafbfc;
  }
  img {
    max-width: 95%;
    height: auto;
    display: block;
    margin: 25px auto 10px auto;
    border: 1px solid #dcdde1;
    border-radius: 4px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
  }
  em {
    display: block;
    text-align: center;
    font-size: 9.5pt;
    color: #555;
    margin-bottom: 25px;
  }
  pre {
    background: #f4f6f7;
    border: 1px solid #d5dbdb;
    border-left: 4px solid #3498db;
    padding: 14px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 9.5pt;
    overflow-x: auto;
    border-radius: 3px;
    line-height: 1.45;
  }
  code {
    font-family: 'Consolas', 'Courier New', monospace;
    background: #edf2f7;
    padding: 2px 5px;
    font-size: 10pt;
    border-radius: 3px;
  }
  hr {
    border: 0;
    height: 1px;
    background: #ccc;
    margin: 40px 0;
  }
  @media print {
    body {
      background: #fff;
      padding: 0;
    }
    .paper-container {
      box-shadow: none;
      padding: 0;
      max-width: 100%;
    }
    .page-break {
      page-break-after: always;
      break-after: page;
    }
  }
</style>
"""

# Convert markdown basic elements
lines = md_text.split('\n')
html_lines = []
in_table = False
table_header = True
in_code = False

for line in lines:
    stripped = line.strip()

    if stripped.startswith('```'):
        if not in_code:
            html_lines.append('<pre><code>')
            in_code = True
        else:
            html_lines.append('</code></pre>')
            in_code = False
        continue

    if in_code:
        html_lines.append(line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
        continue

    # Page breaks
    if '<div style="page-break-after: always;"></div>' in line:
        html_lines.append('<div class="page-break"></div>')
        continue

    # Headers
    if stripped.startswith('# '):
        html_lines.append(f'<h1>{stripped[2:]}</h1>')
        continue
    elif stripped.startswith('## '):
        html_lines.append(f'<h2>{stripped[3:]}</h2>')
        continue
    elif stripped.startswith('### '):
        html_lines.append(f'<h3>{stripped[4:]}</h3>')
        continue

    # Tables
    if '|' in stripped and ('---' in stripped or len(stripped.split('|')) > 2):
        if '---' in stripped:
            continue
        parts = [p.strip() for p in stripped.split('|')[1:-1]]
        if not in_table:
            html_lines.append('<table>')
            html_lines.append('<thead><tr>' + ''.join([f'<th>{p}</th>' for p in parts]) + '</tr></thead><tbody>')
            in_table = True
        else:
            html_lines.append('<tr>' + ''.join([f'<td>{p}</td>' for p in parts]) + '</tr>')
        continue
    else:
        if in_table:
            html_lines.append('</tbody></table>')
            in_table = False

    # Images
    img_match = re.match(r'!\[(.*?)\]\((.*?)\)', stripped)
    if img_match:
        alt, src = img_match.groups()
        html_lines.append(f'<img src="{src}" alt="{alt}">')
        continue

    # Horizontal rule
    if stripped == '---':
        html_lines.append('<hr>')
        continue

    # Paragraphs / Text
    if stripped:
        formatted = stripped
        # Bold
        formatted = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', formatted)
        # Italics
        formatted = re.sub(r'\*(.*?)\*', r'<em>\1</em>', formatted)
        # Inline code
        formatted = re.sub(r'`(.*?)`', r'<code>\1</code>', formatted)
        # Math delimiters simple display
        formatted = formatted.replace('$', '')
        html_lines.append(f'<p>{formatted}</p>')
    else:
        html_lines.append('')

if in_table:
    html_lines.append('</tbody></table>')

final_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Major Project Report: Early Detection of Academic Burnout</title>
{css}
</head>
<body>
<div class="paper-container">
{''.join(html_lines)}
</div>
</body>
</html>
"""

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Generated standalone publication HTML thesis at: {html_path}")
