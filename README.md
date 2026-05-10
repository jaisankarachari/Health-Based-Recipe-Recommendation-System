# Smart Recipe Recommendation System

## Overview

This project is a Python-based recipe recommendation system built with Flask and a simple machine learning model. It helps users find menu suggestions based on diet preferences, health conditions, and available cooking time. The project also includes a small Express.js API for recipe management and ingredient-based recommendations.

## Key Features

- Secure login-protected Flask web application
- Personalized recipe recommendations using diet, health condition, and cooking time
- TF-IDF and cosine similarity model for text-based recipe matching
- Dataset-driven recipe search and display
- Dynamic recommendation results with recipe detail pages
- Sample Node.js API to list recipes, retrieve by ID, add new recipes, and recommend by ingredient

## Project Structure

- `app.py` - Entry point for the Flask web application. Handles routing, user login/logout, recommendation requests, and recipe detail pages.
- `model/recommender.py` - Contains dataset loading, normalization, TF-IDF vectorization, and recommendation logic.
- `dataset/recipes.csv` - Core recipe dataset used by the recommender engine.
- `templates/` - Jinja2 HTML templates for the web interface.
  - `login.html` - Login page template.
  - `index.html` - Main recommendation form and home page.
  - `result.html` - Recommended recipes listing page.
  - `recipe.html` - Full recipe detail page.
- `static/css/` - Styling files for the Flask app.
  - `login.css` - Login page styling.
  - `style.css` - Main application styling.
- `my-api/` - Separate Express.js API example.
  - `index.js` - Defines REST endpoints for recipes and recommendations.
  - `package.json` - Node.js dependencies and metadata.
- `requirements.txt` - Python package dependencies for the Flask app.
- `test.py` - Project test file (contents not documented here).

## Technologies Used

- Python 3
- Flask
- pandas
- scikit-learn
- HTML/CSS
- JavaScript / Node.js / Express

## How It Works

1. The Flask app loads `dataset/recipes.csv` when it starts.
2. The recommender module normalizes recipe text fields, converts them into a TF-IDF matrix, and creates similarity vectors.
3. Users log in via the demo credentials and submit their personal information plus diet and health condition.
4. The system filters recipes by diet, health condition, and cooking time, then ranks matches with cosine similarity.
5. Recommended recipes are displayed on `result.html`, and users can click through to view individual recipe details.

## Installation

1. Clone the repository or download the project files.
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open your browser at `http://127.0.0.1:5000`.

## Default Login Credentials

- Username: `admin`
- Password: `password`

> Note: These credentials are hardcoded for demo purposes. For production use, replace this authentication flow with a secure user management system.

## Running the Express API

The `my-api` folder contains an independent recipe API example.

1. Change into the `my-api` directory:
   ```bash
   cd my-api
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the API server:
   ```bash
   node index.js
   ```
4. The API will run on `http://localhost:5000`.

### API Endpoints

- `GET /` - Health check endpoint
- `GET /recipes` - Returns all sample recipes
- `GET /recipes/:id` - Returns a recipe by ID
- `POST /recipes` - Adds a new recipe
- `GET /recommend?ingredient=<ingredient>` - Returns recipes that contain the provided ingredient

## Dataset Format

The recommender uses `dataset/recipes.csv` with the following required columns:

- `recipe_name`
- `diet`
- `condition`
- `ingredients`
- `calories`
- `steps`
- `time`

The recommender performs normalization, converts numeric values to the correct type, and filters invalid entries.

## Customization and Extension Ideas

- Replace the hardcoded login with a database-backed authentication system.
- Add search by ingredient or recipe name in the Flask interface.
- Extend the dataset with more diet and condition labels.
- Introduce a weight-based ranking algorithm combining similarity score and nutritional data.
- Add user profiles and saved favorites.
- Add REST endpoints to the Flask app for AJAX-based recommendations.

## Notes

- The Flask app currently runs in debug mode for development.
- The recommendation engine uses a simple text similarity model; additional improvements can include richer feature engineering and hybrid filtering.
- The API in `my-api/` is a standalone sample and is not required for the Flask application.

## License

This project does not specify a license in repository metadata. Add a `LICENSE` file or choose an open-source license if you intend to distribute the project.
