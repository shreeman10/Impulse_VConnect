import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Feedback Form Submissions
feedback_btn = r'<button className="btn-primary full-width">Submit Feedback</button>'
feedback_btn_mapped = '<button className="btn-primary full-width" onClick={submitFeedback}>Submit Feedback</button>'
text = re.sub(feedback_btn, feedback_btn_mapped, text)

feedback_text_input = r'<textarea className="form-input" rows="4" placeholder="Describe your experience..."></textarea>'
feedback_text_input_mapped = '<textarea className="form-input" rows="4" placeholder="Describe your experience..." value={feedbackInput} onChange={(e) => setFeedbackInput(e.target.value)}></textarea>'
text = re.sub(feedback_text_input, feedback_text_input_mapped, text)

recent_feedback_list = r'<p className="section-label">Recent Submissions</p>\s*<div className="lf-list">.*?<div className="lf-item">\s*<div className="lf-img" style={{background: \'#10b98120\', color: \'#10b981\'}}>\s*<MessageCircle size={18} />\s*</div>\s*<div className="lf-body">\s*<p className="lf-title">WiFi Issues</p>\s*<p className="lf-sub">Library &middot; Pending review</p>\s*</div>\s*<div className="score-pill">IT Support</div>\s*</div>\s*</div>'

feedback_mapped_list = """<p className="section-label">My Past Feedback</p>
          <div className="lf-list">
            {feedbacks.map((fb, idx) => (
              <div className="lf-item" key={idx}>
                <div className="lf-img" style={{background: '#10b98120', color: '#10b981'}}>
                  <MessageCircle size={18} />
                </div>
                <div className="lf-body">
                  <p className="lf-title">{fb.message}</p>
                  <p className="lf-sub">{fb.date} &middot; Rated: {fb.rating}★</p>
                </div>
                <div className="score-pill">{fb.category}</div>
              </div>
            ))}
          </div>"""
text = re.sub(recent_feedback_list, feedback_mapped_list, text, flags=re.DOTALL)


# 2. Lost & Found System
lf_item_input = r'<input className="form-input" placeholder="e.g. Blue Water Bottle" />'
lf_item_input_mapped = '<input className="form-input" placeholder="e.g. Blue Water Bottle" value={lostInput} onChange={(e) => setLostInput(e.target.value)} />'
text = re.sub(lf_item_input, lf_item_input_mapped, text)

lf_loc_input = r'<input className="form-input" placeholder="e.g. Library, 1st Floor" />'
lf_loc_input_mapped = '<input className="form-input" placeholder="e.g. Library, 1st Floor" value={lostLocation} onChange={(e) => setLostLocation(e.target.value)} />'
text = re.sub(lf_loc_input, lf_loc_input_mapped, text)

lf_post_btn = r'<button className="btn-primary full-width">Post Item</button>'
lf_post_btn_mapped = '<button className="btn-primary full-width" onClick={submitLostItem}>Post Item</button>'
text = re.sub(lf_post_btn, lf_post_btn_mapped, text)

# Map lost list directly replacing hardcoded lines
lf_list_raw = r'<div className="lf-list">.*?<p className="lf-title">Black Earphones</p>.*?<button className="claim-btn">Claim</button>\s*</div>\s*</div>\s*</div>\s*<div className="screen" id="screen-feedback">'
lf_list_mapped = """<div className="lf-list">
            {lostItems.map((item, idx) => (
              <div className="lf-item" key={idx}>
                <div className="lf-img lost-tag">LOST</div>
                <div className="lf-body">
                  <p className="lf-title">{item.item}</p>
                  <p className="lf-sub"><MapPin size={18} /> {item.location} · {item.contact}</p>
                </div>
                <button className="claim-btn">Claim</button>
              </div>
            ))}
          </div>
        </div>
      </div>
      <div className="screen" id="screen-feedback">"""
text = re.sub(lf_list_raw, lf_list_mapped, text, flags=re.DOTALL)

# 3. Notification Hub updates
notif_hub_raw = r'<p className="section-label">All Notifications</p>\s*<div className="notif-preview">.*?<p className="notif-title">Fee Receipt Available</p>.*?<p className="notif-time">2d ago</p>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>'
notif_hub_mapped = """<p className="section-label">All Notifications</p>
          <div className="notif-preview">
            {notifications.map((notif, idx) => (
              <div className="notif-item" key={idx}>
                <div className={`notif-dot ${notif.type}`}></div>
                <div className="notif-body">
                  <p className="notif-title">{notif.title}</p>
                  <p className="notif-sub">{notif.sub}</p>
                </div>
                <p className="notif-time">{notif.time}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>"""
text = re.sub(notif_hub_raw, notif_hub_mapped, text, flags=re.DOTALL)

# Home Dashboard dynamic injections
dashboard_notifs_raw = r'<p className="section-label">Notifications</p>\s*<div className="notif-preview">.*?<p className="notif-time">2h</p>\s*</div>\s*</div>'
dashboard_notifs_mapped = """<p className="section-label">Notifications</p>
          <div className="notif-preview">
            <div className={`notif-item`} onClick={() => window.navigate('screen-notifications')}>
              <div className={`notif-dot ${notifications[0]?.type}`}></div>
              <div className="notif-body">
                <p className="notif-title">{notifications[0]?.title}</p>
                <p className="notif-sub">{notifications[0]?.sub}</p>
              </div>
              <p className="notif-time">{notifications[0]?.time}</p>
            </div>
          </div>"""
text = re.sub(dashboard_notifs_raw, dashboard_notifs_mapped, text, flags=re.DOTALL)

# Add Home assignments shortcast
challenges_raw = r'<div className="challenge-card">.*?</div>\s{10,20}<div className="progress-wrap">'
challenges_mapped = """<div className="challenge-card" onClick={() => window.navigate('screen-academic')} style={{cursor: 'pointer'}}>
            <p className="challenge-label"><AlertTriangle size={14} style={{display: "inline", verticalAlign: "middle"}} /> Reminder</p>
            <h3 className="challenge-title">{assignments[0]?.title} due {assignments[0]?.statusText}</h3>
            <p className="challenge-desc">Check your academic panel for the complete details and deadlines.</p>
            <div className="challenge-meta">
              <span className="chip">Academics</span>
              <span className="chip">{assignments[0]?.deadline}</span>
            </div>
            <div className="progress-wrap">"""
text = re.sub(challenges_raw, challenges_mapped, text, flags=re.DOTALL)


with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("App.jsx refactoring phase 2 complete.")
