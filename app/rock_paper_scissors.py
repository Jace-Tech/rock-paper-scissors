from .utils.helpers import response
import random
options = ["r", "p", "s"]

def check (user_choice):
  computer_choice = random.choice(options)
  if user_choice in options:
    if user_choice == computer_choice:
      return response("It's a Tie", { "user": user_choice, "computer": computer_choice })
    elif user_choice == 'r' and computer_choice == 'p':
      return response("Computer wins", { "user": user_choice, "computer": computer_choice, "won": False })
    elif user_choice == 'p' and computer_choice == 's':
      return response("Computer wins", { "user": user_choice, "computer": computer_choice, "won": False })
    elif user_choice == 's' and computer_choice == 'r':
      return response("Computer wins", { "user": user_choice, "computer": computer_choice, "won": False })
    elif user_choice == 's' and computer_choice == 'p':
      return response("User wins", { "user": user_choice, "computer": computer_choice, "won": True })
    elif user_choice == 'r' and computer_choice == 's':
      return response("User wins", { "user": user_choice, "computer": computer_choice, "won": True })
    elif user_choice == 'p' and computer_choice == 'r':
      return response("User wins", { "user": user_choice, "computer": computer_choice, "won": True })
  return response("Invalid choice")