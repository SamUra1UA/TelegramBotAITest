import telebot
import openai
import os



# Telegram Bot Token
TOKEN = 'TOKEN'
# OpenAI API Key
openai.api_key = "OPENAI_API_KEY"


# Create a new Telebot instance
bot = telebot.TeleBot(TOKEN)


# Function to interact with the OpenAI GPT-3 model
def ask_gpt3(question):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=question,
        max_tokens=50
    )
    return response.choices[0].text.strip()



# Handler for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! I am a GPT-3 powered bot. You can ask me anything!")


# Handler for regular messages
@bot.message_handler(func=lambda message: True)
def reply(message):
    # Get the message from the user
    user_message = message.text

    # Generate a response using GPT-3
    response = ask_gpt3(user_message)

    # Send the response back to the user
    bot.send_message(message.chat.id, response)


def main():
    # Start the Bot
    bot.polling()


if __name__ == '__main__':
    main()
