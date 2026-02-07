"""
Module: 03_model_validator
Description: Demonstrates cross-field validation. While @field_validator works for 
single fields, @model_validator allows us to check relationships between multiple fields.
"""

from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    """
    Patient model with logic to enforce data requirements based on the state of other fields.
    """
    
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emerygency_contact(cls, model):
        """
        Enforces a business rule: If a patient is over 60, they MUST provide an 
        emergency contact in the contact_details dictionary.
        """
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model

def update_patient_data(patient: Patient):
    """Utility to display validated patient object."""
    print(f"Name: {patient.name}, Age: {patient.age}, Contact: {patient.contact_details}")

# Testing logic: This will pass because 'emergency' is in contact_details
patient_info = {
    'name': 'Ali', 
    'age': '67', 
    'email': 'nencn@petalnex.com', 
    'weight': 78.3, 
    'married': True, 
    "allergies": ['Dust'], 
    'contact_details': {'number': '3233424', 'emergency': '911'}
}

if __name__ == "__main__":
    obj = Patient(**patient_info)
    update_patient_data(obj)