from abc import ABC,abstractmethod

class DocumentProcessor(ABC):
    def __init__(self,file_name):
        self.file_name = file_name
    @abstractmethod
    def load(self,format):
        pass
    @abstractmethod
    def extract_text(self,format):
        pass
    def show_file_info(self):
        print(f"File name: {self.file_name}")
class PDFProcesser(DocumentProcessor):
    def load (self,format):
        print(f"Loading {format}....")
    def extract_text (self,format):
        return f"Extracting text from {format}...."
class TextProcessor(DocumentProcessor):
    def load (self,format):
        print(f"Loading {format}....")
    def extract_text (self,format):
        print(f"Extracting text from {format}....")
pdf = PDFProcesser("report.pdf")
pdf.show_file_info()
pdf.load("PDF")
print(pdf.extract_text("PDF"))
print()
text = TextProcessor("assignment.txt")
text.show_file_info()
text.load("Text")
text.extract_text("Text")
    
