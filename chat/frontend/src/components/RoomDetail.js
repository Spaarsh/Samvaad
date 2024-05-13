import React, { useEffect, useState, useRef } from 'react';
import WebSocket from 'react-websocket';

const RoomDetail = ({ room, user, messages }) => {
    const [messageInput, setMessageInput] = useState('');
    const [chatLog, setChatLog] = useState(messages);
    const socketRef = useRef(null);

    const handleData = (data) => {
        const result = JSON.parse(data);
        setChatLog([...chatLog, result]);
    };

    const sendMessage = (event) => {
        event.preventDefault();
        const messageObject = {
            message: messageInput,
            user_id: user.id,
            room_id: room.id,
            timestamp: new Date().toISOString()
        };
        socketRef.current.sendMessage(JSON.stringify(messageObject));
        setMessageInput('');
    };

    return (
        <div>
            {/* Add your CSS styles here */}
            <div className="left-margin"></div>
            <div id="logo">
                {/* Add your image here */}
            </div>
            <div id="header">
                <h2>{room.name}</h2>
            </div>
            <div id="chat-log">
                {chatLog.map((message, index) => (
                    <div key={index} className={`message ${message.user === user ? 'self' : 'other'}`}>
                        <strong>{message.user.username}:</strong> {message.content}
                        <div className="timestamp">{message.timestamp}</div>
                    </div>
                ))}
            </div>
            <form id="post-message" onSubmit={sendMessage}>
                <input type="text" id="message-input" placeholder="Enter your awesome message here" value={messageInput} onChange={(e) => setMessageInput(e.target.value)} />
                <button type="submit">Send</button>
            </form>
            <WebSocket url={`ws://${window.location.host}/ws/room/${room.name}/`} onMessage={handleData} ref={socketRef} />
        </div>
    );
};

export default RoomDetail;