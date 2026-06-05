# PLAYER SCORE
player_score = []
# input of score form user
for i in range(11):
    score = int(input("Enter the score of player {}: ".format(i + 1)))
    player_score.append(score)
# display the score of player
print("\n----- Player Scores -----")
print("score of 11 players: ", player_score)