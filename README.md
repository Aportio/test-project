# A simple Django test project

1. Prerequisites:

    * Python 3+ and `pip` installed and available.
    * A reasonably modern Linux as operating system, for example Ubuntu.
    * `sqlite` installed on the system.
    * Ability to create a Python virtual environment.

2. Install Python packages (ideally in a virtual environment):

    `$ pip install -r requirements.txt`

3. Change into the `test-project` directory.

4. Run the necessary migrations:

    `$ ./manage.py migrate`

5. Run the development server:

    `$ ./manage.py runserver`
