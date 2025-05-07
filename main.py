from minecraft.networking.connection import Connection
from minecraft.networking.packets import Packet, clientbound, serverbound

def main():
    # Server configuration
    host = 'localhost'
    port = 25565  # Default Minecraft port
    
    try:
        # Create server connection
        connection = Connection(host, port)
        print(f"Server started on {host}:{port}")
        
        # Keep the server running
        while True:
            connection.handle_packets()
            
    except Exception as e:
         print(f"Error starting server: {e}")

if __name__ == "__main__":
    main()
