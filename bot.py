from telegram import Update
from telegram.ext import Application, MessageHandler, CallbackContext
from telegram.ext.filters import Filters  # Correct import path


# Function to handle notifications (join/leave messages)
def handle_notifications(update: Update, context: CallbackContext):
    if update.message.new_chat_members or update.message.left_chat_member:
        # Delete the join/leave message
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)

def main():
    # Initialize the bot
    TOKEN = "7810125457:AAGX8TlWYWxQCVrJATmrmcaWPQGMpQC2ax8"  # Replace with your token if needed
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add handler for notifications
    dispatcher.add_handler(MessageHandler(Filters.status_update, handle_notifications))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
