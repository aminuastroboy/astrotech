import streamlit as st

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="ASTROTECH",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------
# Custom CSS
# ---------------------------
st.markdown("""
<style>
/* Global page styling */
.stApp {
    background: linear-gradient(180deg, #0f2027, #203a43, #2c5364);
    color: white;
    font-family: 'Trebuchet MS', sans-serif;
}

/* Headings */
h1, h2, h3 {
    color: #0ff !important;
    font-weight: 700 !important;
}

/* Paragraphs and text */
p, label {
    font-size: 1rem !important;
    color: #fff !important;
}

/* Inputs & buttons */
input, textarea, select {
    border-radius: 8px;
    padding: 0.6rem;
    border: none;
    font-size: 1rem !important;
}
.stButton button {
    background: #0ff;
    color: black;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
    font-weight: bold;
    transition: 0.3s;
}
.stButton button:hover {
    background: #00cccc;
    color: white;
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

/* Floating AstroBot button */
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

/* Mobile responsive tweaks */
@media (max-width: 768px) {
    h1, h2, h3 { font-size: 1.2rem !important; }
    .stButton button { font-size: 0.9rem !important; padding: 0.5rem 1rem; }
    input, textarea, select { font-size: 0.9rem !important; }
    .fab { bottom: 1rem !important; right: 1rem !important; transform: scale(0.85); }
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Header
# ---------------------------
st.markdown("<h1 style='text-align: center;'>🚀 Welcome to ASTROTECH 🌌</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Your one-stop solution for fixing accounts, mobile phones & more.</p>", unsafe_allow_html=True)

# ---------------------------
# Services Section
# ---------------------------
st.subheader("🔧 Our Services")

services = {
    "🔑 Social Media Account Recovery": "Get back into your locked or hacked accounts.",
    "📧 Gmail & Email Fix": "Resolve login, recovery, and setup issues quickly.",
    "📱 Mobile Phone Repair": "From software issues to setup assistance.",
    "🛠 Other Tech Support": "General fixes for your digital life."
}

cols = st.columns(2)  # two columns for desktop, collapses on mobile
for index, (title, desc) in enumerate(services.items()):
    with cols[index % 2]:
        st.markdown(f"""
        <div class="service-card">
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------
# Contact Form
# ---------------------------
st.subheader("📩 Contact Us")

with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    issue = st.text_area("Describe Your Issue")
    submitted = st.form_submit_button("Send Message")
    if submitted:
        if name and email and issue:
            st.success("✅ Thank you! We'll get back to you soon.")
        else:
            st.error("⚠️ Please fill out all fields.")

# ---------------------------
# Floating AstroBot Button
# ---------------------------
st.markdown("""
<div class="fab">🤖</div>
""", unsafe_allow_html=True)
