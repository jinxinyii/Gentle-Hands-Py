# Gentle Hands Project

This is a Django-based web application for user registration, login, and homepage functionality. The project is configured to use a PostgreSQL database. This project is a collaborative effort developed during our on-the-job training (OJT) to meet the requirements of our client.

## Group Members

- **Andrea** - UX/UI Designer
- **Elmar** - Lead Developer
- **Hanns** - Database Administrator
- **Jessie** - Frontend Developer
- **Justin** - Quality Assurance
- **Kim** - Frontend Developer
- **Rhoen** - Project Manager

## Features

- User Registration
- User Login
- User Logout
- Homepage
- Dashboard
- Child Records
- Medication Management
- Illness Tracking
- Appointment Scheduling
- Immunization Records
- Medic Finder

## Setup Instructions

1. **Clone the repository:**

    ```sh
    git clone <repository-url>
    cd myproject
    ```

2. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Configure the database:**

    Update the `DATABASES` setting in `myproject/settings.py` to match your PostgreSQL configuration.

4. **Run migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and go to `http://localhost:8000`.

## Custom User Model

The project uses a custom user model defined in `accounts/models.py`. The custom user model extends Django's `AbstractUser`.

## Templates

The HTML templates for the application are located in the `accounts/templates` directory.

- `home.html`: Homepage template
- `register.html`: Registration template
- `login.html`: Login template
- `dashboard.html`: Dashboard template
- `logout.html`: Logout template
- `childrecord.html`: Child Records Dashboard template
- `registerChild.html`: Child Registration template
- `medication.html`: Medication Management template
- `medication_list.html`: Medication List template
- `illness_list.html`: Illness List template
- `appointment_list.html`: Appointment List template
- `immunization.html`: Immunization Records template
- `growth_data.html`: Growth Data template
- `medic.html`: Medic Finder template

## Admin

The custom user model is registered with the Django admin site in `accounts/admin.py`.

## License

This project is licensed under the MIT License.