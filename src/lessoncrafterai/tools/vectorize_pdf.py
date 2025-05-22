from crewai.tools import BaseTool
from pydantic import Field
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

class VectorizePDFTool(BaseTool):
    name: str = "VectorizePDF"
    description: str = "Loads and vectorizes a PDF curriculum document"
    pdf_path: str = Field(..., description="Path to the curriculum PDF")
    persist_dir: str = Field(..., description="Directory to store the vector DB")

    def _run(self, *args, **kwargs) -> str:
        os.makedirs(self.persist_dir, exist_ok=True)

        if not os.path.exists(self.pdf_path):
            return f"File not found: {self.pdf_path}"

        loader = PyPDFLoader(self.pdf_path)
        pages = loader.load()

        if not pages:
            return "PDF has no content."

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = splitter.split_documents(pages)

        vectordb = Chroma.from_documents(docs, OpenAIEmbeddings(), persist_directory=self.persist_dir)
        vectordb.persist()

        return f"Vectorized {len(docs)} chunks from {self.pdf_path}."
