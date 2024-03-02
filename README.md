# Horrible copenheimer
A minecraft server seeker, but horribly bad.

## Installation
1. *Install python*

   Install python (if you haven't already) from [python.org](https://python.org).

   Simply donwload the installer for the latest version of python *3*.
   
   *IMPORTANT: USE PYTHON 3 AND NOT PYTHON 2*
   
3. *Download the files*

  To download, simply clone the repo using git, with this command:

  `git clone https://github.com/JacobborstellCoder/Horrible_copenheimer.git`

  Note: you need to have git installed for this to work. If you don't have git installed, install it or download the ZIP.
  
  To download the ZIP click "Code" -> "Download ZIP", then just unzip the ZIP file.

## Usage
Go into the Horrible_copenheimer folder/directory and run `main.py`.

Tip: Increase the number of workers in the configration file to make it faster.

The found servers will be stored in a file called `found_servers.txt` in the same folder as the other files, and you will see it in the logs:

`
  [INFO] [SERVER] Found minecraft server: xxx.xxx.xxx.xxx:xxxxx
  [INFO] Successfully wrote the server xxx.xxx.xxx.xxx:xxxxx to the server list
`

## Configuration
You can configure it in the `config.json` file.
Available settings:
 - Workers: How many threads the program uses. Deafult is 250.
 - Timeout: For how long the progarm will try to ping the server, in seconds. Deafult is 1.
 - Server Info: Coming soon, currently does nothing.
 - Ports: The ports that the program tries to connect to, as an array. Deafult is only `[25565]`. Add more ports with commas, `[123, 456, 25565, 9999]`.
 - Debug: Logs every attempted connection. Deafult is false, only enable for debugging purposes.
