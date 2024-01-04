# 10001-Ecommerce API

## Primary Modules

1. [django](https://www.djangoproject.com/)
1. [django rest framework](http://www.django-rest-framework.org/)

## Prerequisites

1. Python

## Installation Guide

```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

# Getting Started

Api_url = `https://10001-ecommerce-api-production.up.railway.app/

## Authentication
This API uses token-based authentication. To Obtain an access token, send a POST request to the /token/ endpoint with valid credentials.

**Request**

```bash
curl --location 'https://10001-ecommerce-api-production.up.railway.app/api/token/' \
--data '{
    "username":"your username",
    "password":"your password"
}'
```

For Test Purpose you can use the following login details to obtain the token:

`username`: admin
`password`: 1234

**Response**
```json
{
  "refresh": "your refresh token",
  "access": "your access token"
}
```

### Product Endpoints
##### 1. Retrieve All Products

**Endpoint:** `GET /api/product/`

**Description:** Retrieve a list of all products.

**Parameters:**
- `name` (optional): Filter products by name (case-insensitive)
- `category` (optional): Filter products by category
- `price__gte` (optional): Filter products with a price greater than or equal to the specified value
- `price__lte` (optional): Filter products with a price less than or equal to the specified value
- `stock_quantity__gte` (optional): Filter products with a stock quantity greater than or equal to the specified value

**Request:**
```bash
curl --location 'https://10001-ecommerce-api-production.up.railway.app/api/product/'
--header 'Authorization: Bearer "your access token"
```

**Response:**
```json
{
  "success": true,
  "message": "All Products",
  "response": [
    {
      "id": "5fa1679f-7858-4fc4-82f5-ac72709aa690",
      "name": "Rice",
      "category": "Food",
      "price": "1200.00",
      "description": "This is a demo description",
      "stock_quantity": 10
    },
    {
      "id": "ff483bb6-1520-4743-bc0b-8cf488cf0383",
      "name": "Chair",
      "category": "furniture",
      "price": "14895.00",
      "description": "Plastic chair",
      "stock_quantity": 892
    },
  ]
}
```
##### 2. Retrieve Product Details

**Endpoint:** `GET /api/product/?product_id=<product_id>`

**Description:** Retrieve details for a specific product.

**Parameters:**
- `product_id` (required): ID of the product to retrieve

**Request:**
```bash
curl --location 'https://10001-ecommerce-api-production.up.railway.app/api/product/?product_id=1'
--header 'Authorization: Bearer "your access token"
```

**Response:**
```json
{
  "success": true,
  "message": "Product Details for Rice",
  "response": {
    "id": "5fa1679f-7858-4fc4-82f5-ac72709aa690",
    "name": "Rice",
    "category": "Food",
    "price": "1200.00",
    "description": "This is a demo description",
    "stock_quantity": 10
  }
}
```
##### 3. Create a New Product

**Endpoint:** `POST /api/product/`

**Description:** Create a new product.

**Parameters:**
- `name` (required): Name of the product
- `category` (required): Category of the product
- `price` (required): Price of the product
- `description` (optional): Description of the product
- `stock_quantity` (required): Stock quantity of the product

**Request:**
```bash
curl  -X POST \
  'https://10001-ecommerce-api-production.up.railway.app/api/product/' \
  --header 'Accept: */*' \
  --header 'Authorization: Bearer "your token"' \
  --header 'Content-Type: application/json' \
  --data-raw '{    "name": "Rice",
    "category": "Food",
    "price": "1200.00",
    "description": "This is a demo description",
    "stock_quantity": 10
}'
```

**Response:**
```json
{
  "success": true,
  "message": "Product created successfully",
  "response": {
    "id": 382487-8249823-489248-8938,
    "name": "Rice",
    "category": "Food",
    "price": 1200.0,
    "description": "This is a demo description",
    "stock_quantity": 10
  }
}
```
##### 4. Update a Product

**Endpoint:** `PUT /api/product/?product_id=<product_id>`

**Description:** Update details for a specific product.

**Parameters:**
- `product_id` (required): ID of the product to update
- (Other parameters for updating product details)

**Request:**
```bash
curl  -X PUT \
  'https://10001-ecommerce-api-production.up.railway.app/api/product/?product_id=%22your%20product%20id%22' \
  --header 'Accept: */*' \
  --header 'Authorization: Bearer your-access-token' \
  --header 'Content-Type: application/json' \
  --data-raw '{    "name": "New Rice",
    "category": "Food",
    "price": "1200.00",
    "description": "This is a demo description",
    "stock_quantity": 10
}'
```

**Response:**
```json
{
  "success": true,
  "message": "Product Updated successfully",
  "response": {
    "id": 382487-8249823-489248-8938,
    "name": "New Rice",
    "category": "Food",
    "price": 1200.0,
    "description": "This is a demo description",
    "stock_quantity": 10
  }
}
```

##### 5. Delete a Product

**Endpoint:** `DELETE /api/product/?product_id=<product_id>`

**Description:** Delete a specific product.

**Parameters:**
- `product_id` (required): ID of the product to delete

**Request:**
```bash
curl  -X DELETE \
  'https://10001-ecommerce-api-production.up.railway.app/api/product/?product_id=%22your%20product%20id%22' \
  --header 'Accept: */*' \
  --header 'Authorization: Bearer your-access-token'
```

**Response:**
```json
{
  "success": true,
  "message": "Product Deleted successfully"
}
```

### Order Endpoints

##### 1. Retrieve All Orders

**Endpoint:** `GET /api/order/`

**Description:** Retrieve a list of all orders.

**Parameters:**
- `order_id` (optional): ID of a specific order to retrieve

**Request:**
```bash
curl -X GET https://10001-ecommerce-api-production.up.railway.app/api/order/
--header 'Authorization: Bearer "your access token"
```

**Response:**
```json
{
  "success": true,
  "message": "All Orders",
  "response": [
    {
      "id": "9c12e7af-3963-4947-b9f9-a5142986f0de",
      "product": "5fa1679f-7858-4fc4-82f5-ac72709aa690",
      "quantity": 1,
      "total_price": "3278.00",
      "product_details": {
        "id": "5fa1679f-7858-4fc4-82f5-ac72709aa690",
        "name": "Rice",
        "category": "Food",
        "price": "1200.00",
        "description": "This is a demo description",
        "stock_quantity": 10
      }
    },
    {
      "id": "d9ffb95c-ebcd-4eb6-b4c4-e706f7bd708b",
      "product": "5fa1679f-7858-4fc4-82f5-ac72709aa690",
      "quantity": 3,
      "total_price": "3600.00",
      "product_details": {
        "id": "5fa1679f-7858-4fc4-82f5-ac72709aa690",
        "name": "Rice",
        "category": "Food",
        "price": "1200.00",
        "description": "This is a demo description",
        "stock_quantity": 10
      }
    }
  ]
}
```
##### 2. Retrieve Order Details

**Endpoint:** `GET /api/order/?order_id=<order_id>`

**Description:** Retrieve details for a specific order.

**Parameters:**
- `order_id` (required): ID of the order to retrieve

**Request:**
```bash
curl -X GET https://10001-ecommerce-api-production.up.railway.app/api/order/?order_id=1
--header 'Authorization: Bearer "your access token"'
```

**Response:**
```json
{
  "success": true,
  "message": "Order Details for 9c12e7af-3963-4947-b9f9-a5142986f0de",
  "response": {
    "id": "9c12e7af-3963-4947-b9f9-a5142986f0de",
    "product": "5fa1679f-7858-4fc4-82f5-ac72709aa690",
    "quantity": 1,
    "total_price": "3278.00",
    "product_details": {
      "id": "5fa1679f-7858-4fc4-82f5-ac72709aa690",
      "name": "Rice",
      "category": "Food",
      "price": "1200.00",
      "description": "This is a demo description",
      "stock_quantity": 10
    }
  }
}
```

#### 3. Create a New Order

**Endpoint:** `POST /api/order/`

**Description:** Create a new order.

**Parameters:**
- `product_id` (required): ID of the product to order
- `quantity` (required): Quantity of the product to order

**Example Request:**
```bash
curl  -X POST \
  'http://127.0.0.1:8000/api/order/' \
  --header 'Accept: */*' \
  --header 'Authorization: Bearer your access token' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "product_id": "9c12e7af-3963-4947-b9f9-a5142986f0de", 
  "quantity": 2
  
}'
```

**Example Response:**
```json
{
  "success": true,
  "message": "Order created successfully",
  "response": {
    "id": "9383e134-9470-4279-b36c-2357d9031d6f",
    "product": "5fa1679f-7858-4fc4-82f5-ac72709aa690",
    "quantity": 2,
    "total_price": "2400.00",
    "product_details": {
      "id": "5fa1679f-7858-4fc4-82f5-ac72709aa690",
      "name": "Rice",
      "category": "Food",
      "price": "1200.00",
      "description": "This is a demo description",
      "stock_quantity": 8
    }
  }
}
```

#### Swagger and Redoc Documentation

- Swagger UI: `https://10001-ecommerce-api-production.up.railway.app/swagger/`
- Redoc: `https://10001-ecommerce-api-production.up.railway.app/redoc/`

#### Token Endpoints

- Obtain Token: `POST /token/`
- Refresh Token: `POST /token/refresh/`

GITHUB REPO LINK: https://github.com/ChidiebereIbiam/10001-ecommerce-api