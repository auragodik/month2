class User:
    total_users = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.total_users += 1
    @classmethod
    def get_total_users(cls):
        return cls.total_users
    @staticmethod
    def validate_email(email):
        return '@' in email
print(User.get_total_users())
user_1 = User('albert', 'albert@gmail.com')
user_2 = User('igor', 'igor@gmail.com')
user_1.total_users = 4
print(User.total_users)
print(user_1.total_users)
