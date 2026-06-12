## Python Fundamentals
### A. Strings
1. Reverse String
Write a function that takes a string as input and returns it reversed.
Example: reverse_string("hello") → "olleh"<br>

2. Count Vowels
Write a function that counts the number of vowels (a, e, i, o, u) in a string.
Example: count_vowels("hello") → 2 <br>

3. Palindrome Check
Write a function that checks if a string is a palindrome (case-insensitive).
Example: is_palindrome("Racecar") → True <br>

4. Word Frequency
Write a function that takes a string and returns a dictionary containing the frequency of each word.
Example: word_frequency("the cat the dog") → {"the": 2, "cat": 1, "dog": 1}<br>

5. Character Frequency
Write a function that returns a dictionary containing the frequency of each character in a string.
Example: count_chars("hello") → {'h': 1, 'e': 1, 'l': 2, 'o': 1}<br>

6. Join Words
Write a function that takes a list of words and joins them into a single string using spaces.
Example: join_words(["hello", "world"]) → "hello world"<br>

7. Remove Punctuation
Write a function that removes all punctuation characters from a string.
Example: remove_punctuation("Hi, there!") → "Hi there"<br>


8. Anagram Check
Write a function that checks whether two strings are anagrams of each other (case-insensitive, ignoring spaces).
Example: are_anagrams("Listen", "Silent") → True<br>

9. Longest Word
Write a function that returns the longest word in a sentence.
Example: longest_word("I love machine learning") → "learning"<br>

10. First Non-Repeating Character
Write a function that returns the first character that appears only once in a string.
Example: first_non_repeating("swiss") → "w"<br>

---
Insertion, Deletion for List, Dictionary and Set.
Also Set and Tuple definition
---

### B. Lists
11. Sum of List
Write a function that takes a list of numbers and returns their sum.
Example: sum_list([1, 2, 3, 4]) → 10<br>

12. Find Maximum
Write a function that takes a list of numbers and returns the maximum value.
Example: find_max([3, 1, 4, 1, 5]) → 5<br>

13. Remove Duplicates
Write a function that removes duplicate elements from a list.
Example: remove_duplicates([1, 2, 2, 3, 4, 4]) → [1, 2, 3, 4]<br>

14. Rotate List
Write a function that rotates a list to the right by k positions using slicing.
Example: rotate_list([1, 2, 3, 4, 5], 2) → [4, 5, 1, 2, 3]<br>

15. Flatten Nested List
Write a function that flattens a list of lists into a single list.
Example: flatten_list([[1, 2], [3, 4]]) → [1, 2, 3, 4]<br>

16. List Interaction
Write a function that returns unique elements common to two lists.
Example: list_intersection([1, 2, 3], [2, 3, 4]) → [2, 3]<br>

17. Average of List
Write a function that returns the arithmetic mean of a list. Return None for an empty list.
Example: average_list([4, 8]) → 6.0<br>

18. Square Odd numbers (List Comprehension)
Write a function that squares odd numbers in a list using list comprehension.
Example: square_odds([1, 2, 3, 4]) → [1, 2, 9, 4]<br>

19. Move Zeroes
Write a function that moves all zeroes to the end of the list while maintaining the order of non-zero elements.
Example: move_zeroes([0, 1, 0, 3, 12]) → [1, 3, 12, 0, 0]<br>

---

### C. Dictionaries
20. Merge Two Dictionaries
Write a function that merges two dictionaries. If duplicate keys exist, values from the second dictionary should override the first.
Example: merge_dicts({'a': 1}, {'a': 2, 'b': 3}) → {'a': 2, 'b': 3}<br>

21. Frequency Count of Elements
Write a function that returns the frequency count of elements in a list.
Example: frequency_count([1, 2, 2, 3]) → {1: 1, 2: 2, 3: 1}<br>

22. Sort List of Dictionaries by Key
Write a function that sorts a list of dictionaries by the "name" key in ascending order.
Example: [{"name": "Bob"}, {"name": "Alice"}] → [{"name": "Alice"}, {"name": "Bob"}]<br>
---

### D. Basic Logic
23. Even/Odd
Write a function that returns "even" if a number is even and "odd" if it is odd.
Example: check_even_odd(5) → "odd"<br>

24. Factorial
Write a function that computes the factorial of a non-negative integer.
Example: factorial(5) → 120<br>

25. Second Largest Element
Write a function that returns the second-largest unique element in a list.
Example: second_largest([4, 1, 7, 7, 3]) → 4<br>

26. Leap Year
Write a function that determines whether a year is a leap year.
Example: is_leap_year(2000) → True<br>

---

### E. Mathematical Algorithms
27. Prime Check
Write a function that checks whether an integer is prime.
Example: is_prime(11) → True<br>

28. List of Primes
Write a function that returns all prime numbers less than or equal to a given limit.
Example: list_primes(10) → [2, 3, 5, 7]<br>

29. GCD 
Write a function that returns the greatest common divisor of two integers.
Example: gcd(48, 18) → 6<br>

30. LCM
Write a function that returns the least common multiple of two integers.
Example: lcm(4, 6) → 12<br>

31. Fibonacci Number
Write a function that returns the nth Fibonacci number (0-indexed).
Example: fibonacci(7) → 13<br>

32. Generate Fibonacci Series
Write a function that generates the first n Fibonacci numbers.
Example: generate_fibonacci(5) → [0, 1, 1, 2, 3]<br>

33. Reverse Number 1234
Write a function that reverses the digits of an integer.
Example: reverse_number(1234) → 4321<br>


## F. Important DSA Interview Question
34. Two Sum
Write a function that returns the indices of two numbers whose sum equals a target value.
Example: two_sum([2, 7, 11, 15], 9) → [0, 1]<br>

35. Valid Parentheses
Write a function that checks whether a string containing brackets is valid.
Example: is_valid_parentheses("()[]{}") → True<br>

36. Find Duplicate Using Set
Write a function that finds the first duplicate element in a list using a set.
Example: find_duplicate([1, 3, 4, 2, 2]) → 2<br>

### G. Sorting
37. Bubble Sort
Write a function that sorts a list using the Bubble Sort algorithm.
Example: bubble_sort([5, 3, 8, 1]) → [1, 3, 5, 8]<br>

38. Merge Sort
Write a function that sorts a list using the Merge Sort algorithm.
Example: merge_sort([5, 3, 8, 1]) → [1, 3, 5, 8]<br>

39. Quick Sort
Write a function that sorts a list using the Quick Sort algorithm.
Example: quick_sort([5, 3, 8, 1]) → [1, 3, 5, 8]<br>