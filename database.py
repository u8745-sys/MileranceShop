import sqlite3
import json
import os

DB_NAME = "shop.db"
PRODUCTS_FILE = "products.json"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cart (
                user_id INTEGER,
                item_id TEXT,
                quantity INTEGER DEFAULT 1,
                PRIMARY KEY (user_id, item_id)
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id TEXT PRIMARY KEY,
                user_id INTEGER,
                total INTEGER,
                platima_url TEXT,
                status TEXT DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

def add_user(user_id, username):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (user_id, username))

def get_cart(user_id):
    with sqlite3.connect(DB_NAME) as conn:
        return conn.execute("SELECT item_id, quantity FROM cart WHERE user_id = ?", (user_id,)).fetchall()

def add_to_cart(user_id, item_id):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute("SELECT quantity FROM cart WHERE user_id = ? AND item_id = ?", (user_id, item_id))
        if cur.fetchone():
            conn.execute("UPDATE cart SET quantity = quantity + 1 WHERE user_id = ? AND item_id = ?", (user_id, item_id))
        else:
            conn.execute("INSERT INTO cart (user_id, item_id, quantity) VALUES (?, ?, 1)", (user_id, item_id))

def remove_from_cart(user_id, item_id):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("DELETE FROM cart WHERE user_id = ? AND item_id = ?", (user_id, item_id))

def clear_cart(user_id):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("DELETE FROM cart WHERE user_id = ?", (user_id,))

def save_order(order_id, user_id, total, platima_url):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO orders (order_id, user_id, total, platima_url) VALUES (?, ?, ?, ?)",
                     (order_id, user_id, total, platima_url))

def update_order_status(order_id, status):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("UPDATE orders SET status = ? WHERE order_id = ?", (status, order_id))

def get_all_users():
    with sqlite3.connect(DB_NAME) as conn:
        return conn.execute("SELECT user_id, username, registered_at FROM users ORDER BY registered_at DESC").fetchall()

def get_all_orders():
    with sqlite3.connect(DB_NAME) as conn:
        return conn.execute("SELECT order_id, user_id, total, status, created_at FROM orders ORDER BY created_at DESC").fetchall()

def get_order_by_id(order_id):
    with sqlite3.connect(DB_NAME) as conn:
        return conn.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,)).fetchone()

def get_stats():
    with sqlite3.connect(DB_NAME) as conn:
        users = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        total_orders = conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
        completed_orders = conn.execute("SELECT COUNT(*) FROM orders WHERE status = 'completed'").fetchone()[0]
        pending_orders = conn.execute("SELECT COUNT(*) FROM orders WHERE status = 'pending'").fetchone()[0]
        total_amount = conn.execute("SELECT SUM(total) FROM orders WHERE status = 'completed'").fetchone()[0] or 0
        return {"users": users, "total_orders": total_orders, "completed_orders": completed_orders, "pending_orders": pending_orders, "total_amount": total_amount}

def get_pending_orders_count():
    with sqlite3.connect(DB_NAME) as conn:
        return conn.execute("SELECT COUNT(*) FROM orders WHERE status = 'pending'").fetchone()[0]

def _load_products():
    try:
        with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {
            "game_currency": {"name": " Игровая валюта", "items": {}},
            "subscriptions": {"name": " Подписки", "items": {}}
        }

def _save_products(products):
    with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

def add_product_to_db(category_id, item_id, name, price, desc):
    products = _load_products()
    if category_id not in products:
        products[category_id] = {"name": category_id, "items": {}}
    if item_id in products[category_id]["items"]:
        return False
    products[category_id]["items"][item_id] = {"name": name, "price": price, "desc": desc}
    _save_products(products)
    return True

def remove_product_from_db(item_id):
    products = _load_products()
    for cat_id, cat_data in products.items():
        if item_id in cat_data["items"]:
            del cat_data["items"][item_id]
            _save_products(products)
            return True
    return False

def get_all_products():
    return _load_products()
    
    def get_user_by_order_id(order_id):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute("SELECT user_id FROM orders WHERE order_id = ?", (order_id,))
        row = cur.fetchone()
        return row[0] if row else None
