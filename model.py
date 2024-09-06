import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
class AVML:

    
    nltk.download('stopwords')
    nltk.download('punkt')
    
    def __init__(self):
        self.cv = CountVectorizer( stop_words='english' )
        self.vectors = None
        self.df = None
        self.ps = PorterStemmer() 

    def train(self,df):
        df['words'] = df[['Herb' , 'Benefits' ,'Medicinal_Uses']].apply(lambda row :', '.join(row.values.astype(str)),axis=1)
        df['words'] = df['words'].apply(self.transform_text)
    
        self.df =df
        self.vectors = self.cv.fit_transform(self.df['words']).toarray()   

    def recommend(self,input ,top_n=3):
        trans_input = self.transform_text(input)
        vector_input = self.cv.transform([trans_input])

        similarity_scores = cosine_similarity(vector_input ,self.vectors).flatten()
        top_indx = similarity_scores.argsort()[-top_n:][::-1]
        
        recomend = self.df.iloc[top_indx].reset_index()
        similarity = similarity_scores[top_indx]
        return recomend , similarity
        

    def transform_text(self,text):
        text = text.lower()
        text = text.replace(r',', '')
        text = nltk.word_tokenize(text)
        
        y = []
    
        for i in text:
            if i not in stopwords.words('english') and i not in string.punctuation:
                y.append(i)
             
        text = y[:]
        y.clear()
        for i in text:
            y.append(self.ps.stem(i))
        
        return ' '.join(y)
