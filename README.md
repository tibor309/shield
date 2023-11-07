# 🛡️ Shield
Shield is a basic moderation discord bot that helps keepig your server clean. You can kick, ban, softban members, manage roles/chat, and a few more.

<div id="badges", align="center">
  <a href="https://repl.it/github/tibor309/shield">
    <img src="https://img.shields.io/badge/Replit-F26207.svg?style=for-the-badge&logo=Replit&logoColor=white&label=Run on" alt="Replit Badge"/>
  </a>
  <a href="https://glitch.com/edit/#!/import/github/tibor309/shield">
    <img src="https://img.shields.io/badge/Glitch-3333FF.svg?style=for-the-badge&logo=Glitch&logoColor=white&label=Remix on" alt="Glitch Badge"/>
  </a>
  <a href="https://hub.docker.com/r/tibor309/shield">
    <img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white&label=Run on" alt="Docker Badge"/>
  </a>
  <a href="https://discord.com/api/oauth2/authorize?client_id=1164523697902719026&permissions=8&scope=bot%20applications.commands">
    <img src="https://img.shields.io/badge/Discord-5662f6?style=for-the-badge&logo=discord&logoColor=white&label=Invite to" alt="Discord Invite Badge"/>
  </a>
</div>

## Setup
### Replit and Glitch
First clone the repo with the buttons on top, or manually on the site. Then head over to the secrets tab, and create a new secret called `TOKEN`, and place your bot token in the value field. After that just install the packages, and you're done! Make sure the package manager won't install discord.py or other discord libraries!

### Source
Clone the repo, and run the command below to install all the packages. Then create a secrets file, and set your bot token. After that, just run it somewhere, or change the configuration in the config file.
```
pip3 install -r requirements.txt
```

## Docker
You can also run the bot on docker. But you won't be able to customize the configuration. Simply add your token as an env variable, run the command, and you're done. 
```
docker run -d -it -e TOKEN=your-bot-token tibor309/toolbox:latest
```

## Configuration
You can customize the bot to your liking in the config file.

> All icons were provided by [fontawesome](https://fontawesome.com/)! <3
