from itertools import combinations

if __name__ == '__main__':
    word, level = input().strip().split()
    word= word.upper()
    level = int(level)
    for letter in range(1, level+1):
        l = sorted(list(combinations(sorted(word), letter)))
        for j in l:
            result = ''.join(j)
            print(result)

