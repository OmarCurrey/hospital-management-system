Author:
    Omar Currey

Date Created:
    July 2025

Course:
    ITT103 - Programming Techniques

GitHub Public URL to Code:
    https://github.com/OmarCurrey/hospital-management-system

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

PROGRAM PURPOSE
This program simulates a simple system, its called Healthy Life Hospital Management System (HLHMS).
It allows the hospital to register patients and doctors, schedule appointments, 
cancel appointments, and generate bills. It is designed as a console application
using Python and demonstrates object-oriented programming concepts.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

PROGRAM FUNCTIONALITIES
1. The system register new patients and assign them unique IDs.
2. Add new doctors with their specialty and availability.
3. Book appointments between patients and doctors, while avoiding scheduling conflicts.
4. Cancel appointments and restore the doctor’s availability.
5. Generate a bill that includes:
   - Fixed consultation fee (JMD$ 3000)
   - Additional manual service fees (e.g. medication, tests)
   - Total amount due
6. Prompt the user to choose a payment method:
   - Option 1: Cash — calculates change from amount paid
   - Option 2: Card — requires valid 4-digit numeric PIN to process
7. View a patient's full profile and appointment history.
8. View a doctor's profile and current schedule.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

HOW TO RUN
1. Python 3 must be installed on your computer.
2. Download the program file and save it as HospitalManagementSystem.py
3. Open a terminal or command prompt.
4. Navigate to the folder containing the file.
5. Run the program using:
    python HospitalManagementSystem.py
6. Follow the numbered menu to interact with the system.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
REQUIRED MODIFICATIONS
- You can extend the system by adding file/database saving,
  or more billing categories such as lab tests and pharmacy.
- You may also allow admin login and access restrictions.
- You can also add the feature to the system to ask the user 
  if they'll be using insurance and calculate insurance charges.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

ASSUMPTIONS AND LIMITATIONS
- All data is stored in memory and will reset on closing the program.
- Users must manually enter patient and doctor IDs for operations.
- Payment PIN must be exactly 4 numeric digits. Letters and short PINs are rejected.
- Cash payments must be equal to or more than the amount due to calculate change.
- The system assumes valid date/time formats entered as text.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
