def climbingLeaderboard(scores, alice):
    set_score = sorted(list(set(scores)),reverse=True)
    alice_final_score = []
    len_set_score = len(set_score)
    for i in alice:
        for j in range(len_set_score):
            if set_score[j] <= i:
                alice_final_score.append(j+1)
                break
            elif j == len_set_score -1:
                alice_final_score.append(j+2)
    return alice_final_score
            




print(climbingLeaderboard([100,90,90,80,75,60], [50,65,77,90,102]))