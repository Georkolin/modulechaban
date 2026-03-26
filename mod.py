import math

def check_point_in_torus(x, y, r, R):
    distance = math.sqrt(x**2 + y**2)
    is_inside = min(r, R) <= distance <= max(r, R)
    return round(distance, 2), is_inside

def get_translation(lang_code):
    translations = {
        "uk": {
            "lang_name": "Українська",
            "coords": "Координати точки А(x,y):",
            "rad_r": "Радіус першого кола r:",
            "rad_R": "Радіус другого кола R:",
            "dist": "Відстань до точки A:",
            "inside": "Точка A({}, {}) знаходиться всередині тора.",
            "outside": "Точка A({}, {}) не знаходиться всередині тора.",
            "saved": "Дані збережено в файл MyData.json"
        },
        "en": {
            "lang_name": "English",
            "coords": "Coordinates of point A(x,y):",
            "rad_r": "Radius of the first circle r:",
            "rad_R": "Radius of the second circle R:",
            "dist": "Distance to point A:",
            "inside": "Point A({}, {}) is inside the torus.",
            "outside": "Point A({}, {}) is outside the torus.",
            "saved": "Data saved to MyData.json"
        }
    }
    return translations.get(lang_code, translations["uk"])