import streamlit as st
import time
import base64

# ---------- Apple-Style Page Setup ----------
st.set_page_config(page_title="🧠 Multi-Source Q&A Agent", layout="wide", page_icon="🧊")

# ---------- Inject Apple-Style + Glassmorphism CSS ----------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #e8e8ec 0%, #f6f6f8 100%);
        color: #1d1d1f;
    }

    .glass {
        background: rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 2rem;
    }

    .title {
        font-size: 3em;
        font-weight: 600;
        letter-spacing: -1px;
    }

    .subtitle {
        font-size: 1.2em;
        color: #6e6e73;
        margin-bottom: 20px;
    }

    .input-box {
        background: rgba(255, 255, 255, 0.25);
        padding: 1rem;
        border-radius: 12px;
    }

    .small-text {
        color: #8e8e93;
        font-size: 0.9em;
        margin-top: 20px;
    }

    button[kind="primary"] {
        background-color: #000000 !important;
        color: #ffffff !important;
        border-radius: 12px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="title">🧠 Multi-Source Q&A Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">LangChain | RAG | FAISS | Agents | OLlama</div>', unsafe_allow_html=True)

# ---------- Main Glass Panel ----------
with st.container():
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    # 🔍 Question Input
    st.subheader("Ask your question")
    query = st.text_input("Type here...", placeholder="e.g., What is retrieval-augmented generation?")

    # 🔗 Source Selection
    st.subheader("Choose your sources")
    sources = st.multiselect(
        "Select data sources:",
        ["Wikipedia", "Web Pages", "ArXiv"],
        default=["Wikipedia", "ArXiv"]
    )

    # 🚀 Query Execution
    if st.button("Run Agent 🔍"):
        if query:
            with st.spinner("Retrieving knowledge from multiple silos..."):
                time.sleep(2.5)  # Simulate latency
                st.success("Response generated below!")

                # ✨ Output Section
                st.markdown("### 🧠 Intelligent Response")
                st.markdown("""
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
                This is a simulated intelligent response from your Agentic RAG System.
                """)

                # 📚 Sources used
                st.markdown("### 🔗 Sources Queried")
                for src in sources:
                    st.markdown(f"- {src}")
        else:
            st.warning("Please enter a query.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Sidebar with Glass Style ----------
with st.sidebar:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.title("⚙️ System Design")

    st.markdown("""
    - **LangChain Agents** → Dynamic source routing  
    - **FAISS** → Fast vector similarity search  
    - **RAG** → Context-aware retrieval + generation  
    - **OLlama** → Lightweight LLM for fast answers  
    """)
    st.markdown("---")
    st.caption("🚀 Designed with ❤️ by an Apple-obsessed developer.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown('<p class="small-text">Designed with minimalism, functionality & elegance.</p>', unsafe_allow_html=True)
