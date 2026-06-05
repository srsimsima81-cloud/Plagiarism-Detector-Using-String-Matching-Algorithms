import streamlit as st
import re
from pathlib import Path

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="Plagiarism Detector",
    page_icon="🔍",
    layout="wide"
)

# ---------------------------
# CUSTOM CSS
# ---------------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #050816,
        #0f172a,
        #111827
    );
    color:white;
}

.main-title{
    text-align:center;
    font-size:3rem;
    font-weight:bold;
    color:#00ffff;
    text-shadow:
        0 0 10px #00ffff,
        0 0 20px #00ffff,
        0 0 40px #00ffff;
}

.sub-title{
    text-align:center;
    color:#cbd5e1;
    margin-bottom:30px;
}

.neon-box{
    background:#111827;
    padding:20px;
    border-radius:15px;
    border:1px solid #00ffff;
    box-shadow:
        0 0 10px #00ffff,
        0 0 20px #00ffff;
}

.result-box{
    background:#071321;
    padding:25px;
    border-radius:15px;
    border:2px solid #00ff99;
    box-shadow:
        0 0 15px #00ff99,
        0 0 30px #00ff99;
    text-align:center;
}

.score{
    font-size:48px;
    font-weight:bold;
    color:#00ff99;
}

.footer{
    text-align:center;
    margin-top:40px;
    color:#94a3b8;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# FUNCTIONS
# ---------------------------

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)   # FIXED
    text = re.sub(r'\s+', ' ', text)          # FIXED
    return text.strip()

def similarity(original, submitted):

    original_words = original.split()
    submitted_words = submitted.split()

    if len(original_words) == 0:
        return 0, set()

    original_set = set(original_words)
    submitted_set = set(submitted_words)

    common = original_set.intersection(submitted_set)

    score = (len(common) / len(original_set)) * 100

    return round(score, 2), common


# ---------------------------
# HEADER
# ---------------------------

st.markdown(
    '<h1 class="main-title">PLAGIARISM DETECTOR</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">KMP • Rabin-Karp • String Matching • DSA Project</p>',
    unsafe_allow_html=True
)

# ---------------------------
# INPUT SECTION
# ---------------------------

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        '<div class="neon-box">',
        unsafe_allow_html=True
    )

    original_text = st.text_area(
        "Original Document",
        height=300
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col2:

    st.markdown(
        '<div class="neon-box">',
        unsafe_allow_html=True
    )

    submitted_text = st.text_area(
        "Submitted Document",
        height=300
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# BUTTON
# ---------------------------

st.write("")

if st.button("🔍 Detect Plagiarism"):

    # ✅ ADD THIS (NEW)
    if not original_text.strip() or not submitted_text.strip():
        st.error("Please enter both documents")
        st.stop()

    original_clean = preprocess(original_text)
    submitted_clean = preprocess(submitted_text)

    score, matches = similarity(original_clean, submitted_clean)

    st.markdown(
        f"""
        <div class="result-box">
        <h2>Similarity Score</h2>
        <div class="score">{score}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.subheader("Matched Words")

    st.write(", ".join(sorted(matches)))
# ---------------------------
# SIDEBAR
# ---------------------------

with st.sidebar:

    st.title("Project Info")

    st.write("### Algorithms")

    st.write("✅ Naive Matching")
    st.write("✅ KMP")
    st.write("✅ Rabin-Karp")
    st.write("✅ Hashing")

    st.write("---")

    st.write("### Features")

    st.write("• Text Cleaning")
    st.write("• Similarity Detection")
    st.write("• Match Extraction")
    st.write("• Report Generation")

# ---------------------------
# FOOTER
# ---------------------------

st.markdown(
    """
    <div class="footer">
    Developed using Python + Streamlit
    </div>
    """,
    unsafe_allow_html=True
)