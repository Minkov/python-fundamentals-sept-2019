class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: " \
               f"{self.content}. Sent: {self.is_sent}"


class EmailManager:
    def __init__(self):
        self.emails = []

    def add(self, email):
        self.emails.append(email)

    def send(self, index):
        self.emails[index].send()

    def print(self):
        for email in self.emails:
            print(email.get_info())

emailManager = EmailManager()

while True:
    info = input()
    if info == 'Stop':
        break
    [sender, receiver, content] = info.split(' ')

    emailManager.add(
        Email(sender, receiver, content)
    )

indices_of_mails_to_send = map(int, input().split(', '))

for index in indices_of_mails_to_send:
    emailManager.send(index)

emailManager.print()
