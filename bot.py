import os
from openai import OpenAI
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# Забираем ключи (мы их передадим позже)
VK_TOKEN = os.getenv("VK_TOKEN")
AI_TOKEN = os.getenv("AI_TOKEN")
GROUP_ID = "238580663" 

vk_session = vk_api.VkApi(token=VK_TOKEN)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, GROUP_ID)


ai_client = OpenAI(
    api_key=AI_TOKEN,
    base_url="https://openrouter.ai/api/v1"
)

print("Бот запущен! Ожидаю сообщения...")


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        msg = event.object.message
        user_text = msg["text"]
        peer_id = msg["peer_id"]
        
        
        response = ai_client.chat.completions.create(
            model="google/gemini-2.0-flash-001",
            messages=[{"role": "user", "content": user_text}]
        )
        
        reply = response.choices[0].message.content
        
        
        vk.messages.send(
            peer_id=peer_id,
            message=reply,
            random_id=0  
        )