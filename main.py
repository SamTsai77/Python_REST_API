from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory database (for demonstration purposes)
customers = []

# Pydantic model for customer data
class Customer(BaseModel):
    firstName: str
    lastName: str

    
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/customers")
async def list_customers() -> List[Customer]:
    return customers


# Create a customer
@app.post("/customer/", response_model=Customer)
async def create_customer(customer: Customer):
    customers.append(customer)
    return customer

# Update a customer
@app.put("/customer/{customer_id}", response_model=Customer)
async def update_customer(customer_id: int, customer: Customer):
    if customer_id < 0 or customer_id >= len(customers):
        raise HTTPException(status_code=404, detail="Customer not found")

    customers[customer_id] = customer
    return customer

# Delete a customer
@app.delete("/customer/{customer_id}", response_model=Customer)
async def delete_item(customer_id: int):
    if customer_id < 0 or customer_id >= len(customers):
        raise HTTPException(status_code=404, detail="Item not found")
    
    deleted_customer = customers.pop(customer_id)
    return deleted_customer
