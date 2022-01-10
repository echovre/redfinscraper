# redfinscraper

Quick and dirty script to scrape length/width/area of rooms from redfin. Writes a cost.csv file to do calculate cost using params set in script.

Using redfin because Zillow usually doesnt have measurements.

Usage: `python redfinscraper.py <url_from_redfin> `

Example:
```
python redfinscraper.py https://www.redfin.com/OR/Beaverton/14525-SW-Downing-St-97006/home/26642312

Primary Bedroom Information {'floor area': '126', 'wall area': 1008}
Bedroom #2 Information {'floor area': '110', 'wall area': 880, 'perimeter': 42}
Bedroom #3 Information {'floor area': '88', 'wall area': 704, 'perimeter': 38}
Bathroom Information {}
Kitchen Information {'floor area': '126', 'wall area': 1008, 'perimeter': 46}
Dining Room Information {'floor area': '90', 'wall area': 720, 'perimeter': 38}
Living Room Information {'floor area': '225', 'wall area': 1800, 'perimeter': 60}
Family Room Information {'floor area': '220', 'wall area': 1760, 'perimeter': 62}
Other Room #1 Information {'floor area': '75', 'wall area': 600, 'perimeter': 40}
Other Room #2 Information {'floor area': '126', 'wall area': 1008, 'perimeter': 46}
Other Room #3 Information {'floor area': '63', 'wall area': 504, 'perimeter': 32}
Additional Rooms {}
Interior Features {}
Heating &amp; Cooling {}
```

```
cat cost.csv

https://www.redfin.com/OR/Beaverton/14525-SW-Downing-St-97006/home/26642312
Primary Bedroom Information,floor area,126,3.6,453.6
Primary Bedroom Information,wall area,1008,0.045,45.36
Bedroom #2 Information,floor area,110,3.6,396.0
Bedroom #2 Information,wall area,880,0.045,39.6
Bedroom #2 Information,trim length,42,0.78,32.76
Bedroom #3 Information,floor area,88,3.6,316.8
Bedroom #3 Information,wall area,704,0.045,31.68
Bedroom #3 Information,trim length,38,0.78,29.64
Kitchen Information,floor area,126,3.6,453.6
Kitchen Information,wall area,1008,0.045,45.36
Kitchen Information,trim length,46,0.78,35.88
Dining Room Information,floor area,90,3.6,324.0
Dining Room Information,wall area,720,0.045,32.4
Dining Room Information,trim length,38,0.78,29.64
Living Room Information,floor area,225,3.6,810.0
Living Room Information,wall area,1800,0.045,81.0
Living Room Information,trim length,60,0.78,46.800000000000004
Family Room Information,floor area,220,3.6,792.0
Family Room Information,wall area,1760,0.045,79.2
Family Room Information,trim length,62,0.78,48.36
Other Room #1 Information,floor area,75,3.6,270.0
Other Room #1 Information,wall area,600,0.045,27.0
Other Room #1 Information,trim length,40,0.78,31.200000000000003
Other Room #2 Information,floor area,126,3.6,453.6
Other Room #2 Information,wall area,1008,0.045,45.36
Other Room #2 Information,trim length,46,0.78,35.88
Other Room #3 Information,floor area,63,3.6,226.8
Other Room #3 Information,wall area,504,0.045,22.68
Other Room #3 Information,trim length,32,0.78,24.96
```
