<h1 align="center">
Librarian 📖
</h1>

Upload your documents and get answers to your questions, with citations from the text.

## Installation

Follow the instructions below to run the Streamlit server locally.

### Pre-requisites

Make sure you have Python ≥ 3.10 installed.

### Steps

1. Clone the repository

```bash
git clone https://github.com/AvaterClasher/librarian.git
cd librarian
```

2. Install dependencies with [Poetry](https://python-poetry.org/) and activate virtual environment

```bash
poetry install
poetry shell
```

3. (Optional) Avoid adding the OpenAI API every time you run the server by adding it to environment variables.
   - Add your API key to the `.env` file

4. Run the Streamlit server

```bash
cd librarian
streamlit run main.py
```

## Tech Stack

- User Interface - [Streamlit](https://streamlit.io/)
- LLM Tooling - [Langchain](https://github.com/hwchase17/langchain)

## License

Distributed under the MIT License. See [LICENSE](https://github.com/AvaterClasher/librarian/blob/main/LICENSE) for more information.