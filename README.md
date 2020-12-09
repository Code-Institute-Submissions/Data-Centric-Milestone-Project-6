# OCX Heaven

This Project is my third milestone examination project while studying with the Code Institute, in the Modules
for 'Data-Centric Development' As you can see, I have h=named the site "OCX Heaven" taking inspiring from both
my own and my daughters love of writing, the title itself being a combination of Orignal, Character,
Express and Heaven. Implying that a user may visit the site to find an abundance of orignal character ideas,
and find new inspiration for their own projects.
 
## UX

When designing the website, the intention was to create a sleek easy to use platform for individuals who enjoy creative writing, with a particular focus on the sub category of young writers who like to create their own "OCs" (Original Characters) hence OCX Heaven (the X in the name, standing for express, though I believe that to be a moot point). My  thoughts were to use a basic white background as that is standard for most sites coupled with a nice friendly purple colour for the navbar and opter elements such as buttons that link to pages on the site, other than green for submitting information to a form. nd then of course simple clear black writing.

Wireframes can be found here: [Wireframe01](https://github.com/phillpearsondev/Data-Centric-Milestone-Project/blob/master/wireframes/wireframe01.jpg?raw=true) [Wireframe02](https://github.com/phillpearsondev/Data-Centric-Milestone-Project/blob/master/wireframes/wireframe02.jpg?raw=true) [Wireframe03](https://github.com/phillpearsondev/Data-Centric-Milestone-Project/blob/master/wireframes/wireframe03.jpg?raw=true)

### User Stories

- As an OC enthusiast, I want to be able to quickly create a character using a simple template that I can edit or delete later.
- As a web user, I'm used to entering account details in order to gain access to user specific information hosted through the site.
- As a Mobile user, I'm used to websites having a responsive design so the site can be easily viewed and used via a mobile device.

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
- A full page template view of each chracter profiles, which can allow the user many more options, such as viewing a gallery of multiple images for their characters. Or add, edit and delete other details through the use of texat boxes otherwise unavailable in the standard character creation form.
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
