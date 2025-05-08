import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from drive_uploader import save_image_to_drive, save_video_to_drive

TOKEN = "token có dạng số : chữ chép toàn bộ đoạn đó và dán vào đâyđây"


logging.basicConfig(level=logging.INFO)

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_file = await update.message.photo[-1].get_file()
    url = photo_file.file_path
    filename = f"{update.effective_user.username or 'user'}_{photo_file.file_unique_id}.jpg"

    link = save_image_to_drive(url, filename)
    await update.message.reply_text(f"✅ Ảnh đã được lưu:\n{link}")
    await update.message.reply_text("🙏 Cảm ơn bạn đã sử dụng bot!")

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video_file = await update.message.video.get_file()
    url = video_file.file_path
    filename = f"{update.effective_user.username or 'user'}_{video_file.file_unique_id}.mp4"

    link = save_video_to_drive(url, filename)
    await update.message.reply_text(f"🎥 Video đã được lưu:\n{link}")
    await update.message.reply_text("🙏 Cảm ơn bạn đã sử dụng bot!")

app = ApplicationBuilder().token(TOKEN).build()


app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
app.add_handler(MessageHandler(filters.VIDEO, handle_video))

if __name__ == '__main__':
    app.run_polling()