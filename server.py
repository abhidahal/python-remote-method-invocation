import Pyro5.api
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

@Pyro5.api.expose
class Calculator:
    def add(self, a, b):

        try:
            return int(a) + int(b)
        except Exception as e:
            logging.error(f"Error in add method: {e}")
            raise

    def subtract(self, a, b):
        try:
            return int(a) - int(b)
        except Exception as e:
            logging.error(f"Error in subtract method: {e}")
            raise

def main():
    try:
        # Create a Pyro daemon
        daemon = Pyro5.api.Daemon()

        # Register the Calculator class as a Pyro object
        uri = daemon.register(Calculator)

        # Print the URI so we can use it in the client
        logging.info(f"Ready. Object URI = {uri}")

        # Start the event loop of the server to wait for calls
        daemon.requestLoop()
    except Exception as e:
        logging.error(f"Error in server: {e}")

if __name__ == "__main__":
    main()
