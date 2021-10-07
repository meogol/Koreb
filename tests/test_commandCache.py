from Controller.cache.commandCache import CommandCache


def test_append_to_cache():
    dictionary = [[1, 5, 8], [1, 5, 8], [2, 3, 4], [2, 1, 4], [3, 3, 4], [2, 5, 4]]
    expect = [[1, 5, 8], [2, 3, 4], [2, 1, 4], [3, 3, 4], [2, 5, 4]]
    t_append = CommandCache()
    for item in dictionary:
        t_append.append_to_cache(item)
        match = [i.commands for i in t_append.cache_predicted]
    assert expect == match
