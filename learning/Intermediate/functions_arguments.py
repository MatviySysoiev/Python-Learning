def sum_nums(*args):  # positional arguments can be converted to tuples
    print(args)  # (1, 2, 3)
    print(type(args))  # <class 'tuple>

    print(args[0])  # 1
    return (sum(args))


print(sum_nums(1, 2, 3))  # 6


def sum_nums(*args):  # positional arguments can be converted to tuples
    print(args)  # ()
    print(type(args))  # <class 'tuple>

    return (sum(args))


print(sum_nums())  # 0


def get_posts_info(name, posts_qty):
    return f"{name} wrote {posts_qty} posts"


print(get_posts_info("Matthew", 12))  # positional arguments
# Matthew wrote 12 posts


def get_posts_info(name, posts_qty):
    return f"{name} wrote {posts_qty} posts"


print(get_posts_info(posts_qty=20, name='Matthew'))  # keyword arguments
# We use keyword arguments, so the position of the arguments doesn't matter
# Matthew wrote 20 posts


def get_posts_info(**person):  # ** means keyword arguments can be converted to dics
    print(person)
    print(type(person))  # <class 'dict'>

    info = (
        f"{person.get('name', 'Unknown')} wrote "  # no comma
        f"{person.get('posts_qty', 'unknown')} posts"
    )  # its not a tuple because there is no comma. It's like one stroke
    return info


print(get_posts_info(name='Matthew', posts_qty=25))  # keyword arguments
