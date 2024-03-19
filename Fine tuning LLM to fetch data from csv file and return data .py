

import os 

from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import pyttsx3   
import speech_recognition as sr

import os;

os.environ['OPENAI_API_KEY']='OPENAI API KEY'
from langchain.llms import OpenAI
llm=OpenAI(temperature=0.6)
from langchain.document_loaders.csv_loader import CSVLoader

loader=CSVLoader(file_path='C:/Users/hriti/Downloads/prompt_engineering_dataset.csv',source_column='Prompt')
data=loader.load()


from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
instructor_embeddings=HuggingFaceInstructEmbeddings()

vectordb=FAISS.from_documents(documents=data, embedding=instructor_embeddings)
 
retriever=vectordb.as_retriever()

def speak(text): 
    engine = pyttsx3.init()
    id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty("voices",id)
    engine.say(text=text)
    engine.runAndWait()

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



from langchain.chains import RetrievalQA
qa=RetrievalQA.from_chain_type(
                        llm=llm,
                        chain_type="stuff",
                        retriever=retriever,
                        input_key="query",
                        return_source_documents=True)

from langchain.llms import OpenAI
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever, return_source_documents=True)
speech = " summarize plot romeo julet and what is quantam mechanics?"
result = qa({"query": speech})
result

speak(ans)

