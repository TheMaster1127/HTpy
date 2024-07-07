### HTpy

**HTpy** is a custom scripting language designed to transpile AHK-like syntax files into Python scripts. It allows users to write scripts using HTpy syntax and convert them into executable Python code.

#### Try It Out

You can experiment with HTpy syntax using the [HTpy online editor](https://themaster1127.github.io/HTpy/). Note that this editor provides only a subset of HTpy functionality.
The transpiler processes the code in real time. If you encounter any glitches or the transpiled code doesn't work correctly, simply click on 'Transpile' or press Ctrl+Enter, and it should resolve the issue. Otherwise, it could be an error in your code or possibly an issue with the transpiler itself.

#### Install localy

1. Clone this repository
2. The tarnspiler is HTpy.py
3. You can make a .htpy file then use the HTpy.py to transpile it to python for example:
```
python HTpy.py file_name.htpy
```
or (optional) add run to run it immediately after
```
python HTpy.py file_name.htpy run
```
you should get a .py file whit the same name as the .htpy
When you transpile the .htpy script it will replace the .py whit the same name if it exists.

I recommend using SciTE4HTH where i added HTpy support.

Why use SciTE4HTH for HTpy?
- It provides syntax highlighting and code completion for the HTpy language, making it easier to write and read HTpy scripts.

How to use SciTE4HTH for HTpy:
1. Download and install the SciTE4HTH editor from https://github.com/TheMaster1127/SciTE4HTH
2. Go to the htpy.properties and put the full path of your HTpy.py then restart the SciTE editor by re-opening it.
3. Open SciTE and create a new file with the .htpy extension (or open an existing .htpy file).
4. Write your HTpy code in the editor. You'll get syntax highlighting and code completion as you type.
5. To transpile your HTpy code to Python, simply press F5 or click the "Run" button. This will execute the transpiled Python code.
6. If you just want to transpile without running, press Ctrl+F7 or go to Tools > Compile.

That's it! SciTE4HTH gives you a user-friendly environment to write HTpy scripts, with helpful features like syntax highlighting and code completion, while allowing you to easily transpile to Python code with just a few clicks or keystrokes.

#### Usage Example

HTpy currently supports a subset of commands similar to AutoHotkey:

- Functions
- If, else, else if
- Random
- Sleep
- Msgbox
- FileRead
- FileAppend
- SetTimer
- Labels
- Gosub
- Return/return
- Loop
- Loop, Parse
- Variables
- RunCMD and ExitApp
- Comments
- Sort
- Endpoint
- getDataFromAPI and getDataFromJSON
- Math Functions
- Build-in Functions
- Build-in Variables

here is the full documentation: [Documentation](https://github.com/TheMaster1127/HTpy/wiki)
