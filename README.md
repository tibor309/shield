# 🛡️ Shield
Shield is a basic moderation discord bot that helps keepig your server clean. You can kick, ban, softban members, manage roles/chat, and a few more.

<div id="badges", align="center">
  <a href="https://repl.it/github/tibor309/shield">
    <img src="https://img.shields.io/badge/Replit-a6e3a1.svg?style=for-the-badge&logo=Replit&logoColor=gray&labelColor=b5ffb4&label=Run on" alt="Replit_badge"/>
  </a>
  <a href="https://glitch.com/edit/#!/import/github/tibor309/shield">
    <img src="https://img.shields.io/badge/Glitch-a6e3a1.svg?style=for-the-badge&logo=Glitch&logoColor=gray&labelColor=b5ffb4&label=Remix on" alt="glitch_badge"/>
  </a>
  <a href="https://hub.docker.com/r/tibor309/shield">
    <img src="https://img.shields.io/badge/Docker-a6e3a1.svg?style=for-the-badge&logo=Docker&logoColor=gray&labelColor=b5ffb4&label=Pull from" alt="Docker_badge"/>
  </a>
  <a href="https://discord.com/api/oauth2/authorize?client_id=1164523697902719026&permissions=8&scope=bot%20applications.commands">
    <img src="https://img.shields.io/badge/Discord-a6e3a1?style=for-the-badge&logo=discord&logoColor=gray&labelColor=b5ffb4&label=Invite to" alt="Discord_badge"/>
  </a>
</div>

## Setup
### Replit and Glitch
First clone the repo with the buttons on top, or manually on the site. Then head over to the secrets tab, and create a new secret called `TOKEN`, and place your bot token in the value field. After that just install the packages, and you're done! Make sure the package manager won't install discord.py or other discord libraries!

### Source
Clone the repo, and run the command below to install all the packages.

```bash
pip3 install -r requirements.txt
```

Then create a secrets file, and set your bot token. After that, run the command below to run the bot. At least python 3.10 is required!

```bash
python3 main.py
```

## Docker
You can also run the bot on docker. But you won't be able to customize the configuration. Simply add your token as an env variable, run the command, and you're done. 

```bash
docker run -d -it -e TOKEN=your-bot-token tibor309/shield:latest
```

## Configuration
You can customize the bot to your liking in the config file.

> All icons were provided by [fontawesome](https://fontawesome.com/)! <3
