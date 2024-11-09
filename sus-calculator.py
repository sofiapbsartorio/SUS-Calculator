# Replace the list below with the answers you got. Each line of the list represents a participant and its answers.
answers = [
    [5, 1, 5, 1, 4, 2, 5, 2, 5, 1],
    [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],
    [4, 2, 5, 2, 4, 2, 4, 2, 4, 1],
    [4, 1, 5, 1, 5, 1, 3, 2, 5, 1]
]

def calculate_sus_score(answers):
    scores = []
    for answer in answers:
        total = 0
        for i, value in enumerate(answer):
            if (i % 2) == 0:  # Even questions
                total += value - 1
            else:  # Odd questions
                total += 5 - value
        sus_score = total * 2.5  # Puts the result on a scale of 0 to 100.
        scores.append(sus_score)
    return scores

sus_scores = calculate_sus_score(answers)

for i, score in enumerate(sus_scores): 
    print(f"SUS score for participant {i+1}: {score}")

mean_score = sum(sus_scores) / len(sus_scores)
print(f"\nSUS mean score: {mean_score}")


