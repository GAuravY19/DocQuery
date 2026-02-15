import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
import secrets


class LLMPipeline:
    def __init__(self):

        load_dotenv()
        os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 150,
            separators=["\n\n", "\n"]
        )

        self.model = ChatGoogleGenerativeAI(
            model = 'models/gemini-2.5-flash',
            temperature = 1.0
        )

        self.template = ChatPromptTemplate(
            [
                ('system', '''You are a Q&A assistant. Given below is the details based on which you have to answer the users Query.
                 The answer should not have markdown text. It should be in plain text format.
                            Details:- {context}'''),
                ('user', '{user_query}')
            ]
        )

        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

    def loading_documents(self, doc_path):
        loader = PyPDFLoader(file_path = doc_path)
        document = loader.load()

        return document

    def chunk_embed_store(self, documents):
        chunks = self.text_splitter.split_documents(documents)
        vectorstore = FAISS.from_documents(
            documents=chunks,
            embedding=self.embeddings
        )

        vectorname = secrets.token_hex(8)
        vectorpath = os.path.join('D:/RAG/DocQuery/docquery/storage', vectorname)
        vectorstore.save_local(vectorpath)

        return (vectorname, vectorpath)

    def load_vectorstore(self, vectorpath):
        vectorstore = FAISS.load_local(
            vectorpath, self.embeddings, allow_dangerous_deserialization=True
        )

        return vectorstore

    def Retrieve(self, vectorstore):
        retriever = vectorstore.as_retriever(
            search_type = "similarity",
            search_kwargs = {'k':8}
        )

        return retriever

    def respond(self, docs, user_input):
        message = self.template.invoke({
                    "context": f'{docs}',
                    "user_query": f"{user_input}"
                })

        response = self.model.invoke(message)

        return response.content




