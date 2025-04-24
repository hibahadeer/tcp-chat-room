# TCP Chat Room 

A simple, multi-client chat room application built with Python and TCP sockets.

---

## Overview

This project demonstrates how to create a basic chat server and client using Python's built-in `socket` and `threading` modules. Multiple users can join the server and exchange messages in real-time. Ideal for learning about network programming and socket communication.

---

## Features

- Real-time chat communication
- Multi-user support via threading
- Displays user join/leave notifications
- Clean and minimal code structure

---

## Files Included

- `server.py`: Handles all incoming client connections and message broadcasting
- `client.py`: Allows users to connect to the server and participate in the chat

---

## Requirements

- Python 3.x
- No third-party libraries needed

---

## Getting Started

### Step 1: Run the Server

Open a terminal and start the server with:

```bash
python server.py
```

You should see a message confirming the server is running and ready to accept connections.

### Step 2: Run the Clients

For each user, open a new terminal window and run:

```bash
python client.py
```

When prompted, enter a nickname. You can then begin sending and receiving messages with other users connected to the server.

---

## Notes

- The server must be running before any clients can connect.
- Each client should run in a separate terminal window.
- Default setup runs on `localhost (127.0.0.1)`. For use over a network, replace the IP in both server and client files with the host's actual IP address.

---
