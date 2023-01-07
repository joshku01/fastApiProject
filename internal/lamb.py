class Lambda:
    def __init__(self):
        pass

    def title(self):
        title = "HelloPython"
        (lambda title: print(title))(title)
