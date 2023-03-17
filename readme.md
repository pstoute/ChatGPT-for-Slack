# ChatGPT for Slack

This repo is a Slack app that creates a slash command for Slack that will call to ChatGPT and receive a private response back. 

Services required:
- Slack
- Glitch.com paid account (or another server, although this guide only covers using Glitch)
- OpenAI API Key

## Install Steps

1. (GitHub) Star this Repo
2. (glitch) Create your account with Glitch.com
3. (glitch) Create a new product via GitHub import
4. (glitch) Paste in the "http" GitHub repo link
5. (glitch) This should import all the required files into the repo. 
6. (Slack) Go to developers.slack.com
7. (Slack) Create App
8. (Slack) Create using a manifest file
9. (GitHub) Open "raw" the /slack/manifest.txt file
10. (GitHub) Select all and copy the text
11. (Slack) Paste the manifest text into the slack window where it asks for your Manifest data. 
12. (Slack) Add a app token (copy it)
13. (glitch) open the .env file and replace the app token variable with your app token from Slack
14. (Slack) Go to OAuth and create a bot token
15. (glitch) Replace the bot token with the one from Slack
16. (OpenAI) Goto program.OpenAI.com/api and generate an API key. 
17. (glitch) Replace the OpenAI token in the .env file with the one from OpenAPI. 
18. (Slack) Install the app on your workspace
19. (glitch) Open the terminal
20. (glitch) paste in "pip3 install -r requirements.txt" to install the requirements. 
21. (glitch) paste in "python3 chatgpt_slack_app.py" to start the program which will activate the app in Slack
22. (Slack) test your /chatGPT slack command. 
