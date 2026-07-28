# Student Management System (VS-4)

A Python-based Student Management System that stores student information using JSON. This project allows users to add, search, update, delete, and display student records through a menu-driven interface.

## Features

- Add a new student
- View all students
- Search students by name
- Update student information
- Delete a student by ID
- Store data permanently using JSON
- Sort students alphabetically by name
- Error handling for invalid input

## Technologies Used

- Python 3
- JSON

## Project Structure

```
Student-Management-VS-4/
│
├── main.py
├── student.json
└── README.md
```

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/Student-Management-VS-4.git
```

2. Open the project folder.

```bash
cd Student-Management-VS-4
```

3. Run the program.

```bash
python main.py
```

## Sample Menu

```
Welcome to Student Management System

1. Add New Student
2. Show All Student
3. Search Student
4. Delete Student
5. Update Student
6. Exit
```

## Data Format

Student information is stored in `student.json`.

Example:

```json
[
    {
        "name": "Sabrin",
        "id": "101",
        "section": "A"
    }
]
```

## Author

**Sabrin Nahar**
