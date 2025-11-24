HOSPITAL APPOINTMENT INTERFACE
A simple python command line application that simulate booking a medical check-up appointment at a hospital.
The program collects basic patient details, shows available check-ups with prices and optionally books a random date and time slot

FILES
1. hospital_appointment.py
    Main script that:
    - It takes the patient's details-name, mobile number, and address-from the user's input.
    - stores these informations in 'details.txt'.
    - Presents a list of check‑ups available and asks the user to pick one.
    - Displays the price for the selected check‑up using the 'check_up_price' module
    - Optionally books a random date and time slot using a 'time_slot' module.

2. check_up_price.py
    Contains a dictionary 'checkup_price' mapping check‑up names (e.g., `CBC`, `BMP`, `Thyroid Profile Test`) to their prices in INR.

3.  time_slot.py
    - Takes the date from the user.
    - Succeeding four date are added in list 'slot_date'.
    - List 'slot_time' contains the time interval.

4. details.txt
    - Output file where the script writes the patient’s name, mobile number, and address (one per line).

REQUIREMENTS
    - Python 3.x installed on your system.
    - A 'time_slot.py' file in the same directory, containing:
    - 'slot_date': a list of date strings.
    - 'slot_time': a list of time slot strings.
    - No external third‑party libraries are required.

HOW TO RUN
    1. Put the following files in the same directory:
     - 'hospital_appointment.py'
     - 'check_up_price.py'
     - 'time_slot.py'
    2. Open a terminal or command prompt in that directory.
    3. Run : python hospital_appointment.py
    4. Follow the on‑screen prompts to:
       - Enter patient information.
       - Select a check‑up from the list below by typing in the name exactly as it appears.
       - Make a decision to book an appointment slot(yes or no).
       The details of the patient will be saved in `details.txt`, and a random date and time slot will be printed if you choose to book.

USAGE NOTES
 - Input the name of the check‑up exactly as printed in the list, to avoid a key error when looking up the price from 'checkup_price'.
 - The script currently supports only one patient per run and overwrites 'details.txt' each time.