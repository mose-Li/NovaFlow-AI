from pathlib import Path


class PromptBuilder:

    TEMPLATE_PATH = Path("prompts/rag_prompt.txt")

    @classmethod
    def build(
        cls,
        question: str,
        contexts: list,
    ):

        context_text = ""

        for index, item in enumerate(contexts, start=1):

            context_text += f"""
资料 {index}

{item["content"]}

----------------------------------------

"""

        template = cls.TEMPLATE_PATH.read_text(
            encoding="utf-8"
        )

        prompt = template.replace(
            "{contexts}",
            context_text.strip(),
        )

        prompt = prompt.replace(
            "{question}",
            question,
        )

        return prompt