# OCX Heaven

This Project is my third milestone examination project while studying with the Code Institute, in the Modules
for 'Data-Centric Development' As you can see, I have h=named the site "OCX Heaven" taking inspiring from both
my own and my daughters love of writing, the title itself being a combination of Orignal, Character,
Express and Heaven. Implying that a user may visit the site to find an abundance of orignal character ideas,
and find new inspiration for their own projects.
 
## UX

When designing the website, the intention was to create a sleek easy to use platform for individuals who enjoy creative writing, with a particular focus on the sub category of young writers who like to create their own "OCs" (Original Characters) hence OCX Heaven (the X in the name, standing for express, though I believe that to be a moot point). My  thoughts were to use a basic white background as that is standard for most sites coupled with a nice friendly purple colour for the navbar and opter elements such as buttons that link to pages on the site, other than green for submitting information to a form. nd then of course simple clear black writing.

Wireframes can be found here: [Wireframe01](https://github.com/phillpearsondev/Data-Centric-Milestone-Project/blob/master/wireframes/wireframe01.jpg?raw=true) [Wireframe02](https://github.com/phillpearsondev/Data-Centric-Milestone-Project/blob/master/wireframes/wireframe02.jpg?raw=true) [Wireframe03](https://github.com/phillpearsondev/Data-Centric-Milestone-Project/blob/master/wireframes/wireframe03.jpg?raw=true)

Wireframes can also be found in the main GitHub directory under the folder named "wireframes".

#### Login/Register

For the account registration functionallity, I wanted to keep everything very simple and clean looking, while also adhereing to the base aesthetic of purple and white for the overall site. And so the login and register screen are effectively the same base-level code, where the template is an extension of the base.html, and injects its form and css into that template allowing for much more than just a Navbar. The difference lies in the app.py file, where where the forms are submitted, the login.html template will "GET" user information such as hashed passwords, generated using werkzeug, and the username stored with that hashed password. Whereas the register.html form will "POST" a dict, based off of key value pairs, bareing the same name as the html elements, under the attribute 'name="app-demonstration-name"' for example (it is labelled this way so python can read it properly). Then that grabbed information is stored in the database. Hosted by [MongoDB](https://www.mongodb.com/)

Relevent wireframe: [Login/Register](https://github.com/phillpearsondev/Data-Centric-Milestone-Project/blob/master/wireframes/wireframe02.jpg?raw=true)

#### Home Page

This was actually the very last thing that was built, and was not wireframed ahead of time. By this point in the project I had a very good idea about how the overall projet and the design was shaping up, and based off of the Thorin and Company miniproject, I thought having a banner image under the navbar with the site brand name across it would be a good design design choice. Then I created tow simple extra features to fill up the content on the page, taking more of an advertising approach where, the features would simply be blurbs floating from the left adn the right side of the page, telling the user in very brief terms what you could do on the app, and providing a centred button linking to the html template that the feature reflected, following the same purple aesthetic.

#### Characters on the site

For this I had a really basic idea based off what I knew could be done utilizing the materialize lightweight framework. the idea like described in the section above with the login/register templates, was to inject the template code into the base.html template by using the Jinja templating language to extend the code. I knew I wanted to have effectively a list of characters in the MongoDB database to display in their own special card-panel (a class created in the materialize framework) in a fairly light grey colour, which would then display fairly rudimentary information about the characters a user could create based off of typical character profiling templates that writers would use to plan their stories, many of which can be found online with varying degrees of complexity and depth. But until this point I havnt seen a website, do a web app version of this template.

Relevent wireframe: [Characters.html](https://github.com/phillpearsondev/Data-Centric-Milestone-Project/blob/master/wireframes/wireframe01.jpg?raw=true)

#### Create/Edit/Delete... Characters

Create and edit templates are like the login/register templates are almost clones of eachother, though of course with the create.html template in app.py will "POST" information to the database once its complet and only "GET" the user information from a session coookie stored in the users browser cache so you could tag the chracter with the username of the user who authored that particular creation. Again, as with every page, using this uses Jinja templating to inject the code into the base.html file then in app.py, when a character is posted, based once again off the html attribute 'name="example-name"' so python knows what to use, then storing that information in a dict to store on MongoDB. For the edit_character.html template file however, to edit existing characters, it was required to grab the object_ID information from the database so the browser knows exactly what dataset the user are editing before effectively repeating the process used in the create.html page process.

An extra 'Exception handling' esque feature I added here, using the Jinja templating in the html templates was that, if the username stored in the session cookie in the users browsers cache was the same as the authored_by key value pair stored in the database, then only that username could see the buttons appear on the appropriate characters card panel, displaying "Edit" in green and "Delete" in red on the page. Then once "Edit" button is clicked, the app.py file "GET"s the Object_ID for the characters card-panel, (as each card panel is already iterated over per entry character entry in the database) then that character information, including image url, traits, talents etc would be displayed on the character screen and stored for being posted once again in a dict back into the database, overwriting the previous entry of that Object_ID. For the Delete button, the app.py file also grabs the Object_ID for that particular character entry, but will simply delete the entry, flash a message to the screen and route back to the characters.html page. Ideally I would expand this will perhaps an alert box to confirm the change just incase a user mis-clicks.

Relevant wireframe: [create.html](https://github.com/phillpearsondev/Data-Centric-Milestone-Project/blob/master/wireframes/wireframe03.jpg?raw=true)

#### Logout

Is very simple, where the app.py file will remove the current session cookie from the user web browser. And any user specific data can no longer be menipulated by the user. The user will then need to login in again to edit or delete any entries in the characters.html page. Or even see the create, or logout options in the navbar. Also as a final note, once a user has registered or logged in and been routed back to the home page, in roughly the centre-right part of the PC screen-size a "Logged in as {username}!" message will appear in white, then will dissapear once the user logs out.

### User Stories

- As an OC enthusiast, I want to be able to quickly create a character using a simple template that I can edit or delete later.
- As a web user, I'm used to entering account details in order to gain access to user specific information hosted through the site.
- As a Mobile user, I'm used to websites having a responsive design so the site can be easily viewed and used via a mobile device.
- As a web user, I want to know that I'm actually logged in, and I can do things on the site that are exclusive to me.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features
 
### Existing Features
- OCX Heaven Home Page, to greet users as their first point of contact for the site, and point them in the direction of login or account registration.
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

- Messenger or chat popup feature, so members can communicate and collaborate on projects together.
- A full page template view of each character profiles, which can allow the user many more options, such as viewing a gallery of multiple images for their characters. Or add, edit and delete other details through the use of texat boxes otherwise unavailable in the standard character creation form.
- A sidebar nav allowing users to select and query chracters by genre, such as sci-fi, fantasty etc.
- a search bar in order for users to query specific characters or genres of characters, or even those made by specific usernames. Held in the characters template page.
- A User specific profile page, allowing users to upload their own display pictures, post their creative writing efforts, and the abillity to add comments to each post by themselves or other users.
- A forum, containing sub-forums, where users can create their own posts, show stories, discusss characters or other creative writing endeavours. This should also include a search bar so users can query specific forum entries, or usernames that created the posts.
- A "forgot my password" option for users who have lost their passwords, and wish to regain access to their profiles.

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
- [GitHub Desktop](https://desktop.github.com/)
    - The main method I used to upload all my 'git commits' up to GitHub.com
- [MongoDB](https://www.mongodb.com/)
    - The database hosting platform used to store all the key, value pairs of information used in the project.

## Testing

In order to test the code locally, I used the terminal command below.
- python -m flask run

## Deployment

To run the code locally on my own machine, I used the terminal command below then clicking on the link provided in the terminal
- python -m flask run

I acknowledge however that this is not the industry standard way to run the project, as it was not able to work on my machine in the standard way shown below.
- python3 app.py

### Host on GitHub

- First you must create a git repository by using "git init" in the terminal window in your chosen IDE.
- Before going any further you will need to create a Procfile with this command in the terminal window: "echo web: python app.py > Procfile".
- Then do exactly the same with the requirements.txt (which tells herohu which dependencies it will need to install in order to run your app. In the terminal window type this command: "pip3 freeze --local > requirements.txt"
- Next you must use "git add -A" this will add anything untracked or modified into the repository you just created.
- Use "git commit -m" followed by the "" marks in order to leave a comment in your git commit in order to 'save' to the git repository locally on your machine.
- I used [Github desktop](https://desktop.github.com) app for this step. Load up the app, and ensure you are signed into you Github account via clicking on 'file' in the top left corner of the client screen. Then, scroll down to option and click on it, you should see the app asking for your Github credentials. sign in.
- Once you've done the above you should be all current repositories in the tab just under'file'. However, to add a new repo, click on 'file' then click on 'add local repository', this will allow you to select a local folder which is the directory for the git repo you created using "git init". Add it buy clicking "Add Repository".
- Giving the app a few seconds to buffer, you should now see in the client window that you have 'local commit' that you can 'push' to Github. click and of these 'push' buttons either at the top of the screen or centre to begin.
- Your git repo will now be available on Github under repositories.

### Heroku Deployment

- Now that you have your project hosted on Github. Ensure you are logged in to your [Heroku](https://heroku.com) account.
- Ensure you are in the apps page by clicking the Heroku brand logo in the top left corner of the screen.
- Then click the "New" button in the top right corner of the screen, then several options will appear. click "create new app".
- Once the page has loaded, give your app a unique name (that another user hasn't already used) and seleect the server region in the box just below. Once you've done that, click on the purple "create app" button just below".
- After creating the app, a new page will load, near the top of the dashboard, scroll along and click on "settings" and at the bottom of the screen you will "reveal config variables", click the button, and copy and pastet each of the variables from your "env.py" file without "" into each key, value pairs. once added, siply navigate away from the page, they are saved.
- Be sure to use DEBUG as a Key, and a blank "" as the value, so Heroku knows to switch debug off for the purposes of deploying the website. Otherwise the app will crash.
- Go back to the "Deploy" option allow the same option bar you found "Settings". Click on it. Then in the centre of the page that loads you should see, an option in the middle, displaying the Gituhub logo, saying "connect to github", since I have hosted my projects code via Github I chose this.
- You may need to give your github login credentials, but once thas done scroll the whole page down a little bit, then in the box search for the repository you wish to link to heroku.
- Onced connected, its a siple matter of scrolling the whole page down until you see the "deploy branch" button in dark grey. Provided you created your Procfile and its in your git repository, Heroku will detect python, and the type of app you are building, in this case a web app. and will install then deploy the project based on your requirements.txt
- You should now be able to view your deployed app via the purple "Open app" button in the top right corner of the screen.

## Credits

### Media
- The images stored in any of the character profiles were obtained via copying the URL via google.com search.

### Acknowledgements

- I received inspiration for this project from both my own and my daughters interest in creative writing.
- Much of the code in the DOM and app.py were inspired by the Task Manager mini-project as taught by Code Institute.
- Many custom classes and HTML code were taken and altered from the Materialize frameworks website.
