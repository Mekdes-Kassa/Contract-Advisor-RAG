from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

class DatasetLoader:
    def __init__(self):
        pass
        
    def create_vector_store(self, documents):
            """
            Create a vector store from a list of documents.

            Args:
            - documents (list): A list of documents.

            Returns:
            - vectorstore: A vector store created from the documents.
            """
            # Initialize the text splitter
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=10, separators=["\n\n", "\n", ".", " ", ""])

            # Split documents into chunks
            docs = text_splitter.split_documents(documents)

            # Create vector store from documents
            vectorstore = Chroma.from_documents(docs, OpenAIEmbeddings())

            return vectorstore

# Example usage:
#file_path = "/content/Raptor Contract.docx.pdf"
#loader = DatasetLoader()
#documents = loader.load_dataset_from_pdf(file_path)
#if documents:
    #vectorstore = loader.create_vector_store(documents)