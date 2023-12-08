<!-- @format -->

<h1 align="center">
Librarian 📖
</h1>

<p align="center">
   <img src="https://img.shields.io/github/license/AvaterClasher/librarian?style=for-the-badge" />
   <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" />
   <img src="https://img.shields.io/badge/OpenAI-000000?style=for-the-badge&logo=OpenAI&logoColor=white" />
   <img src="https://img.shields.io/badge/Quine-Quests_4-9FFF45?style=for-the-badge"/>
   <img src="https://img.shields.io/badge/Pip-3.10-000000?style=for-the-badge"/>
</p>

Upload your documents and get answers to your questions, with citations from the text.

Link to the deployed app: [Librarian GPT](https://librarian-gpt.streamlit.app)

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

-   User Interface - [Streamlit](https://streamlit.io/)
-   LLM Tooling - [Langchain](https://github.com/hwchase17/langchain)

## License

Distributed under the MIT License. See [LICENSE](https://github.com/AvaterClasher/librarian/blob/main/LICENSE) for more information.

## Acknowledgements

Thank you to [OpenAI](https://openai.com/) for providing the API and [Streamlit](https://streamlit.io/) for making it easy to build the UI.
And [Quine](quine.sh) for holding this awesome quest .