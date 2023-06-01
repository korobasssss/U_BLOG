class User:
    def __init__(self, name, surname, username, password, message):
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        self.messages = message

    @property
    def get_name(self):
        return self.name

    @property
    def get_surname(self):
        return self.surname

    @property
    def get_username(self):
        return self.username

    @property
    def get_password(self):
        return self.password

    def get_messages(self):
        return self.messages

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_message(self, message):
        self.messages.append(message)
