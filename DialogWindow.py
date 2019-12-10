import dialogs as dl


class DialogWindow:
    def __init__(self):
        self.width = 500
        self.height = 200
        self.color = (0, 0, 0)
        self.text = ''

    def set_phrase(self, human, i):
        self.text = dl.dialogs[human][i]
