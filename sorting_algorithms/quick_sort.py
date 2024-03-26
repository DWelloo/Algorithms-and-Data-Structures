import gc
import time


def quick_sort(list):
    if len(list) < 2:
        return list
    sorted_list = []
    main_index = int(len(list)//2)
    lists = sort(list[main_index], list)
    left_list = quick_sort(lists[0])
    right_list = quick_sort(lists[1])
    sorted_list = left_list + right_list
    return sorted_list


def sort(main_value, list):
    new_left_list = []
    new_right_list = []
    if min(list) == main_value:
        list.remove(main_value)
        return [[main_value], list]
    for element in list:
        if element >= main_value:
            new_right_list.append(element)
        else:
            new_left_list.append(element)
    return [new_left_list, new_right_list]


def file_reader(file, max_counter=0):
    words = []
    with open(file) as fl:
        for line in fl:
            spl = line.split()
            for sp in spl:
                words.append(sp)
                if len(words) == max_counter:
                    break
            if len(words) == max_counter:
                break
    return words


def main(max_counter):
    gc_old = gc.isenabled()
    gc.disable()

    file = "pan-tadeusz-unix.txt"
    list_of_words = file_reader(file, max_counter)

    start = time.process_time()

    sorted_list = quick_sort(list_of_words)

    stop = time.process_time()
    print('Czas wykonania w sekundach (quick_sort):', stop - start)

    if gc_old:
        gc.enable()

    return [stop - start, sorted_list]


if __name__ == "__main__":
    sorted_list = main(10000)[1]
    with open("sorted.txt", 'w') as srt:
        counter = 1
        for word in sorted_list:
            counter += 1
            srt.write(word)
            srt.write(" ")
            if counter == 15:
                srt.write('\n')
                counter = 1
