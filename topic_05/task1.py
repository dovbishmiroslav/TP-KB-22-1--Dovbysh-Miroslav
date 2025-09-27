import random

variations = ["stone", "scissor", "paper"]
variants = "123"

def game (choice):
    if choice in variants:
        BotChoice = random.choice(variations)
        PlayerChoice = variations[int(choice)-1]
    if BotChoice == PlayerChoice:
        print ("Нічия, бот обрав", BotChoice)
    elif variations.index(PlayerChoice) == variations.index(BotChoice) - 1 or PlayerChoice == "paper" and BotChoice == "stone":
        print ("ви перемогли, бот обрав", BotChoice)
    else:
        print ("Ви програли, бот обрав", BotChoice)

while True:
    choice = input("Введіть ваш варіант 1 - камінь, 2 - ножиці, 3 - папір або 'stop' щоб закінчити")
    if choice == "stop":
        break
    else:
        game(choice)