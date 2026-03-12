import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure remaining icons are imported
if "ArrowRight" not in text:
    text = text.replace("import { AlertTriangle,", "import { AlertTriangle, ArrowRight,")
# Note GraduationCap is already imported

# Replace "→"
text = re.sub(r'>→<', r'><ArrowRight size={16} /><', text)

# Replace "CO" logo
text = re.sub(r'<div className="id-logo">CO</div>', r'<div className="id-logo"><GraduationCap size={24} /></div>', text)

# Replace PDF/PPT/DOC text with icons + text
# e.g., <div className="material-icon pdf">PDF</div> -> <div className="material-icon pdf"><FileText size={20} /> PDF</div>
text = re.sub(r'<div className="material-icon pdf">PDF</div>', r'<div className="material-icon pdf"><FileText size={20} style={{marginBottom: "4px"}} /> PDF</div>', text)
text = re.sub(r'<div className="material-icon ppt">PPT</div>', r'<div className="material-icon ppt"><Monitor size={20} style={{marginBottom: "4px"}} /> PPT</div>', text)
text = re.sub(r'<div className="material-icon doc">DOC</div>', r'<div className="material-icon doc"><FileText size={20} style={{marginBottom: "4px"}} /> DOC</div>', text)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("Final icons enhanced")
