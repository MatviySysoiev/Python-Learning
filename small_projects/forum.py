class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email


class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author


class Forum:
    def __init__(self):
        self.users = []
        self.posts = []

    def register_user(self, username: str, email: str):
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, title: str, content: str, author: User):
        post = Post(title, content, author)
        self.posts.append(post)
        return post

    def find_user_by_username(self, username: str):
        for user in self.users:
            if user.username == username:
                return user

    def find_user_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user

    def find_posts_by_author(self, author: User):
        found_posts = []
        for post in self.posts:
            if post.author == author:
                found_posts.append(post)
        return found_posts

    def find_posts_by_email(self, email: str):
        user_found = forum.find_user_by_email(email)
        if user_found:
            res = forum.find_posts_by_author(user_found)
            return res
        else:
            return f"User with email {email} was not found!"


forum = Forum()

new_user = forum.register_user('Matvii', 'mat@gmail.com')
user2 = forum.register_user('Alice', 'alice@gmail.com')

forum.create_post("My first post", "Post content", new_user)

# Find user by their username
print(forum.find_user_by_username("Matvii2"))  # None
# <__main__.User object at 0x000001C8441286E0>
print(forum.find_user_by_username("Matvii"))

print(forum.find_user_by_username("Matvii").email)  # mat@gmail.com

forum.create_post("Second great post", "New post that I created",
                  new_user)

# Find posts of the user
found_posts = forum.find_posts_by_author(new_user)
found_posts_titles = [post.title for post in found_posts]
print(found_posts_titles)

# Find posts by user's email
print(forum.find_posts_by_email('mat@gmail.com'))
