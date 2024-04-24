### HTpy: Early Development Preview

**HTpy** is a custom scripting language designed to transpile AHK-like syntax files into Python scripts. It allows users to write scripts using HTpy syntax and convert them into executable Python code.

**Note:** This project is still in its early stages of development.

#### Try It Out

You can experiment with HTpy syntax using the [HTpy online editor](https://themaster1127.github.io/HTpy/). Note that this editor provides only a subset of HTpy functionality.

#### Usage Example

HTpy currently supports a subset of commands similar to AutoHotkey:

- `msgbox`: Display a message box.
- `sleep`: Pause script execution for a specified duration.
- Variables: Declare and manipulate variables.
- `Random`: Generate random numbers within specified ranges.

Here's an example of HTpy syntax:

```ahk
var1 := "Python is not so bad!"
MsgBox, %var1%
num := 42
var%num% := num
MsgBox, %var42%

var23 := (55 + 3) - 1 . var%num%
MsgBox, %var23%
Sleep, 600
var1 := true
var2 := false
MsgBox, %var1%
MsgBox, %var2%

somNumber := 55
somNumber += somNumber
somNumber += somNumber
somNumber += somNumber
somNumber += somNumber
MsgBox, %somNumber%

Random, someRandomNums, 1, 20
MsgBox, %someRandomNums%
Random, someRandomNums, 1, 20
MsgBox, %someRandomNums%
Random, someRandomNums, 1, 20
MsgBox, %someRandomNums%
Random, someRandomNums, 1, 20
MsgBox, %someRandomNums%
Random, someRandomNums, 1, 20
MsgBox, %someRandomNums%
Random, someRandomNums, 1, 20
MsgBox, %someRandomNums%
Random, someRandomNums, 1, 20
MsgBox, %someRandomNums%
```
