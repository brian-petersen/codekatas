# Kata04: Data Munging

Martin Fowler gave me a hard time for Kata02, complaining that it was yet
another single-function, academic exercise. Which, or course, it was. So this
week let’s mix things up a bit.

Here’s an exercise in three parts to do with real world data. Try hard not to
read ahead—do each part in turn.

## Part One: Weather Data

In `weather.dat` you’ll find daily weather data for Morristown, NJ for June 2002.
Download this text file, then write a program to output the day number (column
one) with the smallest temperature spread (the maximum temperature is the second
column, the minimum the third column).

## Part Two: Soccer League Table

The file `football.dat` contains the results from the English Premier League for
2001/2. The columns labeled ‘F’ and ‘A’ contain the total number of goals scored
for and against each team in that season (so Arsenal scored 79 goals against
opponents, and had 36 goals scored against them). Write a program to print the
name of the team with the smallest difference in ‘for’ and ‘against’ goals.

## Part Three: DRY Fusion

Take the two programs written previously and factor out as much common code as
possible, leaving you with two smaller programs and some kind of shared
functionality.

## Kata Questions

> To what extent did the design decisions you made when writing the original
> programs make it easier or harder to factor out common code?

It made it fairly easy. By using regular expressions for line filtering and
splitting, a common data structure to store parsed data points, and a function
for finding the smallest spread, finding common code to factor out was a breeze.

> Was the way you wrote the second program influenced by writing the first?

Heavily. I copied and pasted the code from the first solution and reworked it to
work with for the second data set.

> Is factoring out as much common code as possible always a good thing? Did the
> readability of the programs suffer because of this requirement? How about the
> maintainability?

Factoring out common code is not always a good thing. Sometimes "duplicate" code
happens by chance. It might be simple enough that it happened to be the same.

Readability can suffer by factoring common code at each chance. If done with
too much zeal, one may find themselves reading multiple files for what should be
a trivial problem.

Maintainability can suffer too. If a third data set (with different parsing
logic needed) is added later, the factoring costs would encourage adding the new
parsing logic to the `shared` module. It requires testing of the previous
parsers and could complicate things further.
