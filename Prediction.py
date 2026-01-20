import pandas as pd
import numpy as np

# making mock historical data
data = {
  "booking_type" : ["online","online","offline","online","online","offline","online","online","online","offline"],
  "Status" : ["Confirmed","Confirmed","Cancelled","Confirmed","Confirmed","Cancelled","Confirmed","Cancelled","Confirmed","Confirmed"]
}

df = pd.DataFrame(data)

# changing categorical 'Status' to numerical 'Confirmed_flag'.
df["Confirmed_flag"] = df["Status"].apply(lambda x:1 if x =="Confirmed" else 0)   

# Confirmaion prediction -- MOCK logic
Confirmation_percentage = (
    df.groupby("booking_type")["Confirmed_flag"].mean() *100
)

# prediction by new booking 
new_booking_type = "online"
probability = round(Confirmation_percentage.get(new_booking_type, 0),2)

# rule based pridiction
if probability >= 70:
    Prediction = "high chance of Confirmation"
elif 40<= probability <70:
    Prediction = "medium chance of Confirmation"
else:
    Prediction = "low chance of Confirmation"

# here printing the OUTPUT
print(f"Booking_type: {new_booking_type}")
print(f"confirmation Probability: {probability}%")
print("Prediction:", Prediction)
