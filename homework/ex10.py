from ex9 import get_even_list

even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
    print(even_list)
else:
    print("Ooops, bugs detected")

