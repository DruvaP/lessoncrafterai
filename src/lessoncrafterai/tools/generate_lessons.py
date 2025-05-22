import json
from crewai.tools import BaseTool
from langchain_openai import ChatOpenAI
from pydantic import Field

class GenerateLessonsTool(BaseTool):
    name: str = "GenerateLessons"
    description: str = "Generate structured lesson plans from analyzed topics"

    def _run(self, *args, **kwargs) -> str:
        # Get raw string or object passed from previous task
        context_raw = kwargs.get("context", "")
        if not context_raw:
            return "No curriculum context provided."

        try:
            topics = json.loads(context_raw)  # Convert string to list of dicts
        except Exception as e:
            return f"Failed to parse context JSON: {e}"

        # Convert topics into readable prompt
        formatted = ""
        for t in topics:
            formatted += f"\nTopic: {t['topic']}\nObjectives:\n" + "\n".join(f"- {obj}" for obj in t["objectives"]) + "\n"

        prompt = (
            "You are an expert educator. Based on the following curriculum topics and learning objectives, "
            "generate a detailed lesson plan for each topic. Each plan should include:\n"
            "- Topic Title\n"
            "- Learning Objectives\n"
            "- Estimated Duration (in minutes)\n"
            "- Teaching Activities\n"
            "- In-class Examples or Demonstrations\n"
            "Return the lesson plans as a JSON array.\n"
            f"\nCurriculum:\n{formatted}"
        )

        llm = ChatOpenAI(temperature=0.4)
        return llm.predict(prompt)
