import uuid
import aiohttp
from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from config import BOT_TOKEN, CATALOG
from database import (add_user, get_cart, add_to_cart, clear_cart,
                      save_order, update_order_status, get_all_products)
from keyboards import (main_menu, catalog_keyboard, items_keyboard,
                       item_detail_keyboard, cart_keyboard, order_summary_keyboard)
from admin import notify_admin_new_order

router = Router()
bot = Bot(token=BOT_TOKEN)

@router.message(CommandStart())
async def cmd_start(message: Message):
    add_user(message.from_user.id, message.from_user.username)
    await message.answer("Добро пожаловать в MileranceShop!\nВыберите действие:", reply_markup=main_menu())

@router.callback_query(F.data == "main_menu")
async def back_to_main(call: CallbackQuery):
    await call.message.edit_text("Главное меню:", reply_markup=main_menu())
    await call.answer()

@router.callback_query(F.data == "catalog")
async def show_catalog(call: CallbackQuery):
    products = get_all_products()
    if not products:
        await call.message.edit_text("Каталог пуст. Добавьте товары через админ-панель.")
        return
    await call.message.edit_text("Выберите категорию:", reply_markup=catalog_keyboard())
    await call.answer()

@router.callback_query(F.data.startswith("cat_"))
async def show_items(call: CallbackQuery):
    category_id = call.data.split("_")[1]
    products = get_all_products()
    if category_id not in products:
        await call.answer("Категория не найдена")
        await show_catalog(call)
        return
    await call.message.edit_text(f"Товары в {products[category_id]['name']}:", reply_markup=items_keyboard(category_id))
    await call.answer()

@router.callback_query(F.data.startswith("item_"))
async def show_item_detail(call: CallbackQuery):
    try:
        _, category_id, item_id = call.data.split("_")
        products = get_all_products()
        if category_id not in products or item_id not in products[category_id]["items"]:
            await call.answer("Товар не найден")
            return
        item = products[category_id]["items"][item_id]
        text = f"📦 {item['name']}\n💰 {item['price']}₽\n📝 {item['desc']}"
        await call.message.edit_text(text, reply_markup=item_detail_keyboard(category_id, item_id))
    except:
        await call.answer("Ошибка")
    await call.answer()

@router.callback_query(F.data.startswith("add_"))
async def add_to_cart_callback(call: CallbackQuery):
    try:
        _, category_id, item_id = call.data.split("_")
        user_id = call.from_user.id
        add_to_cart(user_id, f"{category_id}_{item_id}")
        products = get_all_products()
        if category_id in products and item_id in products[category_id]["items"]:
            await call.answer(f"✅ {products[category_id]['items'][item_id]['name']} добавлен в корзину!")
        else:
            await call.answer("✅ Товар добавлен в корзину!")
        await call.message.delete()
        await show_catalog(call)
    except Exception as e:
        await call.answer("Ошибка при добавлении")
        print(f"Add error: {e}")

@router.callback_query(F.data == "view_cart")
async def show_cart(call: CallbackQuery):
    user_id = call.from_user.id
    cart_items = get_cart(user_id)
    if not cart_items:
        await call.message.edit_text("Корзина пуста.", reply_markup=main_menu())
        await call.answer()
        return

    products = get_all_products()
    total = 0
    text = "🛒 Ваша корзина:\n\n"
    for item_key, qty in cart_items:
        try:
            category_id, item_id = item_key.split("_")
            if category_id in products and item_id in products[category_id]["items"]:
                name = products[category_id]["items"][item_id]["name"]
                price = products[category_id]["items"][item_id]["price"]
                total += price * qty
                text += f"{name} × {qty} = {price * qty}₽\n"
        except:
            continue
    if total == 0:
        await call.message.edit_text("Корзина пуста.", reply_markup=main_menu())
        return
    text += f"\n💵 Итого: {total}₽"
    await call.message.edit_text(text, reply_markup=cart_keyboard())
    await call.answer()

@router.callback_query(F.data == "clear_cart")
async def clear_cart_callback(call: CallbackQuery):
    clear_cart(call.from_user.id)
    await call.message.edit_text("Корзина очищена.", reply_markup=main_menu())
    await call.answer()

@router.callback_query(F.data == "checkout")
async def checkout(call: CallbackQuery):
    user_id = call.from_user.id
    cart_items = get_cart(user_id)
    if not cart_items:
        await call.answer("Корзина пуста!")
        return

    products = get_all_products()
    total = 0
    for item_key, qty in cart_items:
        try:
            category_id, item_id = item_key.split("_")
            if category_id in products and item_id in products[category_id]["items"]:
                price = products[category_id]["items"][item_id]["price"]
                total += price * qty
        except:
            continue

    if total == 0:
        await call.answer("Ошибка: корзина пуста")
        return

    order_id = str(uuid.uuid4())[:8]
    async with aiohttp.ClientSession() as session:
        params = {
            "amount": total,
            "description": f"Заказ {order_id} от @{call.from_user.username or call.from_user.id}",
            "order_id": order_id,
            "currency": "RUB",
            "success_url": f"https://t.me/{(await bot.get_me()).username}",
            "webhook_url": ""
        }
        async with session.get("https://platima.ru/api/create", params=params) as resp:
            data = await resp.json()
            platima_url = data.get("url")

    if platima_url:
        save_order(order_id, user_id, total, platima_url)
        await notify_admin_new_order(bot, order_id, user_id, total)
        await call.message.edit_text(f"Заказ №{order_id} на сумму {total}₽. Оплатите по ссылке:",
                                     reply_markup=order_summary_keyboard(order_id, platima_url))
    else:
        await call.message.edit_text("Ошибка при создании платежа. Попробуйте позже.")
    await call.answer()

@router.callback_query(F.data.startswith("check_order_"))
async def check_order(call: CallbackQuery):
    order_id = call.data.split("_")[2]
    from database import get_order_by_id
    order = get_order_by_id(order_id)
    if order and order[4] == "completed":
        await call.answer("✅ Заказ уже оплачен!")
        await call.message.edit_text("✅ Оплата подтверждена! Спасибо за покупку.")
    else:
        await call.answer("⏳ Оплата не обнаружена. Подтвердите заказ вручную через /confirm " + order_id, show_alert=True)
