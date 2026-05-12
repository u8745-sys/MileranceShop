BOT_TOKEN = "8664623285:AAFlvJqJOYH7jMEbY8M4MuWLiNOGFM8QKa4"

PLATIMA_API_URL = "https://platima.ru/api/create"
WEBHOOK_URL = None

CATALOG = {
    # ----- Fortnite -----
    "fortnite": {
        "name": "🔫 Fortnite",
        "items": {
            "fn_800": {"name": "800 В-баксов", "price": 499, "desc": "Для аккаунтов с регионом Турция"},
            "fn_2400": {"name": "2400 В-баксов", "price": 1299, "desc": "Для аккаунтов с регионом Турция"},
            "fn_4500": {"name": "4500 В-баксов", "price": 1995, "desc": "Для аккаунтов с регионом Турция"},
            "fn_12500": {"name": "12500 В-баксов", "price": 4699, "desc": "Для аккаунтов с регионом Турция"},
            "fn_25000": {"name": "25000 В-баксов", "price": 9210, "desc": "Для аккаунтов с регионом Турция"},
            "fn_37500": {"name": "37500 В-баксов", "price": 13395, "desc": "Для аккаунтов с регионом Турция"},
            "fn_bp": {"name": "Боевой пропуск", "price": 999, "desc": "Новый сезон + 1000 ВБ сразу"},
            "fn_starter": {"name": "Стартер-пак", "price": 299, "desc": "600 ВБ + облик"},
            "fn_squad": {"name": "Отрядный пак", "price": 444, "desc": "1200 ВБ + облик"},
        }
    },
    # ----- Valorant -----
    "valorant": {
        "name": "🎯 Valorant",
        "items": {
            "val_240": {"name": "240 VP", "price": 260, "desc": "EU/NA регион"},
            "val_325": {"name": "325 VP", "price": 327, "desc": "EU/NA регион"},
            "val_475": {"name": "475 VP", "price": 417, "desc": "EU/NA регион"},
            "val_1000": {"name": "1000 VP", "price": 853, "desc": "EU/NA регион"},
            "val_1520": {"name": "1520 VP", "price": 1270, "desc": "EU/NA регион"},
            "val_1750": {"name": "1750 VP", "price": 1621, "desc": "EU/NA регион"},
            "val_tr_375": {"name": "375 VP (Турция)", "price": 230, "desc": "Для аккаунтов с регионом Турция"},
            "val_tr_825": {"name": "825 VP (Турция)", "price": 492, "desc": "Для аккаунтов с регионом Турция"},
            "val_tr_1700": {"name": "1700 VP (Турция)", "price": 979, "desc": "Для аккаунтов с регионом Турция"},
        }
    },
    # ----- Brawl Stars -----
    "brawl": {
        "name": "⚡ Brawl Stars",
        "items": {
            "bs_30": {"name": "30 гемов", "price": 309, "desc": "На аккаунт по SUPERCELL ID"},
            "bs_80": {"name": "80 гемов", "price": 699, "desc": "На аккаунт по SUPERCELL ID"},
            "bs_170": {"name": "170 гемов", "price": 1269, "desc": "На аккаунт по SUPERCELL ID"},
            "bs_360": {"name": "360 гемов", "price": 2539, "desc": "На аккаунт по SUPERCELL ID"},
            "bs_950": {"name": "950 гемов", "price": 6235, "desc": "На аккаунт по SUPERCELL ID"},
            "bs_pass": {"name": "Браул Пасс", "price": 999, "desc": "Новый сезон"},
            "bs_pass_plus": {"name": "Браул Пасс+", "price": 1499, "desc": "Новый сезон + скины"},
        }
    },
    # ----- Подписки -----
    "subscriptions": {
        "name": "📺 Подписки",
        "items": {
            "netflix_premium": {"name": "Netflix Premium 1 мес", "price": 1000, "desc": "4K, 4 устройства"},
            "youtube_premium": {"name": "YouTube Premium 1 мес", "price": 200, "desc": "Без рекламы, фон. режим"},
            "spotify_1m": {"name": "Spotify Premium 1 мес", "price": 300, "desc": "Без рекламы, скачивание"},
            "chatgpt_plus": {"name": "ChatGPT Plus 1 мес", "price": 2000, "desc": "GPT-4, генерация изображений"},
            "telegram_premium": {"name": "Telegram Premium 6 мес", "price": 699, "desc": "Стикеры, реакции, перевод"},
        }
    },
    # ----- Steam -----
    "steam": {
        "name": "🎮 Steam",
        "items": {
            "steam_5": {"name": "5$ (400₽)", "price": 380, "desc": "Пополнение баланса Steam"},
            "steam_10": {"name": "10$ (800₽)", "price": 760, "desc": "Пополнение баланса Steam"},
            "steam_20": {"name": "20$ (1600₽)", "price": 1520, "desc": "Пополнение баланса Steam"},
            "steam_50": {"name": "50$ (4000₽)", "price": 3800, "desc": "Пополнение баланса Steam"},
        }
    },
    # ----- Epic Games -----
    "epic": {
        "name": "🎮 Epic Games",
        "items": {
            "epic_game": {"name": "Покупка любых игр", "price": 0, "desc": "Через Турцию. Цена зависит от игры — уточняйте"},
        }
    }
}
