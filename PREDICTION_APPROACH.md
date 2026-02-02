# 🎫 Bus Ticket Confirmation Prediction - Mock or simulated model 

## Overview
This Document is describes a Historical data based Statistical approach to predict bus ticket confirmation probability using mock historical booking data. This approach focuses on simplicity, explainability of problem solving.

---
## 1. Prediction Logic
The prediction is based on historical confirmation rates.

### Logic Used:
- Each booking has a status: `Confirmed` or `Cancelled`
- Status is converted into numeric form:
  - Confirmed → 1  ,   Cancelled → 0
- Confirmation probability is calculated by converting booking status into a numeric flag
(Confirmed = 1, Cancelled = 0) and computing the mean value per booking type.

Mathematically:

mean(confirmed_flag) × 100
= (Total Confirmed Bookings / Total Bookings) × 100

I have provide this Mock prediction model python file as "[Prediction.py](Prediction.py)".

---
## 2. Model Choice
This solution uses a mock, **Historical data based statistical model** and for prediction, it uses **rule-based Probability model** instead of a machine learning model. This approach mimics how a real ML model behaves but without model training.

### Proposed Model -- RandomForestClassifier
here is the proposed model python file link for your consideration- [Proposed_model.py](Proposed_model.py) .

The reason for using this particular model is that Random Forest is an ensemble machine learning method which reduces variance and helps prevent underfitting. As a result, the model is no more likely to be noisy or perform poorly on testing data.   

---
## 4. Mock Dataset
A small simulated dataset is used to represent mock historical booking records.

### Sample Dataset:
| Booking Type| Status     |
|-------------|------------|
| Online      | Confirmed  |
| Online      | Confirmed  |
| offline     | Cancelled  |
| Online      | Canfelled  |
| Online      | Confirmed  |
| Offline     | Cancelled  |
| online      | Confirmed  |
| Offline     | Confirmed  |
| Online      | Cancelled  |
| Online      | Confirmed  |
---
## 5. Training Methodology (Mock)
No actual training is performed but instead,
- Confirmation percentage is calculated using historical statistics.
- Pandas `groupby` and NumPy numerical conversion are used

---
## 6. Booking Probability OUTPUT
the final output is percentage based probability.
### Example Output:
```json
{
  "booking_type": "Online",
  "confirmation_probability": "66.67%",
  "prediction": "Medium chance of confirmation"
}
