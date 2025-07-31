# from dotenv import load_dotenv
# import os
# import openai

# load_dotenv()  
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def summarize_content(text, topic):
#     prompt = f"Summarize the following for a student presentation on '{topic}':\n{text}"
    
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.5,
#         max_tokens=800
#     )
    
#     return response.choices[0].message.content.strip()

from openai import OpenAI

def summarize_content(text, topic, api_key):
    prompt = f"Summarize the following content about {topic}:\n\n{text}"

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800
    )

    return response.choices[0].message.content

