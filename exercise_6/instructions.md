# Exercise 6: Fix bugs in game

## Suggested workflow

- Explain the bugs (one by one) and try to get copilot to fix them.

The suggested workflow is described in detail below.

### Steps:

1. **Explain the bugs to copilot and try to get copilot to fix them.**
    - Use the chat, or "Refactor" above a function and select "Check for bugs and null pointers", or mark a code block and open the Codium command (ctrl + shift + i or ctrl + i (depending on your keybindings))

#### Example prompts

- Player 1 can move outside of the game, both at the top and at the bottom, can you fix that bug?
- Player 2 can move outside of the game, both at the top and at the bottom, can you fix that bug?
- The ball does not bounce correctly against the players
- The ball should restart in the middle if it touches the walls behind the players

2. **Verify that the game works as expected.**
    Run the game by writing the following in the terminal:
        python3.11 pong_6.py
