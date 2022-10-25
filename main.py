from bot_commands import *
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = ApplicationBuilder().token("5739117950:AAFAPWiTqA_BXxUg69UO2Ba8KafvZNW9vKA").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("time", time))
app.add_handler(CommandHandler("sum_int", sum_int))
app.add_handler(CommandHandler("sum_float", sum_float))
print('server start')
app.run_polling()
    