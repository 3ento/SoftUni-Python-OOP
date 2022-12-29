class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.domains = domains
        self.mails = mails
        self.min_length = min_length

    def __is_name_valid(self, name):
        if len(name) >= self.min_length:
            return True
        return False

    def __is_mail_valid(self, mail):
        if mail in self.mails:
            return True
        return False

    def __is_domain_valid(self, domain):
        if domain in self.domains:
            return True
        return False

    def validate(self, email):
        a = email.split("@")
        b = a[1].split(".")
        username = a[0]
        mail = b[0]
        domain = b[1]

        if self.__is_name_valid(username) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain):
            return True
        return False

# 100/100
