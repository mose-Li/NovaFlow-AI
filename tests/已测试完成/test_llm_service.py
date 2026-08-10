from backend.llm.llm_service import LLMService

llm = LLMService()

answer = llm.chat(
    "Hello NovaFlow AI"
)

print(answer)