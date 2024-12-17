from flask import Flask, render_template

app = Flask(__name__, template_folder = "templates")

test_string = "Es funktioniert!"

@app.route("/")
def index():
    return render_template("index.html", test_string = test_string)

@app.route("/rezepte/1")
def recipe():
    recipe_img = "/static/images/pizza.jpg"
    recipe_name = "Pizza"
    preparation_time = "120"
    cooking_time = "15"
    servings = 2
    ingredients = {"125 ml": "Wasser", "1/2 Würfel": "Hefe", "1 EL": "Öl"}
    instructions = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maxime incidunt voluptatum, laborum dolore aut eligendi nesciunt labore unde autem recusandae pariatur, iusto voluptatem accusantium officiis dignissimos possimus quae. Non, at?"
    rating = 5

    return render_template("recipe.html", 
                           recipe_img = recipe_img,
                           recipe_name = recipe_name, 
                           preparation_time = preparation_time,
                           cooking_time = cooking_time,
                           servings = servings,
                           ingredients = ingredients,
                           instructions = instructions,
                           rating = rating)

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port = 5000)

