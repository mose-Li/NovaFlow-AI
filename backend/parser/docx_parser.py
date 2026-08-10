from docx import Document


class DocxParser:

    def parse(self, file_path: str) -> str:

        doc = Document(file_path)

        paragraphs = []

        for p in doc.paragraphs:
            if p.text.strip():
                paragraphs.append(p.text)

        return "\n".join(paragraphs)