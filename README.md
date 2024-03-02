# Horrible copenheimer
A minecraft server seeker, but horribly bad

## Installation
To install, simply clone the repo using git:

`git clone https://github.com/JacobborstellCoder/Horrible_copenheimer.git`

Or you can download the ZIP, click "Code" -> "Download ZIP", then just unzip the ZIP file.

## Usage
Go into the Horrible_copenheimer folder/directory and run `main.py`.

## Configuration
You can configure it in the `config.json` file.
Available settings:
 - Workers: How many threads the program uses. Deafult is 50.
 - Timeout: The timeout when trying to connect to ports, in seconds. Deafult is 1.
 - Server Info: Coming soon, currently does nothing.
 - Ports: The ports that the program tries to connect to, as an array. Deafult is only [25565]. Add more ports with commas, [123, 456, 25565, 9999].
 - Debug: Logs every connection. Deafult is false, only enable for debugging purposes.
