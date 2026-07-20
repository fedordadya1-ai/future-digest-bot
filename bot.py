import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я Future Digest.\n\n"
        "Я буду вашим персональным аналитиком:\n"
        "🤖 ИИ\n"
        "💰 Экономика\n"
        "🧬 Медицина\n"
        "🚀 Будущее\n\n"
        "Скоро научусь анализировать главные новости дня."
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен")
    app.run_polling()

if __name__ == "__main__":
    main()
