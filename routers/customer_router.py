from fastapi import APIRouter, Depends, HTTPException
from schemas.customer_schema import CustomerSchema, CustomerResponseSchema, CustomerUpdate
from models.user import User
from models.customer import Customer
from dependencies.verify_token import verify_token
from sqlalchemy.orm import Session
from dependencies.session import get_session
from services.customer_service import verify_customer

customer_router = APIRouter(prefix="/customer", tags=["Customer"])

@customer_router.post("")
async def create_customer(customer_shema: CustomerSchema, user: User = Depends(verify_token), session: Session = Depends(get_session)):
    customer = verify_customer(customer_shema.tax_id, customer_shema.email, session)
    new_customer = Customer(idcity=customer_shema.idcity, name=customer_shema.name, contact=customer_shema.contact, email=customer_shema.email, tax_id=customer_shema.tax_id, birth_date=customer_shema.birth_date, observation=customer_shema.observation)
    session.add(new_customer)
    session.commit()
    return {"message": "Customer was successfully created"}

@customer_router.get("", response_model=list[CustomerResponseSchema])
async def list_customer(user: User = Depends(verify_token), session: Session = Depends(get_session)):
    customer = session.query(Customer).all()
    return customer

@customer_router.patch("/{idcustomer}")
async def update_customer(idcustomer: int, customer_data: CustomerUpdate, user: User = Depends(verify_token), session: Session = Depends(get_session)):
    customer = session.query(Customer).filter(Customer.idcustomer==idcustomer).first()
    if not customer:
        raise HTTPException(status_code=404, detail="The customer was not found")
    data = data.model_dump(exclude_unset=True)
    for models, value in data.items():
        setattr(customer, models, value)
    session.commit()
    return {"message": "Customer successfully updated"}

@customer_router.delete("/{idcustomer}")
async def delete_customer(idcustomer: int, user: User = Depends(verify_token), session: Session = Depends(get_session)):
    customer = session.query(Customer).filter(Customer.idcustomer==idcustomer).first()
    if not customer:
        raise HTTPException(status_code=404, detail="The customer was not found")
    session.delete(customer)
    session.commit()
    return {"message": "The Customer was successfully deleted"}