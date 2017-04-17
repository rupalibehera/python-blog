# python-blog
A simple blog application using python's web.py framework.

The blog is stored in MySQL database.

### Running the app locally
- Instal MySQL database server on your machine and create database blog
- clone the repository
- install all the requirements by `pip install -r requirements.txt`
- start the application with the following command `python blog.py`
- open your brower and you will see your blog application running on http://localhost:8080

### Running the app on openshift
- Clone the repository
- login to openshift using `oc login` on your terminal
- create a new project, for eg : foo using `oc new-project foo`
- create the application on openshift using `oc new-app -f ~/python-blog/openshiftpython-mysql-template.yaml -p NAMESPACE=foo`
- check the status of the app using `oc status`
- Open the openshift console you will see two services comming up one for the database and other for the pyhton blog app. Click on
  the route to check if the application is deployed.
