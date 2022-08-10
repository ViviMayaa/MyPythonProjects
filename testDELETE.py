import random
def cards():
    cards = [
        {
            "card_type": "Ace Card",
            "card_art": 'ArtModels.card_a()',
            "card_value": 10
        },
        {
            "card_type": "Ace Card22",
            "card_art": 'ArtModels.card_a()',
            "card_value": 10
        }
    ]
    return cards

card_dict = random.choice(cards())
print(card_dict)
# cards = [
#         {
#           "card_type": "Ace Card",
#           "card_art": "ArtModels.card_a()",
#           "card_value": 10
#         },
# {
#           "card_type": "Ace Card2",
#           "card_art": "ArtModels.card_a()",
#           "card_value": 10
#         }
#     ]
#
# for elements in cards:
#     for element in elements:
#         print(elements[element])
# cards = cards()
# for list_of_dicts_in_cards in cards:
#     for value_in_dict in list_of_dicts_in_cards:
#         print(list_of_dicts_in_cards[value_in_dict])