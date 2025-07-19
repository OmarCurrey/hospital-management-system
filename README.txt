Authors:
    Omar Currey

Date Created:
    July 2025

Course:
    ITT103 - Programming Techniques

GitHub Public URL to Code:
    https://github.com/YOUR-GITHUB-USERNAME/hospital-management-system

-------------------------------------------------------------

PROGRAM PURPOSE
This program is a basic Hospital Management System (HMS).
It enables a hospital to enroll doctors and patients, make appointments, cancel appointments, and create bills. It is a console application
using Python and demonstrates object-oriented programming concepts.
-------------------------------------------------------------

PROGRAM FUNCTIONALITIES

1. Register a new patient, automatically generating a unique patient ID.
2. Insert a new doctor, along with specialty and available time slots.
3. Schedule an appointment between a doctor and a patient without any conflict in their schedules.
4. Cancel a previously booked appointment, freeing the time slot.
5. Create an invoice for an appointment, including a standard consultation charge and extra manual charges.
6. Display a patient's profile, with their details and all their appointments.
7. View a doctor's profile and schedule.
-------------------------------------------------------------

HOW TO RUN

1. Ensure that you have Python 3 installed on your computer.
2. Download the program file and give it the name `HospitalManagementSystem.py`.
3. Open a command prompt or terminal.
4. Navigate to the folder containing the file.
5. Execute the program by typing: python HospitalManagementSystem.py
6. Follow the menu prompts on the console.
-------------------------------------------------------------

REQUIRED CHANGES

- To add more functionality (like pharmacy billing, lab tests, etc.),
new methods or classes can be added adhering to the same object-oriented framework.
- The existing system holds all the data in memory. For real use, it would require
to be linked to a database or files for data persistence.
-------------------------------------------------------------

LIMITATIONS

- The program operates completely in memory and will lose data upon being closed.
- Patient IDs, doctor IDs, and appointment IDs are all created with Universal Unique Identifier (UUID) to maintain uniqueness. 
- Age has to be a positive integer. 
- Fees should be numbers. - Minimal error checking is done (e.g., valid age, IDs that exist). 
- The user must manually input IDs to connect patients and doctors.