# gevpro_final_project

## table of contents

-[description](#description)
-[Labour Division](#labour-division)
-[Program Manual](#program-manual)
-[Stakeholder Value](#stakeholder-value)
-[Datascientist Value](#datascientist-value)

## description:
We are Iwan Hofstra, Valerio and Parsa. We worked on a research question for an assignment.
This project is about the research question:  How do game attributes such as genre, price, and supported platforms interact to influence user engagement and ratings on Steam?​

We have tried to awnser this research question with the following dataset:
https://www.kaggle.com/datasets/fronkongames/steam-games-dataset

We made use of Jupyter Notebook for good visability. In Jupyter Notebook we worked mostly with Python's Pandas module. With these tool we created graphs and infographics to better visualise the results.

## labour division:

Iwan: Pycodestyle, explanations, unit tests, github.

## program manual:
Download all specified files and put them in the same directory
Make sure you have installed python, and the modules Pandas, seaborn and matplotlib.pyplot
press run all on the Jupyter Notebook and all the results should pop up!

We have also added a small test to make sure the data is cleaned.
this test is called test_data_cleaning.py and here is how you run it:
- Make sure you have pytest installed (in your terminal):
"pip install pytest"

-Run the test in your terminal:
"pytest test_data_cleaning.py"


## stakeholder value:
The stakeholder now has valuable data on what variables influence the ratings of the games. The strongest variable was price. Price influenced the games rating a lot, and is very important in making a game. Playtime also played a role in the ratings, and should be a key factor to strive for when developing a game. Variables that are not worth a lot regarding ratings are the genres. These variables should be chosen purely by what is your preference, not if you want good ratings. 


## datascientist value:
We chose Jupiter Notebook voor de good visability and reproduction of code. We ensured that our code fitted the PEP8 python codestyle for clean code and also readable code. Our choise of Panda's was because we worked with an .csv file, and Pandas excells at retrieving data from such 2D information type files. We chose Seaborn because it is a powerful Python library built on top of matplotlib that makes it easier to create visually appealing and informative statistical graphics. Seaborn offers high-level functions for complex visualizations like heatmaps, box plots, and violin plots with very little code. It also integrates smoothly with Pandas DataFrames, which makes it ideal for data analysis. I used Seaborn to clearly visualize trends and patterns in the dataset, such as relationships between variables and category distributions.