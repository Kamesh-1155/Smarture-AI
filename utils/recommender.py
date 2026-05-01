# Crop price dataset
crop_price = {
    "rice": 20, "wheat": 22, "maize": 18, "cotton": 60,
    "sugarcane": 35, "mango": 50, "banana": 25,
    "grapes": 80, "apple": 100, "orange": 70,
    "papaya": 40, "pomegranate": 90
}

def recommend_best_crop(top_crops):
    best_crop = None
    best_score = 0

    for crop, prob in top_crops:
        price = crop_price.get(crop, 10)
        score = prob * price

        if score > best_score:
            best_score = score
            best_crop = crop

    return best_crop