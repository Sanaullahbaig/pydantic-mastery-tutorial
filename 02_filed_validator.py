"""
Module: 02_field_validator
Description: Demonstrates the use of @field_validator to create custom validation logic 
for specific fields, such as domain-specific email checks and custom range validation.
"""

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    """
    Patient model with custom field-level validation logic.
    """

    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def emial_validator(cls, value):
        """
        Validates that the email belongs to an approved organizational domain.
        
        Args:
            value (str): The email string provided by the user.
        Returns:
            str: The validated email if successful.
        Raises:
            ValueError: If the domain is not in the whitelist.
        """
        valid_domains = ['gov.pk.com', 'petalnex.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid Domain')

        return value
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        """
        Ensures the age falls within a specific logical range (0-100).
        Mode 'after' means validation runs after Pydantic converts the input to an int.
        """
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be between 0 and 100')

def update_patient_data(patient: Patient):
    """Prints validated patient details."""
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.contact_details)

# Data for testing the validators
patient_info = {
    'name': 'Ali', 
    'age': 67, 
    'email': 'nencn@petalnex.com', 
    'weight': 78.3, 
    'married': True, 
    "allergies": ['Dust'], 
    'contact_details': {'phone': '3233424'}
}

if __name__ == "__main__":
    obj = Patient(**patient_info)
    update_patient_data(obj)