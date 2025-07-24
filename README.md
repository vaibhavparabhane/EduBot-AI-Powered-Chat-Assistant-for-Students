# 🎓 EduBot: AI-Powered Chat Assistant for Students

**EduBot** is an AI-based chatbot designed to assist students with academics, programming concepts, interview preparation, career guidance, and productivity. It uses Natural Language Processing (NLP) techniques to understand queries and respond accurately — all inside a sleek Streamlit web interface.

---

## 🌟 Features

-   **Conversational Assistant:** Tailored for students to answer academic and career-related questions.
-   **Broad Subject Coverage:** Includes topics like AI, Python, SQL, resume building, and interview tips.
-   **Intelligent Query Matching:** Uses **TF-IDF** to vectorize text and **Cosine Similarity** to find the most relevant answer from its knowledge base.
-   **Natural Interaction:** Handles greetings and provides fallback responses for unrecognized queries.
-   **Lightweight & Fast Frontend:** Built entirely with Streamlit, requiring no HTML/CSS/JavaScript.
-   **Easy to Customize:** The knowledge base (corpus) is easily editable, allowing you to add more questions and answers.

---

## ⚙️ How It Works

The chatbot's intelligence comes from a classic Information Retrieval technique.

1.  **Corpus:** The bot is powered by a predefined set of questions and answers.
2.  **User Input:** A student types a query into the chat interface.
3.  **Text Preprocessing:** The user's query and the corpus are cleaned and standardized using techniques like tokenization and lemmatization from the NLTK library.
4.  **TF-IDF Vectorization:** The processed text is converted into numerical vectors using Term Frequency-Inverse Document Frequency (TF-IDF). This helps in evaluating how important a word is to a document in the corpus.
5.  **Cosine Similarity:** The bot calculates the cosine similarity between the user's query vector and all the question vectors in the corpus. The formula for cosine similarity is:
    $$
    \text{similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}
    $$
6.  **Response:** The answer corresponding to the question with the highest similarity score is returned to the user. If no question meets a certain similarity threshold, a fallback message is displayed.

---

## 🖥️ Technologies Used

-   **Backend:** Python
-   **NLP:** NLTK (Natural Language Toolkit), Scikit-learn
-   **Frontend:** Streamlit

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have Python 3.8 or higher installed on your system.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/EduBot.git](https://github.com/your-username/EduBot.git)
    cd EduBot
    ```

2.  **Create a virtual environment (recommended):**
    ```sh
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    Create a `requirements.txt` file with the following content:
    ```txt
    streamlit
    scikit-learn
    nltk
    ```
    Then, run the installation command:
    ```sh
    pip install -r requirements.txt
    ```

4.  **Download NLTK data:**
    You will need to download the `punkt` tokenizer and `wordnet` lemmatizer. Run this command to open the NLTK downloader and select them.
    ```sh
    python -m nltk.downloader punkt wordnet
    ```

### Running the Application

Once the installation is complete, you can run the Streamlit app with the following command:

```sh
streamlit run app.py
>>>>>>> 37672ce7856b16895d312beaa28d02f595151302
