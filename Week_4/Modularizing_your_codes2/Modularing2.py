# Modularizing your Code 2
# 3. Python Modules
#  - What a module is (a .py file that can be reused)

#  - Importing built-in modules (math, random, datetime)

#  - Writing your own module (creating my_module.py and importing it)

#  - Aliasing modules (import numpy as np)

# **What is a Module?**

# - A module in Python is simply a file with .py extension that contains Python code (functions, variables, or classes) which can be reused in other programs.

# - Instead of writing the same code again and again, you can write it once in a module and then import it anywhere.


# - LEts think of a module as a toolbox. Each tool (function, variable, or class) can be taken out and used whenever needed, without rebuilding the tool from scratch.

# **Importing Built-in Modules**

# - Python already comes with many pre-built modules that you can use directly.
# - Some common examples are:

# - math -for mathematical operations

# - random - for generating random numbers

# - datetime - for working with dates and time.
# - etc.

# - To use built in modules, you have to load them into your environment, that is, `import` them.

# Different ways to import Modules

import math


# Lets put it to use

print(math.sqrt(9))    # 3.0
# - Note that you must specify the module name when calling a function within it.


# 1. import as an alias

import math as m
 
# lets put it to use

print(m.sqrt(25))    # 5.0

# - This shortens the module name, this is common with libraries like numpy, pandas, etc


# 3. Import specific functions or variables

from math import sqrt, pi

print(sqrt(36))   # 6.0
print(pi)         # 3.141592653589793

# -here you don't need the prefix 'math.' anymore

# **Writing Your Own Module**

# - step1: Create a folder. Name it my_module

# - step2: Create a file inside the folder. Name it first.py

# - step3: Create another file inside the same folder. Name it second.py

# - Step4: Create another file still inside the same folder. Name it main.py

# ### **4. Python Packages**

# - What a package is (a folder with __init__.py)

# - Installing and using third-party packages (pip install requests, import requests)

# - Organizing multiple modules into a package

# **What is a Package?**

# - A package in Python is a way to organize related modules together into a folder.

# - Inside this folder, there must be a special file called `__init__.py` (can be empty). This file tells Python that the folder should be treated as a package.

# - uhmm, let think of a package as a standard mechanic workshop, and each module is a different toolbox inside the workshop. The __init__.py file is like the label on the workshop telling passerbys that this is a mechanic workshop.

# *Do you understand?*

# **Third-Party Packages**

# - Python comes with some built-in modules, but you can also install extra packages created by others.

# These packages are stored in the Python Package Index (PyPI).

# We install them using pip (Python’s package manager) or conda a

# How to install Python Packages
# 1. Using pip
# - This is the most common method.
# - It installs packages from PyPI. It is the Python's central package repository.

# To work with it, you have to use it in your terminal

# ```
# pip install requests                # Install latest version

# pip install requests==2.28         # Install specific version

# pip install --upgrade requests     # Upgrade existing package

# pip uninstall requests             # Remove package
# ```

# Using uv 
# - This is the modern, super-fast package and project manager
# - IT is a RUST-based that unifies package installation, virtual environment and python version management into one fast, modern CLI.

# - To use uv

# ```
# # Run this command on your terminal depending on your OS

# # Recommended method: standalone installer
#  # macOS/Linux

# curl -LsSf https://astral.sh/uv/install.sh | sh

# # or

# # Windows

# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"  
# ```

# - After installation, verify version.

# ```
# uv --version
# ```

# - Using uv to install packages
# - But before it works you must have a workin `virtual environment` 

# ```
# uv add requests              # Install package and update project files

# uv pip install flask         # Works like pip but much faster

# uv remove requests           # Uninstall

# uv venv                      # Create a virtual environment automatically

# uv run script.py             # Run scripts in the managed environment

# ```

# Other package managers that you should try exploring
# | Method                            | Description                     | Best For                                 |
# | --------------------------------- | ------------------------------- | ---------------------------------------- |
# | `pip install ...`                 | Standard installation from PyPI | Most common and simple use case          |
# | `pip install -r requirements.txt` | Batch install from file         | Reproducible projects                    |
# | Virtualenv + `pip`                | Isolated environments           | Independent project setups               |
# | `conda install ...`               | Data science ecosystem          | Scientific and system-level dependencies |
# | Clone + `pip install .`           | Custom or non-PyPI packages     | Local development and experiments        |
# | `.whl install`                    | Prebuilt package install        | Faster installations                     |
# | `pip install -e .`                | Editable (development) install  | Active package development               |
# | `uv ...`                          | All-in-one modern manager       | Speed, simplicity, and full workflow     |

