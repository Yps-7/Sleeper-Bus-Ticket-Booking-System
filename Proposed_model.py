# HERE WE GO for making Bus Booking Confirmation prediction model(prposed model) BY USING RANDOM FOREST CLASSIFIER

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# making historical mock data 
np.random.seed(42)
data = pd.DataFrame({
    'lead_time': np.random.randint(1,90, size =10000),
    'deposit' : np.random.choice([0,1], size = 10000, p=[0.3,0.7]),
    'past_cancels' : np.random.poisson(0.5,size =10000),
    'Confirmed' : np.random.choice([0,1], size = 10000, p =[0.3,0.7])
})
#print(data.head(17)) # agar banaya hua data dekhna ho to
# Prepare data
data = pd.get_dummies(data, columns=['deposit'])
X = data.drop('confirmed', axis=1)
y = data['confirmed']

# Split data into train adn test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

new_booking = pd.DataFrame({
    'lead_time': [20], 
    'past_cancels': [1], 
    'deposit_Yes': [0], 
    'deposit_No': [1]
})

prob_confirm = model.predict_proba(new_booking)[0][1] * 100
print(f"Confirmation probability: {prob_confirm:.1f}%") 
