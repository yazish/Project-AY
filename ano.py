from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import pandas as pd
import os
os.environ["OPENAI_API_KEY"] = r"***************************"

loader = CSVLoader(file_path=r'./dateset.csv')    

# Create an index using the loaded documents
index_creator = VectorstoreIndexCreator()
docsearch = index_creator.from_loaders([loader])

chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.vectorstore.as_retriever(), input_key="question")
query = input("Type the Query  ")
response = chain({"question": query})
print(response['result'])
print("--------------------------------")

