# 📦 CodeCache - Modern Snippets Sharing Platform

![GitHub repo size](https://img.shields.io/github/repo-size/DevTroli/PasteBin)
[![Project Status][status-shield]][status-url]
[![License][license-shield]][license-url]
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Django Version](https://img.shields.io/badge/django-5.0.1-green)

## 🌟 Overview
CodeCache is a modern code sharing platform inspired by Pastebin, built with Django and Django REST Framework. It offers syntax highlighting, expiration control, privacy, and a modern interface with Tailwind CSS.

## ✨ Features
- 🚀 Snippet Management
  - Create and edit code snippets
  - Syntax highlighting for multiple languages
  - Automatic expiration of snippets
  - Privacy control
  
- 👤 User System
  - Registration and authentication
  - Customized user profiles
  - Manage own snippets
  
- 🔌 RESTful API
  - Complete CRUD endpoints
  - Token-based authentication
  - Interactive documentation
  
- 🎨 Modern Interface
  - Responsive design with Tailwind CSS
  - Syntax highlighting themes
  - Line number support

## 🛠️ Technologies
- [Django 5.0.1](https://www.djangoproject.com/) - High-level Python web framework
- [Django REST Framework 3.14.0](https://www.django-rest-framework.org/) - Powerful toolkit for building Web APIs
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
- [Pygments 2.17.2](https://pygments.org/) - Syntax highlighting library
- [django-cors-headers 4.3.1](https://github.com/adamchainz/django-cors-headers) - CORS management for Django

## 🚀 Installation
<details>
<summary>📖 Guide Step-by-Step</summary>
  
1. Clone the repository:
```bash
git clone https://github.com/DevTroli/PasteBin.git && cd PasteBin
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv --clear && source .venv/bin/activate  # or venv\Scripts\activate  # Windows
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python manage.py migrate
```
</details>

## 💻 Usage
1. Start the development server:
```bash
python manage.py createsuperuser && python manage.py runserver
```

2. Access the endpoints:
* Web Interface: http://127.0.0.1:8000
* API Root: http://127.0.0.1:8000/api/
* Admin Interface: http://127.0.0.1:8000/admin/

## 🔌 API Endpoints
### Snippets
* `GET /api/snippets/` - List all snippets
* `POST /api/snippets/` - Create a new snippet
* `GET /api/snippets/{id}/` - Snippet details
* `PUT /api/snippets/{id}/` - Update a snippet
* `DELETE /api/snippets/{id}/` - Delete a snippet
* `GET /api/snippets/{id}/highlight/` - Highlighted version of the snippet

### Users
* `GET /api/users/` - List users
* `GET /api/users/{id}/` - User details

## 🔧 Development
<details>
<summary>📖 How it all works</summary>

#### Project Structure
```
PasteBin/
├── manage.py  # The main Django management script
├── requirements.txt  # The project dependencies
├── .gitignore  # Ignored files for Git
├── LICENSE  # Project license
├── README.md  # Project documentation
├── contrib/
│   ├── envGen.py  # Script to generate environment variables
├── setup/
│   ├── settings.py  # Django project settings
│   ├── urls.py  # Django URL configuration
│   └── wsgi.py  # WSGI server configuration
│   └── __init__.py  # Python package initialization
├── snippets/
│   ├── migrations/  # Django database migrations
│   ├── templatetags/  # Custom Django template tags
│   ├── __init__.py  # Python package initialization
│   ├── models.py  # Django models for the Snippets app
│   ├── serializers.py  # Django REST Framework serializers
│   ├── views.py  # Django views for the Snippets app
│   └── urls.py  # URLs for the Snippets app
│   └── tests.py  # Tests for the Snippets app
│   └── apps.py  # Django app configuration
├── staticfiles/
│   ├── admin/  # Static files for the Django admin interface
│   ├── django_extentions/  # Static files for Django extensions
│   ├── rest_framework/  # Static files for Django REST Framework
└── templates/
    ├── base.html  # The main base template
    ├── includes/  # Additional template partials
    ├── registration/  # Templates for user registration and authentication
    └── snippets/  # Templates for the Snippets app
```

#### Configure environment variables
```bash
python contrib/envGen.py
# Don't forget to add your database access to .env
```
</details>

## 🧪 Testing
Run the tests with:
```bash
python manage.py test
```

## 👥 How to Contribute
1. Fork the project
2. Create your Feature Branch (`git checkout -b NewFeatureAmazing`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin NewFeatureAmazing`)
5. Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact
[@DevTroli](https://github.com/DevTroli) - pablotroli@outlook.com

---
⭐️ Made with ❤️ by @DevTroli

<!-- MARKDOWN LINKS & IMAGES -->
[status-shield]: https://img.shields.io/badge/status-active-success.svg
[status-url]: #
[version-shield]: https://img.shields.io/badge/version-1.0.0-blue.svg
[version-url]: #
[license-shield]: https://img.shields.io/badge/license-MIT-green.svg
[license-url]: #
