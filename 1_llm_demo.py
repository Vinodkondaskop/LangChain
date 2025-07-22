#This code is for the LLMs and they are now not that much used instead of this chat models are been utilized more
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Load environment variables 
load_dotenv()

# Instantiate Gemini with API key from AI Studio
Chat_Model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")  # Make sure this is set in .env as the api key is there in the .env file 
)

# Prompt
response = Chat_Model.invoke("Who is the president of India?")
print(response.content) # This provides only the content which is needed not the additional_kwargs, response_metadata 


