import json

def encode(py_file: str):
    with open('src/template.c', 'r') as file:
        with open(py_file, 'r') as insert_file:
            return (
                 file.read().replace(
                      'CODE GOES HERE', 
                      json.dumps( # Automatically escapes all quotes
                           insert_file.read()
                        )
                    )
                )