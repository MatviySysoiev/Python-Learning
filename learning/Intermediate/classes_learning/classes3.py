class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class AdminUser(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        # super() calls the parent class's constructor
        # to initialize shared attributes
        self.role = role
        self.is_admin = True


my_admin = AdminUser('admin123', 'admin@admin.com',
                     'Administator')


print(my_admin)  # <__main__.AdminUser object at 0x000001D0BD798590>
print(type(my_admin))  # <class '__main__.AdminUser'>
print(isinstance(my_admin, AdminUser))  # True
print(isinstance(my_admin, User))  # True
print(isinstance(my_admin, object))  # True

print(my_admin.__dict__)

my_user = User("bob", 'bob@bob.com')

print(my_user.__dict__)
print(User.__subclasses__())
