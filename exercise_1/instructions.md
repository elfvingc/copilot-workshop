# Exercise 1: Code explanation

## Suggested workflow

- Use Codeium Chat or Codeium Explain (above functions)
- Get explanation of the files.
- Run the game.

The suggested workflow is described in detail below.

## Explaining code

### Steps:

1. **Open Codeium chat**
2. **Track correct file**
    - Make sure the correct file is marked as "script_1.js CURRENT"
3. **Get copilot to explain the code**
    - Try to get copilot to explain the code for you.
    - Either use the chat or Explain (or try both):
      - Chat:
        1. Try to get an explanation of one of the files, example:
            - Explain the code in script_1.js
        2. Get explanation through "advanced context":
            - /explain @script_1.js
            - Type in the chat "/explain @<any-function-name>" (replace <any-function-name> with a function that exists in one of the files), select the function that are in the correct directory and file and press enter, example:
                - /explain @update
     - Explain:
        1. Press "Explain" in the text "Codeium: Refactor | Explain | Generate Docstring | X" above any of the functions.
    - Repeat until you have explained the code in all files.


## Run the game

### Steps:

1. **Open the terminal**
    Use the terminal inside VS Code:
    - VS Code: Press "Terminal in the top left corner of the window".
2. **Run the game**
    - Write the following in the terminal (assuming that you are in the exercise_1 directory):
        ./main.sh
3. **Play the game**
    - The left player can be controlled by the up and down arrows on the keyboard, the right player is the computer.
