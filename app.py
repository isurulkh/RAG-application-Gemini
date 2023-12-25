import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from dotenv import load_dotenv
import PyPDF2
import os
import io

st.title("Chat Your PDFs")  # Updated title

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
google_api_key = os.getenv("GOOGLE_API_KEY")

# Check if the API key is available
if google_api_key is None:
    st.warning("API key not found. Please set the google_api_key environment variable.")
    st.stop()

# File Upload with user-defined name
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    st.text("PDF File Uploaded Successfully!")

    # PDF Processing (using PyPDF2 directly)
    pdf_data = uploaded_file.read()
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_data))
    pdf_pages = pdf_reader.pages

    # Create Context
    context = "\n\n".join(page.extract_text() for page in pdf_pages)

    # Split Texts
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=200)
    texts = text_splitter.split_text(context)

    # Chroma Embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_index = Chroma.from_texts(texts, embeddings).as_retriever()

    # Get User Question
    user_question = st.text_input("Ask a Question:")

    if st.button("Get Answer"):
        if user_question:
            # Get Relevant Documents
            docs = vector_index.get_relevant_documents(user_question)

            # Define Prompt Template
            prompt_template = """
            Answer the question as detailed as possible from the provided context,
            make sure to provide all the details, if the answer is not in
            provided context just say, "answer is not available in the context",
            don't provide the wrong answer\n\n
            Context:\n {context}?\n
            Question: \n{question}\n
            Answer:
            """

            # Create Prompt
            prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

            # Load QA Chain
            model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3, api_key=google_api_key)
            chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

            # Get Response
            response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)

            # Display Answer
            st.subheader("Answer:")
            st.write(response['output_text'])

        else:
            st.warning("Please enter a question.")
