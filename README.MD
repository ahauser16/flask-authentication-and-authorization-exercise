# Flask Feedback Assignment

## Assignment Instructions

In this exercise, we’ll be creating an application that lets users **sign up** and **log in** to their own accounts. Once logged in, users can _add_ feedback, _edit_ their feedback, _delete_ their feedback, and _see a list_ of all feedback that they’ve given. Many of these routes should be protected, so that for example `user1` can’t edit a piece of feedback that `user2` created. (More on this below.)

### Part 0: Set up your environment

You know the drill. Make a venv, pip install all the things, put your code on GitHub, etc.

### Part 1: Create User Model

First, create a **_User_** model for SQLAlchemy. Put this in a **_models.py_** file.

It should have the following columns:

- **_username_** - a unique primary key that is no longer than 20 characters.
- **_password_** - a not-nullable column that is text
- **_email_** - a not-nullable column that is unique and no longer than 50 characters.
- **_first_name_** - a not-nullable column that is no longer than 30 characters.
- **_last_name_** - a not-nullable column that is no longer than 30 characters.

### Part 2: Make a Base Template

Add a base template with slots for the page title and content. Your other templates should use this.

You can use Bootstrap for this project, but don’t spend a lot of time worrying about styling — this is **not** a goal of this exercise.

### Part 3: Make Routes For Users

Make routes for the following:

- **GET */ :*** Redirect to /register.

- **GET */register :*** Show a form that when submitted will register/create a user. This form should accept a username, password, email, first_name, and last_name. Make sure you are using WTForms and that your password input hides the characters that the user is typing!

- **POST */register :*** Process the registration form by adding a new user. Then redirect to **_/secret_**

- **GET */login :*** Show a form that when submitted will login a user. This form should accept a username and a password. Make sure you are using WTForms and that your password input hides the characters that the user is typing!

- **POST */login :*** Process the login form, ensuring the user is authenticated and going to **_/secret_** if so.

- **GET */secret :*** Return the text “You made it!” (don’t worry, we’ll get rid of this soon)

### Part 4: Don’t let everyone go to `/secret`

Despite all of this wonderful password hashing that you have been doing, anyone can navigate to `***/secret***` and see the text “You made it!”. Let’s protect this route and make sure that only users who have logged in can access this route!

To do that, we’re going to make sure that when we log a user in (and after they register), we store just a little information in the session. When the user successfully registers or logs in, store the **_username_** in the session.

### Part 5: Log out users

Make routes for the following:

- **GET */logout :*** Clear any information from the session and redirect to *`/`*

### **Part 6: Let’s change *`/secret`* to *`/users/<username>`***

Now that we have some logging in and and logging out working. Let’s add some authorization! When a user logs in, take them to the following route:

- **GET */users/<username> :*** Display a template the shows information about that user (everything except for their password). You should ensure that only logged in users can access this page.

### Part 7: Give us some more feedback!

It’s time to add another model.

Create a **_Feedback_** model for SQLAlchemy. Put this in a **_models.py_** file.

It should have the following columns:

- **_id_** - a unique primary key that is an auto incrementing integer
- **_title_** - a not-nullable column that is at most 100 characters
- **_content_** - a not-nullable column that is text
- **_username_** - a foreign key that references the username column in the users table

### Part 8: Make/Modify Routes For Users and Feedback

**GET */users/<username> :*** Show information about the given user. Show all of the feedback that the user has given. For each piece of feedback, display with a link to a form to edit the feedback and a button to delete the feedback. Have a link that sends you to a form to add more feedback and a button to delete the user **Make sure that only the user who is logged in can successfully view this page.**

**POST */users/<username>/delete :*** Remove the user from the database and make sure to also delete all of their feedback. Clear any user information in the session and redirect to **_/_**. **Make sure that only the user who is logged in can successfully delete their account.**

**GET */users/<username>/feedback/add :*** Display a form to add feedback  **Make sure that only the user who is logged in can see this form.**

