import numpy as np

def predict_top_crops(model, N, P, K, temp, humidity, ph, rainfall):
    data = np.array([[N, P, K, temp, humidity, ph, rainfall]])

    probs = model.predict_proba(data)[0]
    crops = model.classes_

    top_indices = probs.argsort()[-3:][::-1]

    results = []
    for i in top_indices:
        results.append((crops[i], probs[i]))

    return results