def get_ai_advice(weather):
    temperature = weather["temperature"]
    description = weather["description"]

    if temperature >= 35:
        return "It is very hot today. Stay hydrated and avoid direct sunlight."

    elif temperature >= 30:
        return "The weather is warm. Drink enough water and stay comfortable."

    elif temperature <= 20:
        return "The weather is cool. Consider carrying a light jacket."

    elif "rain" in description.lower():
        return "Rain is expected. Carry an umbrella and take care while travelling."

    else:
        return "The weather looks comfortable. Have a pleasant day!"
