'''
Quick Sort

Лучший случай: O(n log n). Это происходит, когда опорный элемент
является медианным элементом массива, и каждое разделение делится 
на две равные части.

Средний случай: O(n log n). В среднем случае быстрая сортировка 
работает быстрее, чем большинство других алгоритмов сортировки, 
потому что массив разбивается на две части, каждая из которых 
сортируется отдельно.

Худший случай: O(n²). Это происходит, когда опорный элемент является 
наименьшим или наибольшим элементом массива, и каждое разделение создает
массивы, содержащие только один элемент.

'''


def partition(nums, low, high):

    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):

    def _quick_sort(items, low, high):
        if low < high:

            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

random_list_of_nums = [22, 5, 1, 18, 99]
quick_sort(random_list_of_nums)
print(random_list_of_nums)
