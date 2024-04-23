from transformers import pipeline
import giskard
from typing import Sequence, Optional
from giskard.llm.client import set_default_client
from giskard.llm.client.base import LLMClient, ChatMessage
from giskard.llm import set_llm_model
import pandas as pd
import os

os.environ["OPENAI_API_KEY"] = "openai api key here"

set_llm_model('gpt-3.5-turbo')

generator = pipeline('text-generation', model='gpt2')

def model_wrapper(df):
    return [generator(question, max_length=1000)[0]['generated_text'] for question in df['question'].values]

giskard_model = giskard.Model(
    model=model_wrapper,  # our model function
    model_type="text_generation",
    name="Chatbot for QA",
    description="This model is a chatbot",
    feature_names=["question"],  # input variables needed by your model
)
scan_res = giskard.scan(giskard_model)

scan_res.to_html('scan_res2.html')
# display(scan_res)


