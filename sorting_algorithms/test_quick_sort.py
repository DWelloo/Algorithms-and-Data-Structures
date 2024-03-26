from quick_sort import quick_sort


def test_quick_sort_int():
    list_of_values = [53, 0, -3, 1000, 8, 235, 12, 83, 1, 99]
    sorted_list = [-3, 0, 1, 8, 12, 53, 83, 99, 235, 1000]
    assert quick_sort(list_of_values) == sorted_list


def test_quick_sort_float():
    list_of_values = [-15.95, 2045.0, -267.23, 82.5, 67.114,
                      -8.4, 3.14, 15.0, 35.1384, 0]
    sorted_list = [-267.23, -15.95, -8.4, 0, 3.14, 15.0, 35.1384,
                   67.114, 82.5, 2045.0]
    assert quick_sort(list_of_values) == sorted_list


def test_quick_sort_string():
    list_of_values = ["Anatolli", "(Oh my!", "aboba", "Roman", "PROI",
                      "13214235345", ")))", "XD", "Skam", "PIPR"]
    sorted_list = ['(Oh my!', ')))', '13214235345', 'Anatolli',
                   'PIPR', 'PROI', 'Roman', 'Skam', 'XD', 'aboba']
    assert quick_sort(list_of_values) == sorted_list


def test_quick_sort_float_and_int():
    list_of_values = [-15.95, 2045.0, 14, 82.5, 67.114,
                      53, 0, -3, 1000, 8]
    sorted_list = [-15.95, -3, 0, 8, 14, 53, 67.114, 82.5, 1000, 2045.0]
    assert quick_sort(list_of_values) == sorted_list
