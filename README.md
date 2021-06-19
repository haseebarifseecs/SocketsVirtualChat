# Virtual Chat
Foobar is a Python library for dealing with word pluralization.

## Usage

Use the command prompt/linux terminal to access Clients.py file and specify commands line argument as

```bash
Client.py –n [client’s name] –i [server’s IP] –p [port number] –f [ftpserver IP]
```

## Implemented Client's Functionality

* Ability to change username.
* Ability to snooze notifications
* Ability to blacklist other client.
* Ability to transfer file.
* Ability to send as well as receive message at the same time.

## Implemented Client's Functionality

* Ability to handle multiple clients.
* Key record of each socket connection in a hash table/dictionary.

## Used Python Libraries
*	Socket library for creating TCP connection.
*	Re using regular expressions for string manipulation by generating patterns for extracting cmds.
*	Ftplib for creating FTP connection for file transfer.
*	Threading for handling multiple clients at server side and simultaneous receive send functionality of clients.
*	Sys for command line arguments.
*	Time for adding variable delays.
* Random for selecting random range for delay.

## Available Commands at Client's Terminal
```Commands should follow the following syntax
/command/ -> available commands
/sleep/ [time for sleeping out notifications]
/name/ [new name]
/send/ [file_path <space> filename]
/blacklist/ [username]
```

[MIT](https://choosealicense.com/licenses/mit/)