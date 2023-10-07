# Define the input and output file names
input_file_name = 'input.txt'
output_file_name = 'output.txt'

# Read from the input file
try:
    with open(input_file_name, 'r') as input_file:
        # Read the content of the input file
        file_content = input_file.read()
        
        # You can perform operations on the file_content as needed
        # For example, let's convert the content to uppercase
        file_content = file_content.upper()
        
        # Write the modified content to the output file
        with open(output_file_name, 'w') as output_file:
            output_file.write(file_content)
    
    print(f'Successfully read from {input_file_name} and wrote to {output_file_name}')
    
except FileNotFoundError:
    print(f'The file {input_file_name} was not found.')
except Exception as e:
    print(f'An error occurred: {str(e)}')

#'a' method is used to append the data after the data of the existing file.
