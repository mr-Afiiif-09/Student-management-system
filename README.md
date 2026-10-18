# StudentHub — Student Management System

A beginner-friendly student management web application built with **Python, Flask, HTML, CSS, and JSON storage**. It adapts an object-oriented Python Student Management System into a browser-based dashboard.

## Features

- Add student records
- View student records in a dashboard
- Search by name or roll number
- Edit student name and marks
- Delete records
- View total student count and average marks
- Store records in a local JSON file
- Responsive layout for desktop and mobile screens
- Validate roll numbers and marks

## Tech Stack

- Python
- Flask
- HTML5
- CSS3
- Jinja templates
- JSON

## Run locally

1. Install Python 3.10 or later.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment:

   **Windows PowerShell**
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

5. Start the application:

   ```powershell
   python app.py
   ```

6. Open the local address shown in the terminal, usually `http://127.0.0.1:5000`.

## Data storage

Student records are stored in `students_OOPS.json` beside `app.py`. The included file starts empty. Keep a backup of your JSON file if it contains records you need.

## Project structure

```text
student-management-web/
├── app.py
├── students_OOPS.json
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   ├── index.html
│   └── edit.html
└── static/
    └── style.css
```

## Notes

- This is a local learning project, not a production-ready multi-user system.
- Before deploying publicly, replace the Flask secret key, disable debug mode, and consider using a database such as SQLite or MySQL.
- Do not commit virtual environments, private keys, or secrets to GitHub.

## Future improvements

- Add a database
- Add authentication and user roles
- Export student records to CSV
- Add sorting and pagination
- Add automated tests
