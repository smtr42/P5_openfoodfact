
<h1 align="center">
  Project 5 - OpenfoodFact
</h1>

<p align="center">
  <a href="">
    <img src="https://upload.wikimedia.org/wikipedia/fr/0/0d/Logo_OpenClassrooms.png" alt="Logo" width="100" height="100">
  </a>
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.7-green.svg">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg">
  </a>
  <a href="https://www.linkedin.com/in/teiva-s/">
    <img src="https://img.shields.io/badge/linkedin-Simonnet-blue.svg">
  </a>
</p>



  <h3 align="center">Use OpenFoodFacts data</h3>

 <p align="center">
    A Openclassrooms practical case where you use OpenFoodFacts to find alternatives to lesser nutritious food.
    <br />
  </p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Contact](#contact)

<!-- ABOUT THE PROJECT -->
## About The Project

<p align="center">
  <a href="https://fr.openfoodfacts.org/">
    <img src="https://static.openfoodfacts.org/images/misc/openfoodfacts-logo-fr-178x150.png">
  </a>
</p>

OpenFoodFacts is a database fed by volunteers in order to map the food and its ingredients. It's available under the Open Database License.

The goal is to create an application so the user can find an healthier alternative to a specific food using OpenFoodFacts. It will specify what type of food and where to find it.

This project is the 5th assignment for the Python developer diploma from OpenClassrooms.
The goal is to learn about:
* RESTful APIs,
* Databases architecture and manipulation with MySQL as a start,
* Agile development,
* Doc Driven Development,
* Common good practices.

Personal challenges and technical choices :
* Use Requests: HTTP for Humans™,
* Use Records: SQL for Humans™,
* Make UML model of the database,
* Make a orm-like code structure,
* Use a Finite State Machine to navigate in the menu.

### Functionality

* Ability to find a reference in the OpenFoodFacts Database
* The user is able to use the terminal
* The search is made in a local Database
 
<!-- GETTING STARTED -->
## Getting Started

### Installation
I used Python 3.7.
I use pipenv to manage dependencies.

1. Clone the repo
```sh
git clone https://github.com/smtr42/P5_openfoodfact.git
```
2. Install required dependencies
```sh
pipenv install
```
### Database creation
The user must create himself the MySQL database. Open a MySQL Command Line Client.
```sql
CREATE DATABASE your-database-name CHARACTER SET 'utf8';
```

You must enter the name of the database in the file **configuration/constant.py** as well as your username and your password.


<!-- USAGE EXAMPLES -->
## Usage
Open a Command Line Interface and launch the main.py script with Python.
```shell script
python -m main
```
### Specifications

When prompted, answer the question by typing the appropriate number or letter.
For a first start you must download data from the API and reset the database. 
Here is an example of usage :
* Type "y" to donwload data
* Type "y" to reset the database
* Type "1" to search for food to substitute
* Select a category
* Select food
* Select healthy food
* You can either go back or save the food in the database for later use.
<br>

All along you can write "r" for going back, "q" to quit, "m" to go back to the first menu.

## Authors
Project Link: [https://github.com/smtr42/P5_openfoodfact]

* **Simonnet T** - *Initial work* - [smtr42](https://github.com/smtr42)
   
  <a href="https://www.linkedin.com/in/teiva-s/">
   <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Logo.svg.original.svg" alt="linkedin" width="200" height="54">
 </a>
<br>
