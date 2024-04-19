const {createApp} = Vue
createApp({
    data() {
        return {
            websocketUrl: 'ws://api.cityfarm.com/ws/status/',
            connections: [],
            broadcastConnection: this.buildConnection('broadcast'),
            reconnectInterval: 5000,
        }
    },
    mounted() {
        this.connect(this.broadcastConnection)
    },
    methods: {
        buildConnection(userType) {
            const user_hash = Math.random().toString(36).slice(2)
            return {
                token: `${userType}-${user_hash}`,
                status: 'Disconnected',
                connected: false,
                messages: [],
                socket: null,
                sendMessage: '' // Field for typed message
            }
        },
        addConnection(userType) {
            this.connections.push(this.buildConnection(userType));
        },
        toggleConnection(connection) {
            if (connection.connected) {
                this.disconnect(connection);
            } else {
                this.connect(connection);
            }
        },
        connect(connection) {
            connection.socket = new WebSocket(`${this.websocketUrl}?token=${encodeURIComponent(connection.token)}`);

            connection.socket.onopen = () => {
                connection.status = 'Connected';
                connection.connected = true;
            };

            connection.socket.onmessage = (event) => {
                connection.messages.push(event.data);
            };

            connection.socket.onclose = () => {
                connection.status = 'Disconnected';
                connection.connected = false;
            };

            connection.socket.onerror = (error) => {
                console.error('WebSocket Error:', error);
            };
        },
        disconnect(connection) {
            if (connection.socket) {
                connection.socket.close();
                connection.socket = null; // Clear the socket reference
                connection.status = 'Disconnected';
                connection.connected = false;
            }
        },
        sendMessage(connection) {
            if (connection.socket && connection.socket.readyState === WebSocket.OPEN && connection.sendMessage.trim() !== '') {
                let messageJSON = JSON.stringify({
                    type: "echo.message",
                    message: connection.sendMessage
                });
                connection.socket.send(messageJSON);
                connection.sendMessage = ''; // Clear the input after sending the message
            } else {
                alert('Connection is not open or message is empty.');
            }
        }
    }
}).mount('#app');