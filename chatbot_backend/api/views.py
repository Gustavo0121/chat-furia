from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def perform_create(self, serializer):
        # Salva a mensagem do usuário
        message = serializer.save()
        
        # Processamento simples para criar resposta do bot
        if message.sender == 'user':
            # Lógica simples para resposta
            user_text = message.content.lower()
            
            if 'olá' in user_text or 'oi' in user_text:
                bot_response = "Olá! Como posso ajudar?"
            elif 'ajuda' in user_text:
                bot_response = "Estou aqui para responder perguntas. O que deseja saber?"
            else:
                bot_response = "Entendi sua mensagem. Como posso ajudar mais?"
                
            # Cria resposta do bot
            Message.objects.create(
                content=bot_response,
                sender='bot'
            )