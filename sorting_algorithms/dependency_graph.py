from matplotlib import pyplot as plt
import bubble_sort
import quick_sort
import merge_sort
import selection_sort


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
        if sort_way == quick_sort:
            size = 6
        else:
            size = 3
        plt.plot(quantities, times, 'o-',
                 label=sort_ways[sort_way], markersize=size)
    plt.xlabel("Word\'s quantitties")
    plt.ylabel("Time")
    plt.legend()
    plt.title(label="sorting_graphs")
    plt.savefig('sorting_graphs.png')


graphs = {
    bubble_sort: 'bubble_sort',
    quick_sort: 'quick_sort',
    merge_sort: 'merge_sort',
    selection_sort: 'selection_sort',

}
create_graph(graphs)
