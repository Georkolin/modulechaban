import json
import os
import sys
from mod import check_point_in_torus, get_translation

FILENAME = "MyData.json"

def save_data():
    try:
        raw_coords = input("Введіть координати точки А(x,y): ").split()
        x, y = map(int, raw_coords)
        r = int(input("Введіть радіус першого кола r: "))
        R = int(input("Введіть радіус другого кола R: "))
        lang = input("Введіть мову інтерфейсу (uk/en): ").strip().lower()
        
        data = {"x": x, "y": y, "r": r, "R": R, "lang": lang}
        
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Дані збережено в файл {FILENAME}")
    except (ValueError, IndexError):
        print("Помилка введення даних. Спробуйте ще раз.")

def main():
    if not os.path.exists(FILENAME):
        save_data()
        return

    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        
        required = ["x", "y", "r", "R", "lang"]
        if not all(k in data for k in required):
            raise ValueError("Некоректні дані")
            
    except (json.JSONDecodeError, ValueError):
        save_data()
        return

   
    lang_data = get_translation(data["lang"])
    dist, is_inside = check_point_in_torus(data["x"], data["y"], data["r"], data["R"])

    print(f"Мова: {lang_data['lang_name']}")
    print(f"{lang_data['coords']} {data['x']} {data['y']}")
    print(f"{lang_data['rad_r']} {data['r']}")
    print(f"{lang_data['rad_R']} {data['R']}")
    print(f"{lang_data['dist']} {dist}")

    status = "inside" if is_inside else "outside"
    print(lang_data[status].format(data["x"], data["y"]))

if __name__ == "__main__":
    main()