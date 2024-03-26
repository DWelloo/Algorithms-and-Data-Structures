import gc
import time


def selection_sort(arr):
    for i in range(len(arr)):
        min_val=i
        for j in range(i,len(arr)):
            if arr[j] < arr[min_val]:
                min_val = j
        arr[i],arr[min_val]=arr[min_val],arr[i]
    return arr


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

    sorted_list = selection_sort(list_of_words)

    stop = time.process_time()
    print('Czas wykonania w sekundach (selection_sort):', stop - start)

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
