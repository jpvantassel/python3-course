"""Check examples are valid Python code."""

import re
import os

test_files = ["intro/text_files.md"]

parse = re.compile("```python3([^`]*)```", re.DOTALL)

for fname in test_files:
    with open(fname, "r") as f:
        data = f.read()

    for test_case in parse.finditer(data):
        code_block = test_case.groups()[0]
        try:
            exec(code_block)
        except Exception as e:
            print("")
            print("EXCEPTION!")
            print(f"File Name: {fname}")
            print(f"Code Block: {code_block}")
            raise e
        
os.remove("example.txt")