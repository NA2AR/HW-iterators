import types


def flat_generator(list_of_lists):
    cursor_l = 0
    cursor_i = 0
    while cursor_l != len(list_of_lists):
        yield list_of_lists[cursor_l][cursor_i]
        cursor_i += 1
        if cursor_i == len(list_of_lists[cursor_l]):
            cursor_l += 1
            cursor_i = 0
    StopIteration


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()

# for i in flat_generator(list_of_lists_1):
#     print(i)

