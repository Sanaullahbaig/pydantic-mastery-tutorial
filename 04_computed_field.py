"""
Module: 04_computed_field
Description: Demonstrates how to create fields that are calculated from other 
attributes. These are not provided by the user but are included in the model output.
"""

from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    """
    Model that automatically calculates BMI based on height and weight.
    """
    
    name: str
    age: int
    email: EmailStr
    height: float
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        """
        Calculates Body Mass Index (BMI).
        Formula: weight (kg) / [height (m)]^2
        """
        bmi = round(self.weight / (self.height**2), 2)
        return bmi

def update_patient_data(patient: Patient):
    """Displays patient info including the dynamically computed BMI."""
    print(f"Name: {patient.name}")
    print(f"Calculated BMI: {patient.bmi}")

patient_info = {
    'name': 'Ali', 
    'age': '67', 
    'email': 'nencn@petalnex.com', 
    'weight': 78.3, 
    'height': 5.8, 
    'married': True, 
    "allergies": ['Dust'], 
    'contact_details': {'phone': '123'}
}

if __name__ == "__main__":
    obj = Patient(**patient_info)
    update_patient_data(obj)