**POST */users/<username>/feedback/add :*** Add a new piece of feedback and redirect to /users/<username> — **Make sure that only the user who is logged in can successfully add feedback.**

**GET */feedback/<feedback-id>/update :*** Display a form to edit feedback — [\*\*](https://curric.springboard.com/software-engineering-career-track/default/exercises/flask-feedback/index.html#id1)Make sure that only the user who has written that feedback can see this form \*\*

**POST */feedback/<feedback-id>/update :*** Update a specific piece of feedback and redirect to /users/<username> — **Make sure that only the user who has written that feedback can update it.**

**POST */feedback/<feedback-id>/delete :*** Delete a specific piece of feedback and redirect to /users/<username> — **Make sure that only the user who has written that feedback can delete it.**

### Further Study

- Make sure your registration and authentication logic is being handled in your **_models.py_**
- Make sure that if there is already a **_username_** in the session, do not allow users to see the register or login forms
- Add a 404 page when a user or feedback can not be found as well as a 401 page when users are not authenticated or not authorized.
- Add a column to the users table called **_is_admin_** which is a boolean that defaults to false. If that user is an admin, they should be able to add, update and delete any feedback for any user as well as delete users.
- Make sure that if any of your form submissions fail, you display helpful error messages to the user about what went wrong.
- Tests! Having tests around authentication and authorization is a great way to save time compared to manually QA-ing your app.
- **Challenge:** Add functionality to reset a password. This will involve learning about sending emails (take a look at the Flask Mail module. You will need to use a transactional mail server to get this to work, gmail is an excellent option) and will require you to add a column to your users table to store a password reset token. **HINT** - here is how that data flow works:
  - A user clicks a link and is taken to a form to input their email
  - If their email exists, send them an email with a link and a unique token in the query string (take a look at the built in **_secrets_** module and the **_token_urlsafe_** function. You will create this unique token and store it in the database.
  - Once the user clicks on that link, take them to a form to reset their password (make sure that the unique token is valid before letting them access this form)
  - Once the form has been submitted, update the password in the database and delete the token created for that user

## Steps to create this project

I set up the project by following these steps:

1. `pip install -r requirements.txt`

2. to create a virtual environment named `venv` you can run this command:
   `python3 -m venv venv`

3. There is a virtual environment already set up for this project so you need to activate it:

`source venv/bin/activate`

4. In `Flask`, the `FLASK_APP` environment variable is used to specify how to load the application which can be set to a python file, a module, or a package. In this case, it's being set to the `app.py` file which is where my `Flask` application is defined. When you execute the command `flask run`, `Flask` uses the value of `FLASK_APP` to find my application and run it. If `FLASK_APP` is not set, `Flask` won't know where the application is and won't be able to run it. So before you run the application you must run the command:

`export FLASK_APP=app.py`

5. Now you can run the application with the debugger module activated using the command below, however, you should set up your `psql` database and configuration in `app.py` first.

`flask run --debugger`

6. NB --> I received an error message that was fixed by updating the `werkzeug` package to a version that is compatible with Python 3.10 by running the command `pip install --upgrade werkzeug`.

### configuring `.env` and `.gitignore`

1. I added `dotenv` to the project as a dependency [`pip install python-dotenv`] so that I could use environmental variables from my `.env` file. Consequently I created a `.gitignore` file and added `.env` and `venv` to it.

2. After installation I added the import statements below to the top of my `app.py` file.

```
import os
from dotenv import load_dotenv
```

3.  After ensuring the import statements are correct I refactored the code below to use the `os.getenv` method to reference the variables in my `.env` file.

```
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")  //-->refactored to reference the .env variables
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.getenv("DEBUG_SECRET_KEY")  //-->refactored to reference the .env variables
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
```

### PSQL Database Config

1. log into your `psql` account with `psql` (this automatically logs me into my only `psql` account but you may need to specific which account if you have more than one using `psql -U haus`).

2. run the command `CREATE DATABASE feedback_exercise;` to create your database.

3. I added the code below to ensure that the tables are created in the context of the Flask application. Adding this code below will create the `users` and `feedback` tables based on the models defined in the `models.py` file.

```
# Create all tables
with app.app_context():
    db.create_all()
```

## Flask Route Best Practices checklist

- [ ] Flash Messages for Feedback: Use flash messages to provide feedback to the user, especially for form validation errors or successful registration.
- [ ] Error Handling: Add error handling for potential issues, such as database errors or user registration conflicts.
- [ ] CSRF Protection: Ensure that CSRF protection is enabled and properly configured.
- [ ] Logging: Add logging to help with debugging and monitoring.
- [ ] Form Validation: Ensure that the form validation is comprehensive and secure.

## Testing with `unittest`

I created a folder in the root of my directory named `tests` to contain all my test files. Then I created a new file called `test_redirect.py` within this directory for my redirect tests.

### Running the Tests

To run the tests, navigate to the root of your project in the terminal and execute:
`python -m unittest discover -s tests`

This command will discover and run all the test files in the `tests` directory.

## Postman Notes - Collection Name: Flask Feedback Exercise

- ### registration & login folder
- ### feedback

### Postman Environmental Variables

I created a Postman environment called "flask feedback development" that contains the following variables:

- `base_url` set to `http://localhost:5000`
- `session_cookie` this is dynamically created by the `pre-request` script below:

```
pm.request.headers.add({
    key: 'Cookie',
    value: 'session={{session_cookie}}'
});
```

### Testing with Postman

To test the routes using Postman, you can create two separate requests. One for the homepage route **`/`** which redirects to the register route **`/register`**, and another for the register route itself. Here are the steps to create these requests:

#### Request 1: Test Homepage Redirect

1. Create a new GET request in Postman:

   - Method: `GET`
   - URL: `{{base_url}}/`

2. Follow Redirects:

   - Postman automatically follows redirects by default. Ensure that this setting is **disabled** in Postman otherwise the tests below will fail even when the tests and routes are set up correctly.

3. Send the Request:
   - Click the "Send" button to send the request.
   - Verify that the response is a redirect to `/register` by adding the following test scripts below:

```
pm.test("Status code is 302", function () {
    pm.response.to.have.status(302);
});

pm.test("Redirects to /register", function () {
    pm.response.to.have.header("Location", "/register");
});
```

4. Check for the Session Cookie
   - Go to the "Tests" tab in Postman.
   - Add the following test script to check if the session cookie is present:

```
pm.test("Session cookie is present", function () {
    var cookies = pm.cookies.toObject();
    pm.expect(cookies).to.have.property('session');
});
```

5. Extract the Session Cookie
   - Add a script to extract the session cookie and save it to an environment variable.
   - This will dynamically add the `session_cookie` variable to the Postman environment that I set up earlier (see `base_url` and `session_cookie` above)

```
pm.test("Extract session cookie", function () {
    var cookies = pm.cookies.toObject();
    if (cookies.session) {
        pm.environment.set("session_cookie", cookies.session);
    }
});
```

6. Use the Session Cookie in Subsequent Requests
   - For subsequent requests, ensure that the session cookie is included. You can do this by adding a **pre-request script** to set the cookie.

```
pm.request.headers.add({
    key: 'Cookie',
    value: 'session={{session_cookie}}'
});
```

#### THIS TEST DIDN'T PAN OUT

#### Request 2: Test Register Route

1. Create a new POST request in Postman:

   - Method: `POST`
   - URL: `{{base_url}}/register`

2. Set Headers:

   - Content-Type: `application/x-www-form-urlencoded`

3. Set Body Parameters:

   - Select the "Body" tab.
   - Choose the "x-www-form-urlencoded" option.
   - Add the following key-value pairs:
     - `username`: `<your-username>`
     - `password`: `<your-password>`
     - `first_name`: `<your-first-name>`
     - `last_name`: `<your-last-name>`
     - `email`: `<your-email>`

4. Send the Request:
   - Click the "Send" button to send the request.
   - Verify that the response redirects to `/users/<username>` if the registration is successful.
