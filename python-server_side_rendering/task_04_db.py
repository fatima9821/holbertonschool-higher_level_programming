from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def get_data_from_json():
    with open('products.json', 'r') as f:
        data = json.load(f)
    return data['items']

def get_data_from_csv():
    items = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(row)
    return items

def get_data_from_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    items = cursor.fetchall()
    conn.close()
    return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in items]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        items = get_data_from_json()
    elif source == 'csv':
        items = get_data_from_csv()
    elif source == 'sql':
        items = get_data_from_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        items = [item for item in items if item['id'] == int(product_id)]
        if not items:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5003)

