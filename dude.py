import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database Setup
def setup_database():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        gender TEXT NOT NULL,
        address TEXT NOT NULL,
        phone TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS doctors (
        doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialization TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        doctor_id INTEGER,
        appointment_date TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patients (patient_id),
        FOREIGN KEY (doctor_id) REFERENCES doctors (doctor_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS medical_records (
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        doctor_id INTEGER,
        diagnosis TEXT NOT NULL,
        prescription TEXT NOT NULL,
        visit_date TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patients (patient_id),
        FOREIGN KEY (doctor_id) REFERENCES doctors (doctor_id)
    )
    ''')

    conn.commit()
    conn.close()

setup_database()

# GUI Setup
class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("800x600")
        #self.create_login_screen()
'''
    def create_login_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Login", font=("Helvetica", 24)).pack(pady=20)
        
        tk.Label(self.root, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        
        tk.Label(self.root, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack(pady=5)
        
        tk.Button(self.root, text="Login", command=self.login).pack(pady=20)
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            self.user_id = user[0]
            self.role = user[3]
            if self.role == "admin":
                self.create_admin_dashboard()
            elif self.role == "doctor":
                self.create_doctor_dashboard()
            elif self.role == "patient":
                self.create_patient_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")
        '''

def create_admin_dashboard(self):
        self.clear_screen()
        tk.Label(self.root, text="Admin Dashboard", font=("Helvetica", 24)).pack(pady=20)

        tk.Button(self.root, text="Add Patient", command=self.add_patient_screen).pack(pady=10)
        tk.Button(self.root, text="Add Doctor", command=self.add_doctor_screen).pack(pady=10)
        tk.Button(self.root, text="View Appointments", command=self.view_appointments_screen).pack(pady=10)

def add_patient_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Add Patient", font=("Helvetica", 24)).pack(pady=20)
        
        tk.Label(self.root, text="Name").pack(pady=5)
        self.patient_name_entry = tk.Entry(self.root)
        self.patient_name_entry.pack(pady=5)
        
        tk.Label(self.root, text="Age").pack(pady=5)
        self.patient_age_entry = tk.Entry(self.root)
        self.patient_age_entry.pack(pady=5)
        
        tk.Label(self.root, text="Gender").pack(pady=5)
        self.patient_gender_entry = tk.Entry(self.root)
        self.patient_gender_entry.pack(pady=5)
        
        tk.Label(self.root, text="Address").pack(pady=5)
        self.patient_address_entry = tk.Entry(self.root)
        self.patient_address_entry.pack(pady=5)
        
        tk.Label(self.root, text="Phone").pack(pady=5)
        self.patient_phone_entry = tk.Entry(self.root)
        self.patient_phone_entry.pack(pady=5)
        
        tk.Button(self.root, text="Add", command=self.add_patient).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.create_admin_dashboard).pack(pady=5)
    
def add_patient(self):
        name = self.patient_name_entry.get()
        age = self.patient_age_entry.get()
        gender = self.patient_gender_entry.get()
        address = self.patient_address_entry.get()
        phone = self.patient_phone_entry.get()
        
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO patients (name, age, gender, address, phone) VALUES (?, ?, ?, ?, ?)",
                       (name, age, gender, address, phone))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", "Patient added successfully")
        self.create_admin_dashboard()
        
def add_doctor_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Add Doctor", font=("Helvetica", 24)).pack(pady=20)
        
        tk.Label(self.root, text="Name").pack(pady=5)
        self.doctor_name_entry = tk.Entry(self.root)
        self.doctor_name_entry.pack(pady=5)
        
        tk.Label(self.root, text="Specialization").pack(pady=5)
        self.doctor_specialization_entry = tk.Entry(self.root)
        self.doctor_specialization_entry.pack(pady=5)
        
        tk.Label(self.root, text="Phone").pack(pady=5)
        self.doctor_phone_entry = tk.Entry(self.root)
        self.doctor_phone_entry.pack(pady=5)
        
        tk.Label(self.root, text="Email").pack(pady=5)
        self.doctor_email_entry = tk.Entry(self.root)
        self.doctor_email_entry.pack(pady=5)
        
        tk.Button(self.root, text="Add", command=self.add_doctor).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.create_admin_dashboard).pack(pady=5)
    
def add_doctor(self):
        name = self.doctor_name_entry.get()
        specialization = self.doctor_specialization_entry.get()
        phone = self.doctor_phone_entry.get()
        email = self.doctor_email_entry.get()
        
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO doctors (name, specialization, phone, email) VALUES (?, ?, ?, ?)",
                       (name, specialization, phone, email))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", "Doctor added successfully")
        self.create_admin_dashboard()
    
def view_appointments_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="All Appointments", font=("Helvetica", 24)).pack(pady=20)
        
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointments")
        appointments = cursor.fetchall()
        
        for appointment in appointments:
            tk.Label(self.root, text=str(appointment)).pack(pady=5)
        
        conn.close()
        tk.Button(self.root, text="Back", command=self.create_admin_dashboard).pack(pady=20)
    
def create_doctor_dashboard(self):
        self.clear_screen()
        tk.Label(self.root, text="Doctor Dashboard", font=("Helvetica", 24)).pack(pady=20)

        tk.Button(self.root, text="View Appointments", command=self.view_doctor_appointments_screen).pack(pady=10)
        tk.Button(self.root, text="Update Medical Records", command=self.update_medical_records_screen).pack(pady=10)
    
def view_doctor_appointments_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="My Appointments", font=("Helvetica", 24)).pack(pady=20)
        
        doctor_id = self.get_logged_in_user_id()
        
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointments WHERE doctor_id = ?", (doctor_id,))
        appointments = cursor.fetchall()
        
        for appointment in appointments:
            tk.Label(self.root, text=str(appointment)).pack(pady=5)
        
        conn.close()
        tk.Button(self.root, text="Back", command=self.create_doctor_dashboard).pack(pady=20)
    
def update_medical_records_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Update Medical Records", font=("Helvetica", 24)).pack(pady=20)
        
        tk.Label(self.root, text="Patient ID").pack(pady=5)
        self.record_patient_id_entry = tk.Entry(self.root)
        self.record_patient_id_entry.pack(pady=5)
        
        tk.Label(self.root, text="Diagnosis").pack(pady=5)
        self.record_diagnosis_entry = tk.Entry(self.root)
        self.record_diagnosis_entry.pack(pady=5)
        
        tk.Label(self.root, text="Prescription").pack(pady=5)
        self.record_prescription_entry = tk.Entry(self.root)
        self.record_prescription_entry.pack(pady=5)
        
        tk.Button(self.root, text="Update", command=self.update_medical_record).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.create_doctor_dashboard).pack(pady=5)
    
def update_medical_record(self):
        patient_id = self.record_patient_id_entry.get()
        diagnosis = self.record_diagnosis_entry.get()
        prescription = self.record_prescription_entry.get()
        
        doctor_id = self.get_logged_in_user_id()
        
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO medical_records (patient_id, doctor_id, diagnosis, prescription, visit_date) VALUES (?, ?, ?, ?, DATE('now'))",
                       (patient_id, doctor_id, diagnosis, prescription))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", "Medical record updated successfully")
        self.create_doctor_dashboard()
    
def get_logged_in_user_id(self):
        return 1  # Placeholder, replace with actual logic
    
def create_patient_dashboard(self):
        self.clear_screen()
        tk.Label(self.root, text="Patient Dashboard", font=("Helvetica", 24)).pack(pady=20)

        tk.Button(self.root, text="View Medical Records", command=self.view_medical_records_screen).pack(pady=10)
        tk.Button(self.root, text="Book Appointment", command=self.book_appointment_screen).pack(pady=10)
    
def view_medical_records_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="My Medical Records", font=("Helvetica", 24)).pack(pady=20)
        
        patient_id = self.get_logged_in_user_id()
        
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM medical_records WHERE patient_id = ?", (patient_id,))
        records = cursor.fetchall()
        
        for record in records:
            tk.Label(self.root, text=str(record)).pack(pady=5)
        
        conn.close()
        tk.Button(self.root, text="Back", command=self.create_patient_dashboard).pack(pady=20)
    
def book_appointment_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Book Appointment", font=("Helvetica", 24)).pack(pady=20)
        
        tk.Label(self.root, text="Doctor ID").pack(pady=5)
        self.appointment_doctor_id_entry = tk.Entry(self.root)
        self.appointment_doctor_id_entry.pack(pady=5)
        
        tk.Label(self.root, text="Date (YYYY-MM-DD)").pack(pady=5)
        self.appointment_date_entry = tk.Entry(self.root)
        self.appointment_date_entry.pack(pady=5)
        
        tk.Button(self.root, text="Book", command=self.book_appointment).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.create_patient_dashboard).pack(pady=5)
    
def book_appointment(self):
        doctor_id = self.appointment_doctor_id_entry.get()
        appointment_date = self.appointment_date_entry.get()
        
        patient_id = self.get_logged_in_user_id()
        
        conn = sqlite3.connect('hospital_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO appointments (patient_id, doctor_id, appointment_date, status) VALUES (?, ?, ?, 'Pending')",
                       (patient_id, doctor_id, appointment_date))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", "Appointment booked successfully")
        self.create_patient_dashboard()
    
def get_logged_in_user_id(self):
        return 1  # Placeholder, replace with actual logic

def main():
    root = tk.Tk()
    app = HospitalManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
