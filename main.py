main.py
import os
import telebot
bot = telebot.TeleBot("1958941386:AAGlQ7POBmel5JftXalNsvFOTGWNap9Sm6I")
@bot.message_handler(commands=["start"])
def send_welcome(message):
     bot.reply_to(message,"hello i'm minul chat bot")

@bot.message_handler(commands=["how"])
def send message(message):
     bot.send_message(message, "join telegram grouphttps://t.me/THESLGAMING12363")

bot.polling()
