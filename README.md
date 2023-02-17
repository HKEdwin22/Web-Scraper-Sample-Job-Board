# Purpose of project (keep update)
Practice web scraping with Beautifulsoup and Selenium

## 2023 Feb 17 - Parsing_JD.py
### Objective
This script aims at parsing the info of jobs of the sample page: https://news.ycombinator.com/jobs

### Background
In the first trial, we parsed only 30 items from the webpage. We noticed that each page displays 30 items only, with a button "More" in the bottom.
When the button is clicked, the next 30 items will be displayed. 
When the last item is displayed and the button is clicked again, an error page appears with a button "Reload".

### Methodology
<ol>
  <li>Parse the page with Beautifulsoup</li>
  <li>Click the button "More" with Selenium Webdriver</li>
  <li>Repeat step 1 and 2 until reaching the error page</li>
  <li>Save the results into a csv file</li>
</ol>
