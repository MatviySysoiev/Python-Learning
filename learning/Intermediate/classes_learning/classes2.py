class Comment:
    def __init__(self, text, initial_votes_qty=0):
        self.text = text
        self.votes_qty = 0

    def upvote(self, quantity):
        self.votes_qty += quantity


my_comment = Comment("This is my first comment")
print(my_comment)  # <__main__.Comment object at 0x000001728B8186E0>
print(type(my_comment))  # <class '__main__.Comment'>
# {'text': 'This is my first comment', 'votes_qty': 0}
print(my_comment.__dict__)
print(dir(my_comment))

print(my_comment.text)  # This is my first comment
print(my_comment.votes_qty)  # 0

my_comment.upvote(15)
print(my_comment.votes_qty)  # 15

my_comment.upvote(3)
print(my_comment.votes_qty)  # 18

my_comment.upvote = 10

# TypeError: 'int' object is not callable
# my_comment.upvote(5)

# {'text': 'This is my first comment', 'votes_qty': 18, 'upvote': 10}
print(my_comment.__dict__)

second_comment = Comment("Second comment")
second_comment.upvote(2)
print(second_comment.votes_qty)
