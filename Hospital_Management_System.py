import uuid  # this helps us generate unique IDs automatically


# This is a general class for any person (patient or doctor)
class Person:
    def __init__(self, name, age, gender):
        self.name = name  # the person's name
        if age <= 0:
            raise ValueError("Age must be positive.")  # makes sure the age is a positive number
        self.age = age
        self.gender = gender

    # This prints out the details of the person
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

# -------------------------
# PATIENT CLASS
# -------------------------
# This is a more specific person - a patient
# It inherits (takes over) everything from Person
class Patient(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)  # uses the Person constructor
        self.patient_id = f"P{uuid.uuid4().hex[:6].upper()}"  # generates a unique patient ID
        self.appointment_list = []  # starts with an empty list of appointments

    # This adds an appointment to the patient's record
    def book_appointment(self, appointment):
        self.appointment_list.append(appointment)

    # This shows the patient's information along with their appointments
    def view_profile(self):
        print(f"\nPatient ID: {self.patient_id}")
        self.display()
        if self.appointment_list:
            print("Appointments:")
            for app in self.appointment_list:
                print(f" - {app.appointment_id}: Dr. {app.doctor.name} on {app.date} at {app.time} ({app.status})")
        else:
            print("No appointments.")

# -------------------------
# DOCTOR CLASS
# -------------------------
# This is a specific person - a doctor
class Doctor(Person):
    def __init__(self, name, age, gender, speciality, schedule):
        super().__init__(name, age, gender)
        self.doctor_id = f"D{uuid.uuid4().hex[:6].upper()}"  # unique doctor ID
        self.speciality = speciality  # e.g., cardiologist
        self.schedule = schedule  # list of available times e.g. ["2025-07-15 14:00"]

    # Checks if the doctor is free at a given time
    def is_available(self, date_time):
        return date_time in self.schedule

    # Removes a time slot from the doctor's availability once booked
    def remove_slot(self, date_time):
        self.schedule.remove(date_time)

    # Puts the time slot back if an appointment is cancelled
    def add_slot(self, date_time):
        self.schedule.append(date_time)

    # Prints the doctor's profile and available slots
    def view_schedule(self):
        print(f"\nDoctor ID: {self.doctor_id}")
        self.display()
        print(f"Specialty: {self.speciality}")
        print("Available Slots:")
        for slot in self.schedule:
            print(f" - {slot}")

# -------------------------
# APPOINTMENT CLASS
# -------------------------
# This connects a patient with a doctor at a certain time
class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.appointment_id = f"A{uuid.uuid4().hex[:6].upper()}"  # unique appointment ID
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.status = "Scheduled"  # can also be "Cancelled"

    # Confirms the appointment by printing a message
    def confirm(self):
        print(f"Appointment {self.appointment_id} confirmed for {self.patient.name} with Dr. {self.doctor.name} on {self.date} at {self.time}.")

    # Cancels the appointment and updates status
    def cancel(self):
        self.status = "Cancelled"
        print(f"Appointment {self.appointment_id} has been cancelled.")

