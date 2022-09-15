# Election_Analysis

## Project Overview

A Colarado board of Elections employee has given the following tasks to complete the election audit of a recent local congresional election. In this project, our final Python script will need to be able to deliver the following information when the script is run:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources

- Data Source: election_results.csv
- Software: Python 3.9.12, Visual Studio Code 1.70.2

## Summary

The analysis of the election show that
- There were 369,711 votes cast in the election


![Total Votes Code](https://user-images.githubusercontent.com/47859209/190319343-b5cae841-df8b-4523-8fff-600cf61baf52.png)
![Total Votes Output](https://user-images.githubusercontent.com/47859209/190319345-e2ad0a97-72cd-4282-8a58-de72e9baba75.png)


- The candidates were:

 - Charles Casper Stockham
 - Diana DeGette
 - Raymon Anthony Doane

- The results were:

 - Charles Casper Stockham received 23.0% of the vote and (85,213) number of votes.
 - Diana DeGette received 73.8% of the vote and (272,892) number of votes.
 - Raymon Anthony Doane: received 3.1% of the vote and (11,606) number of votes.

![Candidate Votes Code](https://user-images.githubusercontent.com/47859209/190320629-55e969f6-8a9b-4983-9931-bebcee703dc7.png)
![Candidate Votes Output](https://user-images.githubusercontent.com/47859209/190320632-5bde3b71-3188-446c-b7f9-aa987c1646e3.png)

- The winnder of the election was:

- Diana DeGette who received 73.8% of the vote and (272,892) number of votes.

![Winning Candidate Code](https://user-images.githubusercontent.com/47859209/190321301-2be9c23b-1bfa-4491-903b-025fe5d8f6fe.png)
![Winning Candidate Output](https://user-images.githubusercontent.com/47859209/190321302-e5d19aeb-c61d-4e86-b8c0-4b7937efc198.png)

## Challenge Overview

The purpose for this Election Audit script is to determine: 1.) Who the winner of the election is 2.) Which county had the largest voter turnout 3.) The percentage of total votes contributed by voters of each county

## Challenge Summary

This script can be used to audit other congressional districts and local elections. If we had more data on the voting methods we could write a script to determine which voting method was used the most. We can also pick a district with more than 3 counties and the script would still run.

One more thing we could have added is to analyze the vote percentage for each candidate in each county to understand the voting trend, which will be very helpful for future campaigning.
