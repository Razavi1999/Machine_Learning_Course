data['stopwords_removed'] = data.apply(lambda x: remove_stopwords(x['tokenized']), axis=1)
data[['ReviewBody', 'stopwords_removed']].head()

"""# Stemming"""

data['porter_stemmed'] = data.apply(lambda x: apply_stemming(x['stopwords_removed']), axis=1)
# data[['Review', 'porter_stemmed']].head()

data[['ReviewBody', 'porter_stemmed']].tail()

data['ReviewBodyPreProcess'] = data['porter_stemmed']

# data.insert(7 , 'RemovedStopWords' , '')

# data['RemovedStopWords'] = data.apply(lambda x: remove_stopwords(x['ReviewBody']), axis=1)

# data.head()

data.drop('RemovedStopWords' , axis = 1)

"""# Exporting from dataframe"""

data.to_csv("BA_AirlineReviews_output.csv" , index = False)
