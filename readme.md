# Personal Assistant

This is a Python project made to speed up the morning routine.

It will send you an email with all the necessary data to start the day, such as temperatures, rain probability (tbi), the scheduled activity or the meal planing.
This project is made by using OpenWeatherMap and Sheety.


## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See [Deployment section](#deployment)
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build this project
- Get an account from [OpenWeatherMap](https://www.openweathermap.org)
- Get an account from [Sheety](https://sheety.co/)
- Make a copy in your own Google Drive of [this Spreadsheet](https://docs.google.com/spreadsheets/d/1BtHEZ10FjPA-PPHx71EJEYV9mdJ_VHqWlYaPGSxFtWk/edit?usp=sharing)
- Link your Sheety Account to your Google Account and create a new project with the Spreadsheet that you copied. Make sure the linked account to Sheety is the owner of the Spreadsheet, or it won't work properly.

### Installing

You can set a local script by following these steps:


    1. Fill the .env file with your own credentials

    2. Get your latitude and longitude from Google Maps or another website and write it into the .env
    
    3. Run the script. If everything is okay, it should send you an email to the one you provided in the enviroment file.



#### Demo

<img title="a title" alt="Alt text" src="/images/email_demo_PA_EN.png">


## Deployment

There are several ways to deploy this script daily, I have used:

   - By using a Raspberry Pi server using cron [Tutorial from bc-robotics](https://bc-robotics.com/tutorials/setting-cron-job-raspberry-pi/)
   - By using [PythonAnywhere](https://help.pythonanywhere.com/pages/ScheduledTasks/)


## Built With

  - [Jakub Petriska Quotes](https://gist.github.com/JakubPetriska/060958fd744ca34f099e947cd080b540) - Used
    for the Quote List
  - [PurpleBooth: A Good Readme Template](https://github.com/PurpleBooth/a-good-readme-template) - Used for the readme template


## Authors

  - **Sheila Martinez** - *Created this project* -
    [SheiMG](https://github.com/sheiMG)

## License

This project is licensed under the MIT License. See [license.md](license.md) file for more
details.

