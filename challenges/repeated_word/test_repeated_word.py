from .repeated_word import repeated_word
import pytest


def test_repeated_word1():
    tmp = repeated_word("Once upon a time, there was a brave princess who...")
    assert tmp == 'a'


def test_repeated_word2():
    tmp = repeated_word("It was the best of times, it was the worst of times, \
    it was the age of wisdom, it was the age of foolishness, it was the epoch \
    of belief, it was the epoch of incredulity, it was the season of Light, \
    it was the season of Darkness, it was the spring of hope, it was the winter \
    of despair, we had everything before us, we had nothing before us, we were \
    all going direct to Heaven, we were all going direct the other way – in short,\
     the period was so far like the present period, that some of its noisiest \
     authorities insisted on its being received, for good or for evil, in the \
     superlative degree of comparison only...")
    assert tmp == 'it'


def test_repeated_word3():
    tmp = repeated_word("It was a queer, sultry summer, the summer they electrocuted \
    the Rosenbergs, and I didn’t know what I was doing in New York...")
    assert tmp == 'summer'


def test_bad_input():
    with pytest.raises(TypeError) as t:
        repeated_word(234)
        # import pdb; pdb.set_trace()
        assert 'please input in the type of string.' in str(t.value)
