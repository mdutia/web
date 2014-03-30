CSRF_ENABLED = True
SECRET_KEY = 'Cjq0nz2@kWl2Pm'
SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
SQLALCHEMY_BINDS = {
    'evaluations':      'sqlite:///evaluations.db'
}