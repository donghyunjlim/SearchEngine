from util_function import normalize_token


class Document:
    """
    Contains an initializer that takes a path to a
    document and methods: term_frequency, get_path, get_words.
    """
    def __init__(self, document):
        """
        Takes a document path and precompute the term-frequency
        for each term in the document by constructing a dictionary.
        """
        self._document = document
        self._dictionary = {}
        with open(document) as f:
            for line in f.readlines():
                words = line.split()
                for word in words:
                    normalized = normalize_token(word)
                    if normalized not in self._dictionary:
                        self._dictionary[normalized] = 1
                    else:
                        self._dictionary[normalized] += 1

        total = sum(self._dictionary.values())
        for key in self._dictionary:
            self._dictionary[key] = self._dictionary[key] / total

    def term_frequency(self, term):
        """
        takes a str term and returns the term frequency of
        a given term by looking it up in the dictionary from
        the initializer. If a tern not in a given document,
        term frequency is 0.
        """
        word = normalize_token(term)
        if word in self._dictionary:
            return (self._dictionary[word])
        else:
            return 0

    def get_path(self):
        """
        returns the path of the file that the current document
        represents.
        """
        return self._document

    def get_words(self):
        """
        returns a list of the unique, normalized words in the
        current document.
        """
        return (list(self._dictionary.keys()))