import streamlit as st
import requests


st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.sidebar.title("Sample Questions")
sample_questions = [
    "What are the visiting hours at the hospital?",
    "Who are the cardiology specialists?",
    "What insurance policies does the hospital accept?",
    "What are the patient reviews for Dr. John Doe?",
    "What facilities does Harmony Health Center offer?"
]
for question in sample_questions:
    if st.sidebar.button(question):
        st.session_state["user_query"] = question


st.markdown(
    """
    <style>
    .navbar {
        font-size: 20px;
        font-weight: bold;
        padding: 10px;
        background-color: #f4f4f4;
        border-bottom: 2px solid #ddd;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    }
    </style>
   
    """,
    unsafe_allow_html=True
)
 # <div class="navbar">Harmony Health Center RAG Chatbot</div>
# --- Chat Interface ---
st.write("")  # Spacer
st.header("Ask Me Anything")
st.write("Enter your question below, and I'll try to help!")

# Displaying Chat History
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Input Field for User Questions
if "user_query" in st.session_state:
    user_query = st.text_input(
        "Your question:", value=st.session_state["user_query"], placeholder="Type your question here..."
    )
else:
    user_query = st.text_input("Your question:", placeholder="Type your question here...")

# Send Button
send_button = st.button("Send", disabled=not user_query)
if send_button:
    # Send POST request to backend
    try:
        response = requests.post(
            "http://localhost:8000/generate/", json={"question": user_query}
        )
        if response.status_code == 200:
            bot_response = response.json().get("response", "Sorry, I couldn't understand.")
        else:
            bot_response = f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        bot_response = "Error: Unable to connect to the backend API."

    # Add to chat history
    st.session_state["chat_history"].append(("You", user_query))
    st.session_state["chat_history"].append(("Bot", bot_response))

# --- Chat History Display ---
st.markdown("""
    <style>
        .chat-history {
            max-height: 400px;
            overflow-y: scroll;
        }
    </style>
""", unsafe_allow_html=True)

# Chat history container
with st.container():
    st.markdown('<div class="chat-history">', unsafe_allow_html=True)
    for speaker, message in st.session_state["chat_history"]:
        if speaker == "You":
            st.markdown(f"**{speaker}:** {message}")
        else:
            st.markdown(f"*{speaker}:* {message}")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Instructions at Bottom ---
st.markdown("---")
st.write("Powered by LangChain, FastAPI, and Streamlit.")
