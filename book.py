class Book:
    def __init__(self, title, is_paper):
        self.title = title
        self.is_paper = is_paper
        if is_paper:
            self.price = 9.99
        else:
            self.price = 19.99

    def __str__(self):
        return self.title
