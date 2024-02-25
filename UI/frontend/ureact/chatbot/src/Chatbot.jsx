import React from 'react';
import { Chatbot } from 'react-chatbot-kit';

const config = {
  // Configuration options for the chatbot
};

const ChatbotComponent = () => {
  return (
    <div className="chatbot-container">
      <Chatbot config={config} />
    </div>
  );
};

export default ChatbotComponent;