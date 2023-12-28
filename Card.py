from typing import List

cardValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "plus_2", "skip_next_turn", "reverse"]
powerCardValues = ["plus_4", "change_colour"]
cardColors = ["red", "yellow", "green", "blue"]


class Card:
    """
    Defines the Cards.
    """
    def __init__(self, value, color, isPowerCard: bool):
        self.__value = value
        if type(color) is str:
            self.__color = color
        self.__isPowerCard = isPowerCard

    def __str__(self):
        return f"{self.__value} of color {self.__color}"

    @staticmethod
    def getAllCards() -> List["Card"]:
        ans = []
        for value in cardValues:
            for color in cardColors:
                ans.append(Card(value, color, False))

        for powerCardValue in powerCardValues:
            ans.append(Card(powerCardValue, None, True))

        return ans

