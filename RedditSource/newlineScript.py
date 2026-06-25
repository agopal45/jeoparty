import json

def format_json(input_file, output_file):
    try:
        # Load the raw data from the file
        with open(input_file, 'r') as f:
            data = json.load(f)
            print(len(data))
        
        # Write it back to a file with indentation
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=1)
            
        print(f"Successfully formatted '{input_file}' to '{output_file}'.")
        
    except json.JSONDecodeError:
        print("Error: The file does not contain valid JSON.")
    except FileNotFoundError:
        print("Error: The specified input file was not found.")

# Usage
format_json('JEOPARDY_QUESTIONS1.json', 'output.json')