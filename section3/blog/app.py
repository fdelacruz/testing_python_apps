blogs = dict()  # blog_title: Blog Object


def menu():
    # Show the user the available blogs
    # let the user make a choice
    # Do something with that choice
    # Eventually exit

    print_blogs()


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))
