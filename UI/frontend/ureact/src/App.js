// frontend/src/App.js
import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
    const [input, setInput] = useState('');
    const [messages, setMessages] = useState([]);

    const sendMessage = async () => {
        if (!input.trim()) return;

        setMessages([...messages, { text: input, sender: 'user' }]);
        setInput('');

        const response = await axios.post('/generate', { prompt: input });
        setMessages([...messages, { text: response.data.response, sender: 'bot' }]);
    };

    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
            sendMessage();
        }
    };

    return (
        <div>
            <div className="chat-container">
                {messages.map((message, index) => (
                    <div key={index} className={`message ${message.sender}`}>
                        {message.text}
                    </div>
                ))}
            </div>
            <div className="input-container">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={handleKeyDown}
                    placeholder="Type your message here..."
                />
                <button onClick={sendMessage}>Send</button>
            </div>
        </div>
    );
};

export default App;
