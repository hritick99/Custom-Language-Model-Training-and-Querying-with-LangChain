#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 

from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import pyttsx3   
import speech_recognition as sr


# In[2]:


# load_dotenv()
# GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")


# In[3]:


import os;

os.environ['OPENAI_API_KEY']='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'
# os.environ['SERPAPI_API_KEY']='05f68f715ba6b389889cb88c5b0132e5f5cc8a345111d7d40c6b3cbb754a0984'


# In[ ]:





# In[4]:


from langchain.llms import OpenAI


# In[5]:


llm=OpenAI(temperature=0.6)


# In[6]:


# llm=ChatGoogleGenerativeAI(model="gemini-pro",google_api_key='AIzaSyA_PbY4n8vPwKnjfJQhDinpMiGbvI69EJk')


# In[7]:


# tweet_prompt=PromptTemplate.from_template("{write a poem on samosa}")

# tweet_prompt


# In[8]:


from langchain.document_loaders.csv_loader import CSVLoader

loader=CSVLoader(file_path='C:/Users/hriti/Downloads/prompt_engineering_dataset.csv',source_column='Prompt')
data=loader.load()


# In[9]:


data


# In[10]:


from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
instructor_embeddings=HuggingFaceInstructEmbeddings()

vectordb=FAISS.from_documents(documents=data, embedding=instructor_embeddings)
 
# e=embeddings.embed_query("What is your refund policy")


# In[11]:


retriever=vectordb.as_retriever()


# In[12]:


def speak(text): 
    engine = pyttsx3.init()
    id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty("voices",id)
    engine.say(text=text)
    engine.runAndWait()

speak("Hello sir")


# In[13]:


speak("Hello sir")

def speechrecognition():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        audio=r.listen(source,0,8)

    try:
        print("Recognizing")
        query=r.recognize_google(audio,language="en")
        return query.lower()

    except:
        return ""

speech=speechrecognition()
print(speech)


# In[ ]:





# In[14]:


from langchain.chains import RetrievalQA
qa=RetrievalQA.from_chain_type(
                        llm=llm,
                        chain_type="stuff",
                        retriever=retriever,
                        input_key="query",
                        return_source_documents=True)


# In[27]:


from langchain.llms import OpenAI
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever, return_source_documents=True)
speech = " summarize plot romeo julet and what is quantam mechanics?"
result = qa({"query": speech})
result


# In[28]:


ans=result['result']


# In[24]:


speak(ans)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




