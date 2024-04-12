@echo off
rem Load model
python project\scripts\train_model.py
rem Run Django server
python project\manage.py runserver
