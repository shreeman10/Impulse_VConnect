import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    text = f.read()

# Add needed imports
new_icons = ['ArrowLeft', 'Search', 'Plus', 'Menu', 'X', 'Star', 'Check', 'Circle', 'CheckCircle2']

# Find existing import statement for lucide-react
import_match = re.search(r"import \{([^}]+)\} from 'lucide-react';", text)
if import_match:
    existing_icons = [i.strip() for i in import_match.group(1).split(',')]
    all_icons = sorted(list(set(existing_icons + new_icons)))
    new_import_str = f"import {{ {', '.join(all_icons)} }} from 'lucide-react';"
    text = text.replace(import_match.group(0), new_import_str)
else:
    all_icons = sorted(new_icons)
    text = f"import {{ {', '.join(all_icons)} }} from 'lucide-react';\n" + text

# Replacements
replacements = [
    (r'>←<', r'><ArrowLeft size={20} /><'),
    (r'>🔍<', r'><Search size={18} /><'),
    (r'>\+<', r'><Plus size={16} /><'),
    (r'>☰<', r'><Menu size={24} /><'),
    (r'>✕<', r'><X size={24} /><'),
    (r'>★<', r'><Star fill="currentColor" size={20} strokeWidth={1} /><'),
    (r'>●<', r'><Circle fill="currentColor" size={10} strokeWidth={0} /><'),
    (r'Applied ✓', r'Applied <Check size={16} style={{display: "inline", verticalAlign: "middle"}} />'),
    (r'Joined ✓', r'Joined <Check size={16} style={{display: "inline", verticalAlign: "middle"}} />'),
    (r'>✓<', r'><Check size={16} /><'),
    (r'>○<', r'><Circle size={10} strokeWidth={2} /><'),
]

for old, new in replacements:
    text = re.sub(old, new, text)

# For the streak chevron
text = re.sub(r'<svg className="streak-chevron".*?</svg>', r'<ChevronRight size={16} color="white" />', text, flags=re.DOTALL)
# Also need to add ChevronRight to imports, let's just cheat and do it directly
if 'ChevronRight' not in text.split("import {")[1].split("}")[0]:
    text = text.replace("import { ArrowLeft", "import { ArrowLeft, ChevronRight")

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("Icons enhanced")
