import streamlit as st
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
class AI:
    def __init__(self,key):
        template = """
You are a black pepper expert chatbot.

Current conversation:
{history}

Human: {input}
AI:
"""
        key =  key
        llm = ChatGroq(model="llama-3.1-8b-instant",api_key=key)
        prompt = PromptTemplate(input_variables=["history", "input"],template=template)  
        self.conversationChain = ConversationChain(
            llm=llm,
            prompt=prompt,
            verbose=True,
            memory=ConversationBufferMemory())
       
    def askAI(self,prompt):
        response  = self.conversationChain.predict(input=prompt)
        st.write(response)


st.title("Black pepper info chat bot")
st.write("Hello! I am your black pepper expert. Ask me anything about black pepper. Type 'exit' to end the conversation.")
key = st.text_input("Enter API key", type="password")

if not key:
    st.warning("Please enter your Groq API key to start using the chatbot.")
    st.stop()
topics = [
    "Black pepper cultivation and plantation management",
    "Pest and disease management",
    "Irrigation, nutrition, and yield optimization",
    "Harvesting and post-harvest handling",
    "Black pepper market analysis and pricing trends",
    "Export/import trade dynamics",
    "Logistics, warehousing, moisture control, and quality grading",
    "Commodity trading and risk management",
    "Supply chain and procurement strategy",
    "Farm economics and operational planning",
]
ai = AI(key)
for topic in topics:
   clicked =  st.button(topic)
   if clicked:
      ai.askAI(topic)
input = st.text_input("Prompt")
if input:
    ai.askAI(input)
   

