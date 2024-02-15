# Python Development Template
A generic template for Python projects.

## Features
- Hosts a full Python project (contained in `src` folder).
- Enables the ability to run a Python project in specific "Run Modes"
- Use the `run.bat` alias file for Windows platform.
    - Enter `run <run-code>` in the Command Line, where `run-code` is code of the Run Mode that you want to run (see [Run Modes](#run-modes))
- Currently supported Run Modes:
    - Development
    - Production
    - Test
    - Documentation
    - Build

### Future Features
- Tkinter GUI support (MVC Framework)
- Default SQLite Database support
- Logging
- Deployment Options to Executable
- Testing

## How to Use
Add an alias called `run` to your terminal that runs `run.py` in the current working directory, along with any arguments you pass into it.

For example, the `run.bat` file contains the script `run.py $*` which is meant to run the `run.py` file in the root of this project along with any parameters passed into the script (in Windows Command Prompt).

Alternatively, you can manually run `run.py 0|1|2|...` at the root directory of this project.

Generally, the steps are:
1. Write your application in the `src` directory.
2. Use the `main.py` file to launch the application.
3. Run the application in a specific [Run Mode](#run-modes) using the `run.py` file.

## Run Modes

The following run modes are available. The examples are given assuming you are running the program using the alias `run`.

Replace `run` with `run.py` if you're not using the alias.

1. Development
    - Runs the project in development mode.
    - `run 0` or `run dev`
2. Production
    - Runs the project in production mode.
    - `run 1` or `run prod`
3. Test
    - Runs the project in test mode.
    - `run 2` or `run test`
4. Documentation
    - Runs `mkdocs build` with parameters specified in `constants.py`.
    - `run 3` or `run docs`
5. Build
    - Responsible for creating an `.exe` and implementing version control.
    - `run 4` or `run build`
