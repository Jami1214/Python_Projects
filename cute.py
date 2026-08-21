import pandas as pd
import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Tech Fun Hub ✨",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Rich, Clean Design System ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;600&display=swap');

    :root {
        --bg-1: #0B0A1A;
        --bg-2: #17123A;
        --bg-3: #241A4D;
        --surface: rgba(255, 255, 255, 0.045);
        --surface-border: rgba(242, 197, 114, 0.18);
        --gold: #F2C572;
        --gold-soft: rgba(242, 197, 114, 0.16);
        --violet: #A78BFA;
        --text-primary: #F4F1FB;
        --text-secondary: #ADA6C9;
        --success: #4ADE80;
        --error: #FB7185;
    }

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    /* Background: rich gradient + faint dot-grid texture */
    .stApp {
        background:
            radial-gradient(circle at 15% 10%, rgba(167, 139, 250, 0.10) 0%, transparent 45%),
            radial-gradient(circle at 85% 90%, rgba(242, 197, 114, 0.08) 0%, transparent 45%),
            linear-gradient(160deg, var(--bg-1) 0%, var(--bg-2) 55%, var(--bg-3) 100%);
        background-attachment: fixed;
        color: var(--text-primary);
    }

    /* Baseline text contrast fix — applies to markdown, labels, radio options, captions */
    .stApp, .stApp p, .stApp span, .stApp label, .stApp li,
    .stMarkdown, .stMarkdown p, .stCaption, [data-testid="stWidgetLabel"] p {
        color: var(--text-primary) !important;
    }
    .stCaption, [data-testid="stCaptionContainer"] { color: var(--text-secondary) !important; }

    /* Headings */
    h1, h2, h3 {
        color: var(--gold) !important;
        font-family: 'Sora', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.01em;
    }
    h4, h5 {
        color: var(--text-primary) !important;
        font-family: 'Sora', sans-serif !important;
        font-weight: 600 !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #100C24 0%, #1A1440 100%);
        border-right: 1px solid rgba(242, 197, 114, 0.12);
    }

    /* Glass cards used for st.container(border=True) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: var(--surface);
        border: 1px solid var(--surface-border) !important;
        border-radius: 18px;
        backdrop-filter: blur(6px);
    }

    .mascot-card {
        background: linear-gradient(135deg, rgba(167, 139, 250, 0.16) 0%, rgba(242, 197, 114, 0.10) 100%);
        padding: 2.2rem;
        border-radius: 22px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.35);
        text-align: center;
        margin-bottom: 2rem;
        border: 1px solid var(--surface-border);
        backdrop-filter: blur(8px);
    }
    .mascot-avatar { font-size: 70px; line-height: 1; margin-bottom: 10px; }

    .hero-banner {
        background: linear-gradient(90deg, rgba(167, 139, 250, 0.20) 0%, rgba(242, 197, 114, 0.14) 100%);
        border: 1px solid var(--surface-border);
        padding: 1.4rem 1.6rem;
        border-radius: 18px;
        margin-bottom: 1.6rem;
    }

    .profile-card {
        background: var(--surface);
        border: 1px solid var(--surface-border);
        padding: 1.1rem;
        border-radius: 14px;
        text-align: center;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, var(--gold) 0%, #E8A94E 100%);
        color: #17123A !important;
        font-family: 'Sora', sans-serif;
        font-weight: 700;
        border-radius: 10px;
        border: none;
        padding: 0.6rem 1.5rem;
        box-shadow: 0 4px 16px rgba(242, 197, 114, 0.25);
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(242, 197, 114, 0.4);
    }
    .stButton>button:focus-visible {
        outline: 2px solid var(--violet);
        outline-offset: 2px;
    }

    /* Radio buttons: readable text + gold selection state */
    div[role="radiogroup"] label { color: var(--text-primary) !important; }
    div[role="radiogroup"] input[type="radio"] { accent-color: var(--gold); }

    /* Progress bar */
    .stProgress > div > div > div > div { background-color: var(--gold) !important; }

    /* Metrics */
    [data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace;
        color: var(--gold) !important;
    }
    [data-testid="stMetricLabel"] { color: var(--text-secondary) !important; }

    /* Flashcard */
    .flashcard-box {
        background: var(--surface);
        border: 1px solid var(--surface-border);
        border-radius: 18px;
        padding: 2.6rem 1.5rem;
        text-align: center;
        min-height: 140px;
        display: flex;
        align-items: center;
        justify-content: center;
        backdrop-filter: blur(6px);
    }

    /* Dataframe container polish */
    [data-testid="stDataFrame"] { border-radius: 12px; overflow: hidden; }

    hr { border-color: rgba(242, 197, 114, 0.15) !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Question Bank & Flashcards Data ---
QUIZ_BANK = [
    {
        "id": 1,
        "question": "Which keyboard shortcut is used to copy selected text in Windows?",
        "options": ["Ctrl + V", "Ctrl + C", "Ctrl + X", "Ctrl + Z"],
        "answer": "Ctrl + C",
        "explanation": "Ctrl + C copies selected items, while Ctrl + V pastes them.",
    },
    {
        "id": 2,
        "question": "What does 'CPU' stand for in a computer system?",
        "options": [
            "Central Processing Unit",
            "Computer Power Unit",
            "Control Panel Utility",
            "Central Program User",
        ],
        "answer": "Central Processing Unit",
        "explanation": "The CPU acts as the brain of your computer system.",
    },
    {
        "id": 3,
        "question": "Which of the following is considered primary short-term memory?",
        "options": ["Hard Drive (HDD)", "Solid State Drive (SSD)", "RAM", "USB Flash Drive"],
        "answer": "RAM",
        "explanation": "RAM holds active software data temporarily while your PC is running.",
    },
    {
        "id": 4,
        "question": "What type of software is Google Chrome or Microsoft Edge?",
        "options": ["Operating System", "Web Browser", "Antivirus Software", "Word Processor"],
        "answer": "Web Browser",
        "explanation": "Web browsers allow users to navigate and display pages across the internet.",
    },
    {
        "id": 5,
        "question": "What is 'Cloud Storage'?",
        "options": [
            "Saving files on a local USB drive",
            "Storing data on remote internet servers",
            "Printing physical copies of documents",
            "Downloading files directly to desktop RAM",
        ],
        "answer": "Storing data on remote internet servers",
        "explanation": "Services like Google Drive store data securely on remote internet servers.",
    },
]

FLASHCARDS = [
    {
        "term": "Hardware",
        "definition": "The physical parts of a computer system like monitors, keyboards, and chips.",
    },
    {
        "term": "Software",
        "definition": "Programs and operating instructions that tell computer hardware what to execute.",
    },
    {
        "term": "Phishing",
        "definition": "A cyber scam tricking users into revealing passwords via fraudulent messages.",
    },
    {
        "term": "URL",
        "definition": "Uniform Resource Locator—the web address used to locate a specific web page.",
    },
]

DEFAULT_STATE = {
    "user_name": "",
    "user_title": "",
    "onboarded": False,
    "page": "Quiz Mode 🎯",
    "quiz_index": 0,
    "score": 0,
    "answers_history": [],
    "answer_submitted": False,
    "last_correct": None,
    "flashcard_index": 0,
    "show_definition": False,
}

for key, default in DEFAULT_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = default


def reset_profile():
    for key, default in DEFAULT_STATE.items():
        st.session_state[key] = default


def reset_quiz():
    st.session_state.quiz_index = 0
    st.session_state.score = 0
    st.session_state.answers_history = []
    st.session_state.answer_submitted = False
    st.session_state.last_correct = None


# --- ONBOARDING WELCOME SCREEN ---
if not st.session_state.onboarded:
    st.markdown(
        """
        <div class="mascot-card">
            <div class="mascot-avatar">🤖✨</div>
            <h1 style="margin-bottom: 0.4rem;">Hi there! I'm Byte, your Tech Host!</h1>
            <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 480px; margin: 0 auto;">Welcome to the ultimate Computer Literacy Hub. Before we begin, let's get acquainted!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        name_input = st.text_input("What is your name?", placeholder="Type your name here...")

        title_choice = st.radio(
            "Pick your title:",
            ["Tech Queen 👑", "Tech King 🤴", "Tech Star ⭐"],
            horizontal=True,
        )

        if st.button("🚀 Let's Start the Tech Fun!", use_container_width=True):
            if name_input.strip():
                st.session_state.user_name = name_input.strip().capitalize()
                st.session_state.user_title = title_choice.split(" ")[0] + " " + title_choice.split(" ")[1]
                st.session_state.onboarded = True
                st.balloons()
                st.rerun()
            else:
                st.warning("Please enter your name so Byte knows what to call you!")

# --- MAIN APPLICATION DASHBOARD ---
else:
    st.sidebar.markdown(
        f"""
        <div class="profile-card">
            <div style="font-size: 36px;">🤖</div>
            <h3 style="margin:0;">Welcome, {st.session_state.user_name}!</h3>
            <p style="margin:0.2rem 0 0; font-weight: 600; color: var(--gold) !important;">✨ {st.session_state.user_title} ✨</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown("---")
    st.session_state.page = st.sidebar.radio(
        "Navigation",
        ["Quiz Mode 🎯", "Interactive Flashcards 🎴", "Progress Dashboard 📊"],
        index=["Quiz Mode 🎯", "Interactive Flashcards 🎴", "Progress Dashboard 📊"].index(st.session_state.page),
    )
    st.sidebar.metric("Current Score", f"{st.session_state.score} pts")

    if st.sidebar.button("🔄 Change Profile / Reset"):
        reset_profile()
        st.rerun()

    st.markdown(
        f"""
        <div class="hero-banner" style="text-align: center;">
            <h2 style="margin: 0;">Welcome, {st.session_state.user_title} {st.session_state.user_name} 👑</h2>
            <p style="color: var(--text-secondary) !important; margin: 0.3rem 0 0; font-size: 1.05rem;">Ready for some tech fun with Byte?</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- MODE 1: QUIZ MODE ---
    if st.session_state.page == "Quiz Mode 🎯":
        st.subheader("🎯 Computer Literacy Challenge")

        total_q = len(QUIZ_BANK)
        curr_i = st.session_state.quiz_index

        if curr_i < total_q:
            q_data = QUIZ_BANK[curr_i]

            st.progress(curr_i / total_q)

            with st.container(border=True):
                st.markdown(
                    f'<p style="font-family:\'JetBrains Mono\',monospace; color: var(--text-secondary); '
                    f'font-size: 0.85rem; letter-spacing: 0.05em; margin-bottom: 0.3rem;">'
                    f'QUESTION {curr_i + 1} OF {total_q}</p>',
                    unsafe_allow_html=True,
                )
                st.markdown(f"#### {q_data['question']}")

                selected_option = st.radio(
                    "Select your choice:",
                    q_data["options"],
                    key=f"q_{curr_i}",
                    disabled=st.session_state.answer_submitted,
                    label_visibility="collapsed",
                )

                if not st.session_state.answer_submitted:
                    if st.button("Submit Answer", type="primary"):
                        is_correct = selected_option == q_data["answer"]
                        st.session_state.answer_submitted = True
                        st.session_state.last_correct = is_correct

                        if is_correct:
                            st.session_state.score += 10

                        st.session_state.answers_history.append(
                            {
                                "Question": q_data["question"],
                                "Your Answer": selected_option,
                                "Correct Answer": q_data["answer"],
                                "Status": "Correct" if is_correct else "Incorrect",
                            }
                        )
                        st.rerun()
                else:
                    if st.session_state.last_correct:
                        st.success(f"🎯 Spot on, {st.session_state.user_title}! You got it right!")
                    else:
                        st.error(f"❌ Oops! The correct answer was **{q_data['answer']}**.")

                    st.info(f"💡 **Byte's Tip:** {q_data['explanation']}")

                    if st.button("Next Question ➡️", type="primary"):
                        st.session_state.quiz_index += 1
                        st.session_state.answer_submitted = False
                        st.session_state.last_correct = None
                        st.rerun()

        else:
            st.balloons()
            st.success(
                f"🎉 Outstanding work, {st.session_state.user_title} {st.session_state.user_name}! You completed the challenge!"
            )
            st.metric("Final Score", f"{st.session_state.score} pts")

            if st.button("Replay Quiz"):
                reset_quiz()
                st.rerun()

    # --- MODE 2: FLASHCARDS ---
    elif st.session_state.page == "Interactive Flashcards 🎴":
        st.subheader("🎴 Computer Terminology Flashcards")
        st.caption(f"Card {st.session_state.flashcard_index + 1} of {len(FLASHCARDS)}")

        card = FLASHCARDS[st.session_state.flashcard_index]

        col1, col2, col3 = st.columns([1, 3, 1])

        with col2:
            if not st.session_state.show_definition:
                st.markdown(
                    f"""<div class="flashcard-box"><h2 style="margin:0;">📌 {card['term']}</h2></div>""",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"""<div class="flashcard-box"><p style="font-size:1.1rem; margin:0; color: var(--text-primary);">📖 {card['definition']}</p></div>""",
                    unsafe_allow_html=True,
                )

            if st.button("🔄 Flip Card", use_container_width=True):
                st.session_state.show_definition = not st.session_state.show_definition
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        if c1.button("⬅️ Previous Card", use_container_width=True):
            st.session_state.flashcard_index = (st.session_state.flashcard_index - 1) % len(FLASHCARDS)
            st.session_state.show_definition = False
            st.rerun()

        if c2.button("Next Card ➡️", use_container_width=True):
            st.session_state.flashcard_index = (st.session_state.flashcard_index + 1) % len(FLASHCARDS)
            st.session_state.show_definition = False
            st.rerun()

    # --- MODE 3: PROGRESS DASHBOARD ---
    elif st.session_state.page == "Progress Dashboard 📊":
        st.subheader(f"📊 {st.session_state.user_name}'s Performance Dashboard")

        if st.session_state.answers_history:
            df = pd.DataFrame(st.session_state.answers_history)
            correct_count = (df["Status"] == "Correct").sum()
            accuracy = correct_count / len(df) * 100

            m1, m2, m3 = st.columns(3)
            m1.metric("Questions Answered", len(df))
            m2.metric("Correct", int(correct_count))
            m3.metric("Accuracy", f"{accuracy:.0f}%")

            col1, col2 = st.columns(2)
            with col1:
                with st.container(border=True):
                    st.write("#### Quiz Breakdown")
                    st.dataframe(df, use_container_width=True)
            with col2:
                with st.container(border=True):
                    st.write("#### Accuracy Chart")
                    status_counts = df["Status"].value_counts()
                    st.bar_chart(status_counts)
        else:
            st.warning("No stats recorded yet! Complete the quiz to unlock your personal performance analytics.")