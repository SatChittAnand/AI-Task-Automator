
## AI Task Automator 🧠➡️📊

AI Task Automator is a Gradio-based, agent-powered slide generation tool that transforms any given topic into a structured PowerPoint presentation (`.pptx`). Designed for modularity, clarity, and customization, it uses intelligent components to research, summarize, and build polished slide decks.

---

## 🗂️ Project Structure

```
ai-task-automator/
├── app/                 
│   ├── app/            # Gradio interface and launch logic
│   ├── init.py         # App entry point
│   ├── searcher.py       # Topic enrichment and content retrieval agents
│   ├── slide_maker.py     # Slide construction and formatting logic
│   ├── summarizer.py     # Text summarization and outline generation
│   ├── utils.py          # Helper functions (text processing, file handling)
├── main.py                # Orchestrator coordinating pipeline across modules
├── README.md           # Project documentation
├── LICENSE             # MIT License
├── .env                # API keys and environment variables
├── requirements.txt    # Python dependencies
├── example.pptx        # Sample output deck (auto-generated)
```

---

## 🚀 Features

- **Modular Agents**: Specialized components for search, summarization, slide creation
- **Gradio Frontend**: Clean, responsive UI for topic input and `.pptx` downloads
- **Custom Templates**: Drop in your own branded presentation styles
- **Batch Mode**: Supports multi-topic deck generation with progress tracking
- **Easy Extensibility**: Add new agents or tweak presentation behavior with minimal friction

---

## 🧪 Quickstart

```bash
git clone https://github.com/SatChittAnand/AI-Task-Automator.git
cd ai-task-automator
pip install -r requirements.txt
python ai/init.py
```

Then open `http://localhost:7860` in your browser.

---

## ✍️ Usage

Through Gradio:
1. Enter a topic (e.g., "History of LLMs")
2. Hit “Generate Slides”
3. Download the `.pptx` deck

Through Python CLI:
```python
from ai.main import generate_pptx

generate_pptx("Generative AI and Its Applications", template="default.pptx")
```

---

## 📄 License

MIT License. See [[LICENSE]](https://github.com/SatChittAnand/AI-Task-Automator?tab=MIT-1-ov-file) for full terms.

---

## 👨‍💻 Author

Built by Satyanarayan with 💓, passionate about modular automation, agentic design, and workflow clarity. For contributions, feedback, or feature requests, open an issue or submit a PR!

---

