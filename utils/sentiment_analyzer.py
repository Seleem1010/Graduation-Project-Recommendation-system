
from joblib import load
import string
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
loaded_joblib_model = load(filename="utils/Sentiment_Analysis_unigram.joblib")
feats = loaded_joblib_model.feature_names
feats_len = len(feats)


def sentiment_analyzer(sent):
    lemmatizer = WordNetLemmatizer()
    sent = sent.lower()
    sent = sent.translate(str.maketrans('', '', string.punctuation))
    filtered_sentence = []
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(sent)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    lemmatized_output = []
    lemmatized_output = [lemmatizer.lemmatize(w) for w in filtered_sentence]

    sent_features = []
    sent_dict = {}
    for word in lemmatized_output:
        if not word in sent_dict:
            sent_dict[word] = 0
        sent_dict[word] = sent_dict[word] + 1
    for i in range(feats_len):
        if not feats[i] in sent_dict:
            sent_features.append(0)
        else:
            sent_features.append(sent_dict[feats[i]])
    joblib_y_preds = loaded_joblib_model.predict([sent_features])
    return joblib_y_preds[0]
