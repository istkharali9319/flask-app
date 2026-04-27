from openai import OpenAI
import os
from app.models.conversation import Conversation
import requests

api_key=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# 🔁 Toggle (False = no OpenAI call)
use_open_ai = os.getenv("USE_OPEN_AI")
google_api_key = os.getenv("GOOGLE_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")


# ✅ Keep static response outside
STATIC_AI_RESPONSE = """Hi there! How can I help you today?

I can assist with:
- Answering questions and explaining topics
- Writing and editing (emails, essays, resumes, stories)
- Coding help and debugging
- Math problems (step-by-step)
- Planning, brainstorming, and ideas

What would you like to do? If you’re unsure, tell me your goal and I’ll suggest the next step.
"""


class AiService:

    @staticmethod
    def generate_response(user_message):

        if not use_open_ai:
           return call_gemini_ai(user_message)

        messages = [
            {"role": "user", "content": user_message}
        ]

        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=messages
        )

        return response.choices[0].message.content
        
    # Http request for the OpenAi

    def call_openai_api(user_message):
        # return api_key
        headers = {
            "Authorization":f"Bearer {api_key}",
            "Content-Type":"application/json"
            }

        payload = {
            "model":"gpt-5-nano",
            "messages":[
               {
                 "role":"user",
                "content":user_message
               }
            ]
        }
        api_end_point = "https://api.openai.com/v1/chat/completions"
        response = requests.post(
            api_end_point,
            headers = headers,
            json= payload
        )
        
        return response.json()['choices'][0]['message']['content']
    
    def call_gemini_ai(user_message):
        gemini = OpenAI(base_url=gemini_base_url, api_key=google_api_key)
        response = gemini.chat.completions.create(
            model="gemini-2.5-flash-lite", 
            messages=[{
                    "role": "user", 
                    "content": user_message
                }])
        return response.choices[0].message.content
        