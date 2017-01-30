Extract joor.zip.
Navigate to “joor” folder. Make sure you are inside “joor” folder. You are good to go now.

Creating Virtual ENV: Create Virtual environment using command below
	virtualenv <ENV-NAME>

Activating Environment: Activate newly created environment using command below
	source <ENV-NAME>/bin/activate

Installing Required Packages: Execute below command to install required packages in newly created environment.
	pip install –r <REQ-PACKAGES>

Run Server: To run the development server for this project execute below command.
	python manage.py runserver

Testing Using CURL: Run following curl commands [make sure server is running]

Creating Database Entries: To create DB entries execute below command after running the server.
	curl -X POST http://127.0.0.1:8000/api/ -d '{"long_url":"<LONG-URL-VALUE>"}' -H "Content-Type: application/json"

Checking API Results: Execute below command on terminal to see List of Short Urls.
	curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://127.0.0.1:8000/api/

Checking URL Redirection: Copy any Url from list and paste in browser url bar to test
	Example : http://127.0.0.1:8000/api/931b

Testing Using Python TestCases: Run following command to test [make sure server is running]
	python TestCases.py

VARIABLES: Below are the variables used in above instructions:
	<ENV-NAME>: This will be the virtual environment name. It can be any name like env, new_env, myenv etc.
	<REQ-PACKAGES>:  This is the file name contains all the packages required for this project. In this case it will be “requirements.txt”.
	<LONG-URL-VALUE>: Is the URL you want to shorten. It could be any URL of any length.