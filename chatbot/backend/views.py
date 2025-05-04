"""Views."""

import os

import google.generativeai as genai
from dotenv import load_dotenv
from rest_framework import viewsets

from .models import Message
from .serializers import MessageSerializer
from .get_info import get_current_roster, get_upcoming_matches_and_tournaments, get_recent_achievements

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API')

genai.configure(api_key=GEMINI_API_KEY)

roster = get_current_roster()
conquistas = get_recent_achievements()
torneios = get_upcoming_matches_and_tournaments()


FURIA_INFO = f"""
# Informações sobre a FURIA Esports - Time de Counter-Strike

## Roster Atual (Abril 2025)
{roster}

## Conquistas Recentes
{conquistas}

## {torneios}

## Sobre a Organização
A FURIA Esports é uma organização brasileira fundada em 2017 por Jaime Pádua e André Akkari. A equipe de CS:GO se tornou uma das mais respeitadas do mundo, representando o Brasil em competições internacionais.

## Arena FURIA
Localizada em São Paulo, a Arena FURIA é o centro de treinamento e bootcamp do time. O espaço recebe regularmente eventos e encontros com fãs.

## Redes Sociais
- Twitter/X: @FURIA
- Instagram: @furiagg
- YouTube: FURIA Esports
- Twitch: furiatv
"""

SYSTEM_INSTRUCTION = f"""
Você é o assistente oficial do time de Counter-Strike da FURIA Esports. Seu objetivo é fornecer informações precisas e animadas sobre o time, responder perguntas dos fãs e manter todos atualizados sobre a agenda, resultados e notícias.

Você deve ser entusiasmado quando falar sobre as vitórias do time e otimista mesmo quando mencionar derrotas. Use um tom amigável e animado, como um verdadeiro torcedor da FURIA.

Quando não souber alguma informação específica, seja honesto, mas tente sempre direcionar a conversa para algo que você saiba sobre o time.

Aqui estão as informações atualizadas sobre o time para você usar em suas respostas:

{FURIA_INFO}

Lembre-se de ser conciso em suas respostas, mantendo-as informativas mas diretas.
"""


class MessageViewSet(viewsets.ModelViewSet):
    """Set Message View."""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        """Create perfom."""
        # Salva a mensagem do usuário
        message = serializer.save()

        # Processamento simples para criar resposta do bot
        if message.sender == 'user':
            recent_messages = Message.objects.order_by('-timestamp')[:10]

            # Formatar o histórico para enviar ao modelo
            conversation_history = []
            for msg in reversed(recent_messages):
                role = 'user' if msg.sender == 'user' else 'model'
                conversation_history.append({
                    'role': role,
                    'parts': [msg.content],
                })

            try:
                # Configurar o modelo
                model = genai.GenerativeModel(
                    generation_config={
                        'temperature': 0.7,
                        'max_output_tokens': 1024,
                    },
                    system_instruction=SYSTEM_INSTRUCTION,
                )

                # Iniciar a conversa com o histórico
                chat = model.start_chat(
                    history=conversation_history[:-1],
                )  # Excluir a mensagem atual

                # Obter resposta para a mensagem atual
                response = chat.send_message(message.content)

                # Extrair o texto da resposta
                bot_response = response.text

            except Exception as e:
                # Tratamento de erro caso a API falhe
                bot_response = """
                Desculpe, estou com dificuldades para processar
                sua mensagem no momento.
                """
                print(f'Erro na API Gemini: {e!s}')

            # Cria resposta do bot
            Message.objects.create(content=bot_response, sender='bot')