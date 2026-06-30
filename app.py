import streamlit as st
import pandas as pd
import datetime

# Set crisp corporate canvas properties
st.set_page_config(
    page_title="BhooKavach (भू-कवच) | Sovereign Land Securities Infrastructure",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 💎 PREMIUM CUSTOM CSS CORPORATE INJECTION
# ==========================================
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* Clean System Reset */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #FAFAFA !important;
    }
    
    /* Thin Corporate Top Bar */
    .top-bar {
        border-bottom: 1px solid #E2E8F0;
        padding-bottom: 15px;
        margin-bottom: 35px;
    }
    .brand-title {
        font-size: 1.8rem;
        font-weight: 800;
        color: #0F4A28;
        letter-spacing: -0.02em;
        margin: 0;
    }
    .brand-tagline {
        font-size: 0.85rem;
        color: #64748B;
        margin-top: 2px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Narrative Container Grid Blocks */
    .narrative-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    .card-tag {
        font-size: 0.7rem;
        font-weight: 700;
        color: #16A34A;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 6px;
    }
    .card-heading {
        font-size: 1.4rem;
        font-weight: 700;
        color: #0F4A28;
        margin: 0 0 12px 0;
        letter-spacing: -0.01em;
    }
    .card-body {
        font-size: 0.95rem;
        color: #475569;
        line-height: 1.6;
        margin: 0;
    }
    
    /* Secure Gateway Waitlist Card Form */
    .gateway-box {
        background: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 10px 25px -5px rgba(15, 74, 40, 0.08);
    }
    .gateway-header {
        font-size: 0.95rem;
        font-weight: 700;
        color: #1E293B;
        text-transform: uppercase;
        letter-spacing: 0.03em;
        margin-bottom: 12px;
        border-bottom: 1px solid #F1F5F9;
        padding-bottom: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 🏛️ CORPORATE TOP BRAND NAVIGATION BAR
# ==========================================
st.markdown("""
    <div class="top-bar">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h1 class="brand-title">BhooKavach (भू-कवच)</h1>
                <div class="brand-tagline">Sovereign Land Securities & Anti-Fraud Infrastructure</div>
            </div>
            <div style="text-align: right; font-size: 0.75rem; color: #94A3B8; font-weight: 600; letter-spacing:0.02em;">
                GLOBAL STEALTH DEPLOYMENT PHASE • PILOT REGISTRY 2026
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Initialize a basic mock in-memory database to store early access requests
if "waitlist_records" not in st.session_state:
    st.session_state["waitlist_records"] = []

# ==========================================
# 🪐 MASTER SPLIT VIEW SPLIT LAYOUT
# ==========================================
editorial_side, gateway_side = st.columns([1.6, 1.4])

# ------------------------------------------
# LEFT PANEL: BRAND WALL NARRATIVE
# ------------------------------------------
with editorial_side:
    st.markdown("""
        <div class="narrative-card" style="border-top: 3px solid #0F4A28;">
            <div class="card-tag">👁️ Our Long-Term Vision</div>
            <h2 class="card-heading">The Sovereign Trust Imperative</h2>
            <p class="card-body">
                Project BhooKavach is engineered to eliminate information asymmetry and eradicate real estate title fraud across global property corridors. 
                By identifying hidden risk vectors—prelaunch escrow loops, double title filings, and environmental encroachment metrics—we are building 
                an unshakeable, tamper-proof technological shield to defend the hard-earned life savings of regular families.
            </p>
        </div>
        
        <div class="narrative-card" style="border-top: 3px solid #1E6B38;">
            <div class="card-tag">🎯 Phase 1 Strategic Deployment</div>
            <h2 class="card-heading">Pillar 1 Launch: Core Verification & Legal Firewalls</h2>
            <p class="card-body">
                We are bringing the architecture online in calculated, controlled phases. Our immediate Phase 1 deployment targets 
                <strong>Pillar 1: Core Verification & Legal Firewalls</strong>. This foundational engine utilizes advanced natural language processing (NLP) 
                text analytics to audit historical 30-year property link-deed lineages, cross-checks active Power of Attorney (PoA) validation channels, 
                and isolates clone developer website scams before capital is irreversibly committed.
            </p>
        </div>
    """, unsafe_allow_html=True)

# ------------------------------------------
# RIGHT PANEL: THE STEALTH WAITING LIST GATEWAY
# ------------------------------------------
with gateway_side:
    st.markdown("<div class='gateway-box'>", unsafe_allow_html=True)
    st.markdown("<div class='gateway-header'>🔐 Request Vault Access Allocation</div>", unsafe_allow_html=True)
    st.write("Our operational verification sandboxes are currently locked. Request early access below based on your ecosystem profile role.")
    
    # Form processing elements
    with st.form("stealth_waitlist_form", clear_on_submit=True):
        user_role = st.selectbox(
            "Select Account Category Identity:", 
            ["Property Buyer / Landowner", "Registered Ecosystem Vendor (Fencing/Insurance)", "Enterprise API Partner (Banks/Lenders)"]
        )
        user_name = st.text_input("Full Legal Name / Entity Designation:")
        user_email = st.text_input("Secure Corporate Email Address:")
        target_location = st.text_input("Primary Tracking Market Area (e.g., Gachibowli, Shadnagar, Amaravati):")
        
        st.markdown("<br>", unsafe_allow_html=True)
        submit_request = st.form_submit_button("REQUEST SECURED ACCESS ALLOCATION", use_container_width=True)
        
        if submit_request:
            if not user_name or not user_email or not target_location:
                st.error("❌ Authorization Error: Complete configuration fields are required.")
            else:
                # Store the request token in our local testing cache list
                new_entry = {
                    "Timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "Name": user_name,
                    "Email": user_email,
                    "Role": user_role,
                    "Market": target_location
                }
                st.session_state["waitlist_records"].append(new_entry)
                st.success("🟢 Access Token Reserved! Your account routing priority is queued. Our technical team will review your profile credentials.")
                st.toast("Early access request logged successfully!", icon="🛡️")
                
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 📈 REGIONAL DISPUTE TREND LEDGER (FIXED DATA VECTORS)
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div style='font-size: 1.1rem; font-weight: 700; color: #0F4A28; margin-bottom: 5px;'>📈 LONGITUDINAL REGIONAL RISK AGGREGATIONS</div>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 0.85rem; color: #64748B; margin-bottom: 15px;'>Venture Capital Metrics Grid: Longitudinal tracking of verified land disputes and building regulatory infractions caught annually across major expansion zones.</p>", unsafe_allow_html=True)

years = [2022.0, 2022.5, 2023.0, 2023.5, 2024.0, 2024.5]
st.line_chart(pd.DataFrame({
    "Hyderabad Expansion Corridors":,
    "Amaravati Capital Spine":,
    "Bengaluru Tech Hubs":,
    "Dubai Marina Freezone Window": [5, 9, 12, 18, 22, 31]
}, index=years), use_container_width=True)

# ==========================================
# 🔒 LEGAL PROTECTION SHIELD FOOTER
# ==========================================
st.markdown("<br><br>---", unsafe_allow_html=True)
st.markdown("""
    <div style='background-color: #FFF3CD; padding: 15px; border-left: 6px solid #FFC107; border-radius: 4px;'>
        <h4 style='color: #856404; margin-top: 0; font-size:0.9rem; font-weight:700;'>⚠️ Global Launch Operational Terms & Liability Protection Shield</h4>
        <p style='color: #856404; font-size: 0.8rem; line-height: 1.4; margin-bottom: 0;'>
            <strong>Information Aggregator Disclaimer:</strong> BhooKavach operates strictly as an autonomous centralized civic data aggregation network. This application does not produce certified legal opinions, formal title insurance policies, or official property brokerage counsel. All data layers, metrics, and spatial calculations remain confidential under the core founder equity framework agreement (2026).
        </p>
    </div>
""", unsafe_allow_html=True)
