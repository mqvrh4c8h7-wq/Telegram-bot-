import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ассаляму алейкум 🤍\n\n"
        "Я бот, который помогает:\n"
        "• создавать контент\n"
        "• вести блог\n"
        "• мотивировать\n\n"
        "Напиши слово: КОНТЕНТ"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "контент" in text:
        reply = (
            "🔥 Идея для контента:\n\n"
            "«Деньги — не цель, а средство. "
            "Настоящая ценность — в вере и смысле.»\n\n"
            "Хочешь ещё идеи? Напиши: ИДЕЯ"
        )
    elif "идея" in text:
        reply = (
            "🎥 Рилс:\n"
            "Кадры в движении + субтитры:\n"
            "«Аллах даёт не всем много,\n"
            "но всем даёт достаточно.»"
        )
    else:
        reply = "Напиши слово: КОНТЕНТ"

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
