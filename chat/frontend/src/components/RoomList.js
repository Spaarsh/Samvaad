import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

const RoomList = () => {
    const [rooms, setRooms] = useState([]);

    useEffect(() => {
        // Replace 'http://localhost:8000/api/rooms/' with the URL of your Django rooms API
        fetch('http://localhost:8000/api/rooms/')
            .then((response) => response.json())
            .then((data) => setRooms(data));
    }, []);

    return (
        <div>
            <h2>Rooms</h2>
            <ul>
                {rooms.length > 0 ? (
                    rooms.map((room) => (
                        <li key={room.name}>
                            <Link to={`/rooms/${room.name}`}>{room.name}</Link>
                        </li>
                    ))
                ) : (
                    <li>No rooms available.</li>
                )}
            </ul>
        </div>
    );
};

export default RoomList;