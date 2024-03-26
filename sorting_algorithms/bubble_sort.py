import gc
import time


def bubble_sort(list):
    sorted_list = []
    for element in list:
        counter = 0
        for index in range(len(list) - counter):
            if index == len(list) - 1:
                break
            if list[index] > list[index + 1]:
                temp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = temp
        counter += 1
    sorted_list = list
    return sorted_list


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

    sorted_list = bubble_sort(list_of_words)

    stop = time.process_time()
    print('Czas wykonania w sekundach (bubble_sort):', stop - start)

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