# Creating a Virtual Environment
# - What is a Virtual Environment?
# - A virtual environment (venv) is an isolated workspace where you can install and manage Python packages without affecting the global/system Python installation.

# - Each project can have its own dependencies, even if they conflict with other projects.

# - Why should you form the habit of always creating a Venv before starting a project?

#  - It keeps project dependencies separate.
#  - It prevents version conflicts.
#  - It makes collaboration easier (everyone uses the same environment).
#  - It is required in many production setups.

#**How to create a Virtual Environment**

#```
# Create a virtual environment
#python -m venv virtual_environment_name


# This will create a folder inside your working folder with the name "virtual_environment_name"
#```

#- To use it, you have to activate it.

#```
# 1. Click on the folder

# 2. Look for Script and open it.

# 3. Look for 'activate'

#4.  Right click on it and look for copy relative path

#5. Click on it.

#6.  Finally to your terminal and select Command prompt then paste the path you copied.
#```


#- Altenatively, you can use this script.

# ```
# virtual_environment_name\Scripts\activate  # For windows

#  source virtual_environment_name/bin/activate # linux or macOS
# ```

# **Deactivating a virtual Environment**

# ```
# deactivate
# ```

# **Saving and Sharing Requirements**


# ```

# To freeze the installed packages into a file
# pip freeze > requirements.txt


# To install them later

# pip install -r requirements.txt
# ```

# Creating Your Package

# ```
# my_project/
# │
# ├── my_package/              # Package folder
# │   ├── __init__.py          # Makes this folder a package
# │   ├── math_utils.py        # Module 1
# │   ├── string_utils.py      # Module 2
# │
# └── main.py                  # Script that uses the package

# ```

# **1.__init__.py **

# - This is a special file tells python that my_package is a package. It can be empty or used to initialize the package.

# 5. Code Reusability
# **What is Code Reusability?**

# - Code reusability means writing code once and using it multiple times instead of rewriting it.

# - It helps make programs cleaner, faster to develop, and easier to maintain.

# - In Python, code reusability is achieved using;

#     - Functions (reusing blocks of code)

#     - Modules (saving functions in .py files to import later)

#     - Packages (organizing modules in folders)

#     - Classes & Objects (OOP makes reusable blueprints)

#     - Libraries (built-in or third-party)


# 🔹 Why Reuse Code?

#     - Saves time – no need to rewrite the same logic.

#     - Avoids duplication – reduces errors from copy and paste.

#     - Improves readability – your code is modular and organized.

#     - Easy to maintain – update once, reuse everywhere.

# 6. Organizing a Python Project
 
#  - A modular project is a way of organizing your code into separate files and folders, each responsible for a specific task.

# - This makes the project easier to read, test, and maintain.

# **Why Use Modular Structure?**

# - Separates concerns – Each file has one responsibility.

# - Easier to debug – You can fix issues in one place without breaking others.

# - Reusability – Functions/modules can be reused in other projects.

# - Collaboration-friendly – Multiple developers can work on different parts.

# **Folder & File Structure**

# - Let’s say we want to build a Student Records Project.
# - We will first structure our folder and files like this.

# ```
# student_project/
# │
# ├── data.py        # Handles storing and retrieving student data
# ├── utils.py       # Contains helper functions (e.g., calculations, formatting)
# ├── main.py        # Entry point to run the project

# ```


# Let's try  a Bigger Project Structure
# As the project grow, we can organize into folders.

# Lets work on Library Management System

# - The goal of this project is to
#  - Manage books in a library
#  - Add books, list books, and borrow books.
#  - Organized into folders and files for modularity.

# Lets structure the folder and possible files

# ```

# library_project/
# │
# ├── data/                   # Handles storage & retrieval
# │   ├── __init__.py
# │   └── my_data.py
# │
# ├── utils/                  # Helper functions
# │   ├── __init__.py
# │   └── helpers.py
# │
# ├── services/               # Core business logic
# │   ├── __init__.py
# │   └── library.py
# │
# ├── main.py                 # Entry point of the program
# └── requirements.txt        # (optional) external dependencies
# ```


# Lets implement the project

# Lets make the scope of the implementation broader and interactive

# - Lets have our project structure


# ```
# library_project/
# │
# ├── data/
# │   └── my_data.py
# │
# ├── utils/
# │   └── helpers.py
# │
# ├── services/
# │   └── library.py
# │
# └── main.py
# ```

# Lets implement it

#