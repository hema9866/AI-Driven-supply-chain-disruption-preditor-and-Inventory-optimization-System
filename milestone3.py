import pandas as pd

def analyze_rice_field_risks(file_path):
    # Load the CSV data
    data = pd.read_csv(file_path)

    # Define thresholds and conditions for risk analysis
    climate_change_threshold = "High"  # Risk levels: Low, Medium, High
    pest_outbreak_threshold = "High"  # Risk levels for pests
    soil_degradation_threshold = "Severe"  # Soil issues levels: Low, Moderate, Severe
    sentiment_threshold = "Negative"  # Sentiment: Positive, Neutral, Negative

    alerts = []

    for index, row in data.iterrows():
        # Analyze risk factors for climate change, pests, and soil degradation
        if row['Climate Change Risk'] == climate_change_threshold or row['Pest Outbreak Risk'] == pest_outbreak_threshold:
            if row['Soil Degradation'] == soil_degradation_threshold or row['Sentiment'] == sentiment_threshold:
                alerts.append((row['Country'], "URGENT ACTION", f"High climate change risk, pest outbreak, severe soil degradation, {row['Sentiment']} sentiment"))
            else:
                alerts.append((row['Country'], "MONITOR", f"High climate change or pest risk with {row['Soil Degradation']} soil condition"))
        elif row['Soil Degradation'] == "Low" and row['Climate Change Risk'] == "Low" and row['Pest Outbreak Risk'] == "Low":
            alerts.append((row['Country'], "SAFE", f"Low risk in climate change, pests, and soil degradation"))

    return alerts

# Sample CSV data creation
data = {
    'Country': ['India', 'Vietnam', 'Bangladesh', 'Thailand', 'Nigeria'],
    'Climate Change Risk': ['Medium', 'High', 'High', 'Medium', 'Low'],
    'Pest Outbreak Risk': ['Low', 'High', 'Medium', 'Low', 'Low'],
    'Soil Degradation': ['Moderate', 'Severe', 'Low', 'Moderate', 'Low'],
    'Sentiment': ['Neutral', 'Negative', 'Neutral', 'Positive', 'Negative']
}

# Save sample data to CSV for demonstration
sample_file = "rice_field_risks.csv"
pd.DataFrame(data).to_csv(sample_file, index=False)

# Analyze the rice field risks
alerts = analyze_rice_field_risks(sample_file)

# Display alerts
for alert in alerts:
    print(f"Country: {alert[0]}, Action: {alert[1]}, Reason: {alert[2]}")
