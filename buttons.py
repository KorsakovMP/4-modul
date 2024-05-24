from pyrogram.types import KeyboardButton, InlineKeyboardButton
from pyrogram import emoji

# Общие кнопки
back_button = KeyboardButton(f'{emoji.BACK_ARROW} Назад')

# Кнопки главного меню
time_button = KeyboardButton(f'{emoji.ALARM_CLOCK} Время')
help_button = KeyboardButton(f'{emoji.WHITE_QUESTION_MARK} Помощь')
settings_button = KeyboardButton(f'{emoji.GEAR} Настройки')
weather_button = KeyboardButton(f'{emoji.CLOUD} Погода')
cats_button = KeyboardButton(f'{emoji.CAT}Котики')

weather_current_inline_button = InlineKeyboardButton(f'{emoji.FIVE_O_CLOCK} Погода сейчас', 'weather_current')
weather_forecast_inline_button = InlineKeyboardButton(f'{emoji.CALENDAR} Прогноз погоды', 'weather_forecast')
cats_inline_button = InlineKeyboardButton(f'{emoji.CAT_FACE} Котики', 'show_cats' )