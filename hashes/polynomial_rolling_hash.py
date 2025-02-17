"""
Polynomial Rolling Hash Algo -->
Polynomial rolling hash function is a hash
function that uses only multiplications and additions.

Time Complexity: O(N)

Auxiliary Space: O(1)

Wikipedia link: https://en.wikipedia.org/wiki/Rolling_hash

"""


class Hash:
    def __init__(self, input_str: str) -> None:
        self.hash_value = 0
        self.p, self.m = 31, 10**9 + 7
        self.length = len(input_str)
        hash_so_far = 0
        p_pow = 1
        for i in range(self.length):
            hash_so_far = (
                hash_so_far + (1 + ord(input_str[i]) - ord("a")) * p_pow
            ) % self.m
            p_pow = (p_pow * self.p) % self.m
        self.hash_value = hash_so_far

    def __eq__(self, other):
        return self.hash_value == other.hash_value


if __name__ == "__main__":
    s = "thealgorithms_python"
    h = Hash(s)
    print(f"Hash value of {s} is {h.hash_value}")
