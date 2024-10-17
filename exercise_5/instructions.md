# Exercise 5: Refactor

## Suggested workflow
- Use Codeium Chat.
- Ask for suggestions on how to refactor the game.
- Select a few suggestions to do
- Refactor into separate files

The suggested workflow is described in detail below.

## Steps:

1. **Use Codeium chat or command.**
2. **Example question to get refactoring suggestion**
   - what are your suggestions for refactoring the code in the file pong_5.py?
3. **Refactor constants into separate file.**
   - Example: refactor the constants in pong_5.py into a separate file
4. **Refactor the players into a single class.**
   - Less good prompt:
     - can you help me refactor everything that has to do with the players into a class in pong_5.py?
   - Better prompt (more detailed):
     - can you help me refactor everything that has to do with the players into a class in pont.py? there are 2 types of players, one controlled by the up and down keys and one by the computer that follows the ball on the y-axis
5. **Refactor the ball into a class.**
   - Example: refactor the code that has to do with the ball in pong_5.py into a separate class including all logic
6. **Refactor the game logic into a class.**
   - Example: based on the code in player.py and ball.py, create a Game class.
   - There might be issues with the answer, so you might need to follow up with more questions/prompts, example:
   - there are overlaps in the code in Game.handle_events and Player.update, i want Player to handle that
7. **Create a new main file.**
   Example: based on the content of player.py, ball.py, constants.py, game.py and pong_5.py, can you create a new main file for me?
8. **Run the game.**
    You should now be able to run your new refactored game (hopefully). If not, explain the errors/bugs to copilot and try to fix them, and then try to run it again.