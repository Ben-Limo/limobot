# -*- coding: utf-8 -*-
import os
import json 
import traceback
import logging
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from emoji import emojize

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
			  level=logging.INFO)
logger = logging.getLogger(__name__)

 

def start(bot, update):
	smile = emojize(" :blush:", use_aliases=True)
	point_down = emojize("  :point_down:", use_aliases=True)
	bot.sendMessage(chat_id=update.message.chat_id, text="Hi there "+smile)
	bot.sendMessage(chat_id=update.message.chat_id, text="I am the personal bot of Ben, a recent Math and Computer science graduate.")
	bot.send_photo(chat_id=update.message.chat_id, photo=open('lim.jpg', 'rb'))
	keyboard = [[InlineKeyboardButton("learn about Ben", callback_data='learn')]]
	reply_markup = InlineKeyboardMarkup(keyboard)
	update.message.reply_text( 
		'Want to learn about Ben?\n\n' +
		'simply click'+point_down, 
		reply_markup=reply_markup)

def other(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Beep boop....I am experiencing challenges understanding you, please enter /start to get me up and running")

def button(bot, update):
		relieved =  emojize(" :relieved:", use_aliases=True)
		
		if update.callback_query.data == "learn":
			bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text="I can tell you a bunch of stuff about Ben. Hit me with what interests you")
			bot.editMessageReplyMarkup(
					chat_id=update.callback_query.message.chat.id, 
					message_id=update.callback_query.message.message_id, 
					reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("Education",callback_data="education"),telegram.InlineKeyboardButton("Internships", callback_data="intern")],[telegram.InlineKeyboardButton("Connect with Ben", callback_data="connect")]]))

		elif update.callback_query.data == "education":
			bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text=
				"He was always a visionary with a boyish enthusiasm for new technology earning him respect and love amongst his peers.\n\n" +
				'So during his final year in high school, it was inevitable that a guest speaker who was pursuing Computer Science made a huge impression on him.') 
			bot.editMessageReplyMarkup(
			chat_id=update.callback_query.message.chat.id, 
			message_id=update.callback_query.message.message_id, 
			reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("Degree", callback_data="degree"),telegram.InlineKeyboardButton("Certification", callback_data="cert")],[telegram.InlineKeyboardButton("Mathematics", callback_data="math")]
				]))

	 
		elif update.callback_query.data == "degree":
			bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text=
			'A young and focused lad joined Multimedia University (nairobi) in the year 2012 to pursue a Bachelors Degree in Mathematics and Computer Science.\n' +
			'He graduated with a Second class honors (lower division) in the year 2016.')       
			bot.editMessageReplyMarkup(
				chat_id=update.callback_query.message.chat.id, 
				message_id=update.callback_query.message.message_id,
				reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("Connect with Ben", callback_data="connect")], [telegram.InlineKeyboardButton("Back", callback_data="education")]]))
	
	

		elif update.callback_query.data == "cert":
			bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text=
			'Inorder to ready himself for the competitive I.T sphere and reinvent himself as an indisposible asset for corporations, he has done all the vital certificaions. \n\n' +
			'That is to say:- \n' +
			'1. Cisco-CCNA certifaction. \n' +
			'2. ICDL Microsoft Office suite certifaction.')
			bot.editMessageReplyMarkup(
				chat_id=update.callback_query.message.chat.id, 
				message_id=update.callback_query.message.message_id,
				reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("Connect with Ben", callback_data="connect")],[telegram.InlineKeyboardButton("Back", callback_data="education")]
					]))

		elif update.callback_query.data == "math":
			bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text=
			'Since childhood Ben had an innate knack for Math, achieving straight As in both KCPE and KCSE. So it did not come as a surprise when in his 3rd year at the O-levels he went ahead to major in Pure mathematics. \n\n' +
			'He has always had a secret passion for numbers and intends to enroll for Masters in september of 2018.')
			bot.editMessageReplyMarkup(
				chat_id=update.callback_query.message.chat.id, 
				message_id=update.callback_query.message.message_id,
				reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("Learn more", callback_data="more")]
					]))

		elif update.callback_query.data == "more":
			bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text=
				'It may sound hillarious but it is quiet true. Burried deep in his soul, he has this unsatiable desire to lecture University student. Maybe not now but at a later stage in life following in the footsteps of his mother who is a teacher.')
			bot.editMessageReplyMarkup(
						chat_id=update.callback_query.message.chat.id, 
						message_id=update.callback_query.message.message_id,
						reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("Connect with Ben", callback_data="connect")],[telegram.InlineKeyboardButton("Back", callback_data="education")]]))

		elif update.callback_query.data == "connect":
			blush = emojize(" :blush:", use_aliases=True)
			point_down = emojize("  :point_down:", use_aliases=True)
			bot.sendMessage(chat_id=update.callback_query.message.chat_id, text="Aaaawh "+blush+blush+relieved+"sweet!.\nIf you got any new opportunities, don't look further.\n\n Ben loves getting intros from Bensobot")
			bot.sendMessage(chat_id=update.callback_query.message.chat_id, text=point_down)
			bot.sendMessage(chat_id=update.callback_query.message.chat_id, text="Email:\n bensokiplimo@gmail.com")
			keyboard = [[InlineKeyboardButton("to Education", callback_data='education')]]
			reply_markup = InlineKeyboardMarkup(keyboard)
			bot.sendMessage(chat_id=update.callback_query.message.chat_id, text="Mobile number:\n 0727344570", reply_markup=reply_markup)
	

		elif update.callback_query.data == "intern":
			bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text=
				'Aha... This will give you a glimpse into the experience that he has gunnered from all the major Telecommunication and I.T companies in the country.')
			bot.editMessageReplyMarkup(
						chat_id=update.callback_query.message.chat.id, 
						message_id=update.callback_query.message.message_id,
						reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("Kenic", callback_data="kenic")],[telegram.InlineKeyboardButton("Safaricom", callback_data="saf"),telegram.InlineKeyboardButton("ICTA", callback_data="icta")],[telegram.InlineKeyboardButton("Telkom Kenya", callback_data="telkom")]]))

		elif update.callback_query.data == "kenic":
			smiley =  emojize(" :smiley:", use_aliases=True)
			wink =  emojize(" :wink:", use_aliases=True)
			smirk = emojize("  :smirk:", use_aliases=True)
			bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text=
			smiley+smiley+smiley+'yeah, Kenic was an exciting place for Ben just like all first times for everyone, in his third year, he had to get out of the shell and test his classroom skills. \n ' +
			"A shy and nervous Ben (don't be quick to judge"+wink+" we are all some time"+smirk+") sat for his very first interview at Kenic. His desire and passion radiated from his eyes to the satisfaction of the panel who booked him for his first internship.")
			bot.editMessageReplyMarkup(
						chat_id=update.callback_query.message.chat.id, 
						message_id=update.callback_query.message.message_id,
						reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("life at Kenic"+relieved, callback_data="atkenic")]]))

		elif update.callback_query.data == "atkenic":
			bot.editMessageText(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, text=
				"At Kenic, he got adminster the .KE domain namespace and of course set-up the floor network and computers.\n\n" +
				"But it was not long before he was offered an opportunity to join Safaricom.")
			bot.editMessageReplyMarkup(
						chat_id=update.callback_query.message.chat.id, 
						message_id=update.callback_query.message.message_id,
						reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("to Safaricom", callback_data="saf")],[telegram.InlineKeyboardButton("to start", callback_data="education")]]))

		else :
			bot.sendMessage(chat_id=update.callback_query.message.chat_id, text="Beep boop....I am experiencing challenges understanding you, please enter /start to get me up and running")


def main():
	 # Create the Updater and pass it your bot's token.
	 TOKEN = "428771652:AAEDypv_tKz_FeIN0NFeN8vmSKnrptFkjVM"
	 PORT = int(os.environ.get('PORT', '8443'))
	 updater = Updater(TOKEN)

	 updater.dispatcher.add_handler(CommandHandler('start', start))
	 updater.dispatcher.add_handler(CallbackQueryHandler(button))
	 updater.dispatcher.add_handler(MessageHandler(Filters.text, other))

	 # Start the Bot
	 updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
	 updater.bot.set_webhook("https://kazi-ipo.herokuapp.com/" + TOKEN)


	 # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
	 # SIGTERM or SIGABRT
	 updater.idle()


if __name__ == '__main__':
	 main()



