# Extracting Important URL's from Email history

The goal is to identify if a URL in a given context (context meaning words and topics in an email), is important or not important.
This is a unsupervised learning task whose input words/topics for each link. And output is classification if email is important or not. For each link, we will consider N words before and after the link as relevant words for this email.


Here are two approaches to solve this task     
1. Calculate TF-IDF matrix for all links. And sort the links according to total TF-IDF value, sum(TF-IDF of all words). Since TF-IDF value captures importance of words in a document, the link with many important words associated with it must be important.  
2. Use Term frequency (or any other feature matrix) as an input to cluster links. Links with similar words and topic will form a cluster. The cluster then represents links which are too repetitive and similar pattern. Therefore, links which are not part of any cluster, outliers may have some novelty/importance to them.
Identifying novelty/outliers is possible with OneClassSVM - http://scikit-learn.org/stable/modules/outlier_detection.html  

This project will try both approaches and see which one performs better. All code and experiments are in notebook folder as ipython notebook. Helper scripts are also available. Sample email dataset is uploaded in easy_ham/ directory.
