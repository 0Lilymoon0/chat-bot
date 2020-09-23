from random import choice

def get_math_bot_response(user_response):

  bot_response_correct = ["Correct!", "That's Right!", "You Got It!"]
  bot_response_incorrect = ["Incorrect", "Wrong", "Nope"]

    if user_response == "10" or "ten" or "Ten":
    return choice(bot_response_correct)
  elif user_response !== "10" or "ten" or "Ten":
    return choice(bot_response_incorrect)

print("Welcome to Math Bot")
print("Please enter the answer to 5 + 5. If you get it right, go ahead and say 'done' the next time you are asked. ")

user_response = ""

