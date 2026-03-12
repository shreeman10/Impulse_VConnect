import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add imports for useState and data
if "import { useState" not in text:
    text = text.replace("import React, { useEffect } from 'react';", "import React, { useEffect, useState } from 'react';\nimport { assignments } from './data/assignments';\nimport { menu } from './data/canteenMenu';\nimport { events as rawEvents } from './data/events';\nimport { notifications } from './data/notifications';")

text = text.replace("export default function App() {", """
export default function App() {
  const [cart, setCart] = useState([]);
  const [coupon, setCoupon] = useState("");
  const [discount, setDiscount] = useState(0);
  const [eventsData, setEventsData] = useState(rawEvents);
  
  const [trainStatus, setTrainStatus] = useState(0); // 0: input, 1: submit, 2: verify, 3: approve, 4: download
  
  const [feedbackInput, setFeedbackInput] = useState("");
  const [feedbacks, setFeedbacks] = useState([
    { category: "Canteen", rating: 4, message: "Food quality improved", date: "Today" }
  ]);

  const [lostItems, setLostItems] = useState([
    { item: "Wallet", location: "Library", contact: "Anonymous" }
  ]);
  const [lostInput, setLostInput] = useState("");
  const [lostLocation, setLostLocation] = useState("");

  const handleCanteenAdd = (item) => {
    setCart([...cart, item]);
    const priceEl = document.querySelector('.cart-price');
    const countEl = document.querySelector('.cart-count');
    if(countEl) countEl.textContent = `${cart.length + 1} items`;
    
    // Animate add button
    const btnId = `btn-${item.id}`;
    const btn = document.getElementById(btnId);
    if(btn) {
      btn.style.background = '#4ade80';
      btn.style.color = '#000';
      setTimeout(() => { btn.style.background = ''; btn.style.color = ''; }, 1200);
    }
  };

  const cartTotal = cart.reduce((acc, curr) => acc + curr.price, 0);
  const cartFinal = cartTotal > 0 ? cartTotal - (cartTotal * discount) : 0;

  const handleCoupon = () => {
    if(coupon.toUpperCase() === 'CAMPUS10') {
      setDiscount(0.10);
      alert('Coupon CAMPUS10 applied! 10% Off');
    } else {
      alert('Invalid coupon');
    }
  };

  const handleEventJoin = (id) => {
    setEventsData(eventsData.map(e => e.id === id ? { ...e, joined: !e.joined } : e));
  };
  
  const handleTrainSubmit = () => {
    setTrainStatus(1);
    setTimeout(() => setTrainStatus(2), 1500);
    setTimeout(() => setTrainStatus(3), 3000);
  };
  
  const submitFeedback = () => {
    if(!feedbackInput) return;
    setFeedbacks([{ category: "General", rating: 5, message: feedbackInput, date: "Just now" }, ...feedbacks]);
    setFeedbackInput("");
    alert("Feedback submitted directly to admin panel.");
  };

  const submitLostItem = () => {
    if(!lostInput || !lostLocation) return;
    setLostItems([{ item: lostInput, location: lostLocation, contact: "You" }, ...lostItems]);
    setLostInput("");
    setLostLocation("");
  };

""")

# 2. Update Home Dashboard - Today's Schedule
schedule_raw = """<div className="schedule-list">
            <div className="schedule-item">
              <div className="schedule-time">
                <span className="s-hour">09:00</span>
                <span className="s-ampm">AM</span>
              </div>
              <div className="schedule-dot active-dot"></div>
              <div className="schedule-info">
                <p className="s-title">Data Structures</p>
                <p className="s-sub">Room 302 · Prof. Mehta</p>
              </div>
            </div>
            <div className="schedule-item">
              <div className="schedule-time">
                <span className="s-hour">11:00</span>
                <span className="s-ampm">AM</span>
              </div>
              <div className="schedule-dot"></div>
              <div className="schedule-info">
                <p className="s-title">OS Lab</p>
                <p className="s-sub">Lab 1 · Prof. Singh</p>
              </div>
            </div>
            <div className="schedule-item">
              <div className="schedule-time">
                <span className="s-hour">02:00</span>
                <span className="s-ampm">PM</span>
              </div>
              <div className="schedule-dot"></div>
              <div className="schedule-info">
                <p className="s-title">DBMS</p>
                <p className="s-sub">Room 401 · Prof. Joshi</p>
              </div>
            </div>
          </div>"""

