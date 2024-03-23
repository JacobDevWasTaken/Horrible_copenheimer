# Horrible copenheimer
A minecraft server seeker, but horribly bad.

I only made this beacuase it was fun and it is not made to be efficient or fast. If you want a good server scanner use serverseeker or smthing.

Also stop making issues telling me that my code is bad and that i should kill myself. Please.

## Installation
1. *Install python*

Install python (if you haven't already) from [python.org](https://python.org).

Simply donwload the installer for the latest version of python *3*, and run it.
   
*IMPORTANT: USE PYTHON 3 AND NOT PYTHON 2*

2. *Install the libraries*

This scanner uses [mcstatus](https://github.com/py-mine/mcstatus). Install it using `python3 -m pip install mcstatus` or `python -m pip install mcstatus`

If discord webhooks are enabled in the configration, [discord_webhook](https://github.com/lovvskillz/python-discord-webhook) is required. Install it using `python3 -m pip install discord-webhook` or `python -m pip install discord-webhook`
   
3. *Download the files*

To download, simply clone the repo using git, with this command:

`git clone https://github.com/JacobborstellCoder/Horrible_copenheimer.git`

Note: you need to have git installed for this to work. If you don't have git installed, install git or download the ZIP.
  
To download the ZIP click "Code (The green button on the top left)" -> "Download ZIP", then just unzip the ZIP file.

## Usage
Go into the Horrible_copenheimer folder/directory and run `main.py`.

Tip: Increase the number of workers or the batch size in the configration file to make it faster.

The found servers will be stored in a file called `found_servers.txt` in the same folder as the other files, and you will see it in the logs:

`[INFO] [SERVER] Found minecraft server: xxx.xxx.xxx.xxx:xxxxx`

Press control + c on your keyboard to exit the program.

## Configuration
You can configure it in the `config.json` file.
Available settings:
 - Workers: How many threads the program uses. Deafult is `20`.
 - Batch size: How many connections every worker creates at once. Deafult is `50`.
 - Timeout: For how long the progarm will try to ping the server, in seconds. Deafult is `1`.
 - Ports: The ports that the program tries to connect to, as an array. Deafult is only `[25565]`. Add more ports with commas, `[123, 456, 25565, 9999]`.
 - Debug: Logs every attempted connection. Deafult is `false`, only enable for debugging purposes.
 - Use webhook: Sends all found servers to a discord webhook. [discord_webhook](https://github.com/lovvskillz/python-discord-webhook) is required for this. If this is enabled, paste your discord webhook into the webhook.txt file.
