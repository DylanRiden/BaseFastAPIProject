## Base FastAPI Project

This is a base FastAPI project with an SQLAlchemy connection to your database.

Just run `pip install` to install the required dependencies.

Then, to start your project you must connect your database in the main.py file and 
also connect it in alembic.ini

To create a migration run `alembic revision --autogenerate -m "MIGRATION_NAME"`

To update your database run `alembic upgrade`

To run the project run `uvicorn main:app --reload`
