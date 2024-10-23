import numpy as np

def analyze_performance(scores):
    mean = np.mean(scores)
    median = np.median(scores)
    variance = np.var(scores)
    std_dev = np.std(scores)
    return mean, median, variance, std_dev

player_scores = np.random.randint(50, 100, size=100)

mean, median, variance, std_dev = analyze_performance(player_scores)

print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
