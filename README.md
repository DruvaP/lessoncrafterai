# 📚 LessonCrafterAI

**LessonCrafterAI** is a multi-agent CrewAI application that transforms static curriculum PDFs into structured, ready-to-teach lesson plans. It leverages LangChain and OpenAI to automate topic extraction, lesson generation, assessment design, and resource recommendations for educators.

---

## 🚀 What It Does

LessonCrafterAI reads a curriculum PDF, analyzes its topics, and generates:

- ✅ Extracted topics and learning objectives
- ✅ Structured lesson plans with activities and durations
- ✅ Assessments (MCQs and short-answer questions)
- ✅ Supplemental teaching resources (e.g., videos, simulations)

All orchestrated via a chain of CrewAI agents.

---

## 🧠 How It Works

This project uses CrewAI’s YAML + Python hybrid architecture:

### 🧹 Agents

| Agent ID             | Role                         | Tool Used                       |
|----------------------|------------------------------|----------------------------------|
| `curriculum_ingestor` | Indexes the curriculum PDF   | `VectorizePDFTool`              |
| `topic_analyzer`      | Extracts key topics/goals    | `AnalyzeTopicsTool`             |
| `lesson_planner`      | Designs lesson plans         | `GenerateLessonsTool`           |
| `assessment_creator`  | Generates assessments        | `AssessTopicsTool`              |
| `resource_enhancer`   | Suggests learning resources  | `SupplementResourcesTool`       |

### 🔁 Task Flow (Sequential)

1. `vectorize_pdf_task`
2. `topic_analysis_task`
3. `lesson_planning_task`
4. `assessment_generation_task`
5. `resource_suggestion_task`

Each task passes context to the next for rich, end-to-end curriculum intelligence.

---

## 💠 Setup

### 1. Clone this repository

```bash
git clone https://github.com/your-org/lessoncrafterai.git
cd lessoncrafterai
```

### 2. Install dependencies

```bash
uv pip install -e .
```

Or with `crewAI`:

```bash
crewai install
```

### 3. Set environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=sk-...
```

> Optional if you're using local models.

---

## 📂 Project Structure

```
lessoncrafterai/
├── crew.py                    # Main CrewBase class and logic
├── main.py                    # Entry point: run, test, replay
├── tools/                     # Modular AI tools
│   ├── vectorize_pdf.py
│   ├── analyze_topics.py
│   ├── generate_lessons.py
│   ├── assess_topics.py
│   └── supplement_resources.py
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
├── knowledge/                # Contains your input curriculum PDF
│   └── sample_curriculum.pdf
└── pyproject.toml
```

---

## 🧪 Run the Crew

```bash
crewai run
```

Or directly:

```bash
python -m lessoncrafterai.main
```

---

## 🧠 Future Ideas

- Streamlit interface for drag-and-drop curriculum upload
- Customization by grade level or subject
- Export lesson plans to DOCX or PDF

---

## 👨‍💻 Built With

- [CrewAI](https://github.com/crewAIinc/crewai)
- [LangChain](https://www.langchain.com/)
- [OpenAI](https://platform.openai.com/)
- [ChromaDB](https://www.trychroma.com/)

---

## 📝 License

MIT License © 2024 CloudBridge AI
