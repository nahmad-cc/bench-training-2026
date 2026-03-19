# Day 2: Functions, Lists, and Dicts

## What I Built

I made a word frequency counter that takes text, removes punctuation, and counts how many times each word shows up. Then it prints the top 5 most common words. I also made a grade book that has a list of students (each student is a dict with their name, scores, and subject). It calculates averages, gives grades, and prints a report sorted by score. The top student gets marked with *** TOP ***.

## Lists vs Dicts

A list is ordered - you get items by number like list[0], list[1], etc. Use lists when you have multiple similar things like scores or names in order.

A dict lets you use names as labels instead of numbers. Like student['name'] instead of student[0]. Use dicts when you have related data with labels, like a person's info (name, age, email).

In exercise 2, I used a list of dicts because I have multiple students (list), and each student has properties with names (dict).