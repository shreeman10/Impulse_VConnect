import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace "Today" list
today_raw = r'<p className="section-label">Today</p>\s*<div className="notif-full-list">.*?<p className="nf-time">1 hour ago</p>\s*</div>\s*</div>\s*</div>'

today_mapped = """<p className="section-label">Today</p>
          <div className="notif-full-list">
            {notifications.map((notif, idx) => (
              <div className={`nf-item unread ${notif.type}`} key={idx}>
                <div className="nf-body">
                  <p className="nf-title">{notif.title}</p>
                  <p className="nf-desc">{notif.sub}</p>
                  <p className="nf-time">{notif.time}</p>
                </div>
              </div>
            ))}
          </div>"""

text = re.sub(today_raw, today_mapped, text, flags=re.DOTALL)

earlier_raw = r'<p className="section-label">Earlier</p>\s*<div className="notif-full-list">.*?<p className="nf-time">2 days ago</p>\s*</div>\s*</div>\s*</div>'
earlier_mapped = """<p className="section-label">Earlier</p>
          <div className="notif-full-list">
            <div className="nf-item">
              <div className="nf-icon"><BookOpen size={18} /></div>
              <div className="nf-body">
                <p className="nf-title">New Notes Uploaded</p>
                <p className="nf-desc">Prof. Singh uploaded Unit 4 notes for OS.</p>
                <p className="nf-time">Yesterday, 4:30 PM</p>
              </div>
            </div>
          </div>"""
text = re.sub(earlier_raw, earlier_mapped, text, flags=re.DOTALL)


with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("Phase 5 complete")
