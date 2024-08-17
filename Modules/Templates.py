import fileinput
import re
import os

# Matches fields enclosed in square brackets:
field_pat = re.compile(r'\[(.+?)\]')
# We'll collect variables in this:
scope = {}


# This is used in re.sub:
def execute_assignments(match):
    code = match.group(1)
    try:
        # Execute the assignment to define or update variables
        exec(code, scope)
    except Exception as e:
        print(f"Error processing code '{code}': {e}")
    return ''  # Remove the assignment after processing


def substitute_variables(match):
    code = match.group(1)
    try:
        # Simply evaluate and return the variable
        return str(eval(code, scope))
    except Exception as e:
        print(f"Error processing code '{code}': {e}")
        return ''


# Function to process the variable definitions
def process_definitions(def_file):
    with fileinput.input(files=(def_file,)) as f:
        lines = []
        for line in f:
            lines.append(line)
        definitions = ''.join(lines)

    # Execute all assignments to populate the scope
    field_pat.sub(execute_assignments, definitions)


# Function to handle imports separately
def handle_imports(template_file):
    with fileinput.input(files=(template_file,)) as f:
        lines = []
        for line in f:
            lines.append(line)
        text = ''.join(lines)

    # Extract and execute import statements separately
    imports = field_pat.findall(text)
    for code in imports:
        if code.startswith('import '):
            exec(code, globals(), scope)

    # Remove the import statements from the text
    text = field_pat.sub(lambda match: '' if match.group(1).startswith('import ') else match.group(0), text)

    return text


# Get all the text from the input file(s):
def process_template(input_filename, output_filename):
    text = handle_imports(template_file)

    # Substitute all the occurrences of the field pattern:
    result = field_pat.sub(substitute_variables, text)
    result = result.strip()  # Remove leading and trailing whitespace
    # Write the result to the output file
    with open(output_filename, 'w') as output_file:
        output_file.write(result)


if __name__ == '__main__':
    # print("Current Working Directory:", os.getcwd())
    # Replace 'template.txt' with the actual path to your template file
    definitions_file = 'magnus.txt'
    template_file = 'template.txt'
    output_file = 'output.txt'  # Specify the output file name here

    # Process variable definitions first
    process_definitions(definitions_file)

    process_template(template_file, output_file)
    print(f"Processed output written to {output_file}")
