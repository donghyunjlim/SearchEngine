from util_function import assert_equals

from document import Document
from search_engine import SearchEngine


def test_document(file1, file2):
    """
    tests the Document class and its functions
    """
    assert_equals(0, file1.term_frequency("hi"))
    assert_equals(0.2, file1.term_frequency("DOGS"))
    assert_equals("/Users/donghyunlim/Desktop/GithubPortfolio/SearchEngine/testfile1.txt", file1.get_path())
    assert_equals("/Users/donghyunlim/Desktop/GithubPortfolio/SearchEngine/testfile2.txt", file2.get_path())
    assert_equals(
        ["dogs", "are", "the", "greatest", "pets"], file1.get_words())
    assert_equals(
        ["cats", "are", "just", "okay"], file2.get_words())


def test_search_engine(search):
    """
    tests the Search Engine class and its functions
    """
    assert_equals(0, search._calculate_idf("dog"))
    assert_equals(1.0986122886681098, search._calculate_idf("cats"))
    assert_equals(
        ['/Users/donghyunlim/Desktop/GithubPortfolio/SearchEngine/testfile3.txt', 
         '/Users/donghyunlim/Desktop/GithubPortfolio/SearchEngine/testfile1.txt'], search.search(
            "love dogs"))


def main():
    DOCUMENT1 = Document("/Users/donghyunlim/Desktop/GithubPortfolio/SearchEngine/testfile1.txt")
    DOCUMENT2 = Document("/Users/donghyunlim/Desktop/GithubPortfolio/SearchEngine/testfile2.txt")
    SEARCH = SearchEngine("files")
    test_document(DOCUMENT1, DOCUMENT2)
    test_search_engine(SEARCH)


if __name__ == '__main__':
    main()