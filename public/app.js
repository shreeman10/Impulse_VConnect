// ═══════════════════════════════════════════════
//   CampusOne — Navigation & Interactivity
// ═══════════════════════════════════════════════

// Initialize Lucide icons
document.addEventListener('DOMContentLoaded', () => {
  if (typeof lucide !== 'undefined') lucide.createIcons();
});

var screenHistory = ['screen-home'];
var currentScreen = 'screen-home';

function navigate(screenId) {
  const prev = document.getElementById(currentScreen);
  const next = document.getElementById(screenId);
  if (!next || screenId === currentScreen) return;

  if (prev) prev.classList.remove('active');
  next.classList.add('active');

  if (screenId !== screenHistory[screenHistory.length - 1]) {
    screenHistory.push(screenId);
  }
  currentScreen = screenId;

  updateNavBar(screenId);
}

function goBack() {
  if (screenHistory.length <= 1) return;
  screenHistory.pop();
  const prev = screenHistory[screenHistory.length - 1];
  navigate(prev);
  // correct history after navigate adds it again
  if (screenHistory[screenHistory.length - 1] === prev && screenHistory[screenHistory.length - 2] === prev) {
    screenHistory.pop();
  }
}

function updateNavBar(screenId) {
  const map = {
    'screen-home': 'nav-home',
    'screen-academic': 'nav-academic',
    'screen-canteen': 'nav-canteen',
    'screen-canteen-bill': 'nav-canteen',
    'screen-events': 'nav-events',
    'screen-notifications': 'nav-notifs',
  };
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  const navId = map[screenId];
  if (navId) document.getElementById(navId)?.classList.add('active');
}

// ── TAB SWITCHING ──
document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    const targetTab = tab.dataset.tab;
    const container = tab.closest('.screen-scroll') || tab.closest('.screen');
   
    // Deactivate all tabs and tab-contents in this screen
    container.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    container.querySelectorAll('.tab-content').forEach(tc => tc.classList.remove('active'));
   
    tab.classList.add('active');
    const content = document.getElementById(targetTab);
    if (content) content.classList.add('active');
  });
});

// ── MENU TABS (Canteen) ──
document.querySelectorAll('.menu-tab').forEach(tab => {
  tab.addEventListener('click', () => {
    tab.closest('.screen').querySelectorAll('.menu-tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
  });
});

// ── SUBJECT CHIPS ──
document.querySelectorAll('.schip').forEach(chip => {
  chip.addEventListener('click', () => {
    chip.closest('.subject-chips').querySelectorAll('.schip').forEach(c => c.classList.remove('active'));
    chip.classList.add('active');
  });
});

// ── FEEDBACK CATEGORIES ──
document.querySelectorAll('.fb-cat').forEach(cat => {
  cat.addEventListener('click', () => {
    cat.closest('.feedback-categories').querySelectorAll('.fb-cat').forEach(c => c.classList.remove('active'));
    cat.classList.add('active');
  });
});

// ── STAR RATING ──
document.querySelectorAll('.star-row').forEach(row => {
  const stars = row.querySelectorAll('.star');
  stars.forEach((star, i) => {
    star.addEventListener('click', () => {
      stars.forEach((s, j) => {
        s.classList.toggle('active', j <= i);
      });
    });
  });
});

// ── TOGGLE ──
document.querySelectorAll('.toggle').forEach(toggle => {
  toggle.addEventListener('click', () => toggle.classList.toggle('active'));
});

// ── L&F Toggle ──
document.querySelectorAll('.lft').forEach(btn => {
  btn.addEventListener('click', () => {
    btn.closest('.lf-type-toggle').querySelectorAll('.lft').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  });
});

// ── Add to Cart (simple counter) ──
var cartCount = 2;
var cartTotal = 85;
var cartItems = {};
document.querySelectorAll('.add-btn').forEach((btn, i) => {
  const prices = [60, 55, 30, 15, 25, 20];
  btn.addEventListener('click', () => {
    cartCount++;
    cartTotal += prices[i] || 30;
    const countEl = document.querySelector('.cart-count');
    const priceEl = document.querySelector('.cart-price');
    if (countEl) countEl.textContent = `${cartCount} items`;
    if (priceEl) priceEl.textContent = `₹${cartTotal}`;
    btn.textContent = '✓';
    btn.style.background = '#4ade80';
    btn.style.color = '#000';
    setTimeout(() => { btn.textContent = '+'; btn.style.background = ''; btn.style.color = ''; }, 1200);
  });
});

// ── Countdown Timer (Daily Challenge) ──
function updateTimer() {
  const timerEl = document.querySelector('.timer-val');
  if (!timerEl) return;
  const now = new Date();
  const midnight = new Date();
  midnight.setHours(23, 59, 59, 999);
  const diff = midnight - now;
  const h = String(Math.floor(diff / 3600000)).padStart(2, '0');
  const m = String(Math.floor((diff % 3600000) / 60000)).padStart(2, '0');
  const s = String(Math.floor((diff % 60000) / 1000)).padStart(2, '0');
  timerEl.textContent = `${h}:${m}:${s}`;
}
setInterval(updateTimer, 1000);
updateTimer();

// ── Club Join Toggle ──
document.querySelectorAll('.club-join').forEach(btn => {
  btn.addEventListener('click', () => {
    if (btn.classList.contains('joined')) {
      btn.classList.remove('joined');
      btn.textContent = 'Join';
    } else {
      btn.classList.add('joined');
      btn.textContent = 'Joined';
    }
  });
});

// ── Event Register Toggle ──
document.querySelectorAll('.event-reg-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    if (btn.classList.contains('registered')) {
      btn.classList.remove('registered');
      btn.textContent = 'Join';
    } else {
      btn.classList.add('registered');
      btn.textContent = 'Joined ✓';
    }
  });
});

// ── Coupon Apply Toggle ──
document.querySelectorAll('.avail-label').forEach(lbl => {
  lbl.addEventListener('click', () => {
    alert('Coupon applied! (prototype interaction)');
  });
});

// ── FAB Extra Nav Toggle ──
function toggleExtraNav() {
  const menu = document.getElementById('extra-nav');
  const fab = document.getElementById('fabToggle');
  if (menu.classList.contains('open')) {
    menu.classList.remove('open');
    fab.textContent = '☰';
  } else {
    menu.classList.add('open');
    fab.textContent = '✕';
  }
}

// Close extra nav on outside click
document.addEventListener('click', (e) => {
  const menu = document.getElementById('extra-nav');
  const fab = document.getElementById('fabToggle');
  if (!menu.contains(e.target) && e.target !== fab) {
    menu.classList.remove('open');
    fab.textContent = '☰';
  }
});

console.log('🎓 CampusOne UI Loaded – Prototype Mode');
