import json

import pandas as pd


def process_content_ads(content):
    cards = {}
    for i, card in enumerate(content):
        card_col={}
        columns = [col for col in card.split('\n') if len(col.strip())>0 and col not in ('\u200b')]
        for j, col in enumerate(columns):
            card_col[f'col_{j+1}'] = col
        cards[f'card_{i+1}'] = card_col

    print(cards)
    return cards
