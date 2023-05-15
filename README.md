This code is for performing sentiment analysis on Twitter data using LDA and Logistic Regression models. The code consists of several parts:

Data preprocessing: The data is preprocessed using regular expression tokenizer, stop words remover, and bag of words count. The output is a dataset with features and label columns.

LDA model training: The dataset is used to train an LDA model with a specified number of topics.

Topic distributions: The trained LDA model is used to compute the topic distribution of each tweet in the dataset.

Model training: A logistic regression model is trained on each subset of tweets that has a high probability for a particular topic.

Sentiment estimation: For a given tweet, the logistic regression models are used to estimate the sentiment probabilities for each topic. The sentiment estimation for the tweet is set to the one with the highest probability.

This paradigm has been compared with simple Machine Learning Models such as LogisticRegression, Naive Bayes, Random Forest and Decision Tree classifiers.

The paradigm performs better than all of them.
