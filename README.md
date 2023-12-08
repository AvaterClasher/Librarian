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

Who is this repository for?
This repository is for anyone who wants to easily access information from their documents and find answers to their questions with citations. It is particularly helpful for researchers, students, and anyone who works with large amounts of text data.

Why did I make this repository?
I made this repository because I was tired of spending hours searching through documents and manually finding citations for my research. I wanted to create a tool that would make it easier for me and others to access and analyze information from text documents.

I am also interested in the potential of large language models like GPT-3 to revolutionize the way we interact with information. I believe that Librarian can be a valuable tool for anyone who wants to harness the power of AI to improve their research and learning workflows.

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