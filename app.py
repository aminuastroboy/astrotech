import streamlit as st
import pandas as pd
import os, time
from datetime import datetime

# =========================
# Page config
# =========================
st.set_page_config(page_title="ASTROTECH • Services", page_icon="🚀", layout="wide")

# =========================
# Theme CSS (neon + stars + cards + inputs + chat)
# =========================
st.markdown(
    """
    <style>
    /* App background */
    body, .stApp {
      background: radial-gradient(circle at 20% -10%, #162058, #0d0d2b 60%, #090919 100%);
      color: #fff;
    }

    /* Star field */
    .stApp::before{
      content:"";
      position:fixed; inset: -25% -25% -25% -25%;
      background:
        radial-gradient(#ffffff88, transparent 70%) 10% 20%/2px 2px,
        radial-gradient(#ffffff55, transparent 70%) 30% 80%/2px 2px,
        radial-gradient(#55ffff88, transparent 70%) 70% 40%/2px 2px,
        radial-gradient(#ffffff55, transparent 70%) 90% 10%/2px 2px,
        radial-gradient(#55aaff88, transparent 70%) 50% 60%/2px 2px;
      animation: drift 60s linear infinite;
      pointer-events:none; z-index:-1;
    }
    @keyframes drift { from{transform:translateY(0)} to{transform:translateY(-120px)} }

    /* Headings glow */
    h1,h2,h3{ text-shadow:0 0 10px #00ffffaa, 0 0 22px #0066ff88; }

    /* Service cards */
    .service-card{
      background:rgba(16,22,70,.85); border-radius:20px; padding:20px; margin:10px 0;
      box-shadow:0 0 18px #00ffff33; border:1px solid #00ffff33;
      transition:transform .25s ease, box-shadow .25s ease
    }
    .service-card:hover{ transform:translateY(-3px); box-shadow:0 0 30px #00ffff88 }

    /* Pulsing emoji icons */
    .pulse{ display:inline-block; filter:drop-shadow(0 0 8px #00ffff); animation:pulse 2.2s ease-in-out infinite }
    @keyframes pulse{ 0%,100%{ transform:scale(1) } 50%{ transform:scale(1.12) } }

    /* Inputs */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div{
      background:#0e133d; color:#fff; border:2px solid #00ffff; border-radius:12px;
      box-shadow:0 0 12px #00ffff66 inset;
    }
    .stTextInput input:focus, .stTextArea textarea:focus, .stSelectbox div[data-baseweb="select"]:focus-within{
      border-color:#ff66ff; box-shadow:0 0 16px #ff66ff99 inset;
      outline:none;
    }

    /* Submit button */
    .stForm button{
      background:linear-gradient(90deg,#00ffff,#0066ff); color:#fff; border:none; font-weight:700;
      padding:14px 34px; border-radius:26px; box-shadow:0 0 24px #00ffff88; transition:transform .2s, box-shadow .2s
    }
    .stForm button:hover{ transform:scale(1.06); box-shadow:0 0 42px #00ffffff }

    /* Floating chat FAB */
    .chat-fab{ position:fixed; right:22px; bottom:22px; z-index:9999; width:58px; height:58px;
      display:flex; align-items:center; justify-content:center; border-radius:50%;
      background:linear-gradient(135deg,#00ffff,#6a00ff); color:#fff; text-decoration:none; font-size:26px;
      box-shadow:0 0 24px #00ffff99; border:1px solid #00ffff55 }
    .chat-fab:hover{ box-shadow:0 0 42px #8a2be2 }

    /* Chat window */
    .chat-window{ position:fixed; right:22px; bottom:90px; width:360px; max-width:92vw; background:#0f1547ee;
      border:1px solid #00ffff55; border-radius:16px; box-shadow:0 0 30px #00ffff66; padding:14px; z-index:9998 }
    .chat-close{ position:absolute; right:10px; top:8px; color:#fff; text-decoration:none; font-weight:700 }
    .chat-header{ font-weight:800; color:#00ffff; margin-bottom:6px }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================
# Data/setup
# =========================
SERVICES = [
    ("🌐", "Social Media Account Recovery", "Recover hacked or locked accounts (Facebook, Instagram, X/Twitter, TikTok, etc.)."),
    ("✉️", "Gmail & Email Support",        "Fix login issues, recover accounts, and secure your emails."),
    ("📱", "Mobile Phone Repairs",         "Troubleshooting, unlocking, updates, and performance optimization."),
    ("🛠️", "Tech Support",                 "General IT assistance, error fixes, and system optimization."),
    ("✨", "Custom Requests",               "Have another issue? We’ve got you covered."),
]

requests_path = os.path.join("data", "requests.csv")
os.makedirs("data", exist_ok=True)
if not os.path.exists(requests_path):
    pd.DataFrame(columns=["timestamp","name","email","service","details"]).to_csv(requests_path, index=False)

# =========================
# Hero / header
# =========================
st.markdown(
    """
    <div style='text-align:center; padding:60px 10px;'>
      <h1 style='color:#00ffff; font-size:64px; margin:0'>ASTROTECH</h1>
      <h3 style='color:#ff8cff; margin-top:6px'>Reliable Digital & Tech Solutions</h3>
      <p style='color:#cfd3ff; max-width:760px; margin:10px auto 0'>
        Exploring the digital universe with cutting-edge solutions. We fix accounts, phones, and provide expert IT support.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================
# Services grid
# =========================
st.subheader("🌌 Our Galactic Services")
cols = st.columns(2)
for i, (icon, title, desc) in enumerate(SERVICES):
    with cols[i % 2]:
        st.markdown(
            f"""
            <div class='service-card'>
              <div style='display:flex; gap:12px; align-items:flex-start;'>
                <div class='pulse' style='font-size:28px'>{icon}</div>
                <div>
                  <h3 style='color:#00ffff; margin:0'>{title}</h3>
                  <p style='margin:.25rem 0 0'>{desc}</p>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("---")

# =========================
# Request form + cosmic loader
# =========================
st.subheader("📝 Send Us a Transmission")
with st.form("request_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    service = st.selectbox("Select Service", [s[1] for s in SERVICES])
    details = st.text_area("Describe Your Issue")
    submit = st.form_submit_button("🚀 Submit Request")

    if submit:
        with st.spinner("Launching to Mission Control…"):
            time.sleep(1.2)
        now = datetime.now().isoformat(timespec="seconds")
        row = {"timestamp": now, "name": name, "email": email, "service": service, "details": details}
        try:
            df = pd.read_csv(requests_path)
            df.loc[len(df)] = row
            df.to_csv(requests_path, index=False)
            st.success(f"🛸 Transmission received, {name}! We'll contact you at {email}.")
        except Exception as e:
            st.error("Could not save your request locally. (This may happen on certain hosts.)")
            st.info(str(e))

st.caption("Note: Requests are stored in ./data/requests.csv on the server.")

# =========================
# Simple AstroBot (FAQ) — floating
# =========================
# Toggle chat using a query param
params = st.query_params
chat_open = params.get("chat", [""]) != [""]

# Floating FAB link to toggle chat
if not chat_open:
    st.markdown("<a class='chat-fab' href='?chat=open'>🤖</a>", unsafe_allow_html=True)
else:
    st.markdown(
        """
        <div class='chat-window'>
          <a class='chat-close' href='?'>✕</a>
          <div class='chat-header'>AstroBot</div>
          <div style='font-size:13px; color:#cfe6ff'>Ask about services, pricing, or how to start a recovery. Keep messages short & sweet 🌠</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Chat history
    if "msgs" not in st.session_state:
        st.session_state.msgs = []

    for role, content in st.session_state.msgs:
        with st.chat_message(role):
            st.write(content)

    prompt = st.chat_input("Type a message for AstroBot…")
    if prompt:
        st.session_state.msgs.append(("user", prompt))
        with st.chat_message("user"):
            st.write(prompt)

        # Simple FAQ responses
        low = prompt.lower()
        if "price" in low or "cost" in low:
            reply = "Pricing varies by issue. 🚀 Social recovery from ₦5k, Gmail support from ₦4k, phone software fixes from ₦6k. Get a quick quote via the form."
        elif "gmail" in low or "email" in low:
            reply = "For Gmail recovery: we verify ownership, secure the account, and set up 2FA. Typical turnaround: same day after details are confirmed."
        elif any(k in low for k in ["social", "facebook", "instagram", "tiktok", "twitter", "x "]):
            reply = "Social recovery mission 🛰️: share the handle, last access date, and issue details. We'll guide you through platform recovery steps securely."
        elif "phone" in low or "mobile" in low:
            reply = "Phone repairs 🔧: software resets, updates, optimization, and unlocking (where legal). We'll not bypass security without proof of ownership."
        elif any(k in low for k in ["contact", "office", "reach"]):
            reply = "Reach Mission Control: +234 906 669 9944 • astrotech.ng@gmail.com • Nigeria 🌍"
        else:
            reply = "I’m your cosmic helper! Ask about services, pricing, or send a service request via the form above. ✨"

        st.session_state.msgs.append(("assistant", reply))
        with st.chat_message("assistant"):
            st.write(reply)

# =========================
# Footer / contact
# =========================
st.markdown("---")
st.markdown(
    """
    ### 📡 Contact Mission Control
    - **Phone:** +234 906 669 9944  
    - **Email:** astrotech.ng@gmail.com  
    - **Location:** Nigeria 🌍
    """
)
