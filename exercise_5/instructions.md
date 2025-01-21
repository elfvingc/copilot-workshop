# Exercise 5: Fix bugs

## Suggested workflow

- Explain the bugs (one by one) and try to get copilot to fix them.

The suggested workflow is described in detail below.

### Steps:

1. **Run one of the buggy files**
    - Run any file of your choice with:
        python3 <name-of-file>
    - Check the output of the script.

2. **Explain the bug to copilot and try to get copilot to fix it.**
    - Use any of the following options (or try them all to see if they give different outcomes):
        - Explain the bug in the chat and make sure the correct file is marked as "CURRENT" or refer to it with "@"
        - Use "Refactor" above a function and select "Check for bugs and null pointers"
        - Mark a code block and open the Codium command (ctrl + i or ctrl + shift + i (depending on your keybindings)).
        - Use "@terminal" and choose last command in the chat and explain the bug.

3. **Verify that it works  as expected.**
    Run the file you chose with:
        python3 <name-of-file>

4. **Repeat from 1 until you have solved all bugs in all buggy files**
