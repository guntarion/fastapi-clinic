from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class PatientBase(BaseModel):
    reg_id: str
    full_name: str
    nickname: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    contact_number: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    is_jamaah: Optional[bool] = None
    no_rw: Optional[str] = None
    no_rt: Optional[str] = None
    domisili: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class AppointmentBase(BaseModel):
    patient_id: int
    appointment_date: datetime
    appointment_order: int
    reason: Optional[str] = None
    status: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class TreatmentBase(BaseModel):
    appointment_id: int
    treatment_description: str
    treatment_date: datetime

class TreatmentCreate(TreatmentBase):
    pass

class Treatment(TreatmentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class MedicationBase(BaseModel):
    treatment_id: int
    medication_name: str
    dosage: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None

class MedicationCreate(MedicationBase):
    pass

class Medication(MedicationBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class StaffBase(BaseModel):
    full_name: str
    nickname: Optional[str] = None
    role: str
    contact_number: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

class StaffCreate(StaffBase):
    pass

class Staff(StaffBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    password: str
    role: str
    staff_id: Optional[int] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class CheckupBase(BaseModel):
    patient_id: int
    appointment_id: Optional[int] = None
    gula_darah: Optional[str] = None
    asam_urat: Optional[str] = None
    kolesterol: Optional[str] = None
    tekanan_darah: Optional[str] = None

class CheckupCreate(CheckupBase):
    pass

class Checkup(CheckupBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
