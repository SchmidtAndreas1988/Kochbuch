from flask import Flask, render_template, url_for, request

app = Flask(__name__, template_folder = "templates")

## Example Data
recipe_img = "/static/images/pizza.jpg"
recipe_name = "Pizza"
preparation_time = "120"
cooking_time = "15"
servings = 2
ingredients = {"125 ml": "Wasser", "1/2 Würfel": "Hefe", "1 EL": "Öl"}
instructions = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maxime incidunt voluptatum, laborum dolore aut eligendi nesciunt labore unde autem recusandae pariatur, iusto voluptatem accusantium officiis dignissimos possimus quae. Non, at?Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maxime incidunt voluptatum, laborum dolore aut eligendi nesciunt labore unde autem recusandae pariatur, iusto voluptatem accusantium officiis dignissimos possimus quae. Non, at?"
rating = 5

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hinzufuegen", methods = ["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe_name = request.form["recipe_name"]
        preparation_time = request.form["preparation_time"]
        cooking_time = request.form["cooking_time"]
        servings = request.form["servings"]
        instructions = request.form["instructions"]
        rating = ""

        # placeholder
        ingredients = {"125 ml": "Wasser", "1/2 Würfel": "Hefe", "1 EL": "Öl"}

        return render_template("recipe.html", 
                           # recipe_img = recipe_img,
                           recipe_name = recipe_name, 
                           preparation_time = preparation_time,
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

