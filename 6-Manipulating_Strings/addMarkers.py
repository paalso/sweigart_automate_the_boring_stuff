import pyperclip

MARKER = "*"

_input = pyperclip.paste().split("\r\n")
pyperclip.copy("\n".join(map(lambda text: MARKER + " " + text , _input)))
