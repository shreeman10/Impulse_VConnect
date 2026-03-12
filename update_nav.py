import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add Hamburger Menu to Top Left Header (in screen-home header)
home_header_regex = r'<div className="home-header">\s*<div>'
home_header_replacement = """<div className="home-header" style={{ position: 'relative' }}>
            <button className="fab-toggle-top" id="fabToggleHome" onClick={() => window.toggleExtraNav()} style={{ background: 'transparent', border: 'none', color: '#fff', padding: '0 10px 0 0', cursor: 'pointer', display: 'flex', alignItems: 'center' }} title="Menu">
              <Menu size={28} />
            </button>
            <div>"""
text = re.sub(home_header_regex, home_header_replacement, text)


# 2. Modify Bottom Nav to have exactly 3 icons: Study Materials, Home, Alerts
bottom_nav_regex = r'<nav className="bottom-nav">.*?</nav>'
bottom_nav_replacement = """<nav className="bottom-nav">
        <button className="nav-btn" onClick={() => window.navigate('screen-materials')} id="nav-materials">
          <div className="nav-icon"><BookOpen size={18} /></div>
          <span>Materials</span>
        </button>
        <button className="nav-btn active" onClick={() => window.navigate('screen-home')} id="nav-home">
          <div className="nav-icon"><Home size={18} /></div>
          <span>Home</span>
        </button>
        <button className="nav-btn" onClick={() => window.navigate('screen-notifications')} id="nav-notifs">
          <div className="nav-icon"><Bell size={18} /></div>
          <span>Alerts</span>
        </button>
      </nav>"""
text = re.sub(bottom_nav_regex, bottom_nav_replacement, text, flags=re.DOTALL)


# 3. Restructure Floating Menu items to contain Academics, Canteen, Events since they were removed from nav
floating_menu_regex = r'<div className="floating-menu" id="extra-nav">.*?</div>\s*</div>\{\/\*  /app-container'
floating_menu_replacement = """<div className="floating-menu" id="extra-nav">
        <button onClick={() => { window.navigate('screen-academic'); window.toggleExtraNav(); }}><BookOpen size={18} /> Academics</button>
        <button onClick={() => { window.navigate('screen-canteen'); window.toggleExtraNav(); }}><Utensils size={18} /> Canteen</button>
        <button onClick={() => { window.navigate('screen-events'); window.toggleExtraNav(); }}><CalendarDays size={18} /> Events</button>
        <button onClick={() => { window.navigate('screen-library'); window.toggleExtraNav(); }}><Landmark size={18} /> Library</button>
        <button onClick={() => { window.navigate('screen-concession'); window.toggleExtraNav(); }}><TrainFront size={18} /> Train Pass</button>
        <button onClick={() => { window.navigate('screen-digital-id'); window.toggleExtraNav(); }}><IdCard size={18} /> Digital ID</button>
        <button onClick={() => { window.navigate('screen-lost-found'); window.toggleExtraNav(); }}><Search size={18} /> Lost &amp; Found</button>
        <button onClick={() => { window.navigate('screen-feedback'); window.toggleExtraNav(); }}><MessageCircle size={18} /> Feedback</button>
        <button onClick={() => { window.navigate('screen-forms'); window.toggleExtraNav(); }}><ClipboardList size={18} /> Forms</button>
      </div>

    </div>{/*  /app-container"""
text = re.sub(floating_menu_regex, floating_menu_replacement, text, flags=re.DOTALL)

# 4. Remove floating FAB circle
fab_regex = r'\{\/\*  FAB for extra modules  \*\/\}\s*<button className="fab-toggle" id="fabToggle" onClick=\{\(\) => window\.toggleExtraNav\(\)\}    \s*title="More Modules"><Menu size=\{24\} /></button>'
text = re.sub(fab_regex, '', text)


with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("Nav refactored.")
