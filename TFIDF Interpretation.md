## Results

We averaged the TFIDF. As IDF is a logarithm, it is the same as averaging TF (term frequency).<br>

Figure 1 shows the average TFIDF of all words in a descending order. Starting from the word "London",
the words share a similar TFIDF score. It indicates that those words only appeared in a few sample.
In other words, those words were used specifically in certain positions by a few employers.
![Figure 1. Average TFIDF of all words](https://github.com/KaverH/Web-Scraper-1/blob/main/TFIDF_all%20words.png)
*Figure 1. Average TFIDF of all words*

We are not interested in those specific words. Instead, we want to know words that were commonly used by the employers.<br>

Figure 2 shows the top 12 words with the highest average TFIDF. The term "yc" and "hiring" scored the highest. This indicated that they almost existed in all samples.
While the employers in our dataset used "hiring" in their job descriptions, "yc" was a code assigned by the sample website to the employers.<br>

Next highest average TFIDF words were "engineers", "engineer" and "senior". This reflected that most of our employers were looking for engineers or senior engineers.
If we say this dataset was a sample of the job market, this result would conclude that relevant work experience is important in the job market.<br>

For the rest of the words, we don't go through them one by one. We could still notice that "software", "remote" and "London" are on the list. 
Thus, we can say that the employers were looking for software related professionals, the jobs were usually remote or based in London.
![Figure 2. Top 12 words of highest average TFIDF](https://github.com/KaverH/Web-Scraper-1/blob/main/TFIDF_12.png)
*Figure 2. Top 12 words with highest average TFIDF*

## Conclusions
In conclusion, if our dataset was a sample of the job market, most of the employers were looking for senior engineers and engineers who were professional in building software products.
The jobs were usually remote or based in London.
