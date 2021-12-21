<h1 align="center">MovieRec
  <sub>
    <img src="https://c.pxhere.com/images/6d/90/07af6a31003f44671b90e75d50a4-1566355.jpg!d" height="50" width="90">
  </sub>
</h1>

<p align="center">
  <sup>
    MovieRec is a website with a recommender system for movies.
        
  </sup>
</p>

***

* [Purpose](#purpose)
* [Motivation](#motivation)
* [Resources](#resources)
* [Instructions](#instructions)
* [YouTube Video Link](#youtube-video-link)
* [Team](#team)

## Purpose

This website allows visitors to search for movies and view movie details, and will recommend similar movies based on the text in the movie overview.

## Motivation

We've chosen this project because recommender systems are very common; almost every business wants or uses them. Some of us are also interested in working with text data to find semantic similarities. Beneficiaries of this website include anyone who wants to save time finding movies they will enjoy or appreciate.

## Resources
- Data Source: <https://www.kaggle.com/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows>

## Instructions

### How to clone this repo
- Make sure to use a password-protected SSH key. Instructions to generate an SSH key and add it to your GitHub account are available at: [https://github.com/settings/keys](https://github.com/settings/keys)
- In your terminal, navigate to the directory where you want the project to live.
- Type the following command: `git clone git@github.com:byukan/movie-rec.git`

### Setup
Please do the following so that you can run Flask and run our unit and integration tests.
- Install the project dependencies by running the following commands:
  - `pip install -r MovieRecommender/requirements.txt`
  - `pip install -r model/requirements.txt`
- Install node.js by visiting this website: <https://nodejs.org/en/download/>
- Download Cypress using the following command: `npm install cypress`
  - If this does not work, use one of the other download methods described here: <https://docs.cypress.io/guides/getting-started/installing-cypress>
- Navigate to the top-level folder of this project (it will be *movie-rec* unless you renamed it)
- Run our setup script, which will set a couple Flask variables. Type the following: `source flask_setup` 

### How to run Flask and use the website
- In your terminal, navigate to the *MovieRecommender* directory
- Run *either* of the following commands (both should work):
  - `flask run`
  - `python3 serve.py`
- Open up your web browser and visit: **localhost:5000**

### How to run our unit tests
- To test our text similarity model:
  - Navigate to the *model* directory
  - Type the following command: `python3 -m pytest`
- To test access to our MongoDB collections:
  - Navigate to the *mongo* directory
  - Type the following command: `python3 -m pytest`
- To test our Flask code:
  - Navigate to the *MovieRecommender* directory
  - Type the following command: `python3 -m unittest`

### How to run our integration tests with Cypress
- Run flask first (see instructions above)
- Navigate up one level to the top-level project folder (it will be *movie-rec* unless you renamed it)
- Open Cypress
- Within the Cypress window, select the file to run: *cypress/integration/test.js*
- A new browser window will open and run the tests

## YouTube Video Link
https://youtu.be/eyzZRgSytEM
[![Alt text](https://img.youtube.com/vi/eyzZRgSytEM/maxresdefault.jpg)](https://www.youtube.com/watch?v=eyzZRgSytEM)


## Notes
12/20/21: Mongo password changed and repo made public.


## Team

[Aybike Bayraktar](https://github.com/aybikke), [Annat Koren](https://github.com/a-kor-en), & [Brant Yukan](https://github.com/byukan)

## License

[BSD 3-Clause License](https://github.com/byukan/movie-rec/blob/main/LICENSE)
