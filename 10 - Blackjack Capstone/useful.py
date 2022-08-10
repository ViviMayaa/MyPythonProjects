from art import ArtModels


def positive_feedback(answer_play):
    positive_list = [
        'yes', 'y', 'maybe', 'for sure',
        'sure', 'yeah', 'i may', 'i shall',
        'absolutely', 'whatever', 'why not',
        'i will', 'ok'
    ]
    for positive_element in positive_list:
        if answer_play == positive_element:
            return True
        else:
            continue
    return False


def cards():
    cards_dict = [
        {
            "card_type": "Ace Card",
            "card_art": ArtModels.card_a(),
            "card_value": 10
        },
        {
            "card_type": "Queen Card",
            "card_art": ArtModels.card_q(),
            "card_value": 10
        },
        {
            "card_type": "King Card",
            "card_art": ArtModels.card_k(),
            "card_value": 10
        },
        {
            "card_type": "Jack Card",
            "card_art": ArtModels.card_j(),
            "card_value": 10
        },
        {
            "card_type": "Ten Card",
            "card_art": ArtModels.card_ten(),
            "card_value": 10
        },
        {
            "card_type": "Nine Card",
            "card_art": ArtModels.card_nine(),
            "card_value": 9
        },
        {
            "card_type": "Eight Card",
            "card_art": ArtModels.card_eight(),
            "card_value": 8
        },
        {
            "card_type": "Seven Card",
            "card_art": ArtModels.card_seven(),
            "card_value": 7
        },
        {
            "card_type": "Six Card",
            "card_art": ArtModels.card_six(),
            "card_value": 6
        },
        {
            "card_type": "Five Card",
            "card_art": ArtModels.card_five(),
            "card_value": 5
        },
        {
            "card_type": "Four Card",
            "card_art": ArtModels.card_four(),
            "card_value": 4
        },
        {
            "card_type": "Three Card",
            "card_art": ArtModels.card_three(),
            "card_value": 3
        },
        {
            "card_type": "Two Card",
            "card_art": ArtModels.card_two(),
            "card_value": 2
        },
        {
            "card_type": "One Card",
            "card_art": ArtModels.card_one(),
            "card_value": 1
        }

    ]
    return cards_dict
