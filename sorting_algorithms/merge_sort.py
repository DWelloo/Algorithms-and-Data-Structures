import gc
import time


def merge(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    i = 0
    j = 0
    arr_ans = []
    while i < l1 and j < l2:
        if arr1[i] <= arr2[j]:
            arr_ans.append(arr1[i])
            i += 1
        else:
            arr_ans.append(arr2[j])
            j += 1
    arr_ans += arr1[i:]
    arr_ans += arr2[j:]
    return arr_ans


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        half = int(len(arr)/2)
        left = merge_sort(arr[:half])
        right = merge_sort(arr[half:])
    return merge(left, right)


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

    sorted_list = merge_sort(list_of_words)

    stop = time.process_time()
    print('Czas wykonania w sekundach (merge_sort):', stop - start)

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
