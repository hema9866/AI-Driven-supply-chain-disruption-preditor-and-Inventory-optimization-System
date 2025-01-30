import pandas as pd

def analyze_rice_field_risks(file_path):
    # Load the CSV data
    data = pd.read_csv(file_path)

    # Define risk levels and associated weight scores for each factor
    risk_weights = {
        "Climate Change Risk": {"Low": 1, "Medium": 2, "High": 3},
        "Pest Outbreak Risk": {"Low": 1, "Medium": 2, "High": 3},
        "Soil Degradation": {"Low": 1, "Moderate": 2, "Severe": 3},
        "Sentiment": {"Positive": 1, "Neutral": 2, "Negative": 3},
    }

    # Initialize a list to store results
    results = []

    for index, row in data.iterrows():
        # Handle possible missing or unexpected values for each factor
        climate_risk_score = risk_weights["Climate Change Risk"].get(row.get('Climate Change Risk', 'Low'), 1)
        pest_risk_score = risk_weights["Pest Outbreak Risk"].get(row.get('Pest Outbreak Risk', 'Low'), 1)
        soil_risk_score = risk_weights["Soil Degradation"].get(row.get('Soil Degradation', 'Low'), 1)
        sentiment_risk_score = risk_weights["Sentiment"].get(row.get('Sentiment', 'Neutral'), 2)

        # Calculate the total combined risk score
        total_risk_score = climate_risk_score + pest_risk_score + soil_risk_score + sentiment_risk_score

        # Determine action based on the total risk score and define the reasoning
        if total_risk_score >= 10:
            action = "URGENT ACTION"
            reason = ("High combined risk in Climate Change, Pest Outbreak, Soil Degradation, and Negative Sentiment. "
                      "Immediate measures like soil conservation, pest management, and climate adaptation are needed.")
        elif total_risk_score >= 7:
            action = "MONITOR"
            reason = ("Moderate combined risks, requiring constant monitoring of the factors to mitigate further risks. "
                      "Implement pest control and improve soil management practices.")
        elif total_risk_score <= 4:
            action = "SAFE"
            reason = "Low risk in all factors. Continue current practices, with regular monitoring."
        else:
            action = "MONITOR"
            reason = "Moderate risks detected in some factors. Regular checks are needed to prevent escalation."

        # Append the results to the list
        results.append({
            "Country": row['Country'],
            "Climate Change Risk": row['Climate Change Risk'],
            "Pest Outbreak Risk": row['Pest Outbreak Risk'],
            "Soil Degradation": row['Soil Degradation'],
            "Sentiment": row['Sentiment'],
            "Total Risk Score": total_risk_score,
            "Action": action,
            "Reason": reason
        })

    # Convert results to a DataFrame for better presentation and return it
    result_df = pd.DataFrame(results)

    return result_df

# Sample CSV data creation (Same as your original data, just adding a few more variations for variety)
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
alerts_df = analyze_rice_field_risks(sample_file)

# Display the alerts in a table format
print(alerts_df)
