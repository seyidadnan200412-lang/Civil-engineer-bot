import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# استدعاء التوكن الخاص بالبوت
TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📚 المواد الدراسية", callback_data='subjects')],
        [InlineKeyboardButton("📢 القناة الرسمية", url="ضع_رابط_قناتك_هنا")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("أهلاً بك سيدي في بوت المكتبة الجامعية! اختر من القائمة:", reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'subjects':
        keyboard = [
            # قم باستبدال الروابط أدناه بروابط الملفات التي نسختها من قناتك الخاصة
            [InlineKeyboardButton("📄 ملف المادة الأولى", url="ضع_رابط_الملف_الأول_هنا")],
            [InlineKeyboardButton("📄 ملف المادة الثانية", url="ضع_رابط_الملف_الثاني_هنا")],
            [InlineKeyboardButton("🔙 رجوع", callback_data='main_menu')]
        ]
        await query.edit_message_text("اختر المادة المطلوبة:", reply_markup=InlineKeyboardMarkup(keyboard))
        
    elif query.data == 'main_menu':
        keyboard = [
            [InlineKeyboardButton("📚 المواد الدراسية", callback_data='subjects')],
            [InlineKeyboardButton("📢 القناة الرسمية", url="ضع_رابط_قناتك_هنا")]
        ]
        await query.edit_message_text("القائمة الرئيسية:", reply_markup=InlineKeyboardMarkup(keyboard))

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    app.run_polling()

if __name__ == '__main__':
    main()
