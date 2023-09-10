# Code_Stego
- Code_Stego implements a Steganography algorithm to save source code into Image of
the styled code snippet.
- Code_Stego is the project made by The Magic Methods team, for Python Discord Code Jam 2023

A Code_Stego Demo Website: [Code_Stego](https://codestego.up.railway.app/).

Invite our Discord Bot to your server : [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=1148263715771273278&permissions=0&scope=bot)

## Features
Your code snippet can be shared anywhere, and the image would contain the source code within itself. This would be a lot of help for others, and save them a lot of time, if they want to retype the code by themselves.

## Implementations
This project has 3 implementations within it:
- A Python Module
- Django website
- A Discord Bot






## Installation Guide 1 ( Using Docker )

### Prerequisites

Before you begin, ensure you have met the following requirements:

- [Docker](https://www.docker.com/) installed on your system.

## Installation

Steps To install and run Codestego's Website , follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/StoneSteel27/The-Magic-Methods.git
   ```
2. Change your working directory to the project's django-files folder:
   ```shell
   cd The-Magic-Methods
   cd django-files
   ```
3. Build the Docker image for Codestego:
   ```shell
   docker build -t codestego .
   ```
4. Run Codestego as a Docker container in detached mode, mapping port 8000 on your local machine to port 8000 in the container:
   ```shell
   docker run -d -p 8000:8000 codestego
   ```

5. Access Codestego in your web browser by navigating to  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Installation Guide 2 ( Using python )

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.11 installed on your system.

## Installation

Steps To install and run Codestego's Website , follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/StoneSteel27/The-Magic-Methods.git
   ```
2. Change your working directory to the project's django-files folder:
   ```shell
   cd The-Magic-Methods
   cd django-files
   ```
3. Install the required Python packages using pip:
   ( it is recommended to do `pip install` inside a virtual environment. )
   ```shell
   pip install -r requirements.txt
   ```
5. Run the Django development server:
   ```shell
   python manage.py runserver
   ```

6. Access Codestego in your web browser by navigating to  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## The Magic Methods Team
- [MoltenSteel](https://github.com/StoneSteel27) - Team Leader
- [FusionX](https://github.com/venkat66)
- [hsp](https://github.com/ShakyaMajumdar)
- [ilovetensor](https://github.com/ilovetensor)
- [koushireo](https://github.com/FooChiHen)