schedule_mapped = """<div className="schedule-list">
            {[
              { id: 1, time: "09:00", ampm: "AM", title: "Data Structures", subtitle: "Room 302 · Prof. Mehta", active: true },
              { id: 2, time: "11:00", ampm: "AM", title: "OS Lab", subtitle: "Lab 1 · Prof. Singh", active: false },
              { id: 3, time: "02:00", ampm: "PM", title: "DBMS", subtitle: "Room 401 · Prof. Joshi", active: false }
            ].map(s => (
              <div className="schedule-item" key={s.id}>
                <div className="schedule-time">
                  <span className="s-hour">{s.time}</span>
                  <span className="s-ampm">{s.ampm}</span>
                </div>
                <div className={`schedule-dot ${s.active ? 'active-dot' : ''}`}></div>
                <div className="schedule-info">
                  <p className="s-title">{s.title}</p>
                  <p className="s-sub">{s.subtitle}</p>
                </div>
              </div>
            ))}
          </div>"""
text = text.replace(schedule_raw, schedule_mapped)


# 3. Update Canteen Menu Grid
menu_regex = r'<div className="menu-grid">.*?</button>\s*</div>\s*</div>'
menu_mapped = """<div className="menu-grid">
            {menu.map(item => (
              <div className="menu-item" key={item.id}>
                <div className="menu-img">
                  {item.icon === 'Soup' && <Soup size={32} />}
                  {item.icon === 'ChefHat' && <ChefHat size={32} />}
                  {item.icon === 'Sandwich' && <Sandwich size={32} />}
                  {item.icon === 'Coffee' && <Coffee size={32} />}
                  {item.icon === 'GlassWater' && <GlassWater size={32} />}
                  {item.icon === 'Utensils' && <Utensils size={32} />}
                </div>
                <p className="menu-name">{item.name}</p>
                <p className="menu-price">₹{item.price}</p>
                <button className="add-btn" id={`btn-${item.id}`} onClick={() => handleCanteenAdd(item)}><Plus size={16} /></button>
              </div>
            ))}
          </div>"""
text = re.sub(menu_regex, menu_mapped, text, flags=re.DOTALL)


# 4. Update Canteen Cart pricing in floating bar and cart screen
cart_bar = r'<p className="cart-price">₹85</p>'
text = re.sub(cart_bar, r'<p className="cart-price">₹{cartFinal.toFixed(0)}</p>', text)

coupon_input = r'<input className="coupon-input" placeholder="Enter coupon code" />\s*<button className="coupon-apply">Apply</button>'
coupon_live = """<input className="coupon-input" placeholder="Enter coupon code (CAMPUS10)" value={coupon} onChange={e => setCoupon(e.target.value)} />
              <button className={`coupon-apply ${discount > 0 ? 'active-coupon' : ''}`} onClick={handleCoupon}>{discount > 0 ? "Applied" : "Apply"}</button>"""
text = re.sub(coupon_input, coupon_live, text)

bill_totals = r'<div className="bill-row">\s*<span>Item Total</span>\s*<span>₹85</span>\s*</div>\s*<div className="bill-row discount">\s*<span>Coupon \(FREE10\)</span>\s*<span>-₹10</span>\s*</div>\s*<div className="bill-divider"></div>\s*<div className="bill-row total">\s*<span>Grand Total</span>\s*<span>₹75</span>\s*</div>'
bill_dynamic = """<div className="bill-row">
                <span>Item Total</span>
                <span>₹{cartTotal}</span>
              </div>
              {discount > 0 && (
                <div className="bill-row discount">
                  <span>Coupon</span>
                  <span>-₹{(cartTotal * discount).toFixed(0)}</span>
                </div>
              )}
              <div className="bill-divider"></div>
              <div className="bill-row total">
                <span>Grand Total</span>
                <span>₹{cartFinal.toFixed(0)}</span>
              </div>
"""
text = re.sub(bill_totals, bill_dynamic, text)


# 5. Events List updating
events_regex = r'<div className="event-list">.*?<div className="clubs-grid">'
events_mapped = """<div className="event-list">
              {eventsData.map(e => (
                <div className="event-mini" key={e.id}>
                  <div className="event-date-block">
                    <span className="ed-day">{e.day}</span>
                    <span className="ed-mon">{e.month}</span>
                  </div>
                  <div className="event-mini-body">
                    <p className="event-mini-title">{e.title}</p>
                    <p className="event-mini-sub">{e.sub}</p>
                  </div>
                  <button 
                    className={`event-reg-btn ${e.joined ? 'registered' : ''}`}
                    onClick={() => handleEventJoin(e.id)}
                  >
                    {e.joined ? <><Check size={16} style={{display: "inline", verticalAlign: "middle"}} /> Joined</> : 'Join'}
                  </button>
                </div>
              ))}
            </div>
            <p className="section-label">Campus Clubs</p>
            <div className="clubs-grid">"""
