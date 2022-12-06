if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    choices_pc = {"A": "Rock", "B": "Paper", "C": "Scissors"}
    advice = {"X": "loss", "Y": "draw", "Z": "win"}
    advice_score = {"X": 0, "Y": 3, "Z": 6}
    loses_to = {"A": "B", "B": "C", "C": "A"}
    points_shape = {"A": 1, "B": 2, "C": 3}
    total_score = 0
    for item in data:
        p1, p2 = item.split(" ")
        # draw
        if advice[p2] == "win":
            score = points_shape[loses_to[p1]]
        elif advice[p2] == "draw":
            score = points_shape[p1]
        elif advice[p2] == "loss":
            score = points_shape[loses_to[loses_to[p1]]]
        total_score += advice_score[p2]
        total_score += score
    print(total_score)