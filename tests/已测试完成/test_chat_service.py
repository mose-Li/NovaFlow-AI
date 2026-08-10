from backend.services.chat_service import ChatService

service = ChatService()

result = service.chat(
    question="Hello GPT"
)

print(result)