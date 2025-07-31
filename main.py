from dotenv import load_dotenv
import os
from app.searcher import search_topic
from app.summarizer import summarize_content
from app.slide_maker import generate_slides

load_dotenv()  # Load .env

openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    raise Exception("OpenAI API Key not found in .env")

print("🔍 AI Task Automator for Students")
topic = input("Enter a topic: ")

# Step 1: Search
print("Searching Google...")
raw = search_topic(topic)

# Step 2: Summarize
print("Summarizing content...")
summary = summarize_content(raw, topic, openai_key)

# Step 3: Generate Slides
print("Generating slide deck...")
file_path = generate_slides(summary, topic, bullets_per_slide=4)


print(f"✅ Done! Presentation saved as: {file_path}")

