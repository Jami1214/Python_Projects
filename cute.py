import time
import pandas as pd
import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Tech Fun Hub ✨",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Dynamic Vibrant Custom CSS ---
st.markdown(
    """
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #1A0B2E 0%, #2D124D 50%, #0F172A 100%);
        color: #FFFFFF;
    }
    
    /* Cartoon Mascot Container */
    .mascot-card {
        background: linear-gradient(135deg, #FF007A 0%, #7E22CE 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(255, 0, 122, 0.3);
        text-align: center;
        margin-bottom: 2rem;
        border: 2px solid #FF70A6;
    }
    
    .mascot-avatar {
        font-size: 80px;
        line-height: 1;
        margin-bottom: 10px;
    }
    
    /* Glassmorphic Content Cards */
    div[data-testid="stVerticalBlock"] > div {
        border-radius: 16px;
    }
    
    /* Styled Headers */
    h1, h2, h3 {
        color: #FF70A6 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Custom Primary Button Styling */
    .stButton>button {
        background: linear-gradient(90deg, #FF007A 0%, #FF70A6 100%);
        color: white !important;
        font-weight: bold;
        border-radius: 12px;
        border: none;
        padding: 0.6rem 1.5rem;
        box-shadow: 0 4px 15px rgba(255, 0, 122, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 6px 20px rgba(255, 0, 122, 0.6);
    }
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
        "options": [
            "Hard Drive (HDD)",
            "Solid State Drive (SSD)",
            "RAM",
            "USB Flash Drive",
        ],
        "answer": "RAM",
        "explanation": "RAM holds active software data temporarily while your PC is running.",
    },
    {
        "id": 4,
        "question": "What type of software is Google Chrome or Microsoft Edge?",
        "options": [
            "Operating System",
            "Web Browser",
            "Antivirus Software",
            "Word Processor",
        ],
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

# --- State Initialization ---
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "user_title" not in st.session_state:
    st.session_state.user_title = ""

if "onboarded" not in st.session_state:
    st.session_state.onboarded = False

if "page" not in st.session_state:
    st.session_state.page = "Quiz Mode"

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answers_history" not in st.session_state:
    st.session_state.answers_history = []

if "flashcard_index" not in st.session_state:
    st.session_state.flashcard_index = 0

if "show_definition" not in st.session_state:
    st.session_state.show_definition = False


# --- ONBOARDING WELCOME SCREEN ---
if not st.session_state.onboarded:
    st.markdown(
        """
        <div class="mascot-card">
            <div class="mascot-avatar">🤖✨</div>
            <h1 style="color: white !important;">Hi there! I'm Byte, your Tech Host!</h1>
            <p style="font-size: 1.2rem; color: #FFE5EC;">Welcome to the ultimate Computer Literacy Hub! Before we begin, let's get acquainted!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        name_input = st.text_input(
            "What is your name?", placeholder="Type your name here..."
        )
        gender_choice = st.radio(
            "Are you a girl or a guy?",
            ["I'm a girl 👑", "I'm a guy 🤴"],
            horizontal=True,
        )

        if st.button("🚀 Let's Start the Tech Fun!", use_container_width=True):
            if name_input.strip():
                st.session_state.user_name = name_input.strip().capitalize()
                if "girl" in gender_choice:
                    st.session_state.user_title = "Tech Queen"
                else:
                    st.session_state.user_title = "Tech King"

                st.session_state.onboarded = True
                st.balloons()
                st.rerun()
            else:
                st.warning(
                    "Please enter your name so Byte knows what to call you!"
                )

