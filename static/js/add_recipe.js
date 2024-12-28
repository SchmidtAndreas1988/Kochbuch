function addIngredientRow() {
    // alert("test");

    const container = document.getElementById("recipe_ingredient_table");
    const newRow = document.createElement("tr");

    newRow.innerHTML = `
    <td><input type="number" id="ingredient_amount" name="ingredient_amount" placeholder="Anzahl"></td>
                    <td><input type="text" id="ingredient_unit" name="ingredient_unit" placeholder="Einheit"></td>
                    <td><input type="text" id="ingredient_name" name="ingredient_name" placeholder="Zutat"></td>
                    <td><button type="button" onclick="addIngredientRow()">+</button></td>
                    `
    container.appendChild(newRow);
}