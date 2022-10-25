# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
# import datetime
# from spy import *

# def hi_command(update: Update, context: CallbackContext):
#     log(update, context)
#     update.message.reply_text(f'Hi {update.effective_user.first_name}!')
# def help_command(update: Update, context: CallbackContext):
#     log(update, context)
#     update.message.reply_text(f'/hi\n/time\n/help\n/sum_int\n/sum_float')
# def time_command(update: Update, context: CallbackContext):
#     log(update, context)
#     update.message.reply_text(f'{datetime.datetime.now().time()}')
# def sum_int_command(update: Update, context: CallbackContext):
#     log(update, context)
#     msg = update.message.text
#     print(msg)
#     items = msg.split() # /sum 123 534543
#     x = int(items[1])
#     y = int(items[2])
#     update.message.reply_text(f'{x} + {y} = {x+y}')
# def sum_float_command(update: Update, context: CallbackContext):
#     log(update, context)
#     msg = update.message.text
#     print(msg)
#     items = msg.split() # /sum 123 534543
#     x = float(items[1])
#     y = float(items[2])
#     update.message.reply_text(f'{x} + {y} = {x+y}')

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *
import datetime


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum_int\n/sum_float') 
async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')       
async def sum_int(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')
async def sum_float(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 534543
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

