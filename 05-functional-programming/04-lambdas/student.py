from util import group_by
from util import partition
from util import filter

def group_by_suit(cards):
    return group_by(cards, lambda card: card.suit)


def group_by_value(cards):
    return group_by(cards, lambda card: card.value)


def partition_by_color(cards):
    return partition(cards, lambda card: card.suit == "spades" or card.suit == "clubs")

