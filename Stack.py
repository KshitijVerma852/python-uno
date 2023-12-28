from Card import Card


class Stack:
    """
    Defines the playing and non-playing stacks.
    """
    def __init__(self):
        self.__values = []
        self.__top = None
        self.__bottom = None

    def push(self, card: Card):
        if len(self.__values) == 0:
            self.__top = card
            self.__bottom = self.__top
        else:
            self.__top = card

        self.__values.append(card)

    def pop(self):
        if len(self.__values) == 0:
            raise Exception("Stack is already empty.")
        else:
            self.__values.pop()

    def getLength(self) -> int:
        return len(self.__values)

    def getTop(self) -> Card:
        return self.__top

    def getBottom(self) -> Card:
        return self.__bottom

    def populate(self):
        self.__values = Card.getAllCards()
        self.__top = self.__values[-1]
        self.__bottom = self.__values[0]
