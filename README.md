# Broadcast Server
Sample solution for the [broadcast server](https://roadmap.sh/projects/broadcast-server) challenge from [roadmap.sh](https://roadmap.sh/).


A simple UDP broadcast server and client in Python.

## Files

- `main.py`: Broadcasts a message to all clients on the local network.
- `client.py`: Listens for broadcast messages on port 3777.

## Usage

### 1. Start the Client

Open a terminal and run:

```bash
python3 client.py
```

You should see:

```
Listening for broadcast messages...
```

### 2. Run the Server

Open another terminal and run:

```bash
python3 main.py
```

You should see:

```
Broadcast message 'Hello, World!' sent!
```

The client terminal will display:

```
Received message: Hello, World! from ('<server_ip>', 3777)
```

## Notes

- Both server and client use UDP port 3777.
- Make sure both scripts are running on the