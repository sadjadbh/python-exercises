"""
Exercise: Magic Number Classification

Problem:
In the land of wizards, there's an old spell that defines special properties for numbers:

- If a number is divisible by 3, it is considered "Magical".
- If a number is divisible by 5, it is considered "Cursed".
- If a number is divisible by both 3 and 5, it is considered "Legendary".
- Otherwise, the number is considered "Ordinary".

Write a program that reads an integer from input and classifies it based on the rules above.

Input:
- An integer `n` (no specific bounds given).

Output:
- If `n` is divisible by 3: print "Magical"
- If `n` is divisible by 5: print "Cursed"
- If `n` is divisible by both: print "Legendary"
- Otherwise: print "Ordinary"

Sample Input 1:
9

Sample Output 1:
Magical

Sample Input 2:
10

Sample Output 2:
Cursed
"""


def classify_number(n: int) -> str:
    """
    Classifies a number as Magical, Cursed, Legendary, or Ordinary.
    """
    if n % 15 == 0:
        return "Legendary"
    elif n % 3 == 0:
        return "Magical"
    elif n % 5 == 0:
        return "Cursed"
    else:
        return "Ordinary"


def main():
    """
    Reads input, classifies the number, and prints the result.
    """
    num = int(input("Enter an integer: "))
    result = classify_number(num)
    print(result)


if __name__ == "__main__":
    main()
