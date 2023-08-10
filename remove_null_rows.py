import pandas as pd

dataframe_reaction_type = pd.read_csv("/Users/josephkambham/Downloads/ReactionTypes.csv")

# dataframe_reaction_type.dropna()

# print(dataframe_reaction_type.isnull())

dataframe_reactions = pd.read_csv("/Users/josephkambham/Downloads/Reactions.csv")

dataframe_reactions_after_deletion_null = dataframe_reactions.dropna()

dataframe_contents = pd.read_csv("/Users/josephkambham/Downloads/Content.csv")

dataframe_contents_after_deleting_null = dataframe_contents.dropna()


def aces_player():
    player_cards = [1, 'ace', 'king', 10, 11]
    new_list = []
    total_count = 0
    for i, card in enumerate(player_cards):
        if player_cards[i] == 'ace' or player_cards[i] == 'king':
            player_cards[i] = 10
            # new_list.append(player_cards[i])
        else:
            player_cards[i]
            # new_list.append(player_cards[i])

        total_count = total_count + player_cards[i]
    return total_count
    # print(player_cards)
    # print(total_count)


print(aces_player())
