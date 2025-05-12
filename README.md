# DjangoProject

## Project Overview

This project is an Online Food Management System built using the Django web framework. It provides features for managing food orders, users, and administrative tasks, including separate apps for admin and user functionalities.

## Features

- User registration, login, and profile management
- Browse food menu and place orders
- Order history and tracking
- Admin dashboard for managing users, food items, and orders
- CRUD operations for food items, categories, and users (Admin)
- Upload and manage food images
- Responsive UI with Bootstrap

## Technologies Used

- **Python**: The core programming language for backend logic.
- **Django 4.2.3**: The main web framework used for rapid development and clean design.
- **SQLite**: Default database for development (as seen from `db.sqlite3`).
- **Pillow**: For image processing (used for handling media/images).
- **mysqlclient**: MySQL database support (optional, for production or advanced use).
- **HTML/CSS/JavaScript**: For frontend templates and static files.
- **Bootstrap/Other JS Libraries**: (If included in `static/` for UI enhancements.)

## Database Tables & Relationships

- **User**: Stores user information (username, password, email, etc.)
- **FoodCategory**: Categories for food items (e.g., Snacks, Main Course)
- **FoodItem**: Stores food details (name, price, image, category)
  - *Relation*: Each `FoodItem` belongs to a `FoodCategory`
- **Order**: Stores order details (user, order date, status)
  - *Relation*: Each `Order` is linked to a `User`
- **OrderItem**: Stores items in an order (order, food item, quantity)
  - *Relation*: Each `OrderItem` links an `Order` and a `FoodItem`

## Project Structure

- `OnlineFoodMgmt/` - Main Django project folder.
  - `AdminApp/` - Django app for admin functionalities.
  - `UserApp/` - Django app for user functionalities.
  - `media/` - Stores uploaded images and media files.
  - `static/` - Static files (CSS, JS, images).
  - `db.sqlite3` - SQLite database file.
  - `manage.py` - Django management script.

## Getting Started

1. **Install dependencies**:  
   Activate the virtual environment in `envfood/` and install required packages.
2. **Run migrations**:  
   ```
   python manage.py migrate
   ```
3. **Start the development server**:  
   ```
   python manage.py runserver
   ```

## Admin CRUD Operations

- Admin can create, read, update, and delete food categories and items.
- Admin can manage user accounts and view all orders.
- Admin can update order statuses.

---
