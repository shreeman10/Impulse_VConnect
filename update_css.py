import re

with open('src/app.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace all occurrences of [data-lucide] with svg.lucide
text = text.replace('i[data-lucide]', 'svg.lucide')
text = text.replace('[data-lucide]', 'svg.lucide')

# Add color text primary to app container
text = text.replace(
""".app-container {
  display: flex;
  flex-direction: column;
  height: 810px;
  background: var(--bg);
  overflow: hidden;
  position: relative;
}""",
""".app-container {
  display: flex;
  flex-direction: column;
  height: 810px;
  background: var(--bg);
  color: var(--text-primary);
  overflow: hidden;
  position: relative;
}"""
)

with open('src/app.css', 'w', encoding='utf-8') as f:
    f.write(text)

print("CSS updated successfully")
