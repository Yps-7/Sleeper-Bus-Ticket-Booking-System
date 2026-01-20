# 🎫 Bus Ticket Confirmation Prediction - Mock or simulated model 
---

## Overview
This Document is describes a percentage based approach to predict bus ticket confirmation probability using mock historical booking data. This approach focuses on simplicity , explainability of problem solving.

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

---
## 2. Model Choice
This solution uses a **mock, rule-based Probability model** instead of a machine learning model. This approach mimics how a real ML model behaves but without model training.

### Proposed Model -- RandomForestClassifier

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
