from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CATALOG

def main_menu():
    buttons = [
        [InlineKeyboardButton(text=" Каталог", callback_data="catalog")],
        [InlineKeyboardButton(text=" Корзина", callback_data="view_cart")],
        [InlineKeyboardButton(text=" Поддержка", url="https://t.me/milerance")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def catalog_keyboard():
    buttons = []
    for cat_id, cat_data in CATALOG.items():
        buttons.append([InlineKeyboardButton(text=cat_data["name"], callback_data=f"cat_{cat_id}")])
    buttons.append([InlineKeyboardButton(text=" Назад", callback_data="main_menu")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def items_keyboard(category_id):
    buttons = []
    for item_id, item_data in CATALOG[category_id]["items"].items():
        buttons.append([InlineKeyboardButton(text=f"{item_data['name']}  {item_data['price']}",
                                             callback_data=f"item_{category_id}_{item_id}")])
    buttons.append([InlineKeyboardButton(text=" Назад", callback_data="catalog")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def item_detail_keyboard(category_id, item_id):
    buttons = [
        [InlineKeyboardButton(text=" Добавить в корзину", callback_data=f"add_{category_id}_{item_id}")],
        [InlineKeyboardButton(text=" Назад", callback_data=f"cat_{category_id}")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def cart_keyboard():
    buttons = [
        [InlineKeyboardButton(text=" Оформить заказ", callback_data="checkout")],
        [InlineKeyboardButton(text=" Очистить корзину", callback_data="clear_cart")],
        [InlineKeyboardButton(text=" В меню", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def order_summary_keyboard(order_id, platima_url):
    buttons = [
        [InlineKeyboardButton(text=" Перейти к оплате", url=platima_url)],
        [InlineKeyboardButton(text=" Проверить оплату", callback_data=f"check_order_{order_id}")],
        [InlineKeyboardButton(text=" В меню", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def admin_main_menu():
    buttons = [
        [InlineKeyboardButton(text=" Статистика", callback_data="admin_stats")],
        [InlineKeyboardButton(text=" Пользователи", callback_data="admin_users")],
        [InlineKeyboardButton(text=" Заказы", callback_data="admin_orders")],
        [InlineKeyboardButton(text=" Товары", callback_data="admin_products")],
        [InlineKeyboardButton(text=" Рассылка", callback_data="admin_broadcast")],
        [InlineKeyboardButton(text=" Выход", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def admin_back_button():
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=" Назад", callback_data="admin_back")]])

def admin_orders_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=" Подтвердить заказ", callback_data="admin_confirm")],
        [InlineKeyboardButton(text=" Назад", callback_data="admin_back")]
    ])

def admin_products_menu():
    buttons = [
        [InlineKeyboardButton(text=" Добавить товар", callback_data="admin_add_product")],
        [InlineKeyboardButton(text=" Удалить товар", callback_data="admin_del_product")],
        [InlineKeyboardButton(text=" Назад", callback_data="admin_back")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
