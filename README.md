# Bookyway Scheduler

This project automates the process of booking lessons on the Bookyway app using Selenium WebDriver. The automation script is written in Python and uses pytest for testing.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Requirements

- **Python 3.x**
- **Google Chrome browser**
- **ChromeDriver**

### Python packages (as listed in `requirements.txt`):
- `chromedriver-py==125.0.6422.141`
- `GitPython==3.1.42`
- `node==1.2.2`
- `pytest==8.2.1`
- `pytest-html==4.1.1`
- `pytest-metadata==3.1.1`
- `pytest-json-ctrf==0.2.3`
- `python-dotenv==1.0.1`
- `python-gitlab==3.15.0`
- `selenium==4.21.0`


## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/your-username/bookyway-scheduler.git
   cd bookyway-scheduler
2. **Install the required Python packages:**
   ```
   pip install -r requirements.txt
3. **Set up your environment variables:**
Create a .env file in the root directory of your project and add your Bookyway login credentials:
   ```
   EMAIL=your_email@example.com
   PASSWORD=your_password
4. **Download and install ChromeDriver:**

- Ensure that the version of ChromeDriver matches your version of Google Chrome.
- Download ChromeDriver

## Usage
To run the test, use the following command:
   ```
   pytest skip_burpees.py
