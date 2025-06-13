# A script to process user-submitted ratings
ratings = [4, 5, "3", 4, 2]

total = sum(ratings)
average = total / len(ratings)

print(f"Average rating: {average:.1f}/5")