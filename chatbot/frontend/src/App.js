import React from 'react';
import styled from 'styled-components';
import './App.css';
import Chat from './components/Chat';

// Cores da FURIA
const colors = {
  black: '#0D0D0D',
  orange: '#FF5500',
  white: '#FFFFFF'
};

const AppContainer = styled.div`
  background-color: ${colors.black};
  min-height: 100vh;
  padding: 20px 0;
  color: ${colors.white};
  font-family: 'Roboto', 'Segoe UI', sans-serif;
`;

const Header = styled.header`
  text-align: center;
  margin-bottom: 30px;
`;

const Title = styled.h1`
  color: ${colors.white};
  font-size: 2.5rem;
  margin-bottom: 5px;
  font-weight: 900;
  
  span {
    color: ${colors.orange};
  }
`;

const Subtitle = styled.p`
  color: ${colors.white};
  opacity: 0.8;
  margin-bottom: 20px;
`;

const Footer = styled.footer`
  text-align: center;
  padding: 20px;
  font-size: 0.9rem;
  opacity: 0.7;
  margin-top: 30px;
`;

function App() {
  return (
    <AppContainer>
      <Header>
        <Title>
          <span>FURIA</span> CS:GO Assistant
        </Title>
        <Subtitle>
          Converse com o assistente oficial da equipe de Counter-Strike da FURIA Esports
        </Subtitle>
      </Header>
      <main>
        <Chat />
      </main>
      <Footer>
        © 2025 FURIA Esports Fan Project • Não oficial
      </Footer>
    </AppContainer>
  );
}

export default App;