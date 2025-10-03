# CLI-ChatApp

A real-time, multi-threaded chat server application built with Python sockets that supports group chats, direct messaging, and multiple concurrent connections.

## 🚀 Features

- **Real-time Communication**: Instant message delivery using TCP sockets
- **Multi-threaded Architecture**: Handles multiple clients simultaneously with Python threading
- **Group Chat Rooms**: Create and join multiple chat rooms (hosts)
- **Direct Messaging**: Send private messages to specific users
- **Concurrent Send/Receive**: Non-blocking message handling with separate threads
- **Connection Management**: Graceful handling of client connections and disconnections

## 🛠️ Technical Implementation

### Core Technologies
- **Python Socket Programming**: TCP/IP communication using `socket` module
- **Threading**: Concurrent client handling with `threading` module
- **Client-Server Architecture**: Separate client and server implementations

### Key Concepts Applied

**Network Programming**
- Socket creation and binding
- TCP connection establishment
- Message encoding/decoding (UTF-8)
- Client-server communication protocol

**Concurrency**
- Multi-threaded server for handling multiple clients
- Daemon threads for background message receiving
- Thread-safe data structures (dictionaries and sets)

**Data Structures**
- Dictionary for client username-to-socket mapping
- Sets for tracking users in group chats
- Efficient O(1) lookup for message routing

## 📋 Architecture

```
chat_server/
├── server/
│   ├── server.py       # Main server loop and client acceptance
│   ├── handlers.py     # Client message handling and routing
│   ├── host.py         # Group chat management functions
│   └── config.py       # Server configuration
└── client/
    ├── client.py       # Main client connection logic
    ├── sender.py       # Message sending thread
    ├── reciever.py     # Message receiving thread
    └── config.py       # Client configuration
```

## 🎯 Usage

### Starting the Server

```bash
cd chat_server/server
python server.py
```

The server will start listening on your local IP address at port 9000.

### Connecting as a Client

```bash
cd chat_server/client
python client.py
```

Enter your username when prompted to join the chat.

## 💬 Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/join <host>` | Create or join a group chat | `/join developers` |
| `#<host> <message>` | Send message to a group | `#developers Hello team!` |
| `@<user> <message>` | Send direct message to user | `@john Hey there!` |
| `quit` | Exit the chat | `quit` |
| `/help` | Display command reference | `/help` |

## 🔧 How It Works

### Server-Side Flow

1. **Server Initialization**: Creates socket, binds to IP:PORT, and starts listening
2. **Client Acceptance**: Accepts incoming connections in the main loop
3. **Thread Spawning**: Creates a new thread for each client connection
4. **Message Routing**: 
   - Parses incoming messages for command type (`#`, `@`, `/join`)
   - Routes group messages to all members in that host
   - Routes direct messages to specific users
   - Manages host membership

### Client-Side Flow

1. **Connection**: Connects to server and sends username
2. **Dual Threading**:
   - **Sender Thread**: Handles user input and sends to server
   - **Receiver Thread**: Continuously listens for incoming messages
3. **Non-blocking I/O**: User can send and receive messages simultaneously

### Message Protocols

**Group Message**: `#<host_name> <message>`
- Server broadcasts to all users in the specified host except sender

**Direct Message**: `@<username> <message>`
- Server sends directly to the target user if online

**Join Host**: `/join <host_name>`
- Adds user to the host's member set
- Creates host if it doesn't exist

## 🧠 Learning Outcomes

- Implemented socket programming for network communication
- Applied multi-threading for concurrent client handling
- Designed a custom message protocol for different chat features
- Managed shared state across threads (clients and hosts dictionaries)
- Handled connection errors and edge cases gracefully
- Practiced modular code organization and separation of concerns

## ⚙️ Configuration

Default settings in `config.py`:
```python
IP = socket.gethostbyname(socket.gethostname())  # Auto-detect local IP
PORT = 9000
ENCODER = "utf-8"
```

## 🐛 Known Limitations

- No persistent message storage
- No user authentication
- Limited to local network (can be modified for external hosting)

## 🔮 Future Enhancements

- [ ] Add message encryption for secure communication
- [ ] Implement user authentication and authorization
- [ ] Add message history and persistence
- [ ] Create a GUI client interface
- [ ] Support file sharing capabilities
- [ ] Add typing indicators and read receipts

## 📝 License

This project is for educational purposes and portfolio demonstration.

---

**Author**: Vedang
**Project Type**: Network Programming, Concurrent Systems  
**Skills Demonstrated**: Python, Socket Programming, Threading, Client-Server Architecture
