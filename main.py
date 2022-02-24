# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Easy
import math


def birthdayCakeCandles(candles):
    sum = 0
    max = -100000
    for i in candles:
        if i > max:
            max = i
    for i in range(len(candles)):
        if candles[i] == max:
            sum += 1
    print(sum)


# Easy
def miniMaxSum(arr):
    sum = 0
    max = -100000000000
    min = 1000000000000

    for i in arr:
        sum += i
        if i > max:
            max = i
        if i < min:
            min = i
    print(sum - max, sum - min)


# Easy
def timeConversion(s):
    if "PM" in s:
        s = s.replace("PM", " ")
        t = s.split(":")
        if t[0] != '12':
            t[0] = str(int(t[0]) + 12)
            s = ":".join(t)
        return s
    else:
        s = s.replace("AM", " ")
        t = s.split(":")
        if t[0] == '12':
            t[0] = '00'
            s = ":".join(t)
        return s


# Medium
# either plus 1,2,5
def equal(arr):
    pos = [0, 0, 0, 0]
    mini = min(arr)
    step = 0
    diff = 0
    for i in arr:

        for j in range(4):
            diff = i - (mini - j)
            diff = diff // 5 + (diff % 5) // 2 + (diff % 5) % 2
            pos[j] += diff
    return min(pos)


# Medium
def cost(B):
    A = [0] * len(B)
    test = []
    count = 0
    for i in range(len(B)):
        count = 0
        for x in range(B[i]):
            count += 1
            test.append(count)

    print(max(test))  #


# Easy
def countApplesAndOranges(s, t, a, b, apples, oranges):
    countA = 0
    countO = 0
    for i in range(len(apples)):
        apples[i] += a

    for j in range(len(oranges)):
        oranges[j] += b

    for x in apples:
        if s <= x <= t:
            countA += 1
    for y in oranges:
        if s <= y <= t:
            countO += 1
    print(countA)
    print(countO)


# Easy
def kangaroo(x1, v1, x2, v2):
    if (x2 - x1) * (v2 - v1) < 0 and (x2 - x1) % (v2 - v1) == 0:
        return "YES"
    else:
        return "NO"


def kickstartCandy(case_num):
    (N, M) = tuple(map(int, input().split()))
    candies = list(map(int, input().split()))
    total_candy = 0
    for j in range(N):
        total_candy += candies[j]
    amount_remaining = total_candy % M
    print(f"Case #{case_num}: {amount_remaining}")


def getTotalX(a, b):
    count = 0
    for i in range(max(a), min(b) + 1):
        isFactor = True
        for ele in a:
            if i % ele != 0:
                isFactor = False
                break
        for ele in b:
            if ele % i != 0:
                isFactor = False
                break
        if isFactor:
            count += 1

    return count


def breakingRecords(scores):
    max_score = min_score = scores[0]
    max_count = min_count = 0
    for i in scores:
        if i > max_score:
            max_count += 1
            max_score = i
        elif i < min_score:
            min_count += 1
            min_score = i

    return max_count, min_count


def reverseArray(a):
    a.reverse()
    return a


def hourglassSum(arr):
    max_val = -9 * 7
    row = len(arr)
    column = len(arr[0])
    for i in range(row - 2):
        for j in range(column - 2):
            current_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][
                j + 1] + arr[i + 2][j + 2]

            if current_sum > max_val:
                max_val = current_sum

    return max_val


def dynamicArray(n, queries):
    arr = [[] for i in range(n)]
    answers = []
    lastAnswer = 0
    for q in queries:
        if q[0] == 1:
            idx = (q[1] ^ lastAnswer) % n
            arr[idx].append(q[2])
        else:
            idx = ((q[1] ^ lastAnswer) % n)
            lastAnswer = arr[idx][q[2] % len((arr[idx]))]
            answers.append(lastAnswer)
    return answers


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
