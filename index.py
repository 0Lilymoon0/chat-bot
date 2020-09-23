from random import choice

def get_math_bot_response(user_response):

    bot_response_correct = ["Correct!", "That's Right!", "You Got It!"]
    bot_response_incorrect = ["Incorrect", "Wrong", "Nope"]

    if user_response == "10" or user_response == "ten" or user_response == "Ten":
        return choice(bot_response_correct)
    elif user_response != "10" and user_response != "ten" and user_response != "Ten":
        return choice(bot_response_incorrect)

print("Welcome to Math Bot")
print("You will be questioned on your math knowledge.")

user_response = ""

while True:
  user_response = input("Please enter the answer to 5 + 5. If you get it right, go ahead and say 'done' the next time you are asked. ")

  if user_response == "done" or user_response == "Done":
    break
  
  bot_response = get_math_bot_response(user_response)
  print(bot_response)