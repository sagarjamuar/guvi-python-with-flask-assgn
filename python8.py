def filter_and_square_ratings(ratings):
    if not ratings:
        return "No ratings provided."
    return [r**2 for r in ratings if r >= 5]

movie_ratings = [3, 7, 5, 8, 4, 9, 6, 2, 10]
good_ratings_squared = filter_and_square_ratings(movie_ratings)
print(good_ratings_squared)
