# Standup Starter and Icebreaker Game Picker

This Python script is designed to be used during a standup meeting to randomly select a person to give the first update and pick an icebreaker game to play.

# Installation
To use this script, you need to have Python 3 installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

After installing Python, download the standup.py file to your computer and run it in a Python environment.

# Usage

1. Open your terminal or command prompt and navigate to the directory where `standup.py` is saved.
2. Type `python3 standup.py` to run the script.
3. Enter the number of people present for the standup when prompted.
4. Enter the name of each person present when prompted.
5. The script will randomly select one person to start the updates and pick an icebreaker game for the group to play.
    The selected person will start with the game and then share their updates and any other information they want to share relating to standup. Thereafter they will nominate the next person. The next person will then complete their part of the game and share their updates. This process will continue until everyone has had a turn.

# How It Works

The script contains two functions:

1. `name_picker()`: This function takes in the number of people present and their names, and randomly selects one person to give the first update.

2. `game_picker()`: This function selects a random icebreaker game from a pre-defined list and provides a brief description of the game.

The `main()` function runs both of these functions and prints the results.

# Icebreaker Games

The script currently includes 36 icebreaker games:

1. **One Word Game**: Each person picks one word to describe themselves for the week and is referred to by that name throughout the meeting.

2. **Two Truths, One Lie**: Each person takes a turn saying two truths and one lie about themselves. The other players have to guess which statement is the lie.

3. **Would You Rather...**: Each person takes a turn asking a "would you rather" question. The other players have to answer the question.

4. **What’s Your Favorite Year?**: Each person takes a turn saying what their favorite year is. The other players have to guess why.

5. **No Smiling!**: Each person takes a turn saying something funny. The other players have to try not to smile.

6. **Stranded Desert Island Picks**: Each person takes a turn saying what three things they’d bring to a deserted island. The other players have to guess why.

7. **What Annoys You?**: Each person needs to reveal the personality trait that is most irritating to them and why.

8. **What Kind of Car?**: If your workplace was a car this week, what kind would it be?

9. **What’s Your Theme Song?**: Imagine your life was a movie. What song would be playing in the background?

10. **Be Honest...**: It might seem like a dangerous door to open but ask the team to be honest about their day. The Huffington Post says that, the best  business is done when you're being true and authentic.

11. **Movie That Made You Cry?**: What movie made you cry the most? Why?

12. **Stand Up!**: Remove the chairs from the room in which you’re meeting and tell everyone that it’s a standup meeting.

13. **What’s Your Favorite Color?**: What’s your favorite color and why?

14. **What’s Your Favorite Food?**: What’s your favorite food and why?

15. **skribbl.io**: Go to https://skribbl.io/ and draw something together.

16. **Bucket list**: Name three things that are on your bucket list.

17. **Something else**: If you could be something else. In your ideal world, what would your job be?

18. **Movie pitch**: Pretend that you are an upcoming writer. Give us a synopsis of your debut movie.

19. **Backward names.**: Say your name backward. For the rest of the meeting you are called by your new name.

20. **Famous athlete**: If you were a famous athlete, who would you be and why?

21. **Famous actor**: If you were a famous actor, who would you be and why?

22. **Famous musician**: If you were a famous musician/artist, who would you be and why?

23. **Movie Character**: If you were a movie character, who would you be and why?

24. **Hot date**: If you could go on a date with someone (that's not your true partner), who would it be and why?

25. **Controversial opinion**: Share a controversial opinion you have about a trivial matter (eg pizza is overrated).

26. **Two-Sentence Horror Stories**: Each person takes a turn sharing a two-sentence horror story. The other players can react or ask questions.

27. **Alphabet Game**: Pick a category (such as food, animals, or cities) and take turns naming something in that category that starts with each letter of the alphabet, going in order (A, B, C, etc.).

28. **Impromptu Speeches**: Each person is given a random topic to speak about for one minute without any preparation. The other players can ask questions or provide feedback after each speech.

29. **Guess Who**: One person chooses a famous person (real or fictional) and gives three clues about them. The other players have to guess who it is.

30. **This or That**: Ask each person a series of 'this or that' questions (such as 'coffee or tea?' or 'beach or mountains?') and discuss their answers.

31. **Pictionary**: One person draws a picture and the other players try to guess what it is. You can use a virtual whiteboard or a website like skribbl.io.

32. **Never Have I Ever**: Each person takes a turn saying something they have never done (such as 'never have I ever gone bungee jumping'). The other players who have done that thing have to take a drink (or do a different penalty).

33. **Name Game**: Start with a category (such as fruits, movies, or celebrities) and take turns naming something in that category. Each person has to repeat all the previous answers before adding their own.

34. **Charades**: One person acts out a word or phrase without speaking, and the other players try to guess what it is.

35. **Word Association**: Start with a word and take turns saying a word that is associated with the previous word (such as 'dog' -> 'cat' -> 'mouse' -> 'cheese').

36. **Curve Fever**: Go to https://curvefever.pro/ and play a game together.

# Contributing

If you have an idea for a new icebreaker game or an improvement to the script, feel free to submit a pull request or open an issue