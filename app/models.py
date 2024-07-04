from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    reg_id = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    nickname = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String)
    contact_number = Column(String)
    email = Column(String)
    address = Column(String)
    is_jamaah = Column(Boolean, default=False)
    no_rw = Column(String)
    no_rt = Column(String)
    domisili = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    appointment_date = Column(DateTime, nullable=False)
    appointment_order = Column(Integer, nullable=False)
    reason = Column(Text)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    patient = relationship("Patient", back_populates="appointments")

Patient.appointments = relationship("Appointment", order_by=Appointment.id, back_populates="patient")

class Treatment(Base):
    __tablename__ = 'treatments'

    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey('appointments.id'))
    treatment_description = Column(Text, nullable=False)
    treatment_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    appointment = relationship("Appointment", back_populates="treatments")

Appointment.treatments = relationship("Treatment", order_by=Treatment.id, back_populates="appointment")

class Medication(Base):
    __tablename__ = 'medications'

    id = Column(Integer, primary_key=True, index=True)
    treatment_id = Column(Integer, ForeignKey('treatments.id'))
    medication_name = Column(String, nullable=False)
    dosage = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    treatment = relationship("Treatment", back_populates="medications")

Treatment.medications = relationship("Medication", order_by=Medication.id, back_populates="treatment")

class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    nickname = Column(String)
    role = Column(String, nullable=False)
    contact_number = Column(String)
    email = Column(String)
    address = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    staff = relationship("Staff")

class Checkup(Base):
    __tablename__ = 'checkups'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    appointment_id = Column(Integer, ForeignKey('appointments.id'), nullable=True)
    gula_darah = Column(String, nullable=True)
    asam_urat = Column(String, nullable=True)
    kolesterol = Column(String, nullable=True)
    tekanan_darah = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    patient = relationship("Patient")
    appointment = relationship("Appointment")