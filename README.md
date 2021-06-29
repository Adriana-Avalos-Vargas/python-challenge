# Py Me Up, Charlie

## Introduction

Excel is a very common tool in the business world for all kinds of data analysis tasks. It is simple and provide fast results [1,2,3,4]. However, for more powerful analysis it is necessary to manage it with Visual Basic (VBA). According to [1], VBAs are complex to operate, and they make Excel difficult to work with when dealing with multiple operations during data analysis. Of course, the main advantage of excel is the simplicity when compared with Python.

On the other hand, Python is an open-source programming language, with numerous contributors who volunteer to provide regular updates to the code and improve its functionality [1]. It is possible to use it in Big Data, i.e. it is scalable, it allows data connectivity and has automation capabilities [4]. However, it has a step learning curve.

In this Python Challenge it is presented an analysis of two kinds:

* Financial (PyBank)

* Political voting (PyPoll)

## General notes

In this task a csv file is imported through the *reader* function from de *csv* module.  The idea is toiterate through rows and do some calulations depending on the encomended task. The results of such operations is stored in a list ir a dictionary.

Also, the final result is displayed in the screen and saved as a text file.

## PyBank

![Revenue](Images/revenue-per-lead.png)

* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## PyPoll

![Vote Counting](Images/Vote_counting.png)

* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.



## Copyright

Trilogy Education Services © 2019. All Rights Reserved.
