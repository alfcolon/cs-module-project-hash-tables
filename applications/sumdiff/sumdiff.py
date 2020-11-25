"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
import time


q = list(range(1, 10))
q = list(range(1, 200))
#q = (1, 3, 4, 7, 12)
q_len = len(q)

def f(x):
    return x * 4 + 6

def find_largest_differences(values_dictionary):
    largest_differences_dictionary = {}
    largest_number = q[q_len - 1]
    
    i = q_len - 1
    while i >= 0:
        current_number = q[i]
        difference = values_dictionary[largest_number] - values_dictionary[current_number]
        largest_differences_dictionary[difference] = [largest_number, current_number]
        i -= 1
    return largest_differences_dictionary

def q_element_function_values():
    q_element_function_values_dictionary = {}
    for number in q:
        q_element_function_values_dictionary[number] = f(number)
    return q_element_function_values_dictionary

def sum_diff():
    # get dictionary of all f(x) values
    # time complexity O(n)
    q_element_function_values_dictionary = q_element_function_values()
    # get dictionary of largest differences
    # time complexity O(n)
    largest_differences_dictionary = find_largest_differences(q_element_function_values_dictionary)
    # check if each combination of elements in q's sum is in the largest_differences_dictionary
    # time complexity O(n^2)
    count = 0
    i = 0
    while i < q_len:
        left_operand = q[i]
        j = 0
        while j < q_len:
            right_operand = q[j]
            sum = q_element_function_values_dictionary[left_operand] + q_element_function_values_dictionary[right_operand]
            if sum in largest_differences_dictionary:
                count += 1
                difference_left_operand = largest_differences_dictionary[sum][0]
                difference_right_operand = largest_differences_dictionary[sum][1]
                f_difference_left_operand = q_element_function_values_dictionary[difference_left_operand]
                f_difference_right_operand = q_element_function_values_dictionary[difference_right_operand]
                f_sum_left_operand = q_element_function_values_dictionary[left_operand]
                f_sum_right_operand = q_element_function_values_dictionary[right_operand]
#                print(f'f({left_operand})' + " + " + f'f({right_operand})' + " = "
#                + f'f({difference_left_operand})' + " - " + f'f({difference_right_operand})'
#                + "\t" + f'{f_sum_left_operand}' + " + " + f'{f_sum_right_operand}' + " = "
#                + f'{f_difference_left_operand}' + " - " + f'{f_difference_right_operand}')
            j += 1
        i += 1

def f2(x):
    return x * 4 + 6
    
def classsumdiff():
    cache = {}

    add_cache = {}
    subtract_cache = {}

    results = {}

    # Log all values from f(x) in a cache
    for i in q:
        if i not in cache:
            cache[i] = f2(i)

    cache_list = sorted(cache.items())

    # Iterate through numbers in cache and log all a + b possibilities
    for f in range(len(cache_list)):
        add_cache[(cache_list[f][0], cache_list[f][0])] = cache_list[f][1] + cache_list[f][1]

        for s in range(len(cache_list)):
            add_cache[(cache_list[f][0], cache_list[s][0])] = cache_list[f][1] + cache_list[s][1]

    # Iterate through numbers in cache and log all c-d possibilites
        if f != s and s < len(cache_list):
            subtract_cache[(cache_list[s][0], cache_list[f][0])] = cache_list[s][1] - cache_list[f][1]

    # Compare the add and subtract caches to find where the values are equal
    for value in add_cache.items():
        if value[1] in subtract_cache.values():
            keys = list(subtract_cache.keys())[list(subtract_cache.values()).index(value[1])]

            for key in range(1, len(keys)):
                results[(value[0], value[1])] = ((keys[key - 1], keys[key]), subtract_cache[(keys[key - 1], keys[key])])

    # Calculate results
    results_list = sorted(results.items())

    for result in results_list:
        a = result[0][0][0]
        b = result[0][0][1]
        c = result[1][0][0]
        d = result[1][0][1]

        a_result = cache[a]
        b_result = cache[b]
        c_result = cache[c]
        d_result = cache[d]

start = time.time()
i = 0
while i < 100:
    sum_diff()
    i += 1
end = time.time()
print(end - start)
start = time.time()
i = 0
while i < 100:
    classsumdiff()
    i += 1
end = time.time()
print(end - start)
