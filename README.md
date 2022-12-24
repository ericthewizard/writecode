# Codeit

Codeit is a command-line tool that generates code from text prompts using OpenAI's Codex model. With Codeit, you can quickly and easily generate code snippets in a variety of languages without having to write any code yourself.

## Installation

To install Codeit, you will need to have Python 3 and pip installed on your system. Then, you can use pip to install the Codeit package from PyPI:

```bash
pip install codeit
```

## Usage

The main function in Codeit is `codeit.code`, which takes the following keywords:

- `prompt` (required): A string containing the text prompt with the instructions for Codex.
- `lang` (optional): The language to generate code in. The default is Python.
- `max_tokens` (optional): An integer specifying the maximum number of output tokens.
- `best_of` (optional): An integer specifying the number of completions to generate server-side and return the "best" (the one with the highest log probability per token). The default is 3.
- `save` (optional): The name of the output file to save the code snippet to.

Here's an example of how to use the `code` function to generate a Python code snippet and save it to a file:

```python
from codeit import code

prompt = "Write a function that takes a list of integers and returns the sum of the even numbers in the list."
code(prompt, lang='python', max_tokens=1000, save='output.py')
```

This will generate a Python code snippet with up to 1000 tokens and save it to a file called `output.py`.

## Supported Languages

Codeit currently supports code generation for the following languages:

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

Codeit is powered by OpenAI's Codex model, which is a powerful tool for generating code from text prompts. However, it is not perfect and may not always produce accurate or complete code snippets. It is important to carefully review the generated code before using it in any production systems.

