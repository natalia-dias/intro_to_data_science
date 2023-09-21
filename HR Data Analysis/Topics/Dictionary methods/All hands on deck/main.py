card_dict = {'Jack': 11, "Queen": 12, 'King': 13, 'Ace': 14}
sum_cards = 0
for i in range(6):
    x = input()
    if x in card_dict.keys():
        sum_cards += card_dict[x]
    else:
        sum_cards += int(x)

print(sum_cards / 6)