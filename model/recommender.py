import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def _normalize_text_series(series: pd.Series) -> pd.Series:
    return (
        series.astype(str)
        .str.replace("\ufeff", "", regex=False)
        .str.replace('"', "", regex=False)
        .str.strip()
    )


def _load_dataset(path: str = "dataset/recipes.csv") -> pd.DataFrame:
    data = pd.read_csv(path, encoding="utf-8-sig")

    data.columns = [
        col.replace("\ufeff", "").replace('"', "").strip()
        for col in data.columns
    ]

    required_columns = [
        "recipe_name",
        "diet",
        "condition",
        "ingredients",
        "calories",
        "steps",
        "time",
    ]
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns in recipes.csv: {missing_columns}")

    for col in ["recipe_name", "diet", "condition", "ingredients", "steps"]:
        data[col] = _normalize_text_series(data[col])

    data["calories"] = pd.to_numeric(data["calories"], errors="coerce")
    data["time"] = pd.to_numeric(data["time"], errors="coerce")

    data = data.dropna(subset=["recipe_name", "diet", "condition", "ingredients", "time"]).copy()

    data["ingredients"] = data["ingredients"].str.lower()
    data["diet"] = data["diet"].str.lower()
    data["condition"] = data["condition"].str.lower()

    return data


df = _load_dataset()
df["combined"] = df["ingredients"] + " " + df["diet"] + " " + df["condition"]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["combined"])


def get_recipe_df() -> pd.DataFrame:
    return df.copy()


def recommend_recipes(diet, condition, cooking_time, top_n=5):
    diet = str(diet).strip().lower()
    condition = str(condition).strip().lower()
    cooking_time = int(cooking_time)

    user_text = f"{diet} {condition}"
    user_vec = vectorizer.transform([user_text])
    similarity_scores = cosine_similarity(user_vec, tfidf_matrix).flatten()

    filtered = df[
        (df["diet"] == diet)
        & (df["condition"] == condition)
        & (df["time"] <= cooking_time)
    ].copy()

    if filtered.empty:
        filtered = df[
            (df["diet"] == diet)
            & (df["time"] <= cooking_time)
        ].copy()
        if filtered.empty:
            return []

    filtered["score"] = similarity_scores[filtered.index]
    filtered = filtered.sort_values(by="score", ascending=False)

    return filtered.head(top_n).to_dict(orient="records")
