"""
Module: 01_pydantic_why
Description: This script demonstrates the core reason for using Pydantic: Type Validation.
Python does not enforce types by default; Pydantic solves this by ensuring data 
matches the defined schema during instantiation.
"""

from pydantic import BaseModel, AnyUrl, EmailStr, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    """
    Base model for Patient data using Pydantic's validation features.
    
    Attributes:
        name (str): The patient's name, limited to 50 characters.
        age (int): Annotated field with metadata for documentation.
        email (EmailStr): Validates that the input is a properly formatted email.
        linkedin_url (AnyUrl): Validates that the input is a valid URL.
        weight (float): Uses Field to ensure weight is between 0 and 100 kg.
        height (Optional[float]): An optional field that defaults to None.
        married (Optional[bool]): An optional boolean defaulting to False.
        allergies (Optional[List[str]]): List of strings with a maximum of 5 items.
        contact_details (dict): A dictionary mapping string keys to string values.
    """

    # Field constraints to prevent oversized data
    name: str = Field(max_length=50) 
    
    # Using Annotated to attach extra metadata like titles and examples
    age: Annotated[int, Field(title='Age of the patient', 
                              description='Enter here the name of the patient', examples=[25])]
    
    email: EmailStr
    linkedin_url: AnyUrl
    
    # Custom numeric constraints using gt (greater than) and lt (less than)
    weight: float = Field(gt=0, lt=100)
    
    # Optional fields with default values for better data handling
    height: Optional[float] = None
    married: Optional[bool] = False 
    
    # List validation: ensures the list doesn't exceed 5 items
    allergies: Optional[List[str]] = Field(default=None, max_length=5)
    contact_details: dict[str, str]

def insert_patient_data(patient: Patient):
    """Simulates inserting validated data into a database."""
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.height)
    print(patient.email)
    print(patient.linkedin_url)
    print('inserted into database')

def update_patient_data(patient: Patient):
    """Simulates updating existing patient records."""
    print(patient.name)
    print(patient.age)
    print("Updated into database")

# Test Data
patient_info = {
    'name': 'Ali', 
    'age': 30, 
    "weight": 65.7, 
    "married": True, 
    "allergies": ['dust'], 
    "email": 'ali@example.com', 
    "linkedin_url": 'https://linkedin.com/in/ali', 
    "contact_details": {"phone": "12345"}
}

if __name__ == "__main__":
    obj = Patient(**patient_info)
    insert_patient_data(obj)