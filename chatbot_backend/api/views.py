from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API')

genai.configure(api_key=GEMINI_API_KEY)

SYSTEM_INSTRUCTION = """
Você é um assistente útil e amigável e faz parte do time de E-Sports da Fúria. Forneça respostas claras e concisas.
Mantenha suas respostas informativas mas breves sempre que possível.
"""

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def perform_create(self, serializer):
        # Salva a mensagem do usuário
        message = serializer.save()
        
        # Processamento simples para criar resposta do bot
        if message.sender == 'user':
            recent_messages = Message.objects.order_by('-timestamp')[:10]
            
            # Formatar o histórico para enviar ao modelo
            conversation_history = []
            for msg in reversed(recent_messages):
                role = "user" if msg.sender == "user" else "model"
                conversation_history.append({"role": role, "parts": [msg.content]})
            
            try:
                # Configurar o modelo
                model = genai.GenerativeModel(
                    generation_config={
                        "temperature": 0.7,
                        "max_output_tokens": 1024,
                    },
                    system_instruction=SYSTEM_INSTRUCTION,
                )
                
                # Iniciar a conversa com o histórico
                chat = model.start_chat(history=conversation_history[:-1])  # Excluir a mensagem atual
                
                # Obter resposta para a mensagem atual
                response = chat.send_message(message.content)
                
                # Extrair o texto da resposta
                bot_response = response.text
                
            except Exception as e:
                # Tratamento de erro caso a API falhe
                bot_response = "Desculpe, estou com dificuldades para processar sua mensagem no momento."
                print(f"Erro na API Gemini: {str(e)}")
            
            # Cria resposta do bot
            Message.objects.create(
                content=bot_response,
                sender='bot'
            )