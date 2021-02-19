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

## Technologies Used

### Languages

- [HTML](https://en.wikipedia.org/wiki/HTML)

- [CSS](https://en.wikipedia.org/wiki/CSS)

- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

### Tools & ries

- [Flask](<https://en.wikipedia.org/wiki/Flask_(web_framework)>)

- [Materialize CSS](https://materializecss.com/)

- [Git](https://git-scm.com/)

- [Google Fonts](https://fonts.google.com/)

## Testing

### Bandit -a tool designed to find common security issues in Python code.

[You can find out more about bandit here](https://github.com/PyCQA/bandit)

I used this automated tool to check if there were any security issues in my code. It reported on medium security issue and that is that I am binding to 0.0.0.0 in env.py and this can potentially open up a service to traffic on unintended interfaces.

This should be fine when deployed to Heroku.

### PyTest

[You can find out more about PyTest here](https://flask.palletsprojects.com/en/1.1.x/testing/)

I intented to to this as a last step but I did not have time for this unfortunately.

### Forms, validation, responsiveness etc.

As per usual I ran my code through online validators, code formatters and I also manually tested every part of my page to see if there were any issues that I could fix before submitting the code.

I have done manual tests on all the forms and search fields and I have addressed most of the issues that came up.

I had an issue with forms not clearing after submit but this should be fixed now.

The users could add endless of the same movie but I have fixed this with a conditional statement.

The same problem occurs when the user submits reviews but I have sadly not yet fixed this, because I ran out of time.

I manually test the responsiveness and fixed the issues that I noticed with media queries. I also set images from the movie database to less than 100% to get it to work good.

I also noticed that the search results when searching for movies do not clear as they should, but sadly this is also something I didn't have time to fix.

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

#### If you want to run my website locally you can download it from [here](https://github.com/Gretaah/milestone-project1/archive/master.zip) and after that you can:

- Right click on the file and unzip it.

- Navigate to the unzipped folder.

- double click on index.html to start the file in youwser.

## Credits

### Content

I used what I learned at the [code institute](https://codeinstitute.net/)
to make my login, register and logout pages.

### Acknowledgements

I have spent countless hours on YouTube, Stack Overflow and Google researching how to create this page, just as with my former projects.

It would have been difficult for me to create this project without that help, but I did notice that I had to rely on online content much less to create this project compared to the last one.

### Mentor

I would also like to thank my mentor Reuben Ferrante, his help and advice during this project has been absolutely invaluable. There were times during this project when I had no clue what to do next but I got to the next step with his help.

## My reflections on the project

I am proud of this project and I feel like I have learned a lot when creating it, but I regret not having time to fix the last things that I wanted to.

For future projects I should laern to step away from a problem and do something else, either coding or something else.

I spent too much time on issues I had with wtforms and handling of data and I think that it would have been good for me to take a step back and do something else instead of obsessing on an issue that I could not find the answer to at the moment.

I noticed that the answers came to me during breaks when I did other things.

I also knew that I did not have much time when I started this project and I should have managed my time a little bit better so that I could spend the last days testing and fine tuning the project and this is something that I need to keep in mind for future projects.
