<p align="center">
  <a href="" rel="noopener">
 <img src="/images/banner.png"></a>
</p>
<h3 align="center">Snake-Lingo</h3>

<div align="center">

</div>

---

<p align="center"> Make learning new languages fun!.
    <br> 
</p>

## 📝 Table of Contents

- [Problem Statement](#problem_statement)
- [Idea / Solution](#idea)
- [Future Scope](#future_scope)
- [Setting up a local environment](#getting_started)
- [Usage](#usage)
- [Authors](#authors)

## 🧐 Problem Statement <a name = "problem_statement"></a>

Make an app for students!

## 💡 Idea / Solution <a name = "idea"></a>

Adapt the game "Snake" into a language learning game using some learning optimisation algorithms.

## 🎮 Playing the game!
In this game, you are a snake trying to grow as long as possible. In order to do this,
you have to eat as many apples as possible, but not just any apple that you find,
you have to eat the correct apple that corresponds to the word on your head.

### Controls
To control the snake, use "W-A-S-D" or the arrow keys!

### Game play
In the game you will see a snake with a word from the foreign language on its head. That's you.
Your objective is to eat the apple with the correct definition on it.
If you eat the correct apple, you'll grow longer. Eat the wrong one, you'll shrink so be careful!

Also, if you touch the walls or a part of your body with your head, it's game over.
<img src="/images/game.PNG">

### Main menu
When you start the game, you'll be taken to the main menu.
Here, choose the language you want to learn or practice.
<img src="/images/menu.PNG">

If you choose the "Reverse" option, you will have the English word on your head and the apples showing 
the words in the foreign language instead of the otherwise way round.

### Game Over Screen
Here you can see your stats!

A word counts as being learnt once you get that word correct 3 times in a row.
<img src="/images/gameover.PNG">


## 👨‍💻 Learning algorithm
This game incorporates a simple learning algorithm to optimize your learning!

Firstly, for each word you are learning, the game will keep showing the word until
you get it correct 3 times in a row.

If you get too many words wrong, you will be shown those words over and over so you're
not overloaded with too many new words.


## 🚀 Future Scope <a name = "future_scope"></a>
This project would be an ideal mobile application as it is simple and is the type of game you would
play on the subway or on the bus.
Additionally, the game could be adapted for non-native English speakers.

## 💻 Downloading the project <a name = "getting_started"></a>

### Prerequisites
* Python >= 3.6
* pip3

* For Linux make sure you have distutils, dev and setuptools installed.
    First update apt:
    ```
    $ sudo apt update
    ```
    Then install distutils, dev and setuptools:
    ```
    $ sudo apt-get install python3-distutils python3-setuptools python3-dev
    ```
    You may need to additionally run:
    ```
    $ sudo apt-get install build-essential
    ```
    Also, install wheel before installing any of the requirements:
    ```
    $ pip3 install wheel
    ```

### Installing
1. Make sure you have python and the prerequisites installed

2. Download the ZIP file from github directly or run the following:

    ```
    $ git clone https://github.com/Ryo-not-rio/Snake-Lingo.git
    ```

3. If you have downloaded the ZIP file, unzip it.

4. Install the dependencies

    First, navigate to the downloaded folder of the project.

    Next, dependencies can be installed by running the following command:
    ```
    $ pip3 install -r requirements.txt
    ```

## 🎈 Usage <a name="usage"></a>
To run the game, in the directory where you downloaded the code,
run:
```
$ python3 main.py
```

## ✍️ Authors <a name = "authors"></a>

- [@ryo-not-rio](https://github.com/ryo-not-rio)
