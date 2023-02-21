# Provisional Purposes of the Project
<ol>
  <li>Practice web scraping with Beautifulsoup and Selenium</li>
  <li>Use TFIDF</li>
  <li>Find insight with Power BI</li>
</ol>

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
  <li>Save the results into a csv file (JD.csv)</li>
</ol>

## 2023 Feb 19 - TFIDF.py
### Objective
We try to use TFIDF to analyse the words used in the job descriptions and see if we find any insight there.

### Background
I have used a simple word count to analyse the frequency of occurrence of each word. I try to use TFIDF here to check if there will be other interesting findings.

### Methodology
<ol>
  <li>Read the file into a data frame</li>
  <li>Data cleansing (with stop words)</li>
  <ol>
    <li>Keep only columns of our interests</li>
    <li>Transform the data into an appropriate format</li>
    <li>Remove words that don't bring meanings to our analysis (e.g. is, and, but), punctuations and words that contain numbers</li>
  </ol>
  <li>Apply Sci-Kit Learn vectorizer</li>
  <li>Save the results as a csv file (TFIDF.csv)</li>
</ol>

### Results
The table had a shape of 960 x 877 (960 samples/openings and 877 different words). Words were rated a TFIDF score in each sample. If a word in a sample scored zero, it meant that the corresponding word didn't exist in that sample. If a word in a sample scored high (e.g. 0.7xxx), it indicated that the word existed in the corresponding sample but was seldom found in other samples. Vice versa, if a word in a sample scored low (e.g. 0.02xx), it indicated that the word existed in the corresponding sample but was often found in other samples.

#### Example 1
The word "hiring" scored 0.08575 in sample 1. It indicates that the word "hiring" existed in sample 1 and was often found in other samples.

#### Example 2
The word "hioperator" scored 0.7205 in sample 92. It indicates that the word "hioperator" existed in sample 92 but was seldom found in other samples.

## 2023 Feb 21 - TFIDF Interpretation.md
### Objective
To interpret the results from the previous csv file.

### Methodology
1. Average out the TFIDF
2. Plot scatter graph with Power BI
3. Find insight
4. Write report
