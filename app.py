from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__)

# Modeli yükle
model = pickle.load(open('model.pkl', 'rb'))

# Label Encoder Sözlüğü (Arrival Time ÇIKARILDI)
mappings = {
    'airline': {'AirAsia': 0, 'Air_India': 1, 'GO_FIRST': 2, 'Indigo': 3, 'SpiceJet': 4, 'Vistara': 5},
    'source_city': {'Bangalore': 0, 'Chennai': 1, 'Delhi': 2, 'Hyderabad': 3, 'Kolkata': 4, 'Mumbai': 5},
    'departure_time': {'Afternoon': 0, 'Early_Morning': 1, 'Evening': 2, 'Late_Night': 3, 'Morning': 4, 'Night': 5},
    'stops': {'zero': 0, 'one': 1, 'two_or_more': 2},
    'destination_city': {'Bangalore': 0, 'Chennai': 1, 'Delhi': 2, 'Hyderabad': 3, 'Kolkata': 4, 'Mumbai': 5},
    'class': {'Economy': 0, 'Business': 1}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Formdan verileri al (Arrival Time YOK)
        airline = mappings['airline'][request.form['airline']]
        source = mappings['source_city'][request.form['source_city']]
        departure = mappings['departure_time'][request.form['departure_time']]
        stops = mappings['stops'][request.form['stops']]
        dest = mappings['destination_city'][request.form['destination_city']]
        travel_class = mappings['class'][request.form['class']]
        
        # Sayısal veriler
        duration = float(request.form['duration'])
        days_left = int(request.form['days_left'])
        
        # Modelin beklediği özellik listesi (8 özellik)
        # Sıralama: Airline, Source, Dep_Time, Stops, Dest, Class, Duration, Days_Left
        features = np.array([[airline, source, departure, stops, dest, travel_class, duration, days_left]])
        
        # Tahmin yap
        prediction = model.predict(features)
        output = round(prediction[0], 2)
        
        # Eksi fiyat koruması (Matematiksel sapmayı düzeltir)
        if output < 0:
            output = abs(output)
            # Veya mantıksal bir taban fiyat istersen:
            # output = max(output, 1500.00)

        return render_template('index.html', prediction_text=f'Tahmini Fiyat: {output} ₹')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f'Hata: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)