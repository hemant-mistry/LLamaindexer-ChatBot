from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import Settings
import os
from llama_index.llms.azure_openai import AzureOpenAI

Settings.embed_model = 'local'

api_key = ""
azure_endpoint = ""
api_version = "2024-02-15-preview"

llm = AzureOpenAI(
    model="gpt-35-turbo",
    deployment_name="GPT-35-4k",
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version=api_version,
)
Settings.llm = llm
documents = SimpleDirectoryReader('documents').load_data()

index = VectorStoreIndex.from_documents(documents)

chat_engine = index.as_chat_engine(verbose=True)

chat_engine.chat_repl()