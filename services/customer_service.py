from models.customer import Customer
from fastapi import HTTPException

def verify_customer(tax_id, email, session):
    customer_taxid = session.query(Customer).filter(Customer.tax_id==tax_id).first()
    customer_email = session.query(Customer).filter(Customer.email==email).first()
    if customer_taxid:
        raise HTTPException(status_code=409, detail="The Customer tax id already exists")
    if customer_email:
        raise HTTPException(status_code=409, detail="The Customer email already exists")
    return True

