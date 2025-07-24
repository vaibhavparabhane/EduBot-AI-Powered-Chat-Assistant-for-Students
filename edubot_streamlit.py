import streamlit as st
import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Load and process the corpus
try:
    with open('chatbot_corpus_edubot.txt', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    st.error("❌ chatbot_corpus_edubot.txt not found.")
    st.stop()

# Create question-answer pairs
qa_pairs = [(lines[i], lines[i + 1]) for i in range(0, len(lines) - 1, 2)]
questions = [q.lower() for q, a in qa_pairs]

# Lemmatizer
lemmatizer = nltk.WordNetLemmatizer()

def normalize(text):
    tokens = nltk.word_tokenize(text.lower().translate(str.maketrans('', '', string.punctuation)))
    return ' '.join([lemmatizer.lemmatize(token) for token in tokens])

normalized_questions = [normalize(q) for q in questions]

# Greetings
GREETING_INPUTS = ("hello", "hi", "hey", "greetings")
GREETING_RESPONSES = ["👋 Hi there!", "Hello!", "Hey!", "Hi! How can I assist you today?"]

def greet(text):
    for word in text.lower().split():
        if word in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
    return None

# Fallback responses
FALLBACK_RESPONSES = [
    "🤔 I'm not sure I understand that yet.",
    "🔄 Could you rephrase that?",
    "😅 Sorry, I haven’t learned that yet.",
    "🧐 That’s an interesting question! Let me look into it."
]

# Response generator
def generate_response(user_input):
    norm_input = normalize(user_input)
    vectorizer = TfidfVectorizer().fit(normalized_questions + [norm_input])
    vectors = vectorizer.transform(normalized_questions + [norm_input])
    cosine_sim = cosine_similarity(vectors[-1], vectors[:-1])
    
    index = cosine_sim.argmax()
    if cosine_sim[0][index] < 0.4:
        return random.choice(FALLBACK_RESPONSES)
    return qa_pairs[index][1]

# ---------------- STREAMLIT UI ----------------

st.set_page_config(page_title="EduBot", page_icon="🎓", layout="centered")
st.title("🎓 EduBot: AI Chat Assistant for Students")
st.caption("Ask me about programming, careers, interviews, or productivity! 🧠")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your question:", "")
    submitted = st.form_submit_button("Send")

# Handle input
if submitted and user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "text": user_input})
    
    greeting = greet(user_input)
    if greeting:
        bot_reply = greeting
    else:
        bot_reply = generate_response(user_input)
    
    # Add bot response
    st.session_state.messages.append({"role": "bot", "text": bot_reply})

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"🧑 **You:** {message['text']}")
    else:
        st.markdown(f"🤖 **EduBot:** {message['text']}")

# Clear chat button
if st.button("🧹 Clear Chat"):
    st.session_state.messages = []
