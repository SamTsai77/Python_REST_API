# Showcased how to create RESTful services in Python with FastAPI  
## Applied Technologies: Python, REST API, FastAPI, JSON, HTML
Start: uvicorn main:app --reload

![alt text](./pic0.png)

Add a customer: 
Post http://localhost:8000/customer
{"firstName":"Mary",
"lastName":"Johnson"}

![alt text](./pic1.png)


List all customers: 
Get http://localhost:8000/customers

![alt text](./pic2.png)

Update a customer: 
Put http://localhost:8000/customer/1

![alt text](./pic3.png)

List all customers: 

![alt text](./pic4.png)

Delete a customer: 
Delete http://localhost:8000/customer/1
![alt text](./pic5.png)

List all customers: 

![alt text](./pic6.png)