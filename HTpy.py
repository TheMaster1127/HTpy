import sys
import subprocess
import os

def process_file(input_file_path):
    # Validate input_file_path
    if not os.path.isfile(input_file_path):
        return f"Error: File '{input_file_path}' not found."

    # Read the contents of the input file
    with open(input_file_path, 'r') as file:
        file_contents = file.read()

    # Execute the HTpy.js Node.js script and send file contents as input
    node_process = subprocess.Popen(['node', 'HTpy.js'],
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)

    stdout, stderr = node_process.communicate(input=file_contents.encode('utf-8'))

    if stderr:
        return f"Error running HTpy.js script: {stderr.decode('utf-8')}"

    # Save the output from HTpy.js to a new file with .py extension
    output_file_name = os.path.splitext(input_file_path)[0] + '.py'
    with open(output_file_name, 'w') as output_file:
        output_file.write(stdout.decode('utf-8'))

    return output_file_name  # Return the name of the generated .py file

if __name__ == '__main__':
    # Check if the command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python HTpy.py <input_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]  # Get the file path from command-line argument
    generated_py_file = process_file(input_file_path)

    if generated_py_file:
        # Run the generated .py file using the default Python interpreter
        try:
            subprocess.run(['python', generated_py_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running generated Python file: {e}")