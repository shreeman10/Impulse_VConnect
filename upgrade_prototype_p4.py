import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix Home Dashboard notifications since they were skipped
home_notifs_raw = r'<p className="section-label">Recent Notifications</p>\s*<div className="notif-item" onClick=\{\(\) => window\.navigate\(\'screen-notifications\'\)\}>.*?<span className="notif-time">1h</span>\s*</div>\s*</div>'

home_notifs_mapped = """<p className="section-label">Recent Notifications</p>
          <div className="notif-preview">
            {notifications.slice(0,1).map((notif, idx) => (
              <div className="notif-item" key={idx} onClick={() => window.navigate('screen-notifications')}>
                <div className={`notif-dot ${notif.type}`}></div>
                <div className="notif-body">
                  <p className="notif-title">{notif.title}</p>
                  <p className="notif-sub">{notif.sub}</p>
                </div>
                <span className="notif-time">{notif.time}</span>
              </div>
            ))}
          </div>"""

text = re.sub(home_notifs_raw, home_notifs_mapped, text, flags=re.DOTALL)


# Fix Actual notifications screen
notif_screen_raw = r'<p className="section-label">Today</p>\s*<div className="notif-full-list">.*?<p className="nf-time">2 days ago</p>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>'

notif_screen_mapped = """<p className="section-label">Today</p>
          <div className="notif-full-list">
            {notifications.map((notif, idx) => (
              <div className={`nf-item ${notif.type}`} key={idx}>
                <div className="nf-body">
                  <p className="nf-title">{notif.title}</p>
                  <p className="nf-desc">{notif.sub}</p>
                  <p className="nf-time">{notif.time}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  </div>"""

text = re.sub(notif_screen_raw, notif_screen_mapped, text, flags=re.DOTALL)


with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("Phase 4 notifications complete")
