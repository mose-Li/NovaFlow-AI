from pypdf import PdfReader


class PdfParser:

    def parse(self, file_path: str) -> str:

        reader = PdfReader(file_path)

        contents = []

        for page in reader.pages:

            text = page.extract_text()

            if text:
                contents.append(text)

        return "\n".join(contents)