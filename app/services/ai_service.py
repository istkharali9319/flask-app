from openai import OpenAI
import os
from html import escape
from app.models.conversation import Conversation
import requests

api_key=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


# 🔁 Toggle (False = no OpenAI call)
use_open_ai = os.getenv("USE_OPEN_AI")
google_api_key = os.getenv("GOOGLE_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")
ollama_base_url = os.getenv("OLLAMA_BASE_URL")
ollama = OpenAI(base_url = ollama_base_url, api_key = 'ollama')
gemini = OpenAI(base_url=gemini_base_url, api_key=google_api_key)

# Keep static response outside
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
    def generate_brochure_html(prompt, provider=None):
        brochure_prompt = (
            "Generate a clean, modern single-file company brochure in HTML only. "
            "Return only valid HTML markup for the brochure body content, without markdown fences. "
            "Use clear sections like hero, services, value proposition, and contact. "
            f"User request: {prompt}"
        )

        if provider and provider != "static":
            try:
                response = AiService.call_ai_service(brochure_prompt, provider)
                if response:
                    return response
            except Exception:
                pass

        return AiService.build_static_brochure(prompt)

    @staticmethod
    def call_ai_service(user_message,provider):

        if provider == 'ollama':
            return AiService.ollama_ai(user_message)
        elif provider == 'openai':
            return AiService.open_ai(user_message)
        elif provider == "gemini":
            return AiService.gemini_ai(user_message)
        else:
            return STATIC_AI_RESPONSE
        
    # Http request for the OpenAi
    def open_ai(user_message):
        messages = [
            {"role": "user", "content": user_message}
        ]

        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=messages
        )

        return response.choices[0].message.content
    
    # Make Http Request for the open ai
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
    
    def gemini_ai(user_message):
        response = gemini.chat.completions.create(
            model="gemini-2.5-flash-lite", 
            messages=[{
                    "role": "user", 
                    "content": user_message
                }])
        return response.choices[0].message.content
    
    def ollama_ai(user_message):
        response = ollama.chat.completions.create(
            # deepseek-r1:1.5b to do
            model="llama3.2",
            messages=[{"role": "user", "content": user_message}])

        return response.choices[0].message.content

    @staticmethod
    def build_static_brochure(prompt):
        safe_prompt = escape(prompt.strip() or "Professional sales growth company")
        short_title = safe_prompt[:80]

        return f"""<section style="font-family:Arial,sans-serif;background:linear-gradient(180deg,#fff8ef 0%,#f5efe6 100%);color:#1f2933;padding:0;">
  <div style="max-width:960px;margin:0 auto;padding:48px 24px;">
    <div style="background:#ffffff;border:1px solid #eadfce;border-radius:24px;padding:40px;box-shadow:0 18px 40px rgba(31,41,51,0.08);margin-bottom:24px;">
      <div style="display:inline-block;padding:8px 14px;border-radius:999px;background:#fff1db;color:#9a3412;font-size:12px;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:18px;">AI Brochure Draft</div>
      <h1 style="font-size:44px;line-height:1.05;margin:0 0 16px;">{short_title}</h1>
      <p style="font-size:17px;line-height:1.7;color:#52606d;margin:0 0 22px;">Built from your prompt: {safe_prompt}</p>
      <a href="#contact" style="display:inline-block;padding:14px 22px;background:#d97706;color:#ffffff;text-decoration:none;border-radius:999px;font-weight:700;">Book a Consultation</a>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;margin-bottom:24px;">
      <div style="background:#ffffff;border:1px solid #eadfce;border-radius:20px;padding:24px;">
        <h3 style="margin:0 0 10px;">Sales Strategy</h3>
        <p style="margin:0;color:#52606d;line-height:1.7;">Clarify positioning, tighten your offer, and create a pipeline that is easier to manage.</p>
      </div>
      <div style="background:#ffffff;border:1px solid #eadfce;border-radius:20px;padding:24px;">
        <h3 style="margin:0 0 10px;">Team Enablement</h3>
        <p style="margin:0;color:#52606d;line-height:1.7;">Give your team stronger messaging, objection handling, and a repeatable sales rhythm.</p>
      </div>
      <div style="background:#ffffff;border:1px solid #eadfce;border-radius:20px;padding:24px;">
        <h3 style="margin:0 0 10px;">Performance Insight</h3>
        <p style="margin:0;color:#52606d;line-height:1.7;">Track what is working, improve conversion points, and focus on decisions that grow revenue.</p>
      </div>
    </div>
    <div style="display:grid;grid-template-columns:1.2fr 0.8fr;gap:18px;">
      <div style="background:#ffffff;border:1px solid #eadfce;border-radius:20px;padding:28px;">
        <h2 style="margin:0 0 12px;">Why clients choose us</h2>
        <p style="margin:0 0 12px;color:#52606d;line-height:1.7;">We turn broad ideas into clear sales messaging, structured outreach, and polished buyer conversations.</p>
        <p style="margin:0;color:#52606d;line-height:1.7;">This draft can be refined further based on your audience, product, tone, and preferred call to action.</p>
      </div>
      <div id="contact" style="background:#fff7ed;border:1px solid #f3d5b3;border-radius:20px;padding:28px;">
        <h2 style="margin:0 0 12px;">Contact</h2>
        <p style="margin:0 0 8px;color:#52606d;line-height:1.7;">hello@companybrochure.ai</p>
        <p style="margin:0 0 8px;color:#52606d;line-height:1.7;">+1 (555) 123-4567</p>
        <p style="margin:0;color:#52606d;line-height:1.7;">Request a custom brochure version for your business.</p>
      </div>
    </div>
  </div>
</section>"""

    @staticmethod
    def call_ai_stream(user_message, provider, system_prompt):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]

        if provider == "ollama":
            # For local models like llama3.2 or deepseek-r1
            response = ollama.chat.completions.create(
                model="llama3.2", # or "deepseek-r1:1.5b"
                messages=messages,
                stream=True
            )
            for chunk in response:
                # Ollama returns a dictionary for each chunk
                yield chunk['message']['content']

        elif provider == "openai":
            # For cloud-based GPT models
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                stream=True
            )
            for chunk in response:
                # OpenAI returns an object; we check for content in delta
                content = chunk.choices[0].delta.content
                if content:
                    yield content
        elif provider == "gemini":
            response = gemini.chat.completions.create(
                model="gemini-2.5-flash-lite",
                messages=messages,
                stream=True
            )

            for chunk in response:
                content = chunk.choices[0].delta.content
                if content:
                    yield content

