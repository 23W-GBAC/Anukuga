
# Automating My Blog and Social Media Posts
## Introduction
I've developed a Python-based automation tool to simplify the process of posting blog content to various social media platforms. The current version posts to my Twitter account, Telegram channel, Medium, and Facebook page. Additionally, the tool notifies me on Telegram about each post. I built this application using Python 3.7.5 and Ubuntu 18.04.3 LTS.

## Getting Started
I started by cloning the repository and creating a .env file to store secrets. If I don't want to use specific social media platforms, I simply set the corresponding environment variables to False in the .env file.

### Telegram
For Telegram integration, I created a channel, used Bot Father to generate a bot, obtained the access token, and noted down the chat_id for admin notifications. I then added these details to the .env file:


#### TELEGRAM_TOKEN="my_token"
#### TELEGRAM_USERNAME="username_for_bot"
#### TELEGRAM_CHANNEL="username_for_channel"
#### TELEGRAM_ADMIN_ID="chat_id"

### Facebook (Work in Progress)
For Facebook integration, I created a page, an application, acquired permissions, generated an access token, and noted down the page id. I added these details to the .env file:


#### FACEBOOK_ACCESS_TOKEN="my_access_token"
#### FACEBOOK_PAGE_ID="my_page_id"
Note: Before going live on Facebook, I'm in the review stage, and a privacy policy is required. I might need to go through App Review before being allowed to publish posts.

## Installation and Setup
I set up a virtual environment, activated it, cloned the repository, and installed the necessary requirements. Additionally, I created a MySQL database to store posted links and configured the RSS feed URL in the .env file.


#### DB_NAME="name_of_the_database"
#### DB_HOST="host"
#### DB_USER="user"
#### DB_PASSWORD="password"
#### DB_TABLE="name_of_the_table"
#### DB_COLUMN="name_of_the_column_that_will_store_links"
#### CUSTOM_TXT="THE TEXT THAT WILL BE PREFIXED BEFORE EVERY POST"
#### FEED_URL="MY RSS FEED URL"
I can add entries to the database using:


####python -m social_bost_pot.feeds.processor
##Testing
To test the system, I added a post to my website and ran:


#### python -m social_post_bot
If successful, I receive a notification on Telegram.

## Scheduling
I scheduled a cron job to run the script python -m social_post_bot based on my posting requirements.







