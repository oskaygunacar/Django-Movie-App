# Django Movie App Project

## General Overview

This project is a Django-based web application for a movie website. It features a range of functionalities typical of modern web platforms.

### 1. Site Architecture and Navigation

The website comprises several pages:
- **Most Watched Movies Page**: Showcasing the most popular movies.
- **Home Page**: The central hub of the site.
- **Category Pages**: Dedicated to different genres.
- **Individual Movie Detail Pages**: For detailed information about each movie.
- **User Profile Pages**: For user-specific information and settings.

Navigation through the website is facilitated by a navbar and sidebars on various pages.

### 2. Authentication

- **Signup**: Users can sign up via the 'Become a Member' section in the navbar, which redirects them to the signup page. Post-registration, users are directed to the login screen.
- **Viewing Movies**: Movies can be viewed by any visitor without the need for registration.
- **Commenting**: To comment on movies, users must sign up and log in.
- **Visibility of Comments**: Unregistered users can view comments but cannot see the comment section on movie detail pages.
- **Profile Access**: All users, regardless of login status, can view individual user profiles.
- **Profile Editing**: Logged-in users can edit their profiles, including avatars, information, and social links.

### 3. Database

- The project utilizes the movie API provided by [The Movie Database (TMDB)](https://www.themoviedb.org/).
- A custom database can be created and utilized following the structure defined in the `models.py` file under `movie_app`.

**If you want to use TheMovieDB Database for the project, you need to get the api key from their original site in the above**

### 4. Search Functionality

The site's search functionality operates based on movie titles. It performs a case-insensitive search across the database and returns results, implementing pagination for queries yielding more than 20 results.

### 5. Homepage

The homepage features the six most popular movies and a paginated list of the latest 20 movies. The movies are sorted from newest to oldest in the database and displayed accordingly on the homepage.

### 6. Categories

Each category page displays only the movies belonging to that specific genre, showing the latest 20 movies in a paginated format.

### 7. Most Popular Movies

This page ranks movies based on the 'popularity' metric from TMDB, showing them from most to least popular. Pagination is active, displaying 20 movies per page.

### 8. Profile (Account)

After signing up and logging in, each user has a personal profile page based on their username. Users can update their information, change their password, or delete their account. Profile customization options include changing the avatar, adding a biography, and including social media links.

In profile detail pages people can see user's latest comments (paginated), their social links and bio + avatar.

## Project Setup

Follow these steps to set up the project:

**Step 1**: Clone the project
```bash
git clone https://github.com/oskaygunacar/Django-Movie-App.git
```

**Step 2**: Navigate to the directory
```bash
cd Django-Movie-App
```

**Step 3**: Create and activate a virtual environment
```bash
# Create
python -m venv env

# Activate for MacOS & Linux
source env/bin/activate

# Activate for Windows
env\Scripts\activate
```

**Step 4**: Install dependencies
```bash
pip install -r requirements.txt
```

**Step 5**: Migrate the database and create a superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

**Step 6**: Run the server
```bash
python manage.py runserver
```

After completing these steps, you should be able to access the project by visiting `127.0.0.1:8000` in your browser.

**Step 7 (optional)**: **Creating Bulk TheMovieDB Database For Test**

if you want to use The Movie Database (TMDB), database for the test purposes of the script, then first get your [The Movie Database (TMDB)](https://www.themoviedb.org/) API key from their site by signing up and follow the instructions below:

After receiving the Api KEY ;

***In the create_movie_database.py file under the commands directory in the Movie_app folder, type the api key you received to the api_key variable field at the top of the file.***

***Then, by running the following command, you can pull bulk movie data from The Movie Database's database to your local database very quickly with the help of the functions I created using Python threading***

```bash
python manage.py create_movie_database
```

After getting the API key and entering the specified file and running the command above, you can write the results of these requests to your database by sending requests to various pages of Movie DB with 13 threads every 10 seconds with the help of Python threading.

If you are using SQLITE database, there may be crashes from time to time due to speed.

## Some Screenshots from Project

### Homepage and Sidebar
![Movie-Project-Homepage](https://i.imgur.com/SAxkvL0.png)

## Movie Detail Page

![Django-Movie-App Project Movie Detail](https://i.imgur.com/rK7dx4O.png)


## Movie Detail Comment Section

![Movie Detail Comment Section](https://i.imgur.com/7irgobR.png)


## User Profile Pages (For User Himself)
![Profile Page of User](https://i.imgur.com/5y3cgiT.png)

### Other User's Profile Page Example

![Other Users Profile Detail Pages](https://i.imgur.com/FPosFdg.png)

### Signup Page (Only non logged in users can see)

![](https://i.imgur.com/M8eRJ4e.png)