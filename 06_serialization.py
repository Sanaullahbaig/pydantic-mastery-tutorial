"""
Module: 06_serialization
Description: Shows how to export Pydantic objects back into standard formats 
like Python dictionaries or JSON strings.
"""

from pydantic import BaseModel

class Address(BaseModel):
    city: str
    Province: str
    Postalcode: str

class Patient(BaseModel):
    """Model used to demonstrate data export/serialization."""
    name: str
    age: int
    gender: str
    address: Address

# Setup data
address1 = Address(city='Mansehra', Province='KPK', Postalcode='21300')
patient1 = Patient(name='Ali', gender='male', age=35, address=address1)

if __name__ == "__main__":
    # model_dump converts the object to a dictionary
    # 'include' or 'exclude' can be used to control the output
    temp_dict = patient1.model_dump(include=['name', 'gender'])
    print(f"Dictionary Export: {temp_dict}")

    # model_dump_json converts the object to a JSON string
    temp_json = patient1.model_dump_json()
    print(f"JSON Export: {temp_json}")