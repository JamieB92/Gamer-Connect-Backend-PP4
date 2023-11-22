# GamerConnect

![Gamer-Connect-Logo](https://github.com/JamieB92/Gamer-Connect-Backend-PP4/assets/117354147/e4e36b51-8241-4e63-a082-cbd723366145)

Welcome to GamerConnect, the ultimate social media platform for gamers!

GamerConnect is a dynamic and inclusive platform designed for gamers of all ages and backgrounds. Whether you're a seasoned pro or just starting your gaming journey, our platform is tailored to bring the gaming community together.

This is the Backend Repo for the project please click [here](https://github.com/JamieB92/Gamer-Connect-Frontend-PP4) for the frontend repo.

## Features
- Game Clips & Screenshots: Share your gaming triumphs, epic moments, and funniest fails with our intuitive media uploading features.

- Likes & Follows: Connect with fellow gamers, support their content with likes, and build your own dedicated following.

- Find Gamers: Discover like-minded players and create lasting gaming partnerships. Find friends to join you in your gaming adventures!

## Why GamerConnect?
- Community-First Approach: GamerConnect puts the community at the heart of everything we do. We're all about creating connections, friendships, and epic gaming memories.

- User-Friendly Interface: Our platform is designed with simplicity in mind, ensuring an easy and enjoyable experience for users of all levels.

- Diverse Gaming Experience: No matter your preferred platform, genre, or style, you'll find a welcoming and diverse community here.

## How to Get Started
- Sign up for a GamerConnect account.
- Customize your profile with your favorite games, gaming interests, and a profile picture.
- Start uploading your game clips, screenshots, and engage with the gaming community.
- Connect with other gamers, follow your favorite content creators, and make new gaming buddies.
- Join the Community
- GamerConnect is not just a platform; it's a gaming family waiting to welcome you. Start your gaming journey, connect with fellow players, and level up your social gaming experience today.

## Feedback and Contributions
- We welcome your feedback and contributions to make GamerConnect even better. Feel free to report issues, suggest improvements, and contribute to our open-source development.


# User Stories

## Epic 1 - Post Sharing & Interaction:

### Create Gaming Posts: 
As a GamerConnect user, I aim to share my gaming experiences by crafting posts containing clips and images, facilitating connections with the gaming community.

### View All Posts:
As a GamerConnect user, I wish to scroll through all the latests posts on the site

### View Post Details: 
As a GamerConnect user, I want to check out individual posts to learn more about interesting gaming posts.

## Epic 2 - Content Discovery & Engagement:

### Show Appreciation: 
As a GamerConnect user, I want to show my liking for interesting posts to express support.

### Keyword-Based Search: 
As a GamerConnect user, I aim to search for posts and user profiles using keywords to find content and gamers matching my interests.

### Review Liked Posts: 
As a GamerConnect user, I want a straightforward way to revisit posts I've liked, making it easy to relive favorite gaming moments

## Epic 3 - Post-Specific Interactions:

### Post Editing Privileges: 
As a post owner on GamerConnect, I aim to have control over the editing of my post title and description to ensure accuracy and updates.

### Active Commenting: 
As a GamerConnect user, I intend to contribute to post discussions by adding comments, allowing me to share thoughts and engage with fellow gamers.

### Comment Control: 
As the owner of a comment, I wish to have the capability to delete and edit my comments, allowing me to manage the content within the application.

## Epic 4 - User Profiles & Connections:

### New Account Creation:
As a GamerConnect user, I intend to establish a fresh account to access all the privileges available to registered gamers.

### User Profile Viewing:
As a GamerConnect user, I want to check out fellow gamers' profiles to explore their gaming posts and learn more about their gaming experiences.

### User Following & Unfollowing: 
As a GamerConnect user, I want to be able to follow and unfollow other gamers.

### Profile Customization: 
As a GamerConnect user, when logged in, I want to personalize my gaming identity by changing my profile picture and updating my bio.

## Epic 5 - Developer 

### Initial Backend Setup
As a developer, I need to set up the backend project structure for seamless project development.

### Initial Frontend Setup
As a developer, I must configure the frontend project structure to facilitate project development.

### Deploy Backend
As a developer, I need to guarantee the successful deployment of the project's backend for site accessibility.

### Deploy Frontend
As a developer, I must ensure the successful deployment of the project's frontend for users to interact with.

### Database Setup
As a developer, it's crucial to create a database and integrate it into the project for effective information storage.

## Design

#### Colors
![color-palete](https://github.com/JamieB92/Gamer-Connect-Backend-PP4/assets/117354147/4c72a043-a4e3-49ba-b583-5ec8cf4a4c46)

#### Font
Google Font - Lexend


 # Deployment
Here you can find the instructions to recreate the deployment of the project

## Backend Setup & Deployment

### Github
- In the top right of the page click the plus symbol
- Click New Repository
- Select Template - Code-Institute-Org/gitpod-full-template
- Name the repository (Reference Backend)
- Click Create

### Gitpod (Please use Chrome or Firefox)
- open a new tab in your browser and go to your browsers extensions store
- Search for Gitpod
- Install Gitpod extension
- Go back to your newly created repo
- Click the Green Gitpod Open button
- Click Continue with Github 
- Gitpod will now create a workspace 

### Django and Django Rest Framework Setup
- In your IDE open a new terminal
- Enter in the terminal pip3 install 'django<4'
- Enter in the terminal django-admin startproject {{project_name}} .
- Enter in the terminal to create an App with - python manage.py startapp {{app_name}}
- Add the new app to the allowed apps in the settings.py file.
- Enter in the terminal - pip install djangorestframework
- Now go to settings.py and add 'rest_framework' to installed apps.
- Enter in the terminal pip install django_filter
- Now go to settings.py and 'django_filers' to installed apps.



### Cloudinary and Pillow
- Go to Cloudinary - https://cloudinary.com/
- Create an account
- Click dashboard
- Copy your cloudinary API Environment variable
- Install Cloudinary in the terminal with - pip install django-cloudinary-storage
- pip install django-cloudinary-storage[video]
- Install Pillow in the terminal with - pip install Pillow
- Now go to settings.py in your project 
- In installed apps add 'cloudinary_storage' above 'django.contrib.staticfiles' and 'cloudinary' below.
- create an env.py file in the top directory
- add your cloudinary API Environment variable to the env.py file
- add the following to settings.py underneath "from pathlib import Path":
        
        import os

        if os.path.exists('env.py'):
            import env

        CLOUDINARY_STORAGE = {
            'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
        }
        MEDIA_URL = '/media/'
        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Bugs and Testing 

You can find all the bugs and testing in the following files:

GamerConnect [Backend](https://github.com/JamieB92/Gamer-Connect-Backend-PP5/blob/main/bugs_and_testing_backend.md)