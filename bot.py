from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8249504920:AAFYqrRJKIL3rLcTERR4mNuXWurjHpcrQvc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلًا 👋 البوت يعمل. أرسل أي رسالة.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ البوت يعمل الآن بدون مشاكل")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"أنت قلت: {update.message.text}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("status", status))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("البوت يعمل الآن...")
app.run_polling()