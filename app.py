from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__, template_folder = "templates")

# Add database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipes.db"

# Define secret key
app.config["SECRET_KEY"] = "1234"

# Initialize the database
db = SQLAlchemy(app)

# Create db model
class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_added = db.Column(db.DateTime, default = datetime.now(timezone.utc))
    title = db.Column(db.String(200), nullable = False)
    type = db.Column(db.String(200), nullable = False)
    main_img = db.Column(db.String(200))
    prep_time = db.Column(db.Integer)
    cooking_time = db.Column(db.Integer)
    servings = db.Column(db.Integer)
    ingredients = db.Column(db.String(200))
    instructions = db.Column(db.String(1200))
    rating = db.Column(db.Float)

    # Create a string
    def __repr__(self):
        return "<Name %r>" % self.title


## Example Data
recipe_img = "/static/images/pizza.jpg"
title = "Pizza"
prep_time = "120"
cooking_time = "15"
servings = 2
ingredients = "hallo"
instructions = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maxime incidunt voluptatum, laborum dolore aut eligendi nesciunt labore unde autem recusandae pariatur, iusto voluptatem accusantium officiis dignissimos possimus quae. Non, at?Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maxime incidunt voluptatum, laborum dolore aut eligendi nesciunt labore unde autem recusandae pariatur, iusto voluptatem accusantium officiis dignissimos possimus quae. Non, at?"
rating = 5

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/rezepte")
def all_recipes():
    our_recipes = Recipes.query.order_by(Recipes.date_added)
    return render_template("all_recipes.html", our_recipes = our_recipes)


@app.route("/hinzufuegen", methods = ["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        title = request.form["title"]
        type = ""
        main_img = ""
        prep_time = request.form["prep_time"]
        cooking_time = request.form["cooking_time"]
        servings = request.form["servings"]
        ingredients = ""
        instructions = request.form["instructions"]
        rating = 0

        # Show recipe (EXAMPLE) after creation
        recipe = Recipes(title = title, 
                        type = type,
                        main_img = main_img,
                        prep_time = prep_time,
                        cooking_time = cooking_time,
                        servings = servings,
                        ingredients = ingredients,
                        instructions = instructions,
                        rating = rating)
        db.session.add(recipe)
        db.session.commit()

        # placeholder
        ingredients = "hallo"

        return render_template("recipe.html", 
                           # recipe_img = recipe_img,
                           title = title, 
                           prep_time = prep_time,
                           cooking_time = cooking_time,
                           servings = servings,
                           ingredients = ingredients,
                           instructions = instructions,
                           rating = rating
                           )
    else:
        return render_template("add_recipe.html")

@app.route("/rezepte/1")
def recipe():
    
    # Render recipe - todo: from db
    return render_template("recipe.html", 
                           recipe_img = recipe_img,
                           title = title, 
                           prep_time = prep_time,
                           cooking_time = cooking_time,
                           servings = servings,
                           ingredients = ingredients,
                           instructions = instructions,
                           rating = rating)

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port = 5000)

