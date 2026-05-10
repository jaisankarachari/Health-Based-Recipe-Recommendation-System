from flask import Flask, render_template, request, session, redirect, url_for
from model.recommender import recommend_recipes, get_recipe_df

# Load the dataset
df = get_recipe_df()

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure key

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':  # Hardcoded for demo
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/recommend', methods=['POST'])
def recommend():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    first_name = request.form['first_name']
    age = request.form['age']
    gender = request.form['gender']
    height = request.form['height']
    weight = request.form['weight']
    diet = request.form['diet']
    condition = request.form['condition']
    cooking_time = int(request.form['cooking_time'])
    session['first_name'] = first_name
    results = recommend_recipes(diet, condition, cooking_time)
    return render_template('result.html', results=results, first_name=first_name)

@app.route('/recipe/<recipe_name>')
def recipe(recipe_name):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    matches = df[df['recipe_name'].str.lower() == recipe_name.lower()]
    if matches.empty:
        return redirect(url_for('index'))
    recipe_data = matches.iloc[0].to_dict()
    first_name = session.get('first_name', 'Guest')
    return render_template('recipe.html', recipe=recipe_data, first_name=first_name)

if __name__ == '__main__':
    app.run(debug=True)
