mycards_input = []

for i in range(6):
    mycards_input.append(input())

play_card_ranks: dict = {"2": 2,
                         "3": 3,
                         "4": 4,
                         "5": 5,
                         "6": 6,
                         "7": 7,
                         "8": 8,
                         "9": 9,
                         "10": 10,
                         "Jack": 11,
                         "Queen": 12,
                         "King": 13,
                         "Ace": 14}

mycards_value = []

for card in mycards_input:
    mycards_value.append(play_card_ranks.get(card))


print(sum(mycards_value) / 6)
