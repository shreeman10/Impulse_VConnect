import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    text = f.read()

coupon_section = r'<input className="coupon-input" placeholder="Enter coupon code" value="CAMPUS10" />\s*<button className="coupon-apply active-coupon">Applied <Check size=\{16\} style=\{\{display: "inline",\s*verticalAlign: "middle"\}\} /></button>\s*</div>\s*<div className="coupon-applied-card">\s*<div className="coupon-icon"><Gift size=\{18\} /></div>\s*<div>\s*<p className="coupon-name">CAMPUS10 – 10% Off</p>\s*<p className="coupon-sub">Student discount applied</p>\s*</div>\s*<p className="coupon-save">−₹8\.50</p>\s*</div>'

coupon_dynamic = """<input className="coupon-input" placeholder="Enter coupon code (CAMPUS10)" value={coupon} onChange={(e) => setCoupon(e.target.value)} />
            <button className={`coupon-apply ${discount > 0 ? "active-coupon" : ""}`} onClick={handleCoupon}>
              {discount > 0 ? <>Applied <Check size={16} style={{display: "inline", verticalAlign: "middle"}} /></> : "Apply"}
            </button>
          </div>
          {discount > 0 && (
            <div className="coupon-applied-card">
              <div className="coupon-icon"><Gift size={18} /></div>
              <div>
                <p className="coupon-name">CAMPUS10 – 10% Off</p>
                <p className="coupon-sub">Student discount applied</p>
              </div>
              <p className="coupon-save">−₹{(cartTotal * discount).toFixed(2)}</p>
            </div>
          )}"""

text = re.sub(coupon_section, coupon_dynamic, text, flags=re.DOTALL)


bill_section = r'<div className="bill-card">.*?<div className="bill-row"><span>Veg Thali × 1</span><span>₹60\.00</span></div>.*?<div className="bill-row total"><span>Total</span><span>₹81\.00</span></div>\s*<div className="bill-row"><span>Token No\.</span><span className="token-ref">#14</span></div>\s*</div>'

bill_dynamic = """<div className="bill-card">
            {cart.map((item, idx) => (
              <div className="bill-row" key={idx}><span>{item.name} x 1</span><span>₹{item.price.toFixed(2)}</span></div>
            ))}
            
            <div className="bill-row"><span>Sub Total</span><span>₹{cartTotal.toFixed(2)}</span></div>
            {discount > 0 && (
              <div className="bill-row discount"><span>Coupon Discount</span><span>−₹{(cartTotal * discount).toFixed(2)}</span></div>  
            )}
            <div className="bill-divider"></div>
            <div className="bill-row total"><span>Total</span><span>₹{cartFinal.toFixed(2)}</span></div>
            <div className="bill-row"><span>Token No.</span><span className="token-ref">#14</span></div>
          </div>"""

text = re.sub(bill_section, bill_dynamic, text, flags=re.DOTALL)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("Phase 3 complete")
