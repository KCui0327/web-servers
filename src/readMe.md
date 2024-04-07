The `client.py` script is a client application that interacts with a server running on [http://127.0.0.1:8000](http://127.0.0.1:8000). It uses the current directory as a mock server for testing purposes.

The script contains two main functions: `retrieve_messages` and `main`.

The `retrieve_messages` function takes a Discord `channelId` and an `auth_key` as parameters. It sends a GET request to the Discord API to retrieve messages from the specified channel. The messages are then parsed from the JSON response and written to a file named `data.txt` in the test directory. Each message content is written on a new line.

The `main` function starts by sending a GET request to the server. If the server responds with a 200 status code, it prints the response text. If the server responds with any other status code, it prints an error message along with the status code.

After receiving a response from the server, the `main` function calls the `retrieve_messages` function to retrieve messages from a Discord channel. The channel ID and authorization key are retrieved from a config module.

Once the messages have been retrieved and written to a file, the `main` function attempts to upload the file to the server using a PUT request. If the server responds with a 201 status code, it prints a success message. If the server responds with any other status code, it prints an error message along with the response content.

The script is designed to be run as a standalone program. If it is run directly (i.e., not imported as a module), it calls the `main` function to start the client operations.

> You will need to create the config.py by yourself and add **authorization** and **channel_id** variables for Discord configs. See YouTube for tutorials in getting the authorisation token...
