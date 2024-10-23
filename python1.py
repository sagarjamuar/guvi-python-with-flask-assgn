import os

def read_scores(filename):
    if not os.path.isfile(filename):
        return None
    try:
        with open(filename, 'r') as file:
            scores = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2 and parts[1].isdigit():
                    scores.append((parts[0], int(parts[1])))
            return scores
    except:
        return None

def calculate_average(scores):
    if not scores:
        return None
    total = sum(score for _, score in scores)
    return total / len(scores)

def get_above_average_students(scores, average):
    return [name for name, score in scores if score > average]

filename = 'students_scores.txt'
scores = read_scores(filename)

if scores:
    average = calculate_average(scores)
    if average is not None:
        above_average_students = get_above_average_students(scores, average)
        print("Average score:", average)
        print("Students scoring above average:", above_average_students)
    else:
        print("No valid scores found.")
else:
    print("File not found or contains invalid data.")
