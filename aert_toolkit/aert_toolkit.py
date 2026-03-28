import sys
class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

hanoi_stack = StackADT()


def factorial(n):
    if n < 0: return "Error: Negative Input" # 
    if n == 0 or n == 1: return 1
    return n * factorial(n - 1)

naive_calls = 0
memo_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1: return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_memo(n, memo={}):
    global memo_calls
    memo_calls += 1
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def hanoi(n, source, aux, dest):
    if n == 1:
        move = f"Move disk 1 from {source} to {dest}"
        hanoi_stack.push(move)
        print(move)
        return
    hanoi(n - 1, source, dest, aux)
    move = f"Move disk {n} from {source} to {dest}"
    hanoi_stack.push(move)
    print(move)
    hanoi(n - 1, aux, source, dest)

def binary_search(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)

if __name__ == "__main__":
    print("--- 1. FACTORIAL TEST CASES ---")
    for n in [0, 1, 5, 10]:
        print(f"Factorial({n}): {factorial(n)}")

    print("\n--- 2. FIBONACCI TEST CASES ---")
    for n in [5, 10, 20]:
        naive_calls = 0
        memo_calls = 0
        ans_n = fib_naive(n)
        ans_m = fib_memo(n, {})
        print(f"n={n} | Naive: {ans_n} (Calls: {naive_calls}) | Memo: {ans_m} (Calls: {memo_calls})")

    print("\n--- 3. TOWER OF HANOI (N=3) ---")
    hanoi(3, 'A', 'B', 'C')

    print("\n--- 4. BINARY SEARCH TEST CASES ---")
    arr = [1, 3, 5, 7, 9, 11, 13]
    for key in [7, 1, 13, 2]:
        print(f"Search {key} in {arr}: Index {binary_search(arr, key, 0, len(arr)-1)}")
    print(f"Search 5 in empty list []: {binary_search([], 5, 0, -1)}")
