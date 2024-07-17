from flask import Flask, request, render_template
import json
import csv

app = Flask(__name__)

def read_json_file(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def read_csv_file(filepath):
    products = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        try:
            products = read_json_file('products.json')
        except Exception as e:
            error = f"Error reading JSON file: {e}"
    elif source == 'csv':
        try:
            products = read_csv_file('products.csv')
        except Exception as e:
            error = f"Error reading CSV file: {e}"
    else:
        error = "Wrong source"

    if not error and product_id:
        product_id = int(product_id)
        products = [p for p in products if p['id'] == product_id]
        if not products:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run