# -------------------------
# HOSPITAL SYSTEM CLASS
# -------------------------
# This is the main system that handles patients, doctors, appointments
class HospitalSystem:
    def __init__(self):
        self.patients = {}    # dictionary to store patients using their IDs
        self.doctors = {}     # dictionary to store doctors using their IDs
        self.appointments = {}  # dictionary for appointments

    # -------------------------
    # PATIENT MANAGEMENT
    # -------------------------
    # Adds a new patient to the system
    def add_patient(self):
        try:
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            patient = Patient(name, age, gender)
            self.patients[patient.patient_id] = patient
            print(f"Patient registered successfully with ID: {patient.patient_id}")
        except ValueError as e:
            print(f"Error: {e}")

    # Shows a patient's details
    def view_patient_profile(self):
        patient_id = input("Enter patient ID: ")
        patient = self.patients.get(patient_id)
        if patient:
            patient.view_profile()
        else:
            print("Patient ID not found.")

    # -------------------------
    # DOCTOR MANAGEMENT
    # -------------------------
    # Adds a new doctor to the system
    def add_doctor(self):
        try:
            name = input("Enter doctor name: ")
            age = int(input("Enter doctor age: "))
            gender = input("Enter doctor gender: ")
            speciality = input("Enter specialty: ")
            slots = input("Enter available slots (comma separated e.g. 2025-07-15 14:00,2025-07-16 09:00): ").split(",")
            schedule = [s.strip() for s in slots]
            doctor = Doctor(name, age, gender, speciality, schedule)
            self.doctors[doctor.doctor_id] = doctor
            print(f"Doctor added successfully with ID: {doctor.doctor_id}")
        except ValueError as e:
            print(f"Error: {e}")

    # Shows a doctor's schedule
    def view_doctor_schedule(self):
        doctor_id = input("Enter doctor ID: ")
        doctor = self.doctors.get(doctor_id)
        if doctor:
            doctor.view_schedule()
        else:
            print("Doctor ID not found.")

    # -------------------------
    # APPOINTMENT MANAGEMENT
    # -------------------------
    # Books an appointment for a patient with a doctor
    def book_appointment(self):
        patient_id = input("Enter patient ID: ")
        doctor_id = input("Enter doctor ID: ")
        date = input("Enter appointment date (YYYY-MM-DD): ")
        time = input("Enter appointment time (HH:MM): ")
        date_time = f"{date} {time}"

        patient = self.patients.get(patient_id)
        doctor = self.doctors.get(doctor_id)

        if not patient:
            print("Invalid patient ID.")
            return
        if not doctor:
            print("Invalid doctor ID.")
            return

        # Check if the doctor is available at the given time
        if not doctor.is_available(date_time):
            print("Doctor is not available at this time.")
            return

        # Check if the time slot is already booked
        for app in self.appointments.values():
            if app.doctor == doctor and app.date == date and app.time == time and app.status == "Scheduled":
                print("This slot is already booked.")
                return

        # Create the appointment
        appointment = Appointment(patient, doctor, date, time)
        self.appointments[appointment.appointment_id] = appointment
        patient.book_appointment(appointment)
        doctor.remove_slot(date_time)  # remove time from doctor's schedule
        appointment.confirm()

    # Cancels an appointment
    def cancel_appointment(self):
        appointment_id = input("Enter appointment ID to cancel: ")
        appointment = self.appointments.get(appointment_id)
        if appointment and appointment.status == "Scheduled":
            appointment.cancel()
            appointment.doctor.add_slot(f"{appointment.date} {appointment.time}")  # put time back
        else:
            print("Invalid appointment ID or already cancelled.")

    # -------------------------
    # BILLING
    # -------------------------
    # Generates a bill for an appointment
    def generate_bill(self):
        appointment_id = input("Enter appointment ID to generate bill: ")
        appointment = self.appointments.get(appointment_id)
        if not appointment:
            print("Appointment not found.")
            return
        print("\n----- HEALTHYLIFE HOSPITAL RECEIPT -----")
        print(f"Patient: {appointment.patient.name}")
        print(f"Doctor: Dr. {appointment.doctor.name}")
        print(f"Date: {appointment.date}, Time: {appointment.time}")
        print("Consultation Fee: JMD$ 3000")
        try:
            additional = float(input("Enter additional service fees (tests, meds): JMD$ "))
        except ValueError:
            print("Invalid input, setting to 0.")
            additional = 0.0
        total = 3000 + additional
        print(f"Total Due: JMD$ {total}")
        print("----------------------------------------\n")

# -------------------------
# MAIN MENU
# -------------------------
# This is the main menu that runs repeatedly
def main_menu(system):
    while True:
        print("\n=== HOSPITAL MANAGEMENT SYSTEM ===")
        print("1. Add New Patient")
        print("2. Add New Doctor")
        print("3. Book Appointment")
        print("4. Cancel Appointment")
        print("5. Generate Bill")
        print("6. View Patient Profile")
        print("7. View Doctor Schedule")
        print("8. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            system.add_patient()
        elif choice == "2":
            system.add_doctor()
        elif choice == "3":
            system.book_appointment()
        elif choice == "4":
            system.cancel_appointment()
        elif choice == "5":
            system.generate_bill()
        elif choice == "6":
            system.view_patient_profile()
        elif choice == "7":
            system.view_doctor_schedule()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# -------------------------
# RUN THE PROGRAM
# -------------------------
if __name__ == "__main__":
    hospital_system = HospitalSystem()
    main_menu(hospital_system)
