def text_filter(text, words):
    for word in words:
        text = text.replace(word, '*' * len(word))
    return text

words = 'Linux, Windows'.split(', ')
text ='It is not Linux, it is GNU/Linux. Linux is merely the kernel, while GNU adds the functionality. Therefore we owe it to them by calling the OS GNU/Linux! Sincerely, a Windows client'

print(text_filter(text, words))