import streamlit as st
from datetime import datetime

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="ASTROTECH",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------------------------------
# CUSTOM CSS FOR STYLING + MOBILE RESPONSIVENESS
# ------------------------------------------------
st.markdown("""
<style>
/* General cosmic background */
.stApp {
    background: linear-gradient(180deg, #0f2027, #203a43, #2c5364);
    color: white;
    font-family: 'Trebuchet MS', sans-serif;
}

/* Prevent horizontal scroll */
body, .main, .block-container {
    max-width: 100% !important;
    overflow-x: hidden;
}

/* Service cards */
.service-card {
    padding: 1rem;
    border-radius: 1rem;
    background: rgba(255,255,255,0.08);
    text-align: center;
    margin-bottom: 1rem;
    transition: all 0.3s ease-in-out;
    box-shadow: 0 0 20px rgba(0, 191, 255, 0.2);
}
.service-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 30px rgba(0, 191, 255, 0.5);
}

/* FAB (AstroBot button) */
.fab {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    background: #0ff;
    border-radius: 50%;
    padding: 0.8rem 1rem;
    box-shadow: 0 0 20px rgba(0,255,255,0.6);
    cursor: pointer;
    z-index: 999;
    color: black;
    font-weight: bold;
}

/* Mobile adjustments */
@media (max-width: 768px) {
    h1, h2, h3 { font-size: 1.2rem !important; }
    .stButton button { font-size: 0.9rem !important; padding: 0.6rem 1rem; }
    input, textarea, select { font-size: 0.9rem !important; }
    .fab { bottom: 1rem !important; right: 1rem !important; transform: scale(0.85); }
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# HEADER
# ------------------------------------------------
st.title("🚀 ASTROTECH")
st.subheader("Fixing your digital universe 🌌")

# ------------------------------------------------
# SERVICES GRID
# ------------------------------------------------
services = {
    "📱 Phone Repairs": "We fix broken screens, battery issues, and more.",
    "📧 Gmail Recovery": "Lost access? We’ll help you recover your Gmail.",
    "🌐 Social Media Fixes": "Recover hacked or locked accounts.",
    "💻 Other Tech Support": "General troubleshooting for gadgets & devices."
}

cols = st.columns(2)  # switch to 2 columns for better mobile scaling

for idx, (title, desc) in enumerate(services.items()):
    with cols[idx % 2]:
        st.markdown(f"""
        <div class="service-card">
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------------
# SERVICE REQUEST FORM
# ------------------------------------------------
st.header("📝 Request a Service")

with st.form("service_form"):
    name = st.text_input("Your Name")
    service_type = st.selectbox("Choose Service", list(services.keys()))
    details = st.text_area("Describe the issue")
    submitted = st.form_submit_button("Submit Request")

if submitted:
    with open("data/requests.csv", "a") as f:
        f.write(f"{name},{service_type},{details},{datetime.now()}\n")
    st.success("✅ Your request has been submitted! We'll contact you soon.")

# ------------------------------------------------
# ASTROBOT FAB (Floating Button)
# ------------------------------------------------
st.markdown('<div class="fab">🤖</div>', unsafe_allow_html=True)

with st.expander("🤖 Chat with AstroBot"):
    user_input = st.text_input("Ask me anything about ASTROTECH:")
    if user_input:
        st.info(f"AstroBot: I hear you! You asked about '{user_input}'. Our team will get back to you 🚀")
