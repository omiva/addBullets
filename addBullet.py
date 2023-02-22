import clipboard
import pyperclip
txt = pyperclip.paste()
lines = txt.split('\n')
for i in range(len(lines)-1):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)

