class Count_sort:

    def sort(self, array):
        l = len(array) - 1
        for i in range(len(array)):
            j = 0
            while j < l - i:
                if array[j + 1] < array[j]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                j += 1

        return array


array = list(map(int, input().split()))
object = Count_sort()
print(object.sort(array))
