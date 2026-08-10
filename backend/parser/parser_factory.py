from backend.parser.txt_parser import TxtParser
from backend.parser.docx_parser import DocxParser
from backend.parser.pdf_parser import PdfParser


class ParserFactory:

    @staticmethod
    def get_parser(file_type: str):

        file_type = file_type.lower()

        if file_type == ".txt":
            return TxtParser()

        if file_type == ".docx":
            return DocxParser()

        if file_type == ".pdf":
            return PdfParser()

        raise ValueError(f"Unsupported parser: {file_type}")