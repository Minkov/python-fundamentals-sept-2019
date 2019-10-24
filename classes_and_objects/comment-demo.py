class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

print(Comment('john', 'Hello, my fiend', 3).__dict__)
print(Comment('john', 'Hello, my fiend').__dict__)