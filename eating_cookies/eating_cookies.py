"""
Input: an integer
Returns: an integer
"""


# def eating_cookies(n, p):

#     if n <= 1:
#         return 1
#     elif n == 2:
#         return 2

#     return (
#         eating_cookies(n - 1, p) + eating_cookies(n - 2, p) + eating_cookies(n - 3, p)
#     )


def eating_cookies(n, p=[]):
    if n <= 1:
        return 1
    else:
        num_ways = [0] * (n + 1)
        num_ways[0] = 1
        num_ways[1] = 1
        num_ways[2] = 2

        for i in range(3, n + 1):
            num_ways[i] = num_ways[i - 1] + num_ways[i - 2] + num_ways[i - 3]

        return num_ways[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies"
    )
