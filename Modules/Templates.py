import fileinput
import re
import os

# Matches fields enclosed in square brackets:
field_pat = re.compile(r'\[(.+?)\]')
# We'll collect variables in this:
scope = {}


# This is used in re.sub:
def replacement(match):
    code = match.group(1)
    try:
        # Check if the code can be evaluated
        if code in scope:
            return str(eval(code, scope))
        else:
            # If the variable is not yet defined, execute it to define or update it
            exec(code, scope)
            return str(eval(code, scope))
    except SyntaxError:
        # Otherwise, execute the assignment in the same scope ... exec code in scope
        # ... and return an empty string:
        return ''


# Get all the text from the input file(s):
def process_file(input_filename, output_filename):
    with fileinput.input(files=(input_filename,)) as f:
        lines = []
        for line in f:
            lines.append(line)
        text = ''.join(lines)

    # Substitute all the occurrences of the field pattern:
    result = field_pat.sub(replacement, text)
    result = result.strip()  # Remove leading and trailing whitespace
    # Write the result to the output file
    with open(output_filename, 'w') as output_file:
        output_file.write(result)


if __name__ == '__main__':
    # print("Current Working Directory:", os.getcwd())
    # Replace 'template.txt' with the actual path to your template file
    template_file = 'template1.txt'
    output_file = 'output1.txt'  # Specify the output file name here
    process_file(template_file, output_file)
    print(f"Processed output written to {output_file}")
