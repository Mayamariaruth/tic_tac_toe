# Tic Tac Toe

## Introduction

Tic Tac Toe is a Python terminal game for some quick fun.
It runs in the Code Institute mock terminal on Heroku.

The user plays against the Computer taking turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

Link to the live site here - [Tic Tac Toe]()

![Responsive Mockup](docs/screenshots/)

![Responsive Mockup](docs/screenshots/)

## Table of Contents:
1. [**Introduction**](#introduction)
1. [**How to play**](#how-to-play)
1. [**Features**](#Features)
    * [***Header***](#header)
    * [***Home page***](#home-page)
    * [***Quiz***](#quiz)
    * [***End of quiz popup***](#end-of-quiz-popup)
    * [***Footer***](#the-footer)
1. [**Testing**](#testing)
    * [***Manual testing***](#manual-testing)
    * [***Validator testing***](#validator-testing)
    * [***JSHint testing***](#jshint-testing)
    * [***Lighthouse testing***](#lighthouse-testing)
       * [*Home front page*](#home-front-page)
        * [*Quiz area*](#quiz-area)
    * [***Wave accessibility evaluation***](#wave-accessibility-evaluation)
1. [**Deployment**](#deployment)
    * [***Cloning***](#cloning)
1. [**Bugs**](#bugs)
    * [***Fixed Bugs***](#fixed-bugs)
    * [***Unfixed Bugs***](#unfixed-bugs)
1. [**Credits**](#credits)
    * [***Code***](#code)
    * [***Content***](#content)
    * [***Media***](#media)
    * [***General reference***](#general-reference)

## How to play



## Features 

  - 

  ![Header](docs/screenshots/)

- 

![Home page](docs/screenshots/)

- 

![Quiz](docs/screenshots/)

- 

![End of quiz](docs/screenshots/)


### Future features
- 

## Testing 

### Manual testing
I manually tested this site in multiple ways highlighted below:
* Tested every feature and its responsiveness through an extension of a live server in VScode.
* Deployed the site in an early stage and received feedback from a professional developer (mentor), as well as students in my community.
* Tested the site for cross-compatibility in the two most used browsers, Chrome and Safari.
* I used DevTools to easily move between different screen sizes, simulating sizes between 320px to 4000px (but it is also functional on even larger screens given the max-width setting on the Body element to keep the content compact instead of stretched).

### Validator Testing 
I tested all the pages in the validators to make sure they all passed.
- HTML
  - There were no errors present when passing through the official W3C validator ![W3C validator](docs/screenshots/html-validator.png)

- CSS
  - There were no errors present when passing through the official Jigsaw validator ![(Jigsaw) validator](docs/screenshots/css-validator.png)

### JSHint testing
There were no warnings with the JSHint testing after successfully sorting out the bugs highlighted in the [Bugs section](#bugs).

### Lighthouse testing 

This testing was done in an incognito window in Chrome to make sure the results were not influenced by browser extensions.

The desktop testing was the same score for the home page and quiz page but the mobile testing differed by just a couple of points but both pages scored incredibly well.

At first, the mobile testing was in the high 80s score but after compressing the background image, the scores went up into the 90s range.

__Desktop version:__

![Desktop home page](docs/screenshots/lighthouse-desktop.png)

#### Home front page 
__Mobile version:__

![Mobile home page](docs/screenshots/home-mobile.png)

#### Quiz area

__Mobile version:__

![Mobile quiz page](docs/screenshots/quiz-mobile.png)

### Wave accessibility evaluation

I also used the Wave evaluation tool to make sure I covered all my bases. 

The evaluation is free from errors and below is taken from the Home page and quiz page.

#### Wave home page
![Wave evaluation](docs/screenshots/wave-home.png)

#### Wave quiz page
![Wave evaluation](docs/screenshots/wave-quiz.png)

## Deployment

To deploy the site to GitHub pages, I went through below steps: 
- Go to the Settings tab of the project's GitHub repository.
- There is a General menu on the left side of the screen, go to Code & Automation and click Pages.
- Scroll down to the Build & Deployment section and choose the Source 'Deploy from a branch'.
- Below this, you choose the Branch 'Main' and the Folder '/root'.
- Press Save and go back to the Code page of your repository.
- After a couple of minutes, refresh the page and the successfully deployed site will be found on the right-hand side of the page under 'Deployments' with the name "GitHub pages".

Live link to the site - [Quizzing](https://mayamariaruth.github.io/quizzing/quiz.html)

### Cloning

I used the cloning method to use the VSCode desktop IDE with GitHub, below are the steps I took:
- Generate a repository and click the Code button in the middle of the screen.
- Go to Local and under Clone, copy the Git repository URL on the HTTPS tab.
- Go to the VSCode IDE front page and click 'Clone Git Repository' under Start or go to the Source Control button on the left-hand side menu bar and click 'Clone Repository'.
- Input the URL in the URL tab at the top of the window and press Enter.
- Select the location/folder where you want to store your repository on your computer through the popup and click the 'Select Repository location' button.
- VSCode will now clone the repository and you can choose to open it in your current window or in a new window.

## Bugs

### Fixed Bugs
1. **Issue**
    * 'showQuestions' function kept getting an error that '.question' was not defined when pressing the Next button at the end of the quiz.
* **Fix**
    * I added the 'finishQuiz' function and it was then sorted.

2. **Issue**
    * 'finishQuiz' function was not registering the Display style settings so the end of quiz popup was not popping up after the quiz was over.
* **Fix**
    * I changed the class tag to an ID tag on the HTML elements.

3. **Issue**
    * The score was not showing up at the end of the quiz popup.
* **Fix**
    * I added a new ID tag to the element and a variable 'totalScore' and its textContent equaled the scoreSum in the 'finishQuiz' function.

4. **Issue**
    * When clicking the Next button, the class tags to disable the answer buttons and to add color to the correct/incorrect answers doesn't reset.
* **Fix**
    * I added an eventListener function for the answer options buttons and enabled the buttons in a For loop inside the Next button function.

5. **Issue**
    * Warning in JSHint: "Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (checkAnswer)" 
* **Fix**
    * I changed the For loop inside the eventListener to the forEach method.

6. **Issue**
    * The forEach method in the eventListener function was sending an error back in the console that it wasn't a function so it wasn't executing.
* **Fix**
    * I needed to convert the answer options buttons (choiceButtonRef) to an array using the Array.from() method.

7. **Issue**
    * The 10th question was not displaying before the end of quiz popup shows up.
* **Fix**
    * I changed the '(questionNumber === questions.length)' If statement in the nextBtn.onclick function to (questionCount === questions.length) instead.

### Unfixed Bugs

No unfixed bugs.

## Credits 

### Code 

_External pages credit_
- I drew help from [Codehal YouTube](https://www.youtube.com/watch?v=Vp8x8-reqZA&ab_channel=Codehal) for the code found in the 'checkAnswer' function.

### Content 

- The questions and answers were generated with ChatGPT.
- The social media links directly to the home pages of each site.
- Fonts were acquired from [Google Fonts](https://fonts.google.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The background image was generated with Microsoft Designer's AI tool.
- The color palette was generated with the image on [Coolors](https://coolors.co/).
- [Am I Responsive](https://ui.dev/amiresponsive) was used to generate the initial image of the ReadME to showcase how the site looks on different screens.

### General reference

- I relied upon my code learnings from the Code Institute, as well as the walk-through of the Love Maths project and [Codehal's YouTube video](https://www.youtube.com/watch?v=Vp8x8-reqZA&ab_channel=Codehal). There are similarities in some of the code but I credited the necessary sections.
- W3Schools and StackOverflow were the sites mostly used for external references.
