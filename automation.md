# Local Health News App

## Overview

The Local Health News app is a Flask web application designed to provide users with the latest health news based on their geographical location. Leveraging the IP address of the user, the app retrieves information such as time zone, country code, and region. It then fetches health news specific to the user's country using the News API.

## Features

### 1. Personalized Greeting and Time Information

Upon accessing the app, users are greeted with a personalized message based on the time of day (Good Morning, Good Afternoon, or Good Evening). The app also displays the current time and date in the user's local time zone.

### 2. Location Information

The app retrieves the user's IP address, region name, and country code using the IPinfo API. Additionally, a tooltip provides information about the user's approximate location based on their public IP address.

### 3. Health News Feed

The main feature of the app is the display of the latest health news relevant to the user's country. The app uses the News API to fetch top health headlines for the specified country. Each news article includes a title, publication date, description, and source information.

### 4. Responsive Design

The app utilizes a responsive design, making it accessible and user-friendly across various devices and screen sizes.

### 5. Footer Information

The footer includes a copyright notice and attribution to the app's creator with a link to their GitHub profile.

## Usage

To use the Local Health News app, follow these steps:

1. Clone the GitHub repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask app using `python app.py`.
4. Access the app in your web browser at `http://127.0.0.1:5000/`.

## Technologies Used

- **Flask**: A lightweight web application framework for Python.
- **HTML/CSS**: Used for structuring and styling the web pages.
- **JavaScript**: Notably used for the tooltip feature.
- **News API**: Provides access to real-time and historical news data.

## Dependencies

The app relies on the following external services and APIs:

- **IPinfo API**: Retrieves IP address and location information.
- **News API**: Fetches health news based on the user's country.

## Author & Acknowledgements

The Local Health News app was created by [Anukuga](https://github.com/Anukuga). Special thanks to the developers of IPinfo and News API for providing the necessary data for this application.
