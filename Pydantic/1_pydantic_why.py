from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    # name: str
    # adding some metadata using ANNOTATED
    name : Annotated[str,Field(max_length=50,title='Name of the patient',description='Give the name of the patient in lest than 50 character',examples={'Someone','Shreya'})]
    age: int
    weight: float=Field(gt=0)
    linkdin_url:AnyUrl
    allergies: List[str] 

    # Optional field
    email:Optional[EmailStr]=None
    married: Optional[bool]=False
    height:Optional[int]=None
    # why not just write list, it will give only 1 level validation
    # two level validation , first should be list then inside list is should be a string 

    contact_details:Dict[str,str]


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.height)
    print('Inserted')
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('Updated')

patient_inf={'name':'gaurav','age':20,'weight':55.2,'married':False,'allergies':['Fever','Cough'],'contact_details':{'email':'officialgaurav@gmail.com','College':'Boston University'}}

patient1=Patient(**patient_inf)

insert_patient_data(patient1)
update_patient_data(patient1)