# Chat Your PDFs

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/your-github-username/your-repo-name/main/app.py)

## Description

Chat Your PDFs is a Streamlit web application that allows users to upload PDF files, ask questions about the content, and receive detailed answers using the Google Generative AI model.

## Features

- Upload PDF files.
- Ask questions about the content.
- Get detailed answers using Google Generative AI.

## Demo

You can access the live demo [here](https://share.streamlit.io/your-github-username/your-repo-name/main/app.py).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/isurulkh/RAG-application-Gemini.git
    ```

2. Navigate to the project directory:

    ```bash
    cd RAG-application-Gemini-main
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your browser and go to `http://localhost:8501`.

3. Upload a PDF file, ask a question, and click "Get Answer."

## Configuration

### Environment Variables

- `GOOGLE_API_KEY`: Obtain a Google Generative AI API key from the [Google Cloud Console](https://console.cloud.google.com/) and set it as an environment variable.

    ```bash
    export GOOGLE_API_KEY=your_google_api_key
    ```

## Contributing

If you would like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch:

    ```bash
    git checkout -b feature/my-feature
    ```

3. Commit your changes:

    ```bash
    git commit -m "Add my feature"
    ```

4. Push to the branch:

    ```bash
    git push origin feature/my-feature
    ```

5. Create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
