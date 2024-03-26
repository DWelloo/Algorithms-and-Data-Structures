from matplotlib import pyplot as plt
import quick_sort
import merge_sort
import selection_sort
import bubble_sort
import sys


sys.setrecursionlimit(10000)


def create_graph(sort_ways):
    for sort_way in sort_ways:
        list_of_times = {}
        max_counter = 100
        for i in range(11):
            list_of_times[f'{max_counter}'] =\
                f'{sort_way.main(max_counter)[0]}'
            if max_counter == 100:
                max_counter = 1000
            else:
                max_counter += 1000
        times = [float(time) for time in list_of_times.values()]
        quantities = [quantity for quantity in list_of_times.keys()]
        plt.plot(quantities, times, 'o-',
                 label=sort_ways[sort_way], markersize=3)
        plt.xlabel("Word\'s quantitties")
        plt.ylabel("Time")
        plt.legend()
        plt.title(label=f'{sort_ways[sort_way]}')
        plt.savefig(f'{sort_ways[sort_way]}.png')
        plt.close()


graphs = {
    quick_sort: 'quick_sort',
    merge_sort: 'merge_sort',
    selection_sort: 'selection_sort',
    bubble_sort: 'bubble_sort',

}
create_graph(graphs)
