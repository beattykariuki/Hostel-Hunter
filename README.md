# Hostel Hunter

## Authors
### *Kevin Musoni*, *Betty Kariuki*, *Stacey Chebet*, *Gloria Givondo* (29/11/2018)

## Description 
Hostel Hunter is an application that university students can use to search for and find accommodation near their university. The user is able to rate these hostels by providing reviews.

You can view the live link on: 

## User Stories 
These are the behaviours that the application implenents for use by a user.

As a user, I would like: 

* To search a university.
* To leave a review to a hostel.
* To view hostels under searched universities.
* To see the hostel's offered services.
* To sign-up and log-in.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display all categories | **On page load** | List of various categiroes is displayed on landing page |
| Display pitch from a pitch category | **Click on category** | Redirected to a page with a list of pitches from the category |
| Display the pitch | **On page load** | Each pitch displays the title, content, posted by, on |
| Comment the pitch | **Comment** | Redirected to the sign-in page |
|Profile| **On page load**|The logged in user is able to view their profile-pic, bio, pitches posted and edit their profile|
| Edit profile | **Edit profile** | Redirects the user to a page to update their bio and upload a profile-pic|

## Setup / Installation Requirements
* Web browser
* Virtual environment
* Flask
* Python version 3.6


### Cloning the Repo
* In your terminal run:

        $ git clone https://github.com/beattykariuki/Hostel-Hunter.git
        $ cd Hostel-Hunter

## Running the Application 
* Create the virtual environment

        $ sudo apt-get install python3.6 -venv
        $ python3.6 -m venv virtual

* Activate virtual environment

        $ source virtual/bin/activate

* Install Flask and other Modules

        $ pip install -r requirements.txt

* Set up the environment variables
        
Create a start.sh file and paste the following.
`export SECRET_KEY='<secret_key>'`
`export MAIL_USERNAME='<username>'`
`export MAIL_PASSWORD='<password>'`

* Run the application in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application 
* To run the tests for the class files and check if they function well:

        $ python3.6 manage.py tests

## Technologies Used
* Virtual environment
* Flask
* Python version 3.6
* Flask-Bootstrap4
* Pip
* HTML
* CSS
* Heroku
* Visual Studio Editor

## Known Bugs
There are no known bugs. Contact bettykariuki026@gmail.comin-case of any bugs.

## License
The content of this site is license under the MIT license
Copyright (c) 2018 **Kevine, Betty, Stacey, Gloria**
