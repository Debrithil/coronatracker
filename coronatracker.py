# name: Minna Kuivalainen
# course: Ohjelmistokehityksen teknologiat
# project: Coronavirus tracker
# student number: 1804081

# all necessary libraries imported
from telegram.ext import Updater, CommandHandler
import requests
import json

def start(update, context):
    # sends an automatic message when the bot starts or when the user enters / start in the text field
    update.message.reply_text('Hi pal! You have just launched a coronavirus bot! Here you can find the latest coronavirus data based on research by '
    'Johns Hopkins University.' +
    '\n' 'Please type one of the options below:' +
    '\n' '/info to select the data you want to view' +
    '\n' '/helpline to see the contact number of the Government´s Helpline')

def info(update, context):
    # sends an automatic message when the user enters / info in the text field
    update.message.reply_text('Select the area you want to view:' + '\n' + '/nordiccountries' + '\n' + '/northamerican' +
    '\n' + '/southamerican' + '\n' + '/globally')

def helpline(update, context):
    # sends an automatic message when the user enters / helpline in the text field
    update.message.reply_text('The Government´s joint telephone helpline is open on weekdays at 8-21 and on Saturdays at 9-15.'
    'Calls to the helpline are subject to a regular local network or mobile phone charge.' + 
    '\n' 'Telephone counselling: 0295 535 535')

def globally(update, context):
    # creating a GET request from COVID-19 API
    response = requests.get('https://api.covid19api.com/summary').json()
    # fetch the wanted data from the REST API (Globally)
    data = response['Global']
    text = ''
    # for-loop fetches the wanted objects from the API
    for key, value in data.items():
        text += '{0}: {1}\n'.format(key, value)
    text += '\n If you want to return to the menu click /start or see results from another country or region click /info'
    # sends the wanted data to the Telegram bot as a message
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=text)

def nordiccountries(update, context):
    # creating a GET request from COVID-19 API
    response = requests.get('https://api.covid19api.com/summary').json()
    # fetch the wanted data from the REST API (Country list)
    data = response['Countries']
    text = ''
    # fetch the wanted countries from the API list
    wanted = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Island']
    # for-loop fetches the countries on the list and parses the wanted data.
    # if the country is found in the wanted list, the bot prints its current information
    for country in data:
        if country['Country'] in wanted:       
            text += '{0}\n'.format(country['Country'])
            text += 'New Confirmed: {0}\n'.format(country['NewConfirmed'])
            text += 'Total Confirmed: {0}\n'.format(country['TotalConfirmed'])
            text += 'New Deaths: {0}\n'.format(country['NewDeaths'])
            text += 'Total Deaths: {0}\n'.format(country['TotalDeaths'])
            text += 'New Recovered: {0}\n'.format(country['NewRecovered'])
            text += 'Total Recovered: {0}\n\n'.format(country['TotalRecovered'])
    text += 'If you want to return to the menu click /start or see results from another country or region click /info'
    # sends the wanted data to the Telegram bot as a message
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=text)

def northamerican(update, context):
    # creating a GET request from COVID-19 API
    response = requests.get('https://api.covid19api.com/summary').json()
    # fetch the wanted data from the REST API (country list)
    data = response['Countries']
    text = ''
    # fetch the wanted countries from the API list
    wanted = ['Canada', 'United States', 'Mexico', 'Nicaragua', 'Honduras', 'Cuba', 'Guatemala', 'Panama', 'Costa Rica', 'Dominican Republic', 
    'Haiti', 'Belize', 'El Salvador', 'The Bahamas', 'Jamaica', 'Trinidad and Tobago', 'Dominica', 'Saint Lucia', 'Antigua and Barbuda', 'Barbados',
     'Saint Vincent and the Grenadines', 'Grenada', 'Saint Kitts and Nevis']
    # for-loop fetches the countries on the list and parses the wanted data.
    # if the country is found in the wanted list, the bot prints its current information
    for country in data:
        if country['Country'] in wanted:       
            text += '{0}\n'.format(country['Country'])
            text += 'New Confirmed: {0}\n'.format(country['NewConfirmed'])
            text += 'Total Confirmed: {0}\n'.format(country['TotalConfirmed'])
            text += 'New Deaths: {0}\n'.format(country['NewDeaths'])
            text += 'Total Deaths: {0}\n'.format(country['TotalDeaths'])
            text += 'New Recovered: {0}\n'.format(country['NewRecovered'])
            text += 'Total Recovered: {0}\n\n'.format(country['TotalRecovered'])
    text += 'If you want to return to the menu click /start or see results from another country or region click /info'
    # sends the wanted data to the Telegram bot as a message 
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=text)

def southamerican(update, context):
    # creating a GET request from COVID-19 API
    response = requests.get('https://api.covid19api.com/summary').json()
    # fetch the wanted data from the REST API (country list)
    data = response['Countries']
    text = ''
    # fetch the wanted countries from the API list
    wanted = ['Brazil', 'Argentina', 'Peru', 'Colombia', 'Bolivia', 'Venezuela', 'Chile', 'Paraguay', 'Ecuador', 'Guyana', 'Uruguay', 'Suriname']
    # for-loop fetches the countries on the list and parses the wanted data.
    # if the country is found in the wanted list, the bot prints its current information
    for country in data:
        if country['Country'] in wanted:       
            text += '{0}\n'.format(country['Country'])
            text += 'New Confirmed: {0}\n'.format(country['NewConfirmed'])
            text += 'Total Confirmed: {0}\n'.format(country['TotalConfirmed'])
            text += 'New Deaths: {0}\n'.format(country['NewDeaths'])
            text += 'Total Deaths: {0}\n'.format(country['TotalDeaths'])
            text += 'New Recovered: {0}\n'.format(country['NewRecovered'])
            text += 'Total Recovered: {0}\n\n'.format(country['TotalRecovered'])
    text += 'If you want to return to the menu click /start or see results from another country or region click /info'
    # sends the wanted data to the Telegram bot as a message 
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=text)

def main():
    # create the Updater and pass it to the bot's token.
    updater = Updater('1188316138:AAEStDc2i58iQ46alBAeHTXiZEe8AiweNyE', use_context=True)
    # get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("helpline", helpline))
    dp.add_handler(CommandHandler("nordiccountries", nordiccountries))
    dp.add_handler(CommandHandler("globally", globally))
    dp.add_handler(CommandHandler("northamerican", northamerican))
    dp.add_handler(CommandHandler("southamerican", southamerican))
    # start the bot   
    updater.start_polling()
    # run the bot until Ctrl-C are pressed or the process receives SIGINT
    updater.idle()

# conditional expression (if the name is the same as main, return it to the main () function)
if __name__ == '__main__':
    main()