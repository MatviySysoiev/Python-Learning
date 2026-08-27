class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

    def __add__(self, other):
        return (f"{self.text} {other.text}",
                self.votes_qty + other.votes_qty)

    def __eq__(self, value):
        if self.text == value.text and self.votes_qty == value.votes_qty:
            return True
        else:
            return False


first_comment = Comment("First comment")
first_comment.upvote()
second_comment = Comment("First comment")
second_comment.upvote()

print(first_comment + second_comment)

print(first_comment == second_comment)


class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


new_list = [1, "Hello", True, 2]

custom_list = ExtendedList(new_list)

custom_list.print_list_info()
# List has 4 elements

custom_list.append(7)
custom_list.print_list_info()
# List has 5 elements

print(list.__subclasses__())
# [<class '_frozen_importlib._List'>, <class '__main__.ExtendedList'>]
