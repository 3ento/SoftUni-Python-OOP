class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 < len(value) < 16:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        upper_case = False
        digit = False
        for el in value:
            if el.isupper():
                upper_case = True
            elif el.isdigit():
                digit = True

        if len(value) < 8 or not upper_case or not digit:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        fsk = "*"
        return f"You have a profile with username: " + '"' + self.username + '"' + f" and password: {fsk * len(self.password)}"

# 100/100
