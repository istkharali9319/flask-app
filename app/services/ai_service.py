from openai import OpenAI
import os
from app.models.conversation import Conversation

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🔁 Toggle (False = no OpenAI call)
USE_OPENAI = False

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

        if not USE_OPENAI:
            return STATIC_AI_RESPONSE

        messages = [
            {"role": "user", "content": user_message}
        ]

        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=messages
        )

        return response.choices[0].message.content