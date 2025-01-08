# groomer web app

## Setup Instructions

### Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start Django server
python manage.py runserver

# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev