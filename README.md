# HTpy

HTpy is a custom scripting language that transpiles `.htpy` files into Python scripts. It enables users to write simple scripts using HTpy syntax and convert them into executable Python code.

## Getting Started

To use HTpy, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/TheMaster1127/HTpy.git
   cd HTpy
   ```

2. **Write HTpy Script**

   Create a `.htpy` file and write HTpy code using the supported syntax (e.g., `msgbox, "Hello, World!"`).

3. **Run Transpiler**

   Use the `HTpy.py` script to transpile your `.htpy` file into a Python script.

   ```bash
   python HTpy.py your_script.htpy
   ```

   This command will transpile `your_script.htpy` into `your_script.py`.

4. **Execute Python Script**

   Execute the generated Python script.

   ```bash
   python your_script.py
   ```

   This will run the Python script and execute the corresponding actions defined in your HTpy script.

## HTpy Syntax

HTpy supports a limited set of commands. Currently, you can use `msgbox` to display a message box with text.

Example HTpy script (`example.htpy`):

```plaintext
msgbox, "Hello, HTpy!"
```

