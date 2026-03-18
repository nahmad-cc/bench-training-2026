# Day 1: From Zero to Actually Running Code

## What I Built

I created three Python scripts that cover the fundamentals of programming: data types, operators, control flow, and loops. **Exercise 1** demonstrates how to work with variables (strings, integers, booleans, and floats) and perform real-world calculations like retirement planning and budget tracking. **Exercise 2** implements a grade classifier function and uses it to process multiple test scores without repeating code, showcasing the importance of functions in keeping code DRY (Don't Repeat Yourself). **Exercise 3** builds an interactive multiplication table generator that validates user input and offers a feature to generate all 12 tables in one run, demonstrating loops and clean output formatting.

## What Tripped Me Up & What I'd Do Differently

The main challenge was ensuring input validation in Exercise 3—handling both numeric inputs and string inputs like 'all'. Initially, I didn't consider edge cases like non-numeric strings or numbers outside the range. I'd improve this by adding more robust error handling and providing clearer user feedback. Additionally, I realized that using functions from the start (even in Exercise 1) makes code more maintainable and testable, so I'd refactor any repeated logic into helper functions earlier in development.