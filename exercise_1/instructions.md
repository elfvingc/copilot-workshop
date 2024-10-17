# Exercise 1: Code explanation

## Suggested workflow

- Use Codeium Chat or Codeium Explain (above functions)
- Get explanation of the files/classes.
- Run the game.

The suggested workflow is described in detail below.

## Explaining code

### Steps:

1. **Open Codeium chat**
2. **Track correct file**
    - Make sure the correct file is marked as "pong_1.py CURRENT"
3. **Get copilot to explain the code**
    - Try to get copilot to explain the code for you.
    - Either use the chat or Explain (or try both):
      - Chat:
        1. Try to get an explanation of one of the files, example:
            - Explain the code in ball.py
        2. Get explanation through "advanced context":
            - Type in the chat "/explain @<any-function-name>" (replace <any-function-name> with a function that exists in one of the files), select the function that are in the correct directory and file and press enter.
     - Explain:
        1. Press "Explain" in the text "Codeium: Refactor | Explain | Generate Docstring | X" above any of the functions.
    - Repeat until you have explained the code in all files.


## Run the game

### Steps:

1. **Open the terminal**
    Either use the terminal inside VS Code or the WSL terminal:
    - VS Code: Press "Terminal in the top left corner of the window".
    - WSL: Open the Windows menu and search for "Ubuntu" and start the app.
2. **Run the game**
    - Write the following in the terminal:
        python3.11 pong_1.py
3. **Play the game**
    - The left player can be controlled by the up and down arrows on the keyboard.
