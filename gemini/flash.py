import streamlit as st
import google.generativeai as genai
from google.generativeai import GenerativeModel

# Initialize the GenerativeModel
# Depending on the library, you might need to set up authentication separately.
genai.configure(api_key="AIzaSyDRVAhcGV7RDrm-_ttpNnS0Zns64iBqyBk")

model = genai.GenerativeModel("gemini-pro")

chat=model.start_chat(history=[])
def get_gemini_response(que):
    resp=chat.send_message(que,stream=True)
    return resp
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exis
if 'chat_history' not in st.session_state:
  st.session_state['chat_history'] = []
input=st.text_input("Input:",key="input")
submit=st.button("Ask the question")

if submit and input:
  response=get_gemini_response(input)
## Add user query and response to session chat history
  st.session_state['chat_history'].append(("You",input))
  st.subheader("The Response is")
  for chunk in response:
    st.write(chunk.text)
    st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader("The Chat history is")
for role, text in st.session_state['chat_history']:
  st.write(f"{role}: {text}")