# --- MAIN APPLICATION DASHBOARD ---
else:
    # Sidebar Profile Banner
    st.sidebar.markdown(
        f"""
        <div style="background: rgba(255, 255, 255, 0.1); padding: 1rem; border-radius: 12px; text-align: center; border: 1px solid #FF70A6;">
            <div style="font-size: 40px;">🤖</div>
            <h3 style="margin:0; color: #FF70A6 !important;">Welcome, {st.session_state.user_name}!</h3>
            <p style="margin:0; font-weight: bold; color: #A7F3D0;">✨ {st.session_state.user_title} ✨</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown("---")
    st.session_state.page = st.sidebar.radio(
        "Navigation",
        ["Quiz Mode 🎯", "Interactive Flashcards 🎴", "Progress Dashboard 📊"],
    )
    st.sidebar.metric("Current Score", f"{st.session_state.score} pts")

    if st.sidebar.button("🔄 Change Profile / Reset"):
        st.session_state.onboarded = False
        st.session_state.quiz_index = 0
        st.session_state.score = 0
        st.session_state.answers_history = []
        st.rerun()

    # Greeting Banner
    st.markdown(
        f"""
        <div style="background: linear-gradient(90deg, #7E22CE 0%, #FF007A 100%); padding: 1.2rem; border-radius: 16px; margin-bottom: 1.5rem; text-align: center;">
            <h2 style="color: white !important; margin: 0;">Welcome, {st.session_state.user_title} {st.session_state.user_name}! 👑</h2>
            <p style="color: #FBCFE8; margin: 0; font-size: 1.1rem;">Ready for some tech fun with Byte?</p>
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

            st.progress((curr_i) / total_q)
            st.write(f"### Question {curr_i + 1} of {total_q}")
            st.markdown(f"#### {q_data['question']}")

            selected_option = st.radio(
                "Select your choice:", q_data["options"], key=f"q_{curr_i}"
            )

            if st.button("Submit Answer", type="primary"):
                is_correct = selected_option == q_data["answer"]
                if is_correct:
                    st.session_state.score += 10
                    st.success(
                        f"🎯 Spot on, {st.session_state.user_title}! You got it right!"
                    )
                else:
                    st.error(
                        f"❌ Oops! The correct answer was **{q_data['answer']}**."
                    )

                st.info(f"💡 **Byte's Tip: {q_data['explanation']}")

                st.session_state.answers_history.append({
                    "Question": q_data["question"],
                    "Your Answer": selected_option,
                    "Correct Answer": q_data["answer"],
                    "Status": "Correct" if is_correct else "Incorrect",
                })

                time.sleep(1.8)
                st.session_state.quiz_index += 1
                st.rerun()

        else:
            st.balloons()
            st.success(
                f"🎉 Outstanding work, {st.session_state.user_title} {st.session_state.user_name}! You completed the challenge!"
            )
            st.metric("Final Score", f"{st.session_state.score} pts")

            if st.button("Replay Quiz"):
                st.session_state.quiz_index = 0
                st.session_state.score = 0
                st.session_state.answers_history = []
                st.rerun()

    # --- MODE 2: FLASHCARDS ---
    elif st.session_state.page == "Interactive Flashcards 🎴":
        st.subheader("🎴 Computer Terminology Flashcards")

        card = FLASHCARDS[st.session_state.flashcard_index]

        col1, col2, col3 = st.columns([1, 3, 1])

        with col2:
            if not st.session_state.show_definition:
                st.info(f"### 📌 Term:\n# **")
            else:
                st.success(f"### 📖 Definition:\n{card['definition']}")

            if st.button("🔄 Flip Card", use_container_width=True):
                st.session_state.show_definition = (
                    not st.session_state.show_definition
                )
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        if c1.button("⬅️ Previous Card", use_container_width=True):
            st.session_state.flashcard_index = (
                st.session_state.flashcard_index - 1
            ) % len(FLASHCARDS)
            st.session_state.show_definition = False
            st.rerun()

        if c2.button("Next Card ➡️", use_container_width=True):
            st.session_state.flashcard_index = (
                st.session_state.flashcard_index + 1
            ) % len(FLASHCARDS)
            st.session_state.show_definition = False
            st.rerun()

    # --- MODE 3: PROGRESS DASHBOARD ---
    elif st.session_state.page == "Progress Dashboard 📊":
        st.subheader(
            f"📊 {st.session_state.user_name}'s Performance Dashboard"
        )

        if st.session_state.answers_history:
            df = pd.DataFrame(st.session_state.answers_history)

            col1, col2 = st.columns(2)

            with col1:
                st.write("### Quiz Breakdown")
                st.dataframe(df, use_container_width=True)

            with col2:
                st.write("### Accuracy Chart")
                status_counts = df["Status"].value_counts()
                st.bar_chart(status_counts)
        else:
            st.warning(
                "No stats recorded yet! Complete the quiz to unlock your personal performance analytics."
            )