# News Dashboard

This is a Django-based web application that fetches the latest news using the NewsAPI and displays it in a user-friendly format.

## Technologies Used
- Python
- Django
- NewsAPI
- Bootstrap

## Prerequisites
- Python 3.x
- Django 4.x
- NewsAPI Key (create a free account at [NewsAPI](https://newsapi.org/))

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/khouloudaoued/news_dashboard.git
   cd news_dashboard
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your NewsAPI key to the project. Open the `settings.py` file and add your NewsAPI key:
   ```python
   NEWSAPI_KEY = 'your_newsapi_key_here'
   ```

5. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/news/` to see the news dashboard.

## Contact
If you encounter any issues, feel free to contact me at [khouloudaoued504@gmail.com](mailto:khouloudaoued504@gmail.com).
