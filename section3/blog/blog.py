class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return '{} by {} ({} post{})'.format(self.title,
                                             self.author,
                                             len(self.posts),
                                             's' if len(self.posts) != 1 else '')

