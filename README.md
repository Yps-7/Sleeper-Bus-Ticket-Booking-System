# 🚎Sleeper Bus Ticket Booking System
Web-based booking flow for sleeper bus service Ahmedabad ↔ Mumbai with integrated meal booking during checkout. Single bus with multiple intermediate stations [Ahmedabd - Vadodara - Surat - Vapi - Mumbai ].

----
## Core Features

1. **Bus Selection**
   - Users can browse and select available Bus services.
   - Have multiple Station stop InBetween route.
    
2. **Date & Time Slot Selection**
   - Displays real-time availability.
   - Prevents selection of unavailable slots.

3. **User Information Form**
   - Collects essential user details.
   - Input validation for email and phone number.

4. **Booking Summary**
   - Displays selected service, date, time, and total cost.
  
5. **Meal Package Booking**
   - Good quality Meal packages(VEG, JAIN, SNACKS) booking during checkout.

6. **Payment Integration**
   - Secure payment gateway.
   - Accept multiple Payment choices(UPI, Card payment, Net banking).

7. **Booking Confirmation**
   - Confirmation screen after successful booking.
   - Can download the confirmation.

8. **Error Handling & Alerts**
   - Clear error messages for failed actions.

---
## Quality Assurance Documentation
Here is some Product QA test cases scenarios.

### Functional Test Cases

| Test Case ID | Scenario | Expected Result |
|-------------|--------|----------------|
| FT-01 | User selects a valid service | Service is selected successfully |
| FT-02 | User selects available date & time | Slot is booked |
| FT-03 | Seat lock timeout- Select seat → wait 10min | Seat auto-releases |
| FT-04 | User submits valid personal details | Form submission successful |
| FT-05 | Meal selection toggle | Price updates ±₹150 |
| FT-06 | Successful payment | Booking confirmed |
| FT-07 | Payment failure | Error message displayed |

-------
### Edge Case Scenarios

| Test Case ID | Scenario | Expected Result |
|-------------|--------|----------------|
| EC-01 | User selects a past date | System blocks selection |
| EC-02 | Double-click on “Book Now” | Only one booking created |
| EC-03 | Session timeout during payment | User redirected with message |
| EC-04 | Intermidiate stations | Reduced fare + short berth |
| EC-05 | Full bus booking | No seats available |
| EC-06 | Empty mandatory fields | Validation error shown |

-----
### UI/UX Validation Test Cases

| Test Case ID | Scenario | Expected Result |
|-------------|--------|----------------|
| UI-01 | Button visibility on all screens | Buttons clearly visible |
| UI-02 | Form error messages | Clear and readable |
| UI-03 | Mobile responsiveness | Layout adapts correctly |
| UI-04 | Loading indicators | Displayed during processing |

-----
## UI/UX Design Prototype
The UI/UX prototype for the ticket booking flow has been designed using **Figma**.
It visually represents the complete user journey from service selection
to booking confirmation.

🔗 **Figma Prototype Link:**  
https://www.figma.com/file/XXXXXXXX

-----
# Sleeper Bus Ticket Booking – Backend API

This repository contains the backend implementation for a **sleeper bus ticket booking system** operating between **Ahmedabad and Mumbai** .

The backend is developed using **Python and FastAPI**, focusing on clean API design and clarity.

## 🔗 API Endpoints

| Method | Endpoint | Description |
|------|--------|------------|
| GET | `/stations` | List all stations on the route |
| GET | `/seats` | List available seats for a given route |
| POST | `/book_seat` | Book a sleeper seat |
| POST | `/book_meal` | Add a meal to an existing booking |
| POST | `/cancel_booking` | Cancel a confirmed booking |

-----
## Conclusion

This documentation ensures a well-defined product flow supported by
comprehensive quality assurance coverage. By validating functional,
edge, and UI/UX scenarios, the booking system delivers a reliable
and seamless user experience.

