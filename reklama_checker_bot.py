# reklama_checker_bot.py
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import re
import datetime

TOKEN = '7659365831:AAGTOO9Ua8cKmBDffiRH_jUsgvSB7cCcPEo'
bot = telebot.TeleBot(TOKEN)

# ← 7659365831:AAGTOO9Ua8cKmBDffiRH_jUsgvSB7cCcPEo 
# (7659365831:AAGTOO9Ua8cKmBDffiRH_jUsgvSB7cCcPEo())
