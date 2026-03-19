# Day 4: APIs and HTTP Requests

## What I Built

Two scripts that call external APIs. GitHub fetcher gets user info and their top repos. Weather CLI chains two API calls - first to get coordinates from a city name, then to get the weather for those coordinates.

## Exercise 1: GitHub Profile Fetcher

```
$ python github_fetcher.py gvanrossum

=== GitHub Profile: gvanrossum ===
Name: Guido van Rossum
Bio: None
Public Repos: 27
Followers: 25891

Top 5 Repos by Stars:
  - abc-unix: 166 stars (C)
  - TypeChat: 13 stars (TypeScript)
  - devguide: 1 stars (Unknown)
  - c-parser: 59 stars (Python)
  - old-demos: 100 stars (Python)
```

## Exercise 2: Weather CLI

```
$ python weather_cli.py
Enter city name: London

Fetching weather for London...

=== Weather in London ===
Temperature: 8.1°C / 46.6°F
Wind Speed: 10.4 km/h
Conditions: Clear sky
```

## What Was Hard?

The hardest part was figuring out the API structure before coding. I had to actually call the API and print the JSON response first to understand what fields were available. For the weather script, I had to do two API calls - the geocoding API returns latitude/longitude, then I use those to call the weather API. Getting the second URL right required understanding the first API's output.

Error handling was also important - what happens if someone enters a city that doesn't exist? What if there's no internet? I had to handle all those cases.