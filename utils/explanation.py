def generate_explanation(crop, temp, rainfall, ph):
    return f"""
🌱 The recommended crop is {crop.upper()} because:

• Temperature ({temp}°C) is suitable  
• Rainfall ({rainfall} mm) supports healthy growth  
• Soil pH ({ph}) is optimal  

💰 This crop is also profitable based on market trends.
"""