# Twitch Chat Banner
Finally, a way to randomly ban your chat for no reason at all!

## Requirements
- [Twitchio](https://twitchio.dev/en/latest/)

## Setup
All the settings for this project should be put in a settings.json file in the same directory as the program.
- **nickname:** The name of the bot, should normally be your username.
- **token:** Twitch API token, needs chat:read, chat:edit and channel:moderate.  Get your tokens [here](https://twitchtokengenerator.com/)
- **channel:** What channel this bot is active on, needs to be lower case and proceeded by '#'
- **cooldown:** The minimum amount of time between people being timed out in seconds.
- **probability:** The probability of any given message triggering a timeout, with the chance being 1/probability.
- **duration:** How long the user is timed out in seconds.
