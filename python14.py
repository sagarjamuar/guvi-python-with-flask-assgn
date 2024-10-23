import re

def extract_hashtags(post):
    pattern = r'#\w+'  # Match hashtags containing letters, numbers, or underscores
    hashtags = re.findall(pattern, post)
    unique_hashtags = sorted(set(tag for tag in hashtags if tag[1:].isalnum()))
    return unique_hashtags

post = "Loving the new #Python3 features! #coding #100DaysOfCode #Python #MachineLearning #AI #coding"
unique_hashtags = extract_hashtags(post)

print("Unique Hashtags:", unique_hashtags)
