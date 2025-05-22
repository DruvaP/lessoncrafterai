from crewai.tools import BaseTool
from pydantic import Field
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

class AnalyzeTopicsTool(BaseTool):
    name: str = "AnalyzeTopics"
    description: str = "Retrieves and summarizes curriculum topics from vector DB"
    persist_dir: str = Field(..., description="Vector store directory")

    def _run(self, *args, **kwargs) -> str:
        vectordb = Chroma(
            persist_directory=self.persist_dir,
            embedding_function=OpenAIEmbeddings()
        )
        retriever = vectordb.as_retriever(search_kwargs={"k": 5})

        qa = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(temperature=0.3),
            retriever=retriever,
            chain_type="stuff"
        )

        query = (
            "Extract a list of curriculum topics and their learning objectives. "
            "Format as JSON: [{\"topic\": ..., \"objectives\": [ ... ]}]"
        )

        return qa.run(query)
