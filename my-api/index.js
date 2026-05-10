const express = require("express");

const app = express();
const PORT = 5000;

app.use(express.json()); // Important for POST

app.get("/", (req, res) => {
  res.send("Recipe Recommendation API is running 🚀");
});
// Sample Recipe Data
let recipes = [
  {
    id: 1,
    name: "Chicken Curry",
    ingredients: ["chicken", "onion", "tomato"],
    category: "Non-Veg"
  },
  {
    id: 2,
    name: "Veg Fried Rice",
    ingredients: ["rice", "carrot", "beans"],
    category: "Veg"
  },
  {
    id: 3,
    name: "Paneer Butter Masala",
    ingredients: ["paneer", "butter", "tomato"],
    category: "Veg"
  }
];


// 1️⃣ Get All Recipes
app.get("/recipes", (req, res) => {
  res.json(recipes);
});


// 2️⃣ Get Recipe by ID
app.get("/recipes/:id", (req, res) => {
  const recipe = recipes.find(r => r.id == req.params.id);
  if (!recipe) {
    return res.status(404).json({ message: "Recipe not found" });
  }
  res.json(recipe);
});


// 3️⃣ Add New Recipe
app.post("/recipes", (req, res) => {
  const newRecipe = {
    id: recipes.length + 1,
    name: req.body.name,
    ingredients: req.body.ingredients,
    category: req.body.category
  };

  recipes.push(newRecipe);
  res.status(201).json(newRecipe);
});


// 4️⃣ Recommendation by Ingredient
app.get("/recommend", (req, res) => {
  const ingredient = req.query.ingredient;

  const recommended = recipes.filter(recipe =>
    recipe.ingredients.includes(ingredient)
  );

  res.json(recommended);
});


app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});