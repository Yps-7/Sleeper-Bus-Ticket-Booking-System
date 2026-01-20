# Sleeper Bus Ticket Confirmation Prediction - Mock or simulated model 
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
- Confirmation probability (%) = (confirmed bookings / Total Bookings) * 100
 --> which is implemented here by "Confirmation_flag.mean()*100"
---
## 2. Model Choice
This solution uses a **mock, rule-based model** instead of a machine learning model. This approach mimics how a real ML model behaves but without model training.

### Reason for Choosing Mock Model:
- No training data requirement
- Easy to understand and explain
- Fast computation
- Suitable when historical patterns are stable

