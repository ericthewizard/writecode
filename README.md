# writecode

writecode is a command-line tool that generates code from text prompts using OpenAI's Codex model. With writecode, you can quickly and easily generate code snippets in a variety of languages without having to write any code yourself.

## Installation

To install writecode, you will need to have Python 3 and pip installed on your system. Then, you can use pip to install the writecode package from PyPI:

```bash
pip install writecode
```

## Usage

The main function in writecode is `writecode.code`, which takes the following keywords:

- `prompt` (required): A string containing the text prompt with the instructions for Codex.
- `lang` (optional): The language to generate code in. The default is Python.
- `max_tokens` (optional): An integer specifying the maximum number of output tokens.
- `best_of` (optional): An integer specifying the number of completions to generate server-side and return the "best" (the one with the highest log probability per token). The default is 3.
- `save` (optional): The name of the output file to save the code snippet to.

Here's an example of how to use the `code` function to generate a Python code snippet and save it to a file:

```python
from writecode import code

prompt = "Write a function that takes a list of integers and returns the sum of the even numbers in the list."
code(prompt, lang='python', max_tokens=1000, save='output.py')
```

This will generate a Python code snippet, followed by an explanation, with up to 1000 tokens and save it to a file called `output.py`.

Example output:
```python
def sum_even(list):
    sum = 0
    for i in list:
        if i % 2 == 0:
            sum += i
    return sum

print(sum_even([1,2,3,4,5,6,7,8,9,10]))

# The function takes a list of integers and returns the sum of the even numbers in the list.
# The function first creates a variable called sum and sets it equal to 0.
# The function then loops through the list and checks if the number is even.
# If the number is even, the function adds it to the sum variable.
# The function then returns the sum variable.
# The function is then called and the list is passed as an argument.
# The function returns the sum of the even numbers in the list.
```
## Supported Languages

writecode currently supports code generation for the following languages:

- Python
- HTML
- C++
- Java
- JavaScript
- C#
- Go
- Ruby
- Swift
- PHP

This list is not exhaustive and may be updated in the future as the Codex model continues to evolve.

## Limitations

writecode is powered by OpenAI's Codex model, which is a powerful tool for generating code from text prompts. However, it is not perfect and may not always produce accurate or complete code snippets. It is important to carefully review the generated code before using it in any production systems.

