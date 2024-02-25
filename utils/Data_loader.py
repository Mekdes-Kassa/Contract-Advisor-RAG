from langchain_community.document_loaders import PyPDFLoader
import os

class DatasetLoader:
    def __init__(self):
        pass

    def load_dataset_from_pdf(self, pdf_file_path):
        """
        Load a dataset from a PDF file.

        Args:
        - pdf_file_path (str): The path to the PDF file.

        Returns:
        - documents (list): A list of documents loaded from the PDF file.
        """
        # Check if the file exists
        if not os.path.isfile(pdf_file_path):
            print("File does not exist.")
            return None

        # Check if the file is a PDF file
        if not pdf_file_path.endswith(".pdf"):
            print("File is not a PDF file.")
            return None

        # Initialize the PyPDFLoader with the PDF file path
        loader = PyPDFLoader(pdf_file_path)
        
        # Load the documents from the PDF file
        documents = loader.load()
        
        return documents

# Example usage:
#file_path = "/content/Raptor Contract.docx.pdf"
#loader = DatasetLoader()
#documents = loader.load_dataset_from_pdf(file_path)