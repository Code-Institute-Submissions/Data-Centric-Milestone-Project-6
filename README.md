# OCX Heaven

This Project is my third milestone examination project while studying with the Code Institute, in the Modules
for 'Data-Centric Development' As you can see, I have h=named the site "OCX Heaven" taking inspiring from both
my own and my daughters love of writing, the title itself being a combination of Orignal, Character,
Express and Heaven. Implying that a user may visit the site to find an abundance of orignal character ideas,
and find new inspiration for their own projects.
 
## UX

## Features
 
### Existing Features
- OCX Heaven Navbar - Available in responsive design, allows the user to navigate the different pages on the app. in mobile view, the navbar is compressed into an easy to recognise, industry standard icon.
- User Account Registration - This allows users to create their own usernames and passwords for use in exclusive capacity on the app.
- User Log In - This allows users to Log in with their unique user credentials, and menipulate features exclusive to their particular session cookies stored in cache memory.
- Logout - This Allows the user to remove the session cookie from the cache in their browsers memory, and potentially log in with a different username.
- "Logged in as..." - In the top right corner of the page is displayed an easy to read message denoting the username that is currently signed in based on the presence of a session cookie in the users browsers cached memory.
- "Characters" Page - displaying all original characters currently stored via MongoDB, displayed in a grey box, using Materializes custom card panel, character details on the left, image on the right and an edit and delete button at the bottom of each panel which only displays when the user who authored that particular character profile is logged in.
- "Edit" - Only accessible once clicked on from the Characters page, retrieve the Object ID from MongoDB, and allows the user to edit their own character profile and update the data stored in the database. This consist of a collection of forms in much the same format as the create page (see below), complete with a green submit, and a red cancel button (in case the user decides to edit nothin).
- "Cancel" -  only accessible via the "Edit" page, when clicked by a user will redirect back to the "Characters" page.
- "Create" Page -  This is only visible to a logged in user with a cached session cookie in their Browser. This consists of a form containing several text input fields and selection menus, with predefined options which a user can use to craft their original characters profiles, including assigning talents, traits, title, name, gender, age and rank. The "Create" button allows the user to submit the new dataset to MongoDB and be displayed to the main "Characters" page.

### Features Left to Implement
- Another feature idea

## Technologies Used

- [Python 3.8.5](https://www.python.org/)
    - The main base language used in the env.py and the app.py file to build the back-end of the project, providing routing via @app.route commands, and additional functionallity, such as session cookies.
- [HTML](https://html.spec.whatwg.org/)
    - The language used to build the DOM, and add custom classes allowing for styling.
- [CSS](https://www.codecademy.com/learn/learn-css)
    - The language used to create custom styling to elements within the DOM bases on class and ID names and indivual element assignments.
- [Jinja](https://jinja.palletsprojects.com/)
    - The templating language used to add custom elements to the individual page templates in the DOM, including allow one template to inject code into another template. such as how all Navbar elements are contained within "base.html" and all other templates such as "create.html" will use Jinja templating to extend the base code.
- [JQuery](https://jquery.com)
    - The scripts.js file uses JQuery to initialize certain elements used from the Materialize Framework, such as the mobile navbar, or the multiple select options.
- [Fontawesome](https://fontawesome.com/)
    - The icon classes used in the project were utilized using Fontawesomes custom classes and CDN.
- [Materialize](https://materializecss.com/)
    - A light-weight alternative to Bootstrap, used to simplify the process of build the HTML and CSS elements, using Materializes custom templates and classes.
- [Flask](https://flask.palletsprojects.com/)
    - The main Framework used to build the app.

## Testing

## Deployment

To run the code locally on my own machine, I used the terminal command below then clicking on the link provided in the terminal
- python -m flask run

I acknowledge however that this is not the industry standard way to run the project, as it was not able to work on my machine in the standard way shown below.
- python3 app.py


## Credits

### Media
- The images stored in any of the character profiles were obtained via copying the URL via google.com search.

### Acknowledgements

- I received inspiration for this project from both my own and my daughters interest in creative writing.
- Much of the code in the DOM and app.py were inspired by the Task Manager mini-project as taught by Code Institute.
- Many custom classes and HTML code were taken and altered from the Materialize frameworks website.
