#model instantiate, API Call, demo

import os
from http.client import responses

from dotenv import  load_dotenv
from langchain_groq import ChatGroq
from config import Config, prompt

load_dotenv()

class Model(object):
    def __init__(self)-> None :
        self.llm = ChatGroq(
            temperature=0.8,
            model="llama-3.1-8b-instant",
            groq_api_key=os.getenv("GroqKeyD")
        )
    def chat(self, message: str)-> str:
        sequence_chain = prompt | self.llm.with_structured_output(Config)
        try:
            data = {"user_message": message}
            #Running state
            response= sequence_chain.invoke(data)
            return response.msg
        except:
            error: str = "Error"
            return error

if __name__=="__main__":
    print(f"----------------Welcome User------------------")
    model = Model()
    while True:
        msg: str= input("Me: ")
        if len(msg) < 1:
            response = "Error"
            msg="..."
        response = model.chat(message=msg)
        print(f"WW:{response}")
        check: str = input("Exit? [y/n]:")
        if check.lower() == "y":
            break