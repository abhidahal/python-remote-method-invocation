import Pyro5.api
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def main():
    try:
        # Replace this with the URI printed by the server
        uri = input("Enter the URI of the remote object: ")

        # Get a proxy for the remote object
        calculator = Pyro5.api.Proxy(uri)

        try:

            a = input("Enter number :")
            b = input("Enter number :")
            # Call remote methods
            result_add = calculator.add(a,b)
            result_subtract = calculator.subtract(a,b)

            logging.info(f"Addition result: {result_add}")
            logging.info(f"Subtraction result: {result_subtract}")

        except Pyro5.errors.CommunicationError as e:
            logging.error(f"Communication error: {e}")
        except Pyro5.errors.PyroError as e:
            logging.error(f"Pyro error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

    except Pyro5.errors.NamingError as e:
        logging.error(f"Naming error: {e}")
    except Pyro5.errors.PyroError as e:
        logging.error(f"Pyro error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
