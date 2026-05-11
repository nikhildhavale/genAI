import streamlit as st
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
class AI:
    def __init__(self):
        template = """
You are a black pepper expert chatbot.

Current conversation:
{history}

Human: {input}
AI:
"""
        key =  "API_KEY"
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
ai = AI()
for topic in topics:
   clicked =  st.button(topic)
   if clicked:
      ai.askAI(topic)
input = st.text_input("Prompt")
if input:
    ai.askAI(input)
   

