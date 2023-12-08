# flake8: noqa
from langchain.prompts import PromptTemplate

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
