import React, { useState, useEffect, useRef } from 'react';
import styled from 'styled-components';
import axios from 'axios';

const API_URL = 'http://localhost:8000/backend/messages/';

// Cores da FURIA
const colors = {
  black: '#0D0D0D',
  orange: '#FF5500',  // Laranja vibrante da FURIA
  darkOrange: '#CC4400',
  lightGray: '#E5E5E5',
  darkGray: '#222222',
  white: '#FFFFFF'
};

const ChatContainer = styled.div`
  max-width: 500px;
  margin: 0 auto;
  border: 2px solid ${colors.orange};
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  height: 600px;
  box-shadow: 0 5px 15px rgba(255, 85, 0, 0.2);
  background-color: ${colors.black};
  font-family: 'Roboto', 'Segoe UI', sans-serif;
`;

const ChatHeader = styled.div`
  background-color: ${colors.black};
  color: ${colors.white};
  padding: 15px;
  display: flex;
  align-items: center;
  border-bottom: 2px solid ${colors.orange};
`;

const FuriaLogo = styled.div`
  font-weight: 900;
  font-size: 20px;
  color: ${colors.orange};
  margin-right: 10px;
  letter-spacing: 1px;
`;

const HeaderTitle = styled.div`
  font-weight: 600;
`;

const MessagesContainer = styled.div`
  padding: 16px;
  flex: 1;
  overflow-y: auto;
  background-color: ${colors.darkGray};
  background-image: linear-gradient(rgba(13, 13, 13, 0.7), rgba(13, 13, 13, 0.7)),
                    url('https://i.imgur.com/placeholder.png'); /* Substituir por uma textura sutil */
  background-size: cover;
  background-position: center;
`;

const MessageBubble = styled.div`
  max-width: 75%;
  padding: 12px 16px;
  margin-bottom: 12px;
  border-radius: 18px;
  background-color: ${props => props.isUser ? colors.orange : colors.darkGray};
  color: ${props => props.isUser ? colors.white : colors.white};
  align-self: ${props => props.isUser ? 'flex-end' : 'flex-start'};
  margin-left: ${props => props.isUser ? 'auto' : '0'};
  border: 1px solid ${props => props.isUser ? colors.darkOrange : '#333'};
  font-size: 15px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
  position: relative;
  
  &::after {
    content: '';
    position: absolute;
    bottom: 0;
    ${props => props.isUser ? 'right: -8px' : 'left: -8px'};
    width: 15px;
    height: 15px;
    background-color: ${props => props.isUser ? colors.orange : colors.darkGray};
    border-bottom: 1px solid ${props => props.isUser ? colors.darkOrange : '#333'};
    ${props => props.isUser ? 'border-right: 1px solid ' + colors.darkOrange : 'border-left: 1px solid #333'};
    transform: ${props => props.isUser ? 'rotate(45deg)' : 'rotate(45deg)'};
    border-radius: 0 0 ${props => props.isUser ? '0 5px' : '5px 0'};
    clip-path: ${props => props.isUser ? 'polygon(0 0, 100% 100%, 100% 0)' : 'polygon(0 100%, 100% 0, 0 0)'};
  }
`;

const InputForm = styled.form`
  display: flex;
  padding: 12px;
  border-top: 2px solid ${colors.orange};
  background-color: ${colors.black};
`;

const Input = styled.input`
  flex: 1;
  padding: 12px 16px;
  border: 1px solid ${colors.darkGray};
  border-radius: 24px;
  outline: none;
  background-color: ${colors.darkGray};
  color: ${colors.white};
  font-size: 15px;
  
  &:focus {
    border-color: ${colors.orange};
    box-shadow: 0 0 0 2px rgba(255, 85, 0, 0.2);
  }
  
  &::placeholder {
    color: #888;
  }
`;

const Button = styled.button`
  margin-left: 10px;
  padding: 12px 20px;
  border: none;
  border-radius: 24px;
  background-color: ${colors.orange};
  color: white;
  cursor: pointer;
  font-weight: 600;
  transition: background-color 0.2s;
  
  &:hover {
    background-color: ${colors.darkOrange};
  }
  
  &:disabled {
    background-color: #555;
    cursor: not-allowed;
  }
`;

const BotTypingIndicator = styled.div`
  color: ${colors.lightGray};
  font-style: italic;
  margin: 8px 0;
  font-size: 14px;
`;

function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  // Carregar mensagens ao iniciar
  useEffect(() => {
    fetchMessages();
  }, []);

  // Auto-scroll para novas mensagens
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const fetchMessages = async () => {
    try {
      const response = await axios.get(API_URL);
      setMessages(response.data);
    } catch (error) {
      console.error('Erro ao buscar mensagens:', error);
    }
  };

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    
    setLoading(true);
    
    try {
      // Enviar mensagem do usuário
      await axios.post(API_URL, {
        content: input,
        sender: 'user'
      });
      
      setInput('');
      
      // Buscar todas as mensagens (incluindo a resposta do bot)
      await fetchMessages();
    } catch (error) {
      console.error('Erro ao enviar mensagem:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <ChatContainer>
      <ChatHeader>
        <FuriaLogo>FURIA</FuriaLogo>
        <HeaderTitle>Assistente CS:GO</HeaderTitle>
      </ChatHeader>
      
      <MessagesContainer>
        {messages.map((msg) => (
          <MessageBubble key={msg.id} isUser={msg.sender === 'user'}>
            {msg.content}
          </MessageBubble>
        ))}
        {loading && (
          <BotTypingIndicator>O assistente da FURIA está digitando...</BotTypingIndicator>
        )}
        <div ref={messagesEndRef} />
      </MessagesContainer>
      
      <InputForm onSubmit={handleSubmit}>
        <Input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Pergunte sobre a FURIA CS:GO..."
          disabled={loading}
        />
        <Button type="submit" disabled={loading}>
          {loading ? '...' : 'Enviar'}
        </Button>
      </InputForm>
    </ChatContainer>
  );
}

export default Chat;