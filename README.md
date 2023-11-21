# Final Project Template

The final project for this course has several steps that you must complete. 
To give you an overview of the whole project, all the high-level steps are listed below. 
The project is then divided into several smaller labs that give the detailed instructions for each step. 
You must complete all the labs to successfully complete the project.

## Project Breakdown

**Prework: Sign up for IBM Cloud account and create a Watson Natural language Understanding service**
1. Create an IBM cloud account if you don't have one already.
2. Create an instance of the Natural Language Understanding (NLU) service.

**Fork the project Github repository with a project then build and deploy the template project**
1. Fork the repository in your account
2. Clone the repository in the theia lab environment
3. Create static pages to finish the user stories
4. Deploy the application on IBM Cloud

**Add user management to the application**
1. Implement user management using the Django user authentication system.
2. Set up continuous integration and delivery

**Implement backend services**
1. Create cloud functions to manage dealers and reviews
2. Create Django models and views to manage car model and car make
3. Create Django proxy services and views to integrate dealers, reviews, and cars together
 
**Add dynamic pages with Django templates**
1. Create a page that shows all the dealers
2. Create a page that show reviews for a selected dealer
3. Create a page that let's the end user add a review for a selected dealer

**Containerize your application**
1. Add deployment artifacts to your application
2. Deploy your application



<!-- cd agfzb-CloudAppDevelopment_Capstone/server
Copied!
Install the necessary Python packages.

1
python3 -m pip install -U -r requirements.txt
Copied!
Perform migrations to create necessary tables.

1
python3 manage.py makemigrations
Copied!
Run migration to activate models for the app.

1
python3 manage.py migrate
Copied!
Start the local development server.

1
python3 manage.py runserver
Copied! -->
<!-- {
  "apikey": "NxWy7k28StaanOYWny2yd4D9LZ9MSjRLzDwM9PUnlxlL",
  "host": "27ec14ab-3525-4ea0-a860-3ec65d1ff1fd-bluemix.cloudantnosqldb.appdomain.cloud",
  "iam_apikey_description": "Auto-generated for key crn:v1:bluemix:public:cloudantnosqldb:eu-gb:a/804d94529145466eb7ab706096f0b8a9:ba9a0d0e-62a8-41c2-90a1-d62ee75eb324:resource-key:81e9937e-edf4-4457-a48f-95f554432c63",
  "iam_apikey_name": "Service credentials-1",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/804d94529145466eb7ab706096f0b8a9::serviceid:ServiceId-5be73579-7ab1-49c4-9b42-9557d17a248d",
  "url": "https://27ec14ab-3525-4ea0-a860-3ec65d1ff1fd-bluemix.cloudantnosqldb.appdomain.cloud",
  "username": "27ec14ab-3525-4ea0-a860-3ec65d1ff1fd-bluemix"
} -->


export IAM_API_KEY="NxWy7k28StaanOYWny2yd4D9LZ9MSjRLzDwM9PUnlxlL
export COUCH_URL="https://27ec14ab-3525-4ea0-a860-3ec65d1ff1fd-bluemix.cloudantnosqldb.appdomain.cloud"