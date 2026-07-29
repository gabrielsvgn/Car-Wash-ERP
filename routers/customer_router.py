from fastapi import APIRouter, Depends, HTTPException

cutomer_router = APIRouter(prefix="/customer", tags=["Customer"])

