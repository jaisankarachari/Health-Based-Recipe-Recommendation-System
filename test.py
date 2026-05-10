from model.recommender import recommend_recipes

result = recommend_recipes("veg", "diabetes", 30)
print(result)