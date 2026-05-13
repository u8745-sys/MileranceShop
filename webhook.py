import hashlib
import json
import sqlite3
from aiohttp import web

from database import update_balance, get_user_by_order_id   # эти функции надо будет дописать

PLATIMA_SECRET = "ваш_секретный_ключ"   # задайте любой сложный секрет

async def handle_platima_webhook(request):
    # Проверяем подпись
    body = await request.text()
    signature = request.headers.get("X-Platima-Signature")
    expected = hashlib.sha256((body + PLATIMA_SECRET).encode()).hexdigest()
    if not signature or signature != expected:
        return web.Response(status=403, text="Forbidden")

    data = json.loads(body)
    order_id = data.get("order_id")
    amount = data.get("amount")
    status = data.get("status")

    if status == "paid" and order_id:
        # Находим user_id по order_id (нужна функция в database.py)
        user_id = get_user_by_order_id(order_id)
        if user_id:
            update_balance(user_id, amount)    # зачисляем сумму на баланс
            # Также можно пометить заказ как оплаченный, если нужно
        return web.Response(status=200, text="OK")
    return web.Response(status=400, text="Invalid data")

def run_webhook():
    app = web.Application()
    app.router.add_post("/webhook/platima", handle_platima_webhook)
    web.run_app(app, host="0.0.0.0", port=8080)