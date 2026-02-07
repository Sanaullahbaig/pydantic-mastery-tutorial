"""
Module: 05_nested_models
Description: Highlights the power of composition. Instead of flat dictionaries, 
we use nested Pydantic models to organize related data like addresses.
"""

from pydantic import BaseModel

class Address(BaseModel):
    """Sub-model for address details."""
    city: str
    Province: str
    Postalcode: str

class Patient(BaseModel):
    """
    Main Patient model containing a nested Address model.
    Pydantic automatically validates the nested Address when Patient is instantiated.
    """
    name: str
    age: int
    gender: str
    address: Address

# Creating instances and nesting them
address_dict = {'city': 'Mansehra', 'Province': 'KPK', 'Postalcode': '21300'}
address1 = Address(**address_dict)

patient_dict = {'name': 'Ali', 'gender': 'male', 'age': 35, 'address': address1}

if __name__ == "__main__":
    patient1 = Patient(**patient_dict)
    print(f"Patient Address City: {patient1.address.city}")