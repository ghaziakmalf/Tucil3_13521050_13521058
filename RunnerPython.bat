@echo off
python src/main.py
for /d /r src/lib %%d in (__pycache__) do (
    rd /s /q "%%d"
)