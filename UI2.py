import streamlit as st
from streamlit_option_menu import option_menu
import os
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.memory import ConversationBufferMemory
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.elastic_vector_search import ElasticVectorSearch
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain.chains.question_answering import load_qa_chain

st.write("""
## Attractive LinkedIn Headlines
""")

col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("Work Experience")
   experience = st.radio("1", ["Over 20 years", "10-20 years", "less than 10 years" ], label_visibility= 'collapsed')

with col2:
   st.subheader("Role")
   role = st.radio("2", ["CXO", "Founder", "Data", "Sales", "HR" ], label_visibility= 'collapsed')

with col3:
   st.subheader("Industry")
   industry = st.radio("3", ["Tech", "Financial Services", "Consulting" ], label_visibility= 'collapsed')

context = 'I want you to write Headline for LinkedIn profiles.The headline should be professional and attractive. What is a good headline for a person who has '
prompt  = context + experience +' experience in '+ role + ' role in ' + industry + ' industry.'

context2 = """I want you to write Headline for LinkedIn profiles.
The headline should be professional and attractive.
Here are some examples of good headlines:
- Head of Insurance Analytics Solutions, Crain’s Notable Leader in Consulting
- Most Influential AI Leaders in India Top Analytics Leaders in India
- Helping smart managers keep their employees productive and engaged
- Helping to empower anyone to drive meaningful change through collaborative work
- Ecosystem Builder, Partnership Expert, Business Development Enthusiast, Startup Founder
- Everyone's favorite Tech Recruiter | Nerd at heart | Samwise Gamgee to your Frodo Baggins in recruiting
What is a good headline for a person who has """
prompt2  = context2 + experience +' experience in '+ role + ' role in ' + industry + ' industry.'

# template = """
# I want you to write Headline for LinkedIn profiles.The headline should be short, professional and attractive. What is a good headline for a person who has {input}?
# """
#
# prompt = PromptTemplate(
#     input_variables=[input],
#     template=template,
# )
llm = OpenAI(temperature=0.9)

st.write('>', llm(prompt))
st.write('>', llm(prompt2))

llm = OpenAI(model_name="text-davinci-003", n=2, best_of=2)
st.write('>', llm(prompt))
st.write('>', llm(prompt2))
