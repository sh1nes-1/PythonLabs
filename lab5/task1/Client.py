class Client:
    def __init__(self, first_name, last_name, birthday, sex, credit_amount, tel):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.sex = sex
        self.credit_amount = credit_amount
        self.tel = tel

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}' \
            .format(self.first_name, self.last_name, self.birthday.date(), self.sex, self.credit_amount, self.tel)