text = re.sub(events_regex, events_mapped, text, flags=re.DOTALL)


# 6. Train Pass Simulator
tracker_regex = r'<div className="tracker">.*?</div>\s*</div>\s*</div>\s*<!--  ░░░░ SCREEN: DIGITAL ID ░░░░  -->'
tracker_dynamic = """<div className="tracker">
            <div className={`tracker-step ${trainStatus >= 1 ? 'done' : ''}`}>
              <div className="ts-dot">{trainStatus >= 1 ? <Check size={16} /> : <Circle size={10} strokeWidth={2} />}</div>
              <p>Submitted</p>
            </div>
            <div className={`tracker-line ${trainStatus >= 1 ? 'done' : ''}`}></div>
            <div className={`tracker-step ${trainStatus >= 2 ? 'done' : (trainStatus === 1 ? 'active' : '')}`}>
              <div className={`ts-dot ${trainStatus === 1 ? 'pulsing' : ''}`}>{trainStatus >= 2 ? <Check size={16} /> : (trainStatus === 1 ? <Circle fill="currentColor" size={10} strokeWidth={0} /> : <Circle size={10} strokeWidth={2} />)}</div>
              <p>Verification</p>
            </div>
            <div className={`tracker-line ${trainStatus >= 2 ? 'done' : ''}`}></div>
            <div className={`tracker-step ${trainStatus >= 3 ? 'done' : (trainStatus === 2 ? 'active' : '')}`}>
              <div className={`ts-dot ${trainStatus === 2 ? 'pulsing' : ''}`}>{trainStatus >= 3 ? <Check size={16} /> : (trainStatus === 2 ? <Circle fill="currentColor" size={10} strokeWidth={0} /> : <Circle size={10} strokeWidth={2} />)}</div>
              <p>Approval</p>
            </div>
            <div className={`tracker-line ${trainStatus >= 3 ? 'done' : ''}`}></div>
            <div className={`tracker-step ${trainStatus === 3 ? 'active' : ''}`}>
              <div className={`ts-dot ${trainStatus === 3 ? 'empty' : 'empty'}`}>{trainStatus === 3 ? <Circle fill="currentColor" size={10} strokeWidth={0} /> : <Circle size={10} strokeWidth={2} />}</div>
              <p>Download</p>
            </div>
          </div>
        </div>
      </div>

      {/*  ░░░░ SCREEN: DIGITAL ID ░░░░  */}"""

text = re.sub(r'<div className="tracker">.*?</div>\s*</div>\s*</div>\s*\{\/\*  ░░░░ SCREEN: DIGITAL ID ░░░░  \*\/\}', tracker_dynamic, text, flags=re.DOTALL)

submit_btn = r'<button className="btn-primary full-width">Submit Application</button>'
text = re.sub(submit_btn, '<button className="btn-primary full-width" onClick={handleTrainSubmit}>Submit Application</button>', text)


# 7. Assignments Tracker
assign_regex = r'<p className="section-label">Upcoming Assignments</p>.*?<p className="section-label">Weekly Timetable</p>'
assign_mapped = """<p className="section-label">Upcoming Assignments</p>
            <div className="list-cards">
              {assignments.map(a => (
                <div className="list-card" key={a.id}>
                  <div className="lc-left">
                    <div className="lc-icon" style={{background: a.iconBg, color: a.iconColor}}>
                      {a.iconName === 'AlertTriangle' && <AlertTriangle size={18} />}
                      {a.iconName === 'Folder' && <Folder size={18} />}
                      {a.iconName === 'FileText' && <FileText size={18} />}
                    </div>
                    <div>
                      <p className="lc-title">{a.title}</p>
                      <p className="lc-sub">{a.deadline}</p>
                    </div>
                  </div>
                  <div className={`score-pill ${a.statusClass}`}>{a.statusText}</div>
                </div>
              ))}
            </div>

            <p className="section-label">Weekly Timetable</p>"""
text = re.sub(assign_regex, assign_mapped, text, flags=re.DOTALL)


with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("App.jsx refactoring phase 1 complete.")
