from sqlalchemy.orm import Session
from . import models, schemas

# CRUD operations for Patients
def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def get_patient_by_reg_id(db: Session, reg_id: str):
    return db.query(models.Patient).filter(models.Patient.reg_id == reg_id).first()

def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Patient).offset(skip).limit(limit).all()

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

# CRUD operations for Appointments
def get_appointment(db: Session, appointment_id: int):
    return db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()

def get_appointments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Appointment).offset(skip).limit(limit).all()

def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    db_appointment = models.Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def update_appointment(db: Session, appointment_id: int, appointment: schemas.AppointmentCreate):
    db_appointment = get_appointment(db, appointment_id)
    if db_appointment is None:
        return None
    for key, value in appointment.dict().items():
        setattr(db_appointment, key, value)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def delete_appointment(db: Session, appointment_id: int):
    db_appointment = get_appointment(db, appointment_id)
    if db_appointment:
        db.delete(db_appointment)
        db.commit()
    return db_appointment

# CRUD operations for Treatments
def get_treatment(db: Session, treatment_id: int):
    return db.query(models.Treatment).filter(models.Treatment.id == treatment_id).first()

def get_treatments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Treatment).offset(skip).limit(limit).all()

def create_treatment(db: Session, treatment: schemas.TreatmentCreate):
    db_treatment = models.Treatment(**treatment.dict())
    db.add(db_treatment)
    db.commit()
    db.refresh(db_treatment)
    return db_treatment

def update_treatment(db: Session, treatment_id: int, treatment: schemas.TreatmentCreate):
    db_treatment = get_treatment(db, treatment_id)
    if db_treatment is None:
        return None
    for key, value in treatment.dict().items():
        setattr(db_treatment, key, value)
    db.commit()
    db.refresh(db_treatment)
    return db_treatment

def delete_treatment(db: Session, treatment_id: int):
    db_treatment = get_treatment(db, treatment_id)
    if db_treatment:
        db.delete(db_treatment)
        db.commit()
    return db_treatment

# CRUD operations for Medications
def get_medication(db: Session, medication_id: int):
    return db.query(models.Medication).filter(models.Medication.id == medication_id).first()

def get_medications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Medication).offset(skip).limit(limit).all()

def create_medication(db: Session, medication: schemas.MedicationCreate):
    db_medication = models.Medication(**medication.dict())
    db.add(db_medication)
    db.commit()
    db.refresh(db_medication)
    return db_medication

def update_medication(db: Session, medication_id: int, medication: schemas.MedicationCreate):
    db_medication = get_medication(db, medication_id)
    if db_medication is None:
        return None
    for key, value in medication.dict().items():
        setattr(db_medication, key, value)
    db.commit()
    db.refresh(db_medication)
    return db_medication

def delete_medication(db: Session, medication_id: int):
    db_medication = get_medication(db, medication_id)
    if db_medication:
        db.delete(db_medication)
        db.commit()
    return db_medication

# CRUD operations for Staff
def get_staff(db: Session, staff_id: int):
    return db.query(models.Staff).filter(models.Staff.id == staff_id).first()

def get_staffs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Staff).offset(skip).limit(limit).all()

def create_staff(db: Session, staff: schemas.StaffCreate):
    db_staff = models.Staff(**staff.dict())
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff

def update_staff(db: Session, staff_id: int, staff: schemas.StaffCreate):
    db_staff = get_staff(db, staff_id)
    if db_staff is None:
        return None
    for key, value in staff.dict().items():
        setattr(db_staff, key, value)
    db.commit()
    db.refresh(db_staff)
    return db_staff

def delete_staff(db: Session, staff_id: int):
    db_staff = get_staff(db, staff_id)
    if db_staff:
        db.delete(db_staff)
        db.commit()
    return db_staff

# CRUD operations for Users
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = get_user(db, user_id)
    if db_user is None:
        return None
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# CRUD operations for Checkups
def get_checkup(db: Session, checkup_id: int):
    return db.query(models.Checkup).filter(models.Checkup.id == checkup_id).first()

def get_checkups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Checkup).offset(skip).limit(limit).all()

def create_checkup(db: Session, checkup: schemas.CheckupCreate):
    db_checkup = models.Checkup(**checkup.dict())
    db.add(db_checkup)
    db.commit()
    db.refresh(db_checkup)
    return db_checkup

def update_checkup(db: Session, checkup_id: int, checkup: schemas.CheckupCreate):
    db_checkup = get_checkup(db, checkup_id)
    if db_checkup is None:
        return None
    for key, value in checkup.dict().items():
        setattr(db_checkup, key, value)
    db.commit()
    db.refresh(db_checkup)
    return db_checkup

def delete_checkup(db: Session, checkup_id: int):
    db_checkup = get_checkup(db, checkup_id)
    if db_checkup:
        db.delete(db_checkup)
        db.commit()
    return db_checkup
