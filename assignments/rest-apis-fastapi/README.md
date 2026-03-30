# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using FastAPI framework to understand HTTP methods, routing, request/response handling, and API design patterns. You'll create a functional API with endpoints for managing resources.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Set up a FastAPI application with GET, POST, PUT, and DELETE endpoints to perform CRUD operations on a simple resource.

#### Requirements
Completed program should:

- Define a FastAPI application instance
- Create a GET endpoint that returns a list of items
- Create a POST endpoint that accepts JSON data and adds a new item
- Create a PUT endpoint that updates an existing item by ID
- Create a DELETE endpoint that removes an item by ID
- Use proper HTTP status codes for each operation

### 🛠️ Implement Data Validation

#### Description
Add request validation and error handling using Pydantic models to ensure data integrity.

#### Requirements
Completed program should:

- Define a Pydantic model for your resource with appropriate fields and types
- Validate incoming request data against the model
- Return appropriate error messages for invalid data (400 Bad Request)
- Handle cases where resources are not found (404 Not Found)
- Include meaningful response data for successful operations

### 🛠️ Test API Endpoints

#### Description
Verify that all endpoints work correctly by testing with various inputs.

#### Requirements
Completed program should:

- Test GET endpoint returns correct data
- Test POST endpoint creates new items successfully
- Test PUT endpoint updates existing items correctly
- Test DELETE endpoint removes items properly
- Verify error handling for edge cases (missing IDs, invalid data, etc.)
