---
title: "Research & Write Article Agent"
emoji: "📝"
colorFrom: "gray"
colorTo: "red"
sdk: "streamlit"
sdk_version: "1.47.0"
app_file: "app.py"
pinned: true
---

# 📝 Research & Write Article Agent

A fully automated **AI content creation assistant** powered by [CrewAI](https://github.com/joaomdmoura/crewai) and [Streamlit](https://streamlit.io/). This multi-agent system **researches, writes, and edits** high-quality articles on any topic with minimal human input.

<div align="center">
  <img src="images/demo_screenshot.png" width="80%" alt="App Demo Screenshot">
</div>

---

## 🚀 Features

- 🤖 **Multi-Agent System**: Planner, Writer, and Editor agents collaborate to deliver engaging and polished content.
- 🔎 **SEO-Optimized Research**: Each article is structured with trends, audience targeting, and ranking strategies.
- 📝 **Markdown & PDF Export**: Download the final article in both Markdown and clean PDF formats.
- 🎨 **Streamlit UI**: Clean and responsive interface for input, customization, and outputs.
- 🎯 **Custom Topic Input**: Generate full-length articles on any subject.
- 🔐 **Secure OpenAI API Integration**: Enter your key securely via `.env` or UI.

---

## 🏗️ Architecture Overview

### 👨‍💻 Components
- **Frontend**: Streamlit web app
- **Backend**: Multi-agent system via CrewAI

### 🧠 Agents
- **🧠 Content Planner**: Researches, outlines structure, suggests SEO and trends.
- **✍️ Content Writer**: Writes the article in Markdown based on plan.
- **🪄 Editor**: Polishes content with grammar, tone, and consistency checks.

### ⚙️ Workflow
1. **Plan** → Research, outline, SEO
2. **Write** → Draft article in Markdown
3. **Edit** → Final pass + PDF export

---

## 📁 Project Structure

```
Research-and-Write-Article-Agent/
├── app.py             # 🚀 Streamlit entry point
├── agents.py           # 🧠 Agent definitions
├── tasks.py            # 📎 Task pipeline & logic
├── utils.py            # 🔧 API key + helpers
├── requirements.txt    # 📦 Python dependencies
├── app.ipynb           # 📓 Notebook (optional testing)
├── README.md           # 📖 Documentation
└── images/
    └── demo_screenshot.png  # 🖼️ App screenshot
```

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/saadtoorx/research-write-article-agent.git
   cd research-write-article-agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your OpenAI API key:**
   - Create a `.env` file:
     ```env
     OPENAI_API_KEY=your-api-key-here
     ```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

- 🔐 Enter your OpenAI API key in the sidebar if not using `.env`
- ✍️ Input a topic and hit “Generate Article”
- 📂 Download as `.md` or `.docx`

---

## 📦 Tech Stack

- **Python 3.8+**
- [Streamlit](https://streamlit.io/)
- [CrewAI](https://github.com/joaomdmoura/crewai)
- [OpenAI API](https://platform.openai.com/)
- `dotenv`, `markdown-pdf`, `WeasyPrint`

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## 🤖 Agents Summary

| Agent           | Responsibilities                             |
|----------------|----------------------------------------------|
| **Planner**     | Researches, outlines, trends, SEO           |
| **Writer**      | Drafts structured article in Markdown       |
| **Editor**      | Proofreads, formats, and finalizes          |

---

## 🧠 Future Improvements

- 🔀 Integration with Gemini models
- 📊 Live keyword analysis for SEO
- 🗃️ Export options to HTML/Docx

---

## 📄 License

Licensed under the MIT License. See [`LICENSE`](LICENSE) for full terms.

---

## ✨ Built By

> Created with ❤️ by [Saad Toor](https://www.linkedin.com/in/saadtoorx/) (`@saadtoorx`)  
> Powered by CrewAI & Streamlit
