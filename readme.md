# Movie Review Page

The goal of this site is to provide a movie review page where the user can search for any movie via the movie database and create a review for it.

## UX

### User Stories

#### User Goals

As a movie enthusiast,

- I want to be able to search for movies I am interested in.

- I want to be able to review movies I am interested in.

- I want to have a profile page where I can see my own reviews.

- I also want to be able to edit and delete my own reviews.

As a site owner, I want

- the users to be able to review movies.

- the users to be able to search for movies.

- to display the movies in an organized way that looks good for the users.

- to catch any errors and display them to the users in a better way.

- the users to register, login and logout from the page.

- the users to have a profile page where they can view their own reviews

- the users to be able to edit and delete their own reviews.

## User Requirements and Expectations

### Requirements

- The site needs to look good on all screen sizes.

- There needs to be a search function where the user can search for movies.

- There needs to be a authentication system.

- The users need to have their own profiles where they can view and edit their own reviews.

- Reviews from the database needs to be displayed under each movie but also on the user's profile.

### Expectations

- It needs to be easy to understand for the users how to navigate and use the page.

- The text should be easy to read.

- Search and database results should be displayed in rows.

## Features

- Authentication

Because the users are going to create and edit reviews there needs to be an authentication system. I took what I learned from the code along project at [school](https://codeinstitute.net/) and created my own in this project. The users can register, login, logout and view their profiles. This is the first part that the users will be exposed to, so it also needs to be made clear what the site is here.

- Home

Here the users can search for movies that will be displayed in cards and if they click on create, they will be redirected to the review page where they can create and view already existing reviews if there is any there.

Existing reviews will also be displayed on the home page and the user will also be redirected to the same review page if the user clicks on one of these.

- Review

This is where the users can view or create their own reviews. The movie information will also be displayed here but in a bigger format where an overview of what the movie is about will be displayed as well.

- Profile

Here I want the users to be able to view their reviews but also edit and delete them. I would also like for them to be able to change their password and delete their users, but this is something I might leave for future implementations.

- Error handling

This is something that my mentor Reuben Ferrante adviced me to implement at the start of the project and he showed me where I could read how to do it. I wrote one function for each error code at first, but Reuben showed me how I could do it with less repetition.

- Blueprints

I decided to use flask blueprints tke up the page in different parts.
I think that this makes the code a bit easier to follow and understand but it also allows me to in an easy way use for example the authentication part in another app in the future.

## Design Choices

I used figma to create my wireframes and while most things are exactly as I show in the wireframes there are a few things that I did change, and I will explain why here:

- I moved the edit and delete buttons so that they are displayed on the review page and on the profile page for the users. But only if the user created the post. This is so that only the user that made the post can edit or delete it.

- I also removed the star button; I did this because the movie database actually has a rating system built in and if I were going to use anything like that I would have used their built in one. But at the end I decided against both options and removed the function completely.

- Instead of just having the plus symbol I created a form where the users can search and add new movies. I felt that this way it looked a bit better and it was presented a bit more clearly to the user.

- I did not take the profile page into consideration when I created the wireframes so that is not shown there. I also added a link to the home page because of the profile and this changed the look of my navbar a bit.

## Wireframes

[Mobile Wireframe](https://github.com/Tommyshub/flask-movie-project/blob/main/static/assets/wireframes/mobile-wireframe-movie-app.fig)

[Mobile Wireframe Image](https://github.com/Tommyshub/flask-movie-project/blob/main/static/assets/wireframes/mobile.png)

[Desktop Wireframe](https://github.com/Tommyshub/flask-movie-project/blob/main/static/assets/wireframes/desktop-wireframe-movie-app.fig)

[Desktop Wireframe Image](https://github.com/Tommyshub/flask-movie-project/blob/main/static/assets/wireframes/desktop.png)

## Redesign

After getting feedback on this project and coming back to it I realized that my old design had a lot of flaws and I did not like how it looked.

I decided to change the colors and the layout and I also added a new home template and changed the old one to be movies instead.

## Future design

In the future there are two parts of my design I would like to improve. The home template is as of now a bit of an afterthought and I would like to figure out somethging better to display there in the future. The

I would also like to improve how the reviews are displayed at the profile and the review page.

## Technologies Used

### Languages

- [HTML](https://en.wikipedia.org/wiki/HTML)

- [CSS](https://en.wikipedia.org/wiki/CSS)

- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

### Tools & frameworks

- [Flask](<https://en.wikipedia.org/wiki/Flask_(web_framework)>)

- [Materialize CSS](https://materializecss.com/)

- [Git](https://git-scm.com/)

- [Google Fonts](https://fonts.google.com/)

## Testing

### Am I Respsonsive?

I used the Am I Responsive tool to check if my page is responsive. You can see the screenshot from that test below.

![Am I Respsonsive?](https://github.com/Tommyshub/flask-movie-project/blob/main/static/assets/responsive/responsive.png)

I also tested the page in both the Google Chrome and Firefox dev tools, checking different screen sizes.

I did notice that my navbar was not perfect on large screens so I fixed this by changing the push values from the materialize css framework.

### Forms

I had some serious issues with all of my forms not submitting and updating correctly. After doing some research on the issue I found that the forms should be redirected instead of rendering the template again in order for them to work correctly.

Changing this fixed the problems with all forms except for the search form.

The issue with my search form was quite a bit more complicated and the issue was related to either the api itself or the wrapper for the movie database api.

The problems was that I could not get the search results to clear when I accessed them directly from the api wrapper.

When trying to fix this I assigned the search results to a session instead, which worked okay but I realized that this limited the size of the response from the api and many search results did not work.

Because of this I decided to use server side sessions and at first I thought that I could use local storage for this, but this does not work with Heroku so I tried connecting it to mongodb and using the same database for my sessions.

This did not work good because the search results was slow and I experience many issues with the connection to mongodb. I

Instead I decided to use redis supplied by Heroku and this worked pretty good except for some random issues with the connection that I will explain how I solved below.

The problem was still not solved at this point, but I knew that I could fix it by simply popping search results cookie from the session when someone enters the movies page.

I also needed to set the actaul search fields to an empty string after submitting the form, which I did.

The old search results will still be the if the user just tries to reload the page, but it works as expected when leaving the page and coming back or when searching for a new movie.

If i tried to end the function on a redirect to fix this last issue it would trigger my workaround for popping the cookie and no search results would be displayed. So I decided that this is the best solution.

### Redis connection issues

I noticed that I was having some random connection issues with my redis connection. I googled the issue and found out that this was do to a bug that have been fixed by an update but I needed to add a health check interval option to my connection string.

I have not experienced the problem again after updating the connection string.

### Flask messages

I could not put my toast messages in the base template because of how my page was designed before and I thought that I had fixed this so they worked anyway but I noticed that they didn't after coming back to the project.

I was able to move all these messages to the base template because I had already decided to redesign the page.

After doing this I also gave them a new look with css classes for error, warning and info and I also wrote a function that closes them after 4000ms.

### Message if no movies are found

After fixing the issues with flask messages I added a message that notifies the user if no results can be found for their search query.

### Navigtion and layout issues

A big part of the reason that I decided to change my design was because of the issues with the navigation and layout of my page. I

My intent was to use the page that is now movies as my home view, but for some reason I used the base template.

To fix this and make it better I created a new home template that is rendered when entering the page and I renamed the old one to movies.

### Python formatting

I used the cornflakes linting extension for visual studio code in order to format my code according to the pep8 rules and I thought that this worked great but noticed after getting feedback that this does not work properly in some few cases. For example when some lines are too long.

I used [this](http://pep8online.com/) online validator on top of this to make sure that every line of code is correctly formatted and I also.

I had to manually fix a few lines that were too long and some other issues with the formatting but it should all be fixed now.

### HTML and jinja2 formatting

I have been using the prettier extension for visual studio to format my html but it did not work properly before for some reason.

I have changed computer since first starting this project and now it formats the code correctly, so I am gussing that I had some problems with the extension before.

I had to add comments in between the jinja2 code because the prettier extension does not handle that type of code.

There is one formatting error that I left there on purpose in the edit review template. It put a space in the form in the actual template if I put the correct formatting there so I decided to leave it as it is.

### HTML validation

I tried using online html validators to check my code but I could not find any that handled jinja2 and flask so I got a lot of errors because of that code. But as far as a can tell there was no issues with the actual html after coming back and fixing the old issues.

### Links

The error hanlder have worked as expected when manually trying to break links, except for in the review page for a specific movie.

It raises an exception if you change the movie id to something that does not exist and I need to wrap this part of the code in a try, except block.

I did not get this to work yet without partly breaking the search results for the api and this is the last part I need to figure out how to solve.

### Bandit -a tool designed to find common security issues in Python code.

[You can find out more about bandit here](https://github.com/PyCQA/bandit)

I used this automated tool to check if there were any security issues in my code. It reported on medium security issue and that is that I am binding to 0.0.0.0 in env.py and this can potentially open up a service to traffic on unintended interfaces.

This should be fine when deployed to Heroku and I did not change this setting.

### PyTest

[You can find out more about PyTest here](https://flask.palletsprojects.com/en/1.1.x/testing/)

I intented to to this as a last step but I did not have time for this unfortunately.

### Testing done after June 24th

- Once again checked all python files for pep8 errors but.

- Scanned the css file and added a missing colon.

- I scanned the html from the deployed html and found no errors. But since I knew there were some errors in my html I decided to scan the local files and check for errors not related to jinja code. I found one error in the movies.html that I fixed.

- Checked if the page is responsive with the Am I Responsive tool.

- Manually checked if the site is responsive to make sure pages like the search results that cannot be scanned with the Am I Responsive tool is oka as well.

## Deployment

### I created this site with vscode and git and pushed it to github where I published the site.

I performed the following steps in deploying my site:

### GitHub

- Pushed my commits from git to github.

- Logged in to my github account.

- Selected my repositories.

- Navigated to shopping-list.

- Clicked on settings.

- Scrolled down to where I can do the github pages settings.

- Selected the mastench from the dropdown menu.

- Clicked on save.

### Heroku

- Created a repository for this application

- Connected GitHub to Heroku under the "deploy" tab

- Clicked on deplonch

- Added my config variables in the settings / reveal config vars tab

You can [go here](https://flask-movie-project.herokuapp.com/) if you are interested in checking out my website.

### Local deployment

#### If you want to run my website locally you can download it from [here](https://github.com/Gretaah/milestone-project1/archive/master.zip) and follow these steps:

- Right click on the file and unzip it.

- Navigate to the unzipped folder.

- Rename dummy_env.py to env.py

- Navigate to the unzipped folder in your terminal and run pip install -r requirements.txt to install all required dependencies

- Open the env.py file in your editor in order to add the credentials you will need to run this website locally.

- Start by creating a MongoDB account [here](https://www.mongodb.com/)

- Create a new cluster in your new MongoDB account, you can call this cluster anything you want. You should also create a new collection that also can be named anything you want.

- In your new collection you need to create three entries: movies, reviews and users.

- Now navigate to clusters, connect, connect your application and choose your python version and copy the provided uri and add that to the MONGO_URI in the env.py file. You should also replace the password part with the password you used to sign-up to MongoDB.

- Add the name of your collection to the MONGO_DBNAME variable in the env.py file.

You will also need to get a Redis server to store sessions. I am using the one provided by Heroku in the deployed version but to get one to run this project locally you can either download and run it on your own server or get one that is hosted for you. I have linked to an article below with some suggestions on providers you can use.

- [Redis Server Providers](https://geekflare.com/redis-hosting-platform/)

- Add your redis credentials to the env.py file.

- Navigate to the unzipped folder and run python3 app.py in your terminal.

- Open the link seen in your terminal.

## Credits

I got inspired of how to handle the edit and delete forms from this project after being pointed towards it by my mentor:

[DenyTsjapanov](https://github.com/DenyTsjapanov/Milestone-Project-3/blob/main/app.py)

### Content

I used what I learned at the [code institute](https://codeinstitute.net/)
to make my login, register and logout pages.

### Acknowledgements

I have spent countless hours on YouTube, Stack Overflow and Google researching how to create this page, just as with my former projects.

It would have been difficult for me to create this project without that help, but I did notice that I had to rely on online content much less to create this project compared to the last one.

### Mentor

I would also like to thank my mentor Reuben Ferrante, his help and advice during this project has been absolutely invaluable. There were times during this project when I had no clue what to do next but I got to the next step with his help.

## My reflections on the project

I have realized after coming back to this project that I should have waited a bit with submitting it and I should have managed my time much better to start with.

I could not get the api I was using to work properly and I was trying to fix that issue until the last moments before submitting the project and because of that I missed alot of issues with my code that I should have seen.

## Changes made after June 24th

- Removed the home page and replaced it with the movies page.

- Changed the movies page so that only users that are logged in can search for movies and view reviews. I did this because I do not want people to be able to spam the API and I do not want users that are not registered to be able to view reviews.

- Fixed a formatting error in the css file.

- Removed a value property from the create review form because that property is not supposed to be used on a form.

- Updated classes for the navbar to better center it and I also updated the html structure for the navbar.

- Added media queries for the navbar.

- Added an image to replace images that are not found when searching for movies, I tried blocking these movies from being shown at all before but that messed up the layout of the search results.

- Changed so that users are redirected to the movies page instead of their profile after logging in. I feel that this makes more sense because most users would go there first rather than to their profile page.

- Rewrote the local deployment.

- Changed the class for the images in the search results so that the max-height value only will be used on the images displayed there.

- Deleted the image used on the old home page.
