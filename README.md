# Remote Method Invocation using Pyro5

## Introduction

This is a simple example of Remote Method Invocation using Pyro5. Pyro5 is a library that enables you to write distributed applications in Python. It is designed to be very easy to use, and to handle all the details of network communication for you. It is quite similar to Java's RMI.

## Requirements

- Python 3.6 or higher
- Pyro5 library

## Installation

You can install Pyro5 using pip:

```bash
pip install Pyro5
```

## Usage

1. Run the server:

```bash
python server.py
```

2. Run the client:

```bash
python client.py
```

## Example

In this example, the server has a method called `add` which takes two arguments and returns their sum. The client calls this method remotely.

## Conclusion

Pyro5 is a powerful library that makes it easy to write distributed applications in Python. It handles all the details of network communication for you, so you can focus on writing your application logic. I hope this example helps you get started with Pyro5 and RMI in Python.

## References

- [Pyro5 Documentation](https://pyro5.readthedocs.io/en/latest/)
