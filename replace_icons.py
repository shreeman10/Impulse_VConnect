import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all occurrences of <i data-lucide="some-icon"></i>
icon_names = set(re.findall(r'<i data-lucide="([^"]+)"></i>', text))

def to_pascal_case(s):
    # some-icon -> SomeIcon
    if s == 'code-2': return 'Code2'
    if s == 'building-2': return 'Building2'
    if s == 'bar-chart-2': return 'BarChart2'
    return ''.join(word.capitalize() for word in s.split('-'))

# Build import statement
imports = [to_pascal_case(name) for name in icon_names]
imports.sort()
import_str = f"import {{ {', '.join(imports)} }} from 'lucide-react';\n"

# Add import immediately after React import
text = re.sub(r"(import React.*?;\n)", r"\1" + import_str, text, count=1)

# Replace all <i data-lucide="..."></i> with <Icon />
def replace_icon(match):
    name = match.group(1)
    pascal = to_pascal_case(name)
    return f"<{pascal} size={{18}} />"

# Also remove the script block that inits vanilla lucide icons
text = re.sub(r'// Initialize Lucide icons if not already done in app.js\s*if\s*\(window.lucide\)\s*window.lucide.createIcons\(\);\s*', '', text)

text = re.sub(r'<i data-lucide="([^"]+)"></i>', replace_icon, text)

# There may be other sizes needed but size={{18}} looks fine for now
with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("Icons replaced")
