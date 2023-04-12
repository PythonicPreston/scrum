# Python script to run during standup that returns a random starter and picks an ice-breaker.

import random


def name_picker():
    """This function takes in a user specified number and allows the user to input that many names and randomly selects one."""

    # ask the user how many names they want to enter
    num_names = int(input("How many people are present for standup today? "))
    print(" ")
    # create an empty list
    names = []
    # create a for loop that takes in user input and appends it to the list
    for i in range(num_names):
        names.append(input(f"Person {i+1}: "))
    # randomly select and return a name from the list
    return f"\nOur lucky starter is... {random.choice(names)}!\n"


def game_picker():
    """This function randomly picks a game from a list of games."""

    # create a dictionary of games and descriptions
    games = {
        "One Word Game.": "What’s the one word you’d use to describe yourself for this week? Everyone picks one and then they’re referred to by that name throughout the meeting.",
        "Two Truths, one Lie.": "Each person takes a turn saying two truths and one lie about themselves. The other players have to guess which statement is the lie.",
        "Would You Rather...": "Each person takes a turn asking a question that starts with 'Would you rather...'. The other players have to answer the question.",
        "What’s Your Favorite Year?": "Each person takes a turn saying what their favorite year is. The other players have to guess why.",
        "No Smiling!": "Each person takes a turn saying something funny. The other players have to try not to smile.",
        "Stranded Desert Island Picks.": "Each person takes a turn saying what three things they’d bring to a deserted island. The other players have to guess why.",
        "What Annoys You?": "Each person needs to reveal the personality trait that is most irritating to them and why.",
        "What Kind of Car?": "If your workplace was a car this week, what kind would it be?",
        "What’s Your Theme Song?": "Imagine your life was a movie. What song would be playing in the background?",
        "Be Honest...": "It might seem like a dangerous door to open but ask the team to be honest about their day. The Huffington Post says that, the best business is done when you're being true and authentic.",
        "Movie That Made You Cry?": "What movie made you cry the most? Why?",
        "Stand Up!": "Remove the chairs from the room in which you’re meeting and tell everyone that it’s a standup meeting.",
        "What’s Your Favorite Color?": "What’s your favorite color and why?",
        "What’s Your Favorite Food?": "What’s your favorite food and why?",
        "skribbl.io": "Go to https://skribbl.io/ and draw something together.",
        "Bucket list": "Name three things that are on your bucket list.",
        "Something else": "If you could be something else. In your ideal world, what would your job be?",
        "Movie pitch": "Pretend that you are an upcoming writer. Give us a synopsis of your debut movie.",
        "Backward names.": "Say your name backward. For the rest of the meeting you are called by your new name.",
        "Famous athlete": "If you were a famous athlete, who would you be and why?",
        "Famous actor": "If you were a famous actor, who would you be and why?",
        "Famous musician": "If you were a famous musician/artist, who would you be and why?",
        "Movie Character": "If you were a movie character, who would you be and why?",
        "Hot date.": "If you could go on a date with someone (that's not your true partner), who would it be and why?",
        "Controversial opinion": "Share a controversial opinion you have about a trivial matter (eg pizza is overrated).",
        "Two-Sentence Horror Stories": "Each person takes a turn sharing a two-sentence horror story. The other players can react or ask questions.",
        "Alphabet Game": "Pick a category (such as food, animals, or cities) and take turns naming something in that category that starts with each letter of the alphabet, going in order (A, B, C, etc.).",
        "Impromptu Speeches": "Each person is given a random topic to speak about for one minute without any preparation. The other players can ask questions or provide feedback after each speech.",
        "Guess Who": "One person chooses a famous person (real or fictional) and gives three clues about them. The other players have to guess who it is.",
        "This or That": "Ask each person a series of 'this or that' questions (such as 'coffee or tea?' or 'beach or mountains?') and discuss their answers.",
        "Pictionary": "One person draws a picture and the other players try to guess what it is. You can use a virtual whiteboard or a website like skribbl.io.",
        "Never Have I Ever": "Each person takes a turn saying something they have never done (such as 'never have I ever gone bungee jumping'). The other players who have done that thing have to take a drink (or do a different penalty).",
        "Name Game": "Start with a category (such as fruits, movies, or celebrities) and take turns naming something in that category. Each person has to repeat all the previous answers before adding their own.",
        "Charades": "One person acts out a word or phrase without speaking, and the other players try to guess what it is.",
        "Word Association": "Start with a word and take turns saying a word that is associated with the previous word (such as 'dog' -> 'cat' -> 'mouse' -> 'cheese').",
        "Curve Fever": "Go to https://curvefever.pro/ and play a game together.",
    }

    # randomly select a game from the dictionary and return it
    game = random.choice(list(games.items()))
    return f"The game of the day is: {game[0]} \n{game[1]} \n"


def main():
    """This function runs the name_picker and game_picker functions and prints the results."""
    print(name_picker())
    print(game_picker())


if __name__ == "__main__":
    main()
