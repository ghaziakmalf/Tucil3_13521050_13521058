@echo off
python src/Python/main.py
for /d /r src/Python/lib %%d in (__pycache__) do (
    rd /s /q "%%d"
)