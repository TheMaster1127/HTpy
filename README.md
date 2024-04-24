
### HTpy: Early Development Preview

**HTpy** is a custom scripting language designed to transpile AHK-like syntax files into Python scripts. It allows users to write scripts using HTpy syntax and convert them into executable Python code.

**Note:** This project is still in its early stages of development.

#### Usage Example

So far HTpy supports:

- msgbox
- sleep
- variables

Here's an example of HTpy syntax:

```plaintext
msgbox, hello
sleep, 500
msgbox, hello
var1 := "werfg"
msgbox, %var1%
num := 1
var%num% := "hi"
msgbox, %var1%
```

#### Try It Out

You can experiment with HTpy syntax [here](https://themaster1127.github.io/HTpy/).

