import React, { useEffect } from 'react';
import { AlertTriangle, ArrowRight, ArrowLeft, BarChart2, Bell, Book, BookOpen, Brain, Building2, Calendar, CalendarDays, Camera, Check, CheckCircle, CheckCircle2, ChefHat, ChevronRight, Circle, ClipboardList, Clock, Code2, Coffee, Crown, Database, Download, FileText, Flame, Folder, Gift, GlassWater, Globe, GraduationCap, Home, IdCard, Image, Landmark, Loader, MapPin, Medal, Menu, MessageCircle, Monitor, Paperclip, PenLine, Plus, Receipt, Sandwich, Scroll, Search, ShieldCheck, Soup, Star, Theater, Ticket, TrainFront, Trophy, Upload, Utensils, X, XCircle } from 'lucide-react';
import './app.css';

export default function App() {
  useEffect(() => {
    // Add app.js dynamically so its querySelectors work
    const script = document.createElement('script');
    script.src = "/app.js";
    script.async = true;
    document.body.appendChild(script);
    
    return () => {
      if(document.body.contains(script)) {
        document.body.removeChild(script);
      }
    };
  }, []);

  return (
    <>


  {/*  ═══════════════════════════ APP SHELL ══════════════════════════════  */}
  <div className="phone-frame">
    <div className="phone-notch"></div>
    <div className="app-container">

      {/*  STATUS BAR  */}
      <div className="status-bar">
        <span className="status-time">9:41</span>
        <div className="status-icons">
          <svg width="16" height="12" viewBox="0 0 16 12" fill="white">
            <rect x="0" y="3" width="3" height="9" rx="1" />
            <rect x="4" y="2" width="3" height="10" rx="1" />
            <rect x="8" y="1" width="3" height="11" rx="1" />
            <rect x="12" y="0" width="3" height="12" rx="1" />
          </svg>
          <svg width="16" height="12" viewBox="0 0 24 18" fill="white">
            <path d="M1 5C4.5 1.5 19.5 1.5 23 5" stroke="white" strokeWidth="2" fill="none" />
            <path d="M4 8.5C6.5 6 17.5 6 20 8.5" stroke="white" strokeWidth="2" fill="none" />
            <path d="M7.5 12C9 10.5 15 10.5 16.5 12" stroke="white" strokeWidth="2" fill="none" />
            <circle cx="12" cy="15" r="2" fill="white" />
          </svg>
          <svg width="25" height="12" viewBox="0 0 25 12" fill="none">
            <rect x="0.5" y="0.5" width="22" height="11" rx="2.5" stroke="white" />
            <rect x="1.5" y="1.5" width="16" height="9" rx="1.5" fill="white" />
            <path d="M23.5 4.5V7.5C24.3 7.167 24.3 4.833 23.5 4.5Z" fill="white" />
          </svg>
        </div>
      </div>

      {/*  ─── SCREENS (only one is visible at a time) ───  */}

      {/*  ░░░░ SCREEN: HOME / DASHBOARD ░░░░  */}
      <div className="screen active" id="screen-home">
        <div className="screen-scroll">
          <div className="home-header">
            <div>
              <p className="greeting-sub">Good Morning</p>
              <h1 className="greeting-name">Rahul Sharma</h1>
              <p className="greeting-dept">Computer Engineering · Sem 6</p>
            </div>
            <div className="avatar-wrapper" onClick={() => window.navigate('screen-digital-id')}>
              <div className="avatar">RS</div>
              <div className="avatar-badge"><Circle fill="currentColor" size={10} strokeWidth={0} /></div>
            </div>
          </div>

          {/*  Streak Banner  */}
          <div className="streak-banner" onClick={() => window.navigate('screen-academic')}>
            <div className="streak-icon"><Flame size={18} /></div>
            <div className="streak-text">
              <p className="streak-label">Daily Streak</p>
              <p className="streak-val">12 Days · Keep it up!</p>
            </div>
            <ChevronRight size={16} color="white" />
          </div>

          {/*  Quick Actions Grid  */}
          <p className="section-label">Quick Access</p>
          <div className="quick-grid">
            <button className="quick-card" onClick={() => window.navigate('screen-academic')}>
              <div className="quick-icon"><BookOpen size={18} /></div>
              <span>Academics</span>
            </button>
            <button className="quick-card" onClick={() => window.navigate('screen-library')}>
              <div className="quick-icon"><Landmark size={18} /></div>
              <span>Library</span>
            </button>
            <button className="quick-card" onClick={() => window.navigate('screen-canteen')}>
              <div className="quick-icon"><Utensils size={18} /></div>
              <span>Canteen</span>
            </button>
            <button className="quick-card" onClick={() => window.navigate('screen-events')}>
              <div className="quick-icon"><CalendarDays size={18} /></div>
              <span>Events</span>
            </button>
            <button className="quick-card" onClick={() => window.navigate('screen-concession')}>
              <div className="quick-icon"><TrainFront size={18} /></div>
              <span>Train Pass</span>
            </button>
            <button className="quick-card" onClick={() => window.navigate('screen-lost-found')}>
              <div className="quick-icon"><Search size={18} /></div>
              <span>Lost &amp; Found</span>
            </button>
            <button className="quick-card" onClick={() => window.navigate('screen-feedback')}>
              <div className="quick-icon"><MessageCircle size={18} /></div>
              <span>Feedback</span>
            </button>
            <button className="quick-card" onClick={() => window.navigate('screen-forms')}>
              <div className="quick-icon"><ClipboardList size={18} /></div>
              <span>Forms</span>
            </button>
          </div>

          {/*  Today's Overview  */}
          <p className="section-label">Today's Schedule</p>
          <div className="schedule-list">
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
          </div>

          {/*  Notifications Preview  */}
          <p className="section-label">Recent Notifications</p>
          <div className="notif-preview">
            <div className="notif-item" onClick={() => window.navigate('screen-notifications')}>
              <div className="notif-dot red"></div>
              <div className="notif-body">
                <p className="notif-title">Assignment Due Tomorrow!</p>
                <p className="notif-sub">OS Assignment 3 · 11:59 PM</p>
              </div>
              <span className="notif-time">2m</span>
            </div>
            <div className="notif-item" onClick={() => window.navigate('screen-notifications')}>
              <div className="notif-dot yellow"></div>
              <div className="notif-body">
                <p className="notif-title">Canteen Order Ready</p>
                <p className="notif-sub">Token #14 · Counter 2</p>
              </div>
              <span className="notif-time">15m</span>
            </div>
            <div className="notif-item" onClick={() => window.navigate('screen-notifications')}>
              <div className="notif-dot blue"></div>
              <div className="notif-body">
                <p className="notif-title">New Event: Hackathon 2026</p>
                <p className="notif-sub">Register by March 20</p>
              </div>
              <span className="notif-time">1h</span>
            </div>
          </div>
        </div>
      </div>

      {/*  ░░░░ SCREEN: ACADEMIC SUPPORT ░░░░  */}
      <div className="screen" id="screen-academic">
        <div className="screen-header">
          <button className="back-btn" onClick={() => window.goBack()}><ArrowLeft size={20} /></button>
          <h2 className="screen-title">Academic Support</h2>
          <div></div>
        </div>
        <div className="screen-scroll has-header">

          {/*  Tabs  */}
          <div className="tab-bar">
            <button className="tab active" data-tab="tab-quiz">Quiz</button>
            <button className="tab" data-tab="tab-coding">Coding</button>
            <button className="tab" data-tab="tab-schedule">Schedule</button>
            <button className="tab" data-tab="tab-leaderboard">Leaderboard</button>
          </div>

          {/*  Quiz Tab  */}
          <div className="tab-content active" id="tab-quiz">
            <div className="challenge-card">
              <p className="challenge-label"><PenLine size={18} /> Daily Quiz</p>
              <h3 className="challenge-title">Data Structures & Algorithms</h3>
              <div className="challenge-meta">
                <span className="chip">10 Questions</span>
                <span className="chip">15 min</span>
                <span className="chip" style={{borderColor: '#4ade80', color: '#4ade80'}}>+50 XP</span>
              </div>
              <div className="progress-wrap">
                <div className="progress-label"><span>Daily Progress</span><span>0/10</span></div>
                <div className="progress-bar">
                  <div className="progress-fill" style={{width: '0%'}}></div>
                </div>
              </div>
              <button className="btn-primary full-width">Start Quiz</button>
            </div>

            <p className="section-label">Subject Quizzes</p>
            <div className="list-cards">
              <div className="list-card" onclick>
                <div className="lc-left">
                  <div className="lc-icon"><Globe size={18} /></div>
                  <div>
                    <p className="lc-title">Computer Networks</p>
                    <p className="lc-sub">24 questions · Med</p>
                  </div>
                </div>
                <div className="score-pill green">92%</div>
              </div>
              <div className="list-card">
                <div className="lc-left">
                  <div className="lc-icon"><Database size={18} /></div>
                  <div>
                    <p className="lc-title">DBMS</p>
                    <p className="lc-sub">30 questions · Hard</p>
                  </div>
                </div>
                <div className="score-pill yellow">78%</div>
              </div>
              <div className="list-card">
                <div className="lc-left">
                  <div className="lc-icon"><Monitor size={18} /></div>
                  <div>
                    <p className="lc-title">Operating Systems</p>
                    <p className="lc-sub">20 questions · Med</p>
                  </div>
                </div>
                <div className="score-pill red">61%</div>
              </div>
            </div>
          </div>

          {/*  Coding Tab  */}
          <div className="tab-content" id="tab-coding">
            <div className="challenge-card">
              <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
                <p className="challenge-label"><Flame size={18} /> Daily Challenge</p>
                <span className="streak-chip">12 Day Streak</span>
              </div>
              <h3 className="challenge-title">Two Sum Problem</h3>
              <p className="challenge-desc">Given an array of integers, return indices of the two numbers such that they add
                up to a target.</p>
              <div className="challenge-meta">
                <span className="chip">Array</span>
                <span className="chip">Hash Map</span>
                <span className="chip" style={{borderColor: '#f97316', color: '#f97316'}}>Medium</span>
              </div>
              <div className="timer-row">
                <span className="timer-label"><Clock size={18} /> Time Left</span>
                <span className="timer-val">08:42:17</span>
              </div>
              <button className="btn-primary full-width">Solve Now</button>
            </div>

            <p className="section-label">Recent Submissions</p>
            <div className="list-cards">
              <div className="list-card">
                <div className="lc-left">
                  <div className="lc-icon"><CheckCircle size={18} /></div>
                  <div>
                    <p className="lc-title">Merge Intervals</p>
                    <p className="lc-sub">Yesterday · 100ms</p>
                  </div>
                </div>
                <div className="score-pill green">Passed</div>
              </div>
              <div className="list-card">
                <div className="lc-left">
                  <div className="lc-icon"><XCircle size={18} /></div>
                  <div>
                    <p className="lc-title">Binary Tree Paths</p>
                    <p className="lc-sub">2 days ago</p>
                  </div>
                </div>
                <div className="score-pill red">Failed</div>
              </div>
            </div>
          </div>

          {/*  Schedule Tab  */}
          <div className="tab-content" id="tab-schedule">
            <p className="section-label">Upcoming Assignments</p>
            <div className="list-cards">
              <div className="list-card">
                <div className="lc-left">
                  <div className="lc-icon" style={{background: '#ff444422', color: '#ff4444'}}><AlertTriangle size={18} />
                  </div>
                  <div>
                    <p className="lc-title">OS Assignment 3</p>
                    <p className="lc-sub">Tomorrow · 11:59 PM</p>
                  </div>
                </div>
                <div className="score-pill red">Urgent</div>
              </div>
              <div className="list-card">
                <div className="lc-left">
                  <div className="lc-icon" style={{background: '#f9731622', color: '#f97316'}}><Folder size={18} /></div>
                  <div>
                    <p className="lc-title">DBMS Mini Project</p>
                    <p className="lc-sub">Mar 18 · 11:59 PM</p>
                  </div>
                </div>
                <div className="score-pill yellow">Soon</div>
              </div>
              <div className="list-card">
                <div className="lc-left">
                  <div className="lc-icon" style={{background: '#4ade8022', color: '#4ade80'}}><FileText size={18} /></div>
                  <div>
                    <p className="lc-title">CN Report</p>
                    <p className="lc-sub">Mar 25 · 11:59 PM</p>
                  </div>
                </div>
                <div className="score-pill green">On Track</div>
              </div>
            </div>

            <p className="section-label">Weekly Timetable</p>
            <div className="timetable">
              <div className="tt-row">
                <div className="tt-day">MON</div>
                <div className="tt-slot filled">DS 9–10</div>
                <div className="tt-slot filled">OS 11–12</div>
                <div className="tt-slot">—</div>
                <div className="tt-slot filled">DBMS 2–3</div>
              </div>
              <div className="tt-row">
                <div className="tt-day">TUE</div>
                <div className="tt-slot">—</div>
                <div className="tt-slot filled">CN 10–11</div>
                <div className="tt-slot filled">Lab 12–2</div>
                <div className="tt-slot">—</div>
              </div>
              <div className="tt-row">
                <div className="tt-day">WED</div>
                <div className="tt-slot filled">DS 9–10</div>
                <div className="tt-slot">—</div>
                <div className="tt-slot filled">DBMS 1–2</div>
                <div className="tt-slot filled">SE 3–4</div>
              </div>
            </div>
          </div>

          {/*  Leaderboard Tab  */}
          <div className="tab-content" id="tab-leaderboard">
            <div className="leaderboard-podium">
              <div className="podium-item second">
                <div className="podium-avatar">PK</div>
                <p className="podium-name">Priya K.</p>
                <div className="podium-block" style={{height: '60px', background: '#c0c0c040'}}>2</div>
                <p className="podium-xp">1840 XP</p>
              </div>
              <div className="podium-item first">
                <div className="podium-crown"><Crown size={18} /></div>
                <div className="podium-avatar">AM</div>
                <p className="podium-name">Aman M.</p>
                <div className="podium-block" style={{height: '80px', background: '#ffd70040'}}>1</div>
                <p className="podium-xp">2250 XP</p>
              </div>
              <div className="podium-item third">
                <div className="podium-avatar">RS</div>
                <p className="podium-name">You</p>
                <div className="podium-block" style={{height: '45px', background: '#cd7f3240'}}>3</div>
                <p className="podium-xp">1620 XP</p>
              </div>
            </div>
            <div className="list-cards">
              <div className="list-card">
                <div className="lc-left"><span className="rank-num">4</span>
                  <div>
                    <p className="lc-title">Sneha R.</p>
                    <p className="lc-sub">SE Dept</p>
                  </div>
                </div>
                <p className="lc-xp">1540 XP</p>
              </div>
              <div className="list-card">
                <div className="lc-left"><span className="rank-num">5</span>
                  <div>
                    <p className="lc-title">Karan M.</p>
                    <p className="lc-sub">CE Dept</p>
                  </div>
                </div>
                <p className="lc-xp">1490 XP</p>
              </div>
              <div className="list-card">
                <div className="lc-left"><span className="rank-num">6</span>
                  <div>
                    <p className="lc-title">Isha T.</p>
                    <p className="lc-sub">IT Dept</p>
                  </div>
                </div>
                <p className="lc-xp">1380 XP</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/*  ░░░░ SCREEN: STUDY MATERIAL HUB (V-Refer) ░░░░  */}
      <div className="screen" id="screen-materials">
        <div className="screen-header">
          <button className="back-btn" onClick={() => window.goBack()}><ArrowLeft size={20} /></button>
          <h2 className="screen-title">Study Materials</h2>
          <div></div>
        </div>
        <div className="screen-scroll has-header">
          <div className="search-bar">
            <span className="search-icon"><Search size={18} /></span>
            <input className="search-input" placeholder="Search notes, subjects..." />
          </div>

          <p className="section-label">Recent Uploads</p>
          <div className="material-list">
            <div className="material-card">
              <div className="material-icon pdf"><FileText size={20} style={{marginBottom: "4px"}} /> PDF</div>
              <div className="material-body">
                <p className="material-title">Unit 4 – Deadlock & Synchronization</p>
                <p className="material-meta">Prof. Singh · OS · Mar 10</p>
              </div>
              <button className="dl-btn"><Download size={18} /></button>
            </div>
            <div className="material-card">
              <div className="material-icon pdf"><FileText size={20} style={{marginBottom: "4px"}} /> PDF</div>
              <div className="material-body">
                <p className="material-title">Normalization 1NF–BCNF Notes</p>
                <p className="material-meta">Prof. Joshi · DBMS · Mar 9</p>
              </div>
              <button className="dl-btn"><Download size={18} /></button>
            </div>
            <div className="material-card">
              <div className="material-icon ppt"><Monitor size={20} style={{marginBottom: "4px"}} /> PPT</div>
              <div className="material-body">
                <p className="material-title">TCP/IP Layer Deep Dive</p>
                <p className="material-meta">Prof. Verma · CN · Mar 8</p>
              </div>
              <button className="dl-btn"><Download size={18} /></button>
            </div>
            <div className="material-card">
              <div className="material-icon doc"><FileText size={20} style={{marginBottom: "4px"}} /> DOC</div>
              <div className="material-body">
                <p className="material-title">AVL Tree Rotations Guide</p>
                <p className="material-meta">Prof. Mehta · DS · Mar 7</p>
              </div>
              <button className="dl-btn"><Download size={18} /></button>
            </div>
          </div>

          <p className="section-label">Browse by Subject</p>
          <div className="subject-chips">
            <button className="schip active">All</button>
            <button className="schip">OS</button>
            <button className="schip">DBMS</button>
            <button className="schip">DS</button>
            <button className="schip">CN</button>
            <button className="schip">SE</button>
            <button className="schip">Maths</button>
          </div>
        </div>
      </div>

      {/*  ░░░░ SCREEN: LIBRARY ░░░░  */}
      <div className="screen" id="screen-library">
        <div className="screen-header">
          <button className="back-btn" onClick={() => window.goBack()}><ArrowLeft size={20} /></button>
          <h2 className="screen-title">Library</h2>
          <div></div>
        </div>
        <div className="screen-scroll has-header">
          <div className="search-bar">
            <span className="search-icon"><Search size={18} /></span>
            <input className="search-input" placeholder="Search books, authors..." />
          </div>

          {/*  Issued Books  */}
          <p className="section-label">My Issued Books</p>
          <div className="list-cards">
            <div className="list-card">
              <div className="book-cover" style={{background: '#e11d4820'}}><Book size={18} /></div>
              <div className="lc-mid">
                <p className="lc-title">Operating System Concepts</p>
                <p className="lc-sub">Silberschatz · Due: Mar 20</p>
                <div className="due-bar">
                  <div className="due-fill warn" style={{width: '70%'}}></div>
                </div>
              </div>
              <button className="renew-btn">Renew</button>
            </div>
            <div className="list-card">
              <div className="book-cover" style={{background: '#1d4ed820'}}><Book size={18} /></div>
              <div className="lc-mid">
                <p className="lc-title">Introduction to Algorithms</p>
                <p className="lc-sub">CLRS · Due: Mar 28</p>
                <div className="due-bar">
                  <div className="due-fill ok" style={{width: '30%'}}></div>
                </div>
              </div>
              <button className="renew-btn">Renew</button>
            </div>
          </div>

          {/*  Reserve  */}
          <p className="section-label">Available Books</p>
          <div className="list-cards">
            <div className="list-card">
              <div className="book-cover" style={{background: '#16a34a20'}}><Book size={18} /></div>
              <div className="lc-mid">
                <p className="lc-title">Database System Concepts</p>
                <p className="lc-sub">Silberschatz · 3 copies avail.</p>
              </div>
              <button className="renew-btn" style={{background: '#ffffff15'}}>Reserve</button>
            </div>
            <div className="list-card">
              <div className="book-cover" style={{background: '#7c3aed20'}}><Book size={18} /></div>
              <div className="lc-mid">
                <p className="lc-title">Computer Networks</p>
                <p className="lc-sub">Tanenbaum · 1 copy avail.</p>
              </div>
              <button className="renew-btn" style={{background: '#ffffff15'}}>Reserve</button>
            </div>
            <div className="list-card">
              <div className="book-cover" style={{background: '#b4530020'}}><Book size={18} /></div>
              <div className="lc-mid">
                <p className="lc-title">The Pragmatic Programmer</p>
                <p className="lc-sub">Hunt & Thomas · 0 copies</p>
              </div>
              <button className="renew-btn" style={{opacity: '.4', cursor: 'default'}}>Waitlist</button>
            </div>
          </div>
        </div>
      </div>

      {/*  ░░░░ SCREEN: TRAIN CONCESSION PASS ░░░░  */}
      <div className="screen" id="screen-concession">
        <div className="screen-header">
          <button className="back-btn" onClick={() => window.goBack()}><ArrowLeft size={20} /></button>
          <h2 className="screen-title">Train Concession Pass</h2>
          <div></div>
        </div>
        <div className="screen-scroll has-header">

          {/*  Current Pass Status  */}
          <div className="pass-card">
            <div className="pass-header">
              <span className="pass-type"><TrainFront size={18} /> Rail Concession</span>
              <div className="pass-status approved">APPROVED</div>
            </div>
            <p className="pass-name">Rahul Sharma</p>
            <div className="pass-detail-row">
              <div className="pass-detail">
                <p className="pd-label">From</p>
                <p className="pd-val">Borivali</p>
              </div>
              <div className="pass-divider"><ArrowRight size={16} /></div>
              <div className="pass-detail">
                <p className="pd-label">To</p>
                <p className="pd-val">Churchgate</p>
              </div>
            </div>
            <div className="pass-detail-row" style={{marginTop: '12px'}}>
              <div className="pass-detail">
                <p className="pd-label">Valid Till</p>
                <p className="pd-val">May 2026</p>
              </div>
              <div className="pass-detail">
                <p className="pd-label">Class</p>
                <p className="pd-val">Second</p>
              </div>
            </div>
            <button className="btn-primary full-width" style={{marginTop: '16px'}}>Download Pass</button>
          </div>

          {/*  New Application  */}
          <p className="section-label">Apply / Renew</p>
          <div className="form-card">
            <div className="form-group">
              <label className="form-label">From Station</label>
              <input className="form-input" placeholder="e.g. Borivali" />
            </div>
            <div className="form-group">
              <label className="form-label">To Station</label>
              <input className="form-input" placeholder="e.g. Churchgate" />
            </div>
            <div className="form-group">
              <label className="form-label">Class</label>
              <select className="form-input">
                <option>Second Class</option>
                <option>First Class</option>
              </select>
            </div>
            <div className="form-group">
              <label className="form-label">Institution Certificate</label>
              <div className="upload-box">
                <span><Paperclip size={18} /> Tap to upload PDF/Image</span>
              </div>
            </div>
            <button className="btn-primary full-width">Submit Application</button>
          </div>

          {/*  Progress Tracker  */}
          <p className="section-label">Application Status</p>
          <div className="tracker">
            <div className="tracker-step done">
              <div className="ts-dot"><Check size={16} /></div>
              <p>Submitted</p>
            </div>
            <div className="tracker-line done"></div>
            <div className="tracker-step done">
              <div className="ts-dot"><Check size={16} /></div>
              <p>Verification</p>
            </div>
            <div className="tracker-line done"></div>
            <div className="tracker-step active">
              <div className="ts-dot pulsing"><Circle fill="currentColor" size={10} strokeWidth={0} /></div>
              <p>Approval</p>
            </div>
            <div className="tracker-line"></div>
            <div className="tracker-step">
              <div className="ts-dot empty"><Circle size={10} strokeWidth={2} /></div>
              <p>Download</p>
            </div>
          </div>
        </div>
      </div>

      {/*  ░░░░ SCREEN: DIGITAL ID ░░░░  */}
      <div className="screen" id="screen-digital-id">
        <div className="screen-header">
          <button className="back-btn" onClick={() => window.goBack()}><ArrowLeft size={20} /></button>
          <h2 className="screen-title">Digital ID Card</h2>
          <div></div>
        </div>
        <div className="screen-scroll has-header">
          <div className="id-card">
            <div className="id-card-header">
              <div className="id-logo"><GraduationCap size={24} /></div>
              <div>
                <p className="id-college">Vidyalankar Institute of Technology</p>
                <p className="id-year">Academic Year 2025–26</p>
              </div>
            </div>
            <div className="id-body">
              <div className="id-avatar">RS</div>
              <div className="id-info">
                <p className="id-name">Rahul Sharma</p>
                <p className="id-dept">Information Technology</p>
                <p className="id-roll">Roll No: 24101C0001</p>
                <p className="id-sem">Semester: VI</p>
              </div>
            </div>
            <div className="id-qr">
              <div className="barcode-wrap">
                <svg className="barcode-svg" viewBox="0 0 220 72" xmlns="http://www.w3.org/2000/svg">
                  {/*  Guard bars  */}
                  <rect x="2" y="0" width="2" height="56" fill="#111" />
                  <rect x="6" y="0" width="1" height="56" fill="#111" />
                  <rect x="9" y="0" width="2" height="56" fill="#111" />
                  {/*  Data bars left  */}
                  <rect x="14" y="0" width="3" height="52" fill="#111" />
                  <rect x="19" y="0" width="1" height="52" fill="#111" />
                  <rect x="22" y="0" width="2" height="52" fill="#111" />
                  <rect x="26" y="0" width="1" height="52" fill="#111" />
                  <rect x="29" y="0" width="3" height="52" fill="#111" />
                  <rect x="34" y="0" width="1" height="52" fill="#111" />
                  <rect x="37" y="0" width="2" height="52" fill="#111" />
                  <rect x="41" y="0" width="1" height="52" fill="#111" />
                  <rect x="44" y="0" width="3" height="52" fill="#111" />
                  <rect x="49" y="0" width="2" height="52" fill="#111" />
                  <rect x="53" y="0" width="1" height="52" fill="#111" />
                  <rect x="56" y="0" width="3" height="52" fill="#111" />
                  <rect x="61" y="0" width="1" height="52" fill="#111" />
                  {/*  Center guard  */}
                  <rect x="66" y="0" width="1" height="56" fill="#111" />
                  <rect x="69" y="0" width="1" height="56" fill="#111" />
                  <rect x="72" y="0" width="1" height="56" fill="#111" />
                  {/*  Data bars right  */}
                  <rect x="76" y="0" width="2" height="52" fill="#111" />
                  <rect x="80" y="0" width="3" height="52" fill="#111" />
                  <rect x="85" y="0" width="1" height="52" fill="#111" />
                  <rect x="88" y="0" width="2" height="52" fill="#111" />
                  <rect x="92" y="0" width="1" height="52" fill="#111" />
                  <rect x="95" y="0" width="3" height="52" fill="#111" />
                  <rect x="100" y="0" width="1" height="52" fill="#111" />
                  <rect x="103" y="0" width="2" height="52" fill="#111" />
                  <rect x="107" y="0" width="3" height="52" fill="#111" />
                  <rect x="112" y="0" width="1" height="52" fill="#111" />
                  <rect x="115" y="0" width="2" height="52" fill="#111" />
                  <rect x="119" y="0" width="1" height="52" fill="#111" />
                  <rect x="122" y="0" width="3" height="52" fill="#111" />
                  <rect x="127" y="0" width="2" height="52" fill="#111" />
                  <rect x="131" y="0" width="1" height="52" fill="#111" />
                  <rect x="134" y="0" width="3" height="52" fill="#111" />
                  <rect x="139" y="0" width="1" height="52" fill="#111" />
                  <rect x="142" y="0" width="2" height="52" fill="#111" />
                  <rect x="146" y="0" width="1" height="52" fill="#111" />
                  <rect x="149" y="0" width="3" height="52" fill="#111" />
                  <rect x="154" y="0" width="2" height="52" fill="#111" />
                  <rect x="158" y="0" width="1" height="52" fill="#111" />
                  <rect x="161" y="0" width="2" height="52" fill="#111" />
                  <rect x="165" y="0" width="3" height="52" fill="#111" />
                  <rect x="170" y="0" width="1" height="52" fill="#111" />
                  <rect x="173" y="0" width="2" height="52" fill="#111" />
                  <rect x="177" y="0" width="1" height="52" fill="#111" />
                  <rect x="180" y="0" width="3" height="52" fill="#111" />
                  <rect x="185" y="0" width="1" height="52" fill="#111" />
                  <rect x="188" y="0" width="2" height="52" fill="#111" />
                  <rect x="192" y="0" width="3" height="52" fill="#111" />
                  <rect x="197" y="0" width="1" height="52" fill="#111" />
                  {/*  End guard  */}
                  <rect x="202" y="0" width="2" height="56" fill="#111" />
                  <rect x="206" y="0" width="1" height="56" fill="#111" />
                  <rect x="209" y="0" width="2" height="56" fill="#111" />
                  {/*  Number text below bars  */}
                  <text x="110" y="68" font-family="monospace" font-size="9" fill="#333" text-anchor="middle"
                    letter-spacing="2">CE2023045-06</text>
                </svg>
              </div>
              <p className="qr-scan-label">Scan Barcode to Verify</p>
            </div>
            <div className="id-footer">
              <p>Valid till: May 31, 2026</p>
              <div className="id-status">● Active</div>
            </div>
          </div>
          <div className="id-uses">
            <p className="section-label">Card Uses</p>
            <div className="uses-grid">
              <div className="use-item"><Landmark size={18} /><span>Library</span></div>
              <div className="use-item"><Ticket size={18} /><span>Events</span></div>
              <div className="use-item"><ShieldCheck size={18} /><span>Campus Gate</span></div>
              <div className="use-item"><ClipboardList size={18} /><span>Forms</span></div>
            </div>
          </div>
        </div>
      </div>

      {/*  ░░░░ SCREEN: CANTEEN ░░░░  */}
      <div className="screen" id="screen-canteen">
        <div className="screen-header">
          <button className="back-btn" onClick={() => window.goBack()}><ArrowLeft size={20} /></button>
          <h2 className="screen-title">Smart Canteen</h2>
          <button className="icon-btn" onClick={() => window.navigate('screen-canteen-bill')}><Receipt size={18} /></button>
        </div>
        <div className="screen-scroll has-header">

          {/*  Active Token  */}
          <div className="token-card">
            <p className="token-label">Your Token</p>
            <div className="token-number">#14</div>
            <p className="token-status"><Loader size={18} /> Being Prepared · Counter 2</p>
            <div className="token-progress">
              <div className="tp-step done">Order<br />Placed</div>
              <div className="tp-line done"></div>
              <div className="tp-step done">Preparing</div>
              <div className="tp-line"></div>
              <div className="tp-step active">Ready</div>
              <div className="tp-line"></div>
              <div className="tp-step">Collected</div>
            </div>
          </div>

          {/*  Menu  */}
          <div className="menu-tabs">
            <button className="menu-tab active">All</button>
            <button className="menu-tab">Meals</button>
            <button className="menu-tab">Snacks</button>
            <button className="menu-tab">Drinks</button>
          </div>

          <div className="menu-grid">
            <div className="menu-item">
              <div className="menu-img"><Soup size={18} /></div>
              <p className="menu-name">Veg Thali</p>
              <p className="menu-price">₹60</p>
              <button className="add-btn"><Plus size={16} /></button>
            </div>
            <div className="menu-item">
              <div className="menu-img"><ChefHat size={18} /></div>
              <p className="menu-name">Paneer Rice</p>
              <p className="menu-price">₹55</p>
              <button className="add-btn"><Plus size={16} /></button>
            </div>
            <div className="menu-item">
              <div className="menu-img"><Sandwich size={18} /></div>
              <p className="menu-name">Sandwich</p>
              <p className="menu-price">₹30</p>
              <button className="add-btn"><Plus size={16} /></button>
            </div>
            <div className="menu-item">
              <div className="menu-img"><Coffee size={18} /></div>
              <p className="menu-name">Tea / Coffee</p>
              <p className="menu-price">₹15</p>
              <button className="add-btn"><Plus size={16} /></button>
            </div>
            <div className="menu-item">
              <div className="menu-img"><GlassWater size={18} /></div>
              <p className="menu-name">Juice</p>
              <p className="menu-price">₹25</p>
              <button className="add-btn"><Plus size={16} /></button>
            </div>
            <div className="menu-item">
              <div className="menu-img"><Utensils size={18} /></div>
              <p className="menu-name">Vada Pav</p>
              <p className="menu-price">₹20</p>
              <button className="add-btn"><Plus size={16} /></button>
            </div>
          </div>

          {/*  Cart summary  */}
          <div className="cart-bar">
            <div className="cart-info">
              <span className="cart-count">2 items</span>
              <span className="cart-price">₹85</span>
            </div>
            <button className="btn-primary" onClick={() => window.navigate('screen-canteen-bill')}>View Cart →</button>
          </div>
        </div>
      </div>

      {/*  ░░░░ SCREEN: CANTEEN BILL / COUPON ░░░░  */}
      <div className="screen" id="screen-canteen-bill">
        <div className="screen-header">
          <button className="back-btn" onClick={() => window.goBack()}><ArrowLeft size={20} /></button>
          <h2 className="screen-title">Order Summary</h2>
          <div></div>
        </div>
        <div className="screen-scroll has-header">

          {/*  Coupon Section  */}
          <p className="section-label"><Ticket size={18} /> Apply Coupon</p>
          <div className="coupon-row">
            <input className="coupon-input" placeholder="Enter coupon code" value="CAMPUS10" />
            <button className="coupon-apply active-coupon">Applied <Check size={16} style={{display: "inline", verticalAlign: "middle"}} /></button>
          </div>
          <div className="coupon-applied-card">
            <div className="coupon-icon"><Gift size={18} /></div>
            <div>
              <p className="coupon-name">CAMPUS10 – 10% Off</p>
              <p className="coupon-sub">Student discount applied</p>
            </div>
            <p className="coupon-save">−₹8.50</p>
          </div>

          {/*  My Coupons  */}
          <p className="section-label">My Coupons</p>
          <div className="coupon-list">
            <div className="coupon-card used">
              <div className="coupon-left">
                <p className="c-code">CAMPUS10</p>
                <p className="c-desc">10% off on total</p>
              </div>
              <div className="coupon-right used-label">Used</div>
            </div>
            <div className="coupon-card">
              <div className="coupon-left">
                <p className="c-code">MEAL30</p>
                <p className="c-desc">₹30 off on meals above ₹100</p>
              </div>
              <div className="coupon-right avail-label">Apply</div>
            </div>
            <div className="coupon-card">
              <div className="coupon-left">
                <p className="c-code">SNACK15</p>
                <p className="c-desc">₹15 off on snacks</p>
              </div>
              <div className="coupon-right avail-label">Apply</div>
            </div>
          </div>

          {/*  Bill  */}
          <p className="section-label">Bill Details</p>
          <div className="bill-card">
            <div className="bill-row"><span>Veg Thali × 1</span><span>₹60.00</span></div>
            <div className="bill-row"><span>Sandwich × 1</span><span>₹30.00</span></div>
            <div className="bill-row"><span>Sub Total</span><span>₹90.00</span></div>
            <div className="bill-row discount"><span>Coupon Discount (CAMPUS10)</span><span>−₹9.00</span></div>
            <div className="bill-divider"></div>
            <div className="bill-row total"><span>Total</span><span>₹81.00</span></div>
            <div className="bill-row"><span>Token No.</span><span className="token-ref">#14</span></div>
          </div>

          <button className="btn-primary full-width" style={{marginTop: '16px'}}>Place Order & Pay</button>
          <button className="btn-secondary full-width" style={{marginTop: '10px'}}>Download Receipt</button>
        </div>
      </div>

      {/*  ░░░░ SCREEN: EVENTS & CLUBS ░░░░  */}
      <div className="screen" id="screen-events">
        <div className="screen-header">
          <button className="back-btn" onClick={() => window.goBack()}><ArrowLeft size={20} /></button>
          <h2 className="screen-title">Events & Clubs</h2>
          <div></div>
        </div>
        <div className="screen-scroll has-header">
          <div className="tab-bar">
            <button className="tab active" data-tab="tab-events">Events</button>
            <button className="tab" data-tab="tab-clubs">Clubs</button>
            <button className="tab" data-tab="tab-certs">Certificates</button>
          </div>

          {/*  Events Tab  */}
          <div className="tab-content active" id="tab-events">
            <div className="event-card featured">
              <div className="event-badge"><Flame size={18} /> Featured</div>
              <h3 className="event-title">Hackathon 2026</h3>
              <p className="event-meta"><Calendar size={18} /> Mar 20–21 &middot; <MapPin size={18} /> Main
                Hall &middot; <Trophy size={18} /> ₹50,000 prize</p>
              <p className="event-desc">Build innovative solutions for campus problems in 24 hours.</p>
              <div style={{display: 'flex', gap: '8px', marginTop: '12px'}}>
                <button className="btn-primary" style={{flex: '1'}}>Register Now</button>
                <button className="btn-secondary" style={{width: '44px'}}><Bell size={18} /></button>
              </div>
            </div>

            <div className="event-list">
              <div className="event-mini">
                <div className="event-date-block"><span className="ed-day">15</span><span className="ed-mon">MAR</span></div>
                <div className="event-mini-body">
                  <p className="event-mini-title">Tech Talk: AI in Healthcare</p>
                  <p className="event-mini-sub">Seminar Hall · 2:00 PM · Free</p>
                </div>
                <button className="event-reg-btn">Join</button>
              </div>
              <div className="event-mini">
                <div className="event-date-block"><span className="ed-day">17</span><span className="ed-mon">MAR</span></div>
                <div className="event-mini-body">
                  <p className="event-mini-title">Sports Day Registration</p>
                  <p className="event-mini-sub">Ground · All Day</p>
                </div>
                <button className="event-reg-btn">Join</button>
              </div>
              <div className="event-mini">
                <div className="event-date-block"><span className="ed-day">22</span><span className="ed-mon">MAR</span></div>
                <div className="event-mini-body">
                  <p className="event-mini-title">Photography Workshop</p>
                  <p className="event-mini-sub">Art Room · 3:00 PM</p>
                </div>
                <button className="event-reg-btn registered">Joined <Check size={16} style={{display: "inline", verticalAlign: "middle"}} /></button>
              </div>
            </div>
          </div>

          {/*  Clubs Tab  */}
          <div className="tab-content" id="tab-clubs">
            <div className="clubs-grid">
              <div className="club-card">
                <div className="club-icon"><Code2 size={18} /></div>
                <p className="club-name">Coding Club</p>
                <p className="club-mem">142 members</p>
                <button className="club-join joined">Joined</button>
              </div>
              <div className="club-card">
                <div className="club-icon"><Camera size={18} /></div>
                <p className="club-name">Photography</p>
                <p className="club-mem">87 members</p>
                <button className="club-join">Join</button>
              </div>
              <div className="club-card">
                <div className="club-icon"><Theater size={18} /></div>
                <p className="club-name">Drama Club</p>
                <p className="club-mem">63 members</p>
                <button className="club-join">Join</button>
              </div>
              <div className="club-card">
                <div className="club-icon"><Brain size={18} /></div>
                <p className="club-name">Chess Club</p>
                <p className="club-mem">45 members</p>
                <button className="club-join">Join</button>
              </div>
            </div>
          </div>

          {/*  Certificates Tab  */}
          <div className="tab-content" id="tab-certs">
            <div className="cert-list">
              <div className="cert-card">
                <div className="cert-icon"><Trophy size={18} /></div>
                <div className="cert-body">
                  <p className="cert-title">1st Place – Hackathon 2025</p>
                  <p className="cert-sub">Issued: Dec 10, 2025</p>
                </div>
                <button className="dl-btn"><Download size={18} /></button>
              </div>
              <div className="cert-card">
                <div className="cert-icon"><Scroll size={18} /></div>
                <div className="cert-body">
                  <p className="cert-title">Workshop: React.js Fundamentals</p>
                  <p className="cert-sub">Issued: Jan 5, 2026</p>
                </div>
                <button className="dl-btn"><Download size={18} /></button>
              </div>
              <div className="cert-card">
                <div className="cert-icon"><Medal size={18} /></div>
                <div className="cert-body">
                  <p className="cert-title">Coding Club – Active Member</p>
                  <p className="cert-sub">Issued: Feb 14, 2026</p>
                </div>
                <button className="dl-btn"><Download size={18} /></button>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/*  ░░░░ SCREEN: LOST & FOUND ░░░░  */}
      <div className="screen" id="screen-lost-found">
        <div className="screen-header">
          <button className="back-btn" onClick={() => window.goBack()}><ArrowLeft size={20} /></button>
          <h2 className="screen-title">Lost & Found</h2>
          <div></div>
        </div>
        <div className="screen-scroll has-header">
          <div className="lf-action-row">
            <button className="lf-action-btn red"><Upload size={18} /> Report Lost</button>
            <button className="lf-action-btn green"><Download size={18} /> Report Found</button>
          </div>

          {/*  Report Form (partially shown)  */}
          <p className="section-label">Post an Item</p>
          <div className="form-card">
            <div className="lf-type-toggle">
              <button className="lft active">Lost</button>
              <button className="lft">Found</button>
            </div>
            <div className="form-group">
              <label className="form-label">Item Name</label>
              <input className="form-input" placeholder="e.g. Blue Water Bottle" />
            </div>
            <div className="form-group">
              <label className="form-label">Location</label>
              <input className="form-input" placeholder="e.g. Library, 1st Floor" />
            </div>
            <div className="form-group">
              <label className="form-label">Upload Photo</label>
              <div className="upload-box">
                <span><Camera size={18} /> Tap to add photo</span>
              </div>
            </div>
            <button className="btn-primary full-width">Post Item</button>
          </div>

          {/*  Active listings  */}
          <p className="section-label">Recent Listings</p>
          <div className="lf-list">
            <div className="lf-item">
              <div className="lf-img lost-tag">LOST</div>
              <div className="lf-body">
                <p className="lf-title">Blue Water Bottle</p>
                <p className="lf-sub"><MapPin size={18} /> Near Classroom 302 · 2h ago</p>
              </div>
              <button className="claim-btn">Claim</button>
            </div>
            <div className="lf-item">
              <div className="lf-img found-tag">FOUND</div>
              <div className="lf-body">
                <p className="lf-title">Student ID Card</p>
                <p className="lf-sub"><MapPin size={18} /> Library Entrance · 5h ago</p>
              </div>
              <button className="claim-btn">Claim</button>
            </div>
            <div className="lf-item">
              <div className="lf-img lost-tag">LOST</div>
              <div className="lf-body">
                <p className="lf-title">Black Earphones</p>
                <p className="lf-sub"><MapPin size={18} /> Canteen Area · Yesterday</p>
              </div>
              <button className="claim-btn">Claim</button>
            </div>
          </div>
        </div>
      </div>

      {/*  ░░░░ SCREEN: FEEDBACK ░░░░  */}
      <div className="screen" id="screen-feedback">
        <div className="screen-header">
          <button className="back-btn" onClick={() => window.goBack()}><ArrowLeft size={20} /></button>
          <h2 className="screen-title">Campus Feedback</h2>
          <div></div>
        </div>
        <div className="screen-scroll has-header">
          <div className="feedback-categories">
            <div className="fb-cat active"><Utensils size={18} /><span>Canteen</span></div>
            <div className="fb-cat"><Landmark size={18} /><span>Library</span></div>
            <div className="fb-cat"><Building2 size={18} /><span>Infrastructure</span></div>
            <div className="fb-cat"><BookOpen size={18} /><span>Academics</span></div>
          </div>

          <div className="form-card">
            <p className="form-label" style={{marginBottom: '8px'}}>Rate your experience</p>
            <div className="star-row">
              <span className="star active"><Star fill="currentColor" size={20} strokeWidth={1} /></span>
              <span className="star active"><Star fill="currentColor" size={20} strokeWidth={1} /></span>
              <span className="star active"><Star fill="currentColor" size={20} strokeWidth={1} /></span>
              <span className="star active"><Star fill="currentColor" size={20} strokeWidth={1} /></span>
              <span className="star"><Star fill="currentColor" size={20} strokeWidth={1} /></span>
            </div>

            <div className="form-group" style={{marginTop: '16px'}}>
              <label className="form-label">Your Feedback</label>
              <textarea className="form-input" rows="4" placeholder="Describe your experience..."></textarea>
            </div>

            <div className="form-group">
              <label className="form-label">Attach Photo (optional)</label>
              <div className="upload-box"><span><Image size={18} /> Add photo</span></div>
            </div>

            <div className="anon-toggle">
              <label className="anon-label">Submit Anonymously</label>
              <div className="toggle active"></div>
            </div>

            <button className="btn-primary full-width">Submit Feedback</button>
          </div>

          <p className="section-label">My Past Feedback</p>
          <div className="list-cards">
            <div className="list-card">
              <div className="lc-left">
                <div className="lc-icon"><Utensils size={18} /></div>
                <div>
                  <p className="lc-title">Canteen Feedback</p>
                  <p className="lc-sub">★★★★☆ · Mar 8 · Anonymous</p>
                </div>
              </div>
              <div className="score-pill green">Reviewed</div>
            </div>
            <div className="list-card">
              <div className="lc-left">
                <div className="lc-icon"><Landmark size={18} /></div>
                <div>
                  <p className="lc-title">Library Feedback</p>
                  <p className="lc-sub">★★★☆☆ · Feb 20</p>
                </div>
              </div>
              <div className="score-pill yellow">Pending</div>
            </div>
          </div>
        </div>
      </div>

      {/*  ░░░░ SCREEN: FORMS & SURVEYS ░░░░  */}
      <div className="screen" id="screen-forms">
        <div className="screen-header">
          <button className="back-btn" onClick={() => window.goBack()}><ArrowLeft size={20} /></button>
          <h2 className="screen-title">Forms & Surveys</h2>
          <div></div>
        </div>
        <div className="screen-scroll has-header">
          <p className="section-label">Active Forms</p>
          <div className="form-list">
            <div className="form-list-item urgent">
              <div className="fli-left">
                <div className="fli-icon"><ClipboardList size={18} /></div>
                <div>
                  <p className="fli-title">Hackathon Registration 2026</p>
                  <p className="fli-sub">Closes: Mar 18 · 2:00 PM</p>
                </div>
              </div>
              <button className="fli-btn">Fill</button>
            </div>
            <div className="form-list-item">
              <div className="fli-left">
                <div className="fli-icon"><BarChart2 size={18} /></div>
                <div>
                  <p className="fli-title">Semester Feedback Survey</p>
                  <p className="fli-sub">Closes: Mar 25</p>
                </div>
              </div>
              <button className="fli-btn">Fill</button>
            </div>
            <div className="form-list-item done">
              <div className="fli-left">
                <div className="fli-icon"><CheckCircle size={18} /></div>
                <div>
                  <p className="fli-title">Coding Club Application</p>
                  <p className="fli-sub">Submitted: Mar 5</p>
                </div>
              </div>
              <button className="fli-btn done-btn">Done</button>
            </div>
            <div className="form-list-item">
              <div className="fli-left">
                <div className="fli-icon"><GraduationCap size={18} /></div>
                <div>
                  <p className="fli-title">Scholarship Application</p>
                  <p className="fli-sub">Closes: Apr 1</p>
                </div>
              </div>
              <button className="fli-btn">Fill</button>
            </div>
          </div>
        </div>
      </div>

      {/*  ░░░░ SCREEN: NOTIFICATIONS ░░░░  */}
      <div className="screen" id="screen-notifications">
        <div className="screen-header">
          <button className="back-btn" onClick={() => window.goBack()}><ArrowLeft size={20} /></button>
          <h2 className="screen-title">Notifications</h2>
          <button className="icon-btn" style={{fontSize: '12px', color: '#888'}}>Clear all</button>
        </div>
        <div className="screen-scroll has-header">
          <p className="section-label">Today</p>
          <div className="notif-full-list">
            <div className="nf-item unread red">
              <div className="nf-icon"><FileText size={18} /></div>
              <div className="nf-body">
                <p className="nf-title">Assignment Due Tomorrow!</p>
                <p className="nf-desc">OS Assignment 3 is due by 11:59 PM tomorrow. Submit on time.</p>
                <p className="nf-time">2 minutes ago</p>
              </div>
            </div>
            <div className="nf-item unread yellow">
              <div className="nf-icon"><Utensils size={18} /></div>
              <div className="nf-body">
                <p className="nf-title">Canteen Order Ready</p>
                <p className="nf-desc">Token #14 is ready for pickup at Counter 2.</p>
                <p className="nf-time">15 minutes ago</p>
              </div>
            </div>
            <div className="nf-item unread blue">
              <div className="nf-icon"><CalendarDays size={18} /></div>
              <div className="nf-body">
                <p className="nf-title">Hackathon 2026 – Register Now</p>
                <p className="nf-desc">Registration closes March 18. Don't miss out on ₹50,000 prize!</p>
                <p className="nf-time">1 hour ago</p>
              </div>
            </div>
          </div>

          <p className="section-label">Yesterday</p>
          <div className="notif-full-list">
            <div className="nf-item">
              <div className="nf-icon"><BookOpen size={18} /></div>
              <div className="nf-body">
                <p className="nf-title">New Notes Uploaded</p>
                <p className="nf-desc">Prof. Singh uploaded Unit 4 notes for OS.</p>
                <p className="nf-time">Yesterday, 4:30 PM</p>
              </div>
            </div>
            <div className="nf-item">
              <div className="nf-icon"><TrainFront size={18} /></div>
              <div className="nf-body">
                <p className="nf-title">Train Pass Approved</p>
                <p className="nf-desc">Your railway concession pass has been approved and is ready to download.</p>
                <p className="nf-time">Yesterday, 11:00 AM</p>
              </div>
            </div>
            <div className="nf-item">
              <div className="nf-icon"><Book size={18} /></div>
              <div className="nf-body">
                <p className="nf-title">Book Return Reminder</p>
                <p className="nf-desc">Operating System Concepts is due in 9 days.</p>
                <p className="nf-time">Yesterday, 9:00 AM</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/*  ─── BOTTOM NAV ───  */}
      <nav className="bottom-nav">
        <button className="nav-btn active" onClick={() => window.navigate('screen-home')} id="nav-home">
          <div className="nav-icon"><Home size={18} /></div>
          <span>Home</span>
        </button>
        <button className="nav-btn" onClick={() => window.navigate('screen-academic')} id="nav-academic">
          <div className="nav-icon"><BookOpen size={18} /></div>
          <span>Academics</span>
        </button>
        <button className="nav-btn" onClick={() => window.navigate('screen-canteen')} id="nav-canteen">
          <div className="nav-icon"><Utensils size={18} /></div>
          <span>Canteen</span>
        </button>
        <button className="nav-btn" onClick={() => window.navigate('screen-events')} id="nav-events">
          <div className="nav-icon"><CalendarDays size={18} /></div>
          <span>Events</span>
        </button>
        <button className="nav-btn" onClick={() => window.navigate('screen-notifications')} id="nav-notifs">
          <div className="nav-icon"><Bell size={18} /></div>
          <span>Alerts</span>
        </button>
      </nav>

      {/*  FAB for extra modules  */}
      <button className="fab-toggle" id="fabToggle" onClick={() => window.toggleExtraNav()} title="More Modules"><Menu size={24} /></button>

      {/*  Floating menu for extra screens  */}
      <div className="floating-menu" id="extra-nav">
        <button onClick={() => { window.navigate('screen-materials'); window.toggleExtraNav(); }}><BookOpen size={18} /> Study
          Materials</button>
        <button onClick={() => { window.navigate('screen-library'); window.toggleExtraNav(); }}><Landmark size={18} /> Library</button>
        <button onClick={() => { window.navigate('screen-concession'); window.toggleExtraNav(); }}><TrainFront size={18} /> Train
          Pass</button>
        <button onClick={() => { window.navigate('screen-digital-id'); window.toggleExtraNav(); }}><IdCard size={18} /> Digital
          ID</button>
        <button onClick={() => { window.navigate('screen-lost-found'); window.toggleExtraNav(); }}><Search size={18} /> Lost &amp;
          Found</button>
        <button onClick={() => { window.navigate('screen-feedback'); window.toggleExtraNav(); }}><MessageCircle size={18} />
          Feedback</button>
        <button onClick={() => { window.navigate('screen-forms'); window.toggleExtraNav(); }}><ClipboardList size={18} /> Forms</button>
      </div>

    </div>{/*  /app-container  */}
    </div>{/*  /phone-frame  */}

    </>
  );
}
