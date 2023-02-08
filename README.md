# Albums
A Django web app to store your favorite songs and albums in one place. 


# Installation 

## Prerequisite
* Python
* Django


## Setup the project locally
- Clone the repo.
    ```
    git clone https://github.com/BISHOPDAN/Album-Artist_music.git
    ```

- Create a virtual environment. Make sure you are not inside the repo when you create the virtual environment.
    ```
    python3 -m venv <your-venv-name>
    ```
 
- Activate the virtual environment. 
    ```
    source <your-venv-name>/bin/activate
    ```
 
- Go inside the repo folder. Now you should be inside a folder called Albums

- Install all the requirements
    ```
    pip3 install -r requirements.txt
    ```

- Create database tables.
    ```
    python manage.py migrate
    ```

- Run your program
    ```
    python manage.py runserver
    ```

# Contribution Guidelines

- Fork and star the repo
- Create your feature branch
    ```
    git checkout -b <feature-name>
    ```
- Commit your changes
    ```
    git commit -am "Meaningful commit message
    ```
- Push to the branch
    ```
    git push origin <feature-name>
    ```

- If you see any bug or you have a feature suggestion, create an issue.
- Start working on an issue only after it has been approved by the maintainers.
- Wait till the end of the day to get the reply on an issue or review of a PR.


## SLoP Maintainers
This project is a part of my internship project in Eccles IT Ltd United Kingdom Manchester Area.
maintained by:
- [Daniel Successful](https://github.com/BISHOPDAN)
