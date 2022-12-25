from .main import writecode, explaincode


def code(prompt, lang='Python', max_tokens=256, best_of=3, save=None):
    """
    Generates code from a text prompt using OpenAI's Codex model.

    Args:
        prompt: A string containing the text prompt with the instructions for Codex.
        lang: The language to generate code in. The default is Python.
        max_tokens: An optional integer specifying the maximum number of output tokens.
        best_of: An optional integer specifying the number of completions to generate server-side and return the "best" (the one with the highest log probability per token). The default is 3.
        save: An optional string specifying the name of the output file to save the code snippet to.

    Returns:
        A string containing the generated code. If the `save` parameter is specified, the code will also be saved to the specified file.
    """
    return writecode(prompt, lang=lang, max_tokens=max_tokens, best_of=best_of, save=save)


def explain(prompt, max_tokens=256, best_of=3, save=None):
    return explaincode(prompt, max_tokens=max_tokens, best_of=best_of, save=save)
