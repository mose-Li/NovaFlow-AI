from backend.parser.parser_factory import ParserFactory

print(type(ParserFactory.get_parser(".txt")).__name__)
print(type(ParserFactory.get_parser(".docx")).__name__)
print(type(ParserFactory.get_parser(".pdf")).__name__)