# simple-python-telegram-bot
a simple python telegram bot that you can host on heroku for free
## requirement
 you need to create a telegram bot first 
## run locally 
- create a virtual environment 
- pip install -r requirement.txt
- create .env file
- add TOKEN in .env file (check .en-example)
- pip app.py 
- finally go to the telegram bot you created and type /start /test /whoiam ....

## run on Heroku using webhooks 
- create a Heroku account
- create a project 
- add build pack : heroku/python
- add all env variables under project>settings>config vars 
- get you project url under project>settings>Domains and add as WEB_HOOK_URL in config vars
- set USE_WEBHOOK=True
- finally push to Heroku 
