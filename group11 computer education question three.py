#Question 3
print("\n Question 3i: Array Index Access ")
A = [10, 20, 30, 40, 50]
for i in range(5):
    print(f"Index {i}: {A[i]}")

print("\n Question 3ii: Append to Array ")
A= [1, 2, 3,4,5]
A.append(int(input("Enter a number to append for Q3ii : ")))
print(f"Updated Array: {A}")

print("\nQuestion 3iii: String Length Calculator ")
str_input = input("Enter a string name: ")
print(f"Length: {len(str_input)}")

print("\n Question 3iv: Largest Number Finder ")
nums = [45, 23, 67, 12, 89, 34]
print(f"Largest in {nums}: {max(nums)}")
print()
print()