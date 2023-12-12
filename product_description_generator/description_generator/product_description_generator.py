# description_generator/product_description_generator.py

from __future__ import annotations
import os
import openai
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from typing import Any
from langchain.base_language import BaseLanguageModel
from langchain.chains.llm import LLMChain
import gradio as gr

# Define your OpenAI API key here
OPENAI_API_KEY = "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"

prompt_file = "prompt_template.txt"

class ProductDescGen(LLMChain):
    """LLM Chain specifically for generating multi-paragraph rich text product descriptions using emojis."""

    @classmethod
    def from_llm(
        cls, llm: BaseLanguageModel, prompt: str, **kwargs: Any
    ) -> ProductDescGen:
        """Load ProductDescGen Chain from LLM."""
        return cls(llm=llm, prompt=prompt, **kwargs)

def product_desc_generator(product_name, keywords):
    with open(prompt_file, "r") as file:
        prompt_template = file.read()

    PROMPT = PromptTemplate(
        input_variables=["product_name", "keywords"], template=prompt_template
    )
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.7,
        openai_api_key=OPENAI_API_KEY,  # Use the defined API key
    )

    ProductDescGen_chain = ProductDescGen.from_llm(llm=llm, prompt=PROMPT)
    ProductDescGen_query = ProductDescGen_chain.apply_and_parse(
        [{"product_name": product_name, "keywords": keywords}]
    )
    return ProductDescGen_query[0]["text"]

# ... (other code related to Gradio interface if needed)
