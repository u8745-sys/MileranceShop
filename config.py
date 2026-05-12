BOT_TOKEN = "8664623285:AAHUjjTE4JbxNyIjZ6IlpI3ZXSD56Vi38Lk"
PLATIMA_API_URL = "https://platima.ru/api/create"
WEBHOOK_URL = None

CATALOG = {
    # -------- КАТЕГОРИЯ: ИГРОВАЯ ВАЛЮТА --------
    "game_currency": {
        "name": "🎮 Игровая валюта",
        "items": {
            "val_1000": {"name": "1000 V-Bucks", "price": 800, "desc": "Для Fortnite (актуальная цена 2026)"},
            "v_bucks_2400": {"name": "2400 V-Bucks", "price": 1800, "desc": "Для Fortnite (актуальная цена 2026)"},
            "v_bucks_4500": {"name": "4500 V-Bucks", "price": 2900, "desc": "Для Fortnite (актуальная цена 2026)"},
            "lol_5000": {"name": "5000 RP", "price": 800, "desc": "Для League of Legends"},
            "roblox_800": {"name": "800 Robux", "price": 1000, "desc": "Для Roblox (актуальная цена 2026)"},
            "roblox_1700": {"name": "1700 Robux", "price": 2000, "desc": "Для Roblox (актуальная цена 2026)"},
            "brawl_30": {"name": "30 гемов", "price": 200, "desc": "Для Brawl Stars (ежедневная акция)"},
            "brawl_950": {"name": "950 гемов", "price": 4500, "desc": "Для Brawl Stars"},
            "genshin_300": {"name": "300 Кристаллов", "price": 350, "desc": "Для Genshin Impact"},
            "valorant_475": {"name": "475 VP", "price": 600, "desc": "Для Valorant"},
            "valorant_1000": {"name": "1000 VP", "price": 1200, "desc": "Для Valorant (актуальная цена 2026)"},
        }
    },
    # -------- КАТЕГОРИЯ: ПОДПИСКИ --------
    "subscriptions": {
        "name": "📺 Подписки",
        "items": {
            "netflix_premium": {"name": "Netflix Premium 1 мес", "price": 1000, "desc": "4K, 4 устройства (актуальная цена 2026)"},
            "youtube_premium": {"name": "YouTube Premium 1 мес", "price": 200, "desc": "Без рекламы, фон. режим (выгодная цена РФ)"},
            "spotify_1m": {"name": "Spotify Premium 1 мес", "price": 300, "desc": "Без рекламы, скачивание"},
        }
    }
}
