import './App.css';

import React, { useEffect, useState } from 'react';
import RoomDetail from './RoomDetail';

const App = () => {
    const [userData, setUserData] = useState(null);

    useEffect(() => {
        // Fetch user data from Django backend using Fetch API
        fetch('http://localhost:8000/users/login/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Set the user data received from the backend
                setUserData(data);
            })
            .catch(error => {
                console.error('Error fetching user data:', error);
            });
    }, []);

    return (
        <div>
            <h1>My Chat App</h1>
            {userData && <RoomDetail user={userData} />}
        </div>
    );
};

export default App;
