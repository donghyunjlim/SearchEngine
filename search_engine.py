import os
from document import Document
from operator import itemgetter
import math
from util_function import normalize_token


class SearchEngine:
    """
    Contains an initializer that takes a str path
    and methods: _calculate_idf, search
    """
    def __init__(self, path):
        """
        Takes a str path and precompute the inverted index,
        a dictionary associating each str term to the list of
        Document objects that include the term.
        """
        self._filenames = os.listdir(path)
        self._inverted_index = {}
        for filename in self._filenames:
            x = Document(os.path.join(path, filename))
            for word in x.get_words():
                if word not in self._inverted_index:
                    self._inverted_index[word] = []
                if word in self._inverted_index:
                    self._inverted_index[word].append(x)

    def _calculate_idf(self, term):
        """
        Takes a str term and returns the inverse document
        frequency of the term. If the term not in the corpus,
        return 0.
        """
        if term not in self._inverted_index:
            return 0
        else:
            doc = self._inverted_index[term]
            num_document = len(doc)
            self._inverse_doc_frq = math.log(
                (len(self._filenames) / num_document))
            return self._inverse_doc_frq

    def search(self, query):
        """
        Takes a str query that contains one or more terms.
        returns a list of document paths sorted in descending
        order by tf-idf value. If no matching documents,
        return an empty list.
        """
        tfidf_dict = {}
        # Initialize a dictionary that has documents as keys
        # and tfidfs as values
        for word in query.split():
            word = normalize_token(word)
            if word in self._inverted_index:
                idf = self._calculate_idf(word)
                doc = self._inverted_index[word]
                for document in doc:
                    doc_name = document.get_path()
                    tf = document.term_frequency(word)
                    tfidf = tf * idf
                    if doc_name not in tfidf_dict:
                        tfidf_dict[doc_name] = []
                    tfidf_dict[doc_name].append(tfidf)
        if len(tfidf_dict) == 0:
            return []
        else:
            for tfidf_doc in tfidf_dict:
                tfidf_dict[tfidf_doc] = sum(tfidf_dict[tfidf_doc])

            tfidf_tuple = [(k, v) for k, v in tfidf_dict.items()]
            sorted_tuple = sorted(tfidf_tuple, reverse=True, key=itemgetter(1))
            result = []
            for tuples in sorted_tuple:
                result.append(tuples[0])
            return result