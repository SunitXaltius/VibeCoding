"""Start the MiniMart Flask application."""

from flask import Flask, render_template, request

from database import get_db, init_app

app = Flask(__name__)
init_app(app)


@app.route("/")
def home():
    """Show the MiniMart home page."""
    return render_template("index.html")


@app.route("/products")
def products():
    """Show active products, optionally filtered by a search term."""
    search = request.args.get("search", "").strip()
    database = get_db()

    if search:
        product_rows = database.execute(
            """
            SELECT id, name, description, selling_price, stock
            FROM products
            WHERE active = 1 AND (name LIKE ? OR description LIKE ?)
            ORDER BY name
            """,
            (f"%{search}%", f"%{search}%"),
        ).fetchall()
    else:
        product_rows = database.execute(
            """
            SELECT id, name, description, selling_price, stock
            FROM products
            WHERE active = 1
            ORDER BY name
            """
        ).fetchall()

    return render_template("products.html", products=product_rows, search=search)


if __name__ == "__main__":
    app.run(debug=True)
