# 🍽️ Little Lemon Restaurant API

This is a Django REST API for managing menu items, table bookings, and user authentication in a restaurant app. It uses Django REST Framework and Djoser.

## 🚀 Setup Instructions
activate your virtual environment, then:
```bash
git clone https://github.com/smaniot96/LittleLemon.git
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 🔐 Authentication

To obtain an authentication token:
```http
POST /auth/token/login/
Content-Type: application/json
{
  "username": "your_username",
  "password": "your_password"
}
```

Use the token in headers for protected endpoints:
```
Authorization: Token your_token
```

To logout:
```http
POST /auth/token/logout/
Authorization: Token your_token
```

## 📚 API Endpoints

### Public Endpoints

- `GET /restaurant/` – Home page
- `GET /restaurant/menu/` – List all menu items
- `GET /restaurant/menu/<id>/` – Retrieve a specific menu item

### Menu Management (CRUD)

- `POST /restaurant/menu/` – Create a new menu item  
  Example:
  ```json
  {
    "title": "Pasta",
    "price": "9.99",
    "inventory": 10
  }
  ```

- `PUT /restaurant/menu/<id>/` – Fully update a menu item  
- `PATCH /restaurant/menu/<id>/` – Partially update a menu item  
- `DELETE /restaurant/menu/<id>/` – Delete a menu item  

### Booking Management (CRUD via `/tables/`)

These come from the DRF router for `BookingViewSet`:

- `GET /tables/` – List all bookings  
- `POST /tables/` – Create a new booking  
  Example:
  ```json
  {
    "name": "John Doe",
    "date": "2025-06-01",
    "slot": "19:00"
  }
  ```

- `GET /tables/<id>/` – Retrieve a specific booking  
- `PUT /tables/<id>/` – Fully update a booking  
- `PATCH /tables/<id>/` – Partially update a booking  
- `DELETE /tables/<id>/` – Delete a booking  

### Other Routes

- `GET /restaurant/booking/` – Read-only shortcut for bookings
- `POST /auth/token/login/` – Obtain auth token
- `POST /auth/token/logout/` – Logout and invalidate token

## 🧪 Testing Tips

Use tools like Postman, curl, or the DRF browsable API. Always include your token in the header:
```
Authorization: Token your_token
```

## 🛠️ Admin Panel

Login at: http://127.0.0.1:8000/admin/  
Use your superuser credentials to manage menu items and bookings via GUI.
