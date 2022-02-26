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


def rotateLeft(d, arr):
    return arr[d:] + arr[:d]


def rotatedLeft(d, arr):
    size = len(arr)
    rotated_arr = [] * size
    i = 0
    rotate_index = d

    while rotate_index < size:
        rotated_arr[i] = arr[rotate_index]
        i += 1
        rotate_index += 1

    rotate_index = 0
    while rotate_index < d:
        rotated_arr[i] = arr[rotate_index]
        i += 1
        rotate_index += 1

    return rotated_arr


# Medium
def matchingStrings(strings, queries):
    count = 0
    arr = [0] * len(queries)
    for i in range(len(queries)):
        count = strings.count(queries[i])
        arr[i] = count
    return arr


# Long version
def matchingStringsx(strings, queries):
    count = 0
    arr = [0] * len(queries)
    for i in range(len(queries)):
        count = 0
        for j in range(len(strings)):
            if queries[i] == strings[j]:
                count += 1
        arr[i] = count
    return arr


# Hard
# Short version
def arrayManipulation(n, queries):
    base_arr = [0] * (n + 2)
    max_num = temp = 0
    for a, b, k in queries:
        base_arr[a] += k
        base_arr[b + 1] -= k
    for x in base_arr:
        temp += x
        max_num = max(max_num, temp)
    return max_num


def printLinkedList(head):
    if head is None:
        return

    while head is not None:
        print(head.data)
        head = head.next

    return


def insertNodeAtTail(head, data):
    # new_node = SinglyLinkedListNode(data)
    new_node = data
    current = head
    if head is None:
        head = new_node
        return head

    while current.next is not None:
        current = current.next

    current.next = new_node
    return head


def insertNodeAtHead(llist, data):
    # new_node = SinglyLinkedListNode(data)
    new_node = data
    current = llist
    if llist is None:
        llist = new_node
        return llist

    llist = new_node
    llist.next = current

    return llist


# Short version
def insertNodeAtHeadShort(llist, data):
    # new_node = SinglyLinkedListNode(data)
    new_node = data
    current = llist
    if llist is None:
        llist = new_node
        return llist

    new_node.next = llist
    return new_node


def insertNodeAtPosition(llist, data, position):
    # new_node = SinglyLinkedListNode(data)
    new_node = data
    current_node = llist
    index = 0

    while index < position - 1:
        current_node = current_node.next
        index += 1

    new_node.next = current_node.next
    current_node.next = new_node

    return llist


def deleteNode(llist, position):
    index = 0
    current_node = llist
    if llist is None:
        return llist
    if position == 0:
        return llist.next

    while index < position - 1:
        current_node = current_node.next
        index += 1

    current_node.next = current_node.next.next
    return llist


def reversePrint(llist):
    if llist is None:
        return

    reversePrint(llist.next)
    print(llist.data)


def reverseLinkedList(head):
    current = head
    prev = None
    next = head.next

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head


def compare_lists(llist1, llist2):
    while llist1 and llist2:
        if llist1.data == llist2.data:
            llist1 = llist1.next
            llist2 = llist2.next
        else:
            return 0
    if llist1 is None and llist2 is None:
        return 1
    else:
        return 0


# import sys
# sys.setrecursionlimit(10000)
# Recursion
def mergeLists(head1, head2):
    if head1 == None and head2 == None:
        return None

    if head1 == None:
        return head2
    if head2 == None:
        return head1

    if head1.data < head2.data:
        temp = head1
        temp.next = mergeLists(head1.next, head2)

    else:
        temp = head2
        temp.next = mergeLists(head1, head2.next)

    return temp


# Without recursion but might have some faults
def mergeLists(head1, head2):
    if head1 is None and head2 is None:
        return None

    if head1 is None:
        return head2
    if head2 is None:
        return head1

    head3 = None
    if head1.data < head2.data:
        head3 = head1
        head1 = head1.next
    else:
        head3 = head1
        head1 = head1.next

    current_node = head3

    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            current_node.next = head1
            head1 = head1.next
        else:
            current_node.next = head2
            head2 = head2.next

        current_node = current_node.next

    if head1 is None:
        current_node.next = head2
    else:
        current_node.next = head1

    return head3


# Might not work
def getNode(llist, positionFromTail):
    pointer_node = llist
    count = 0

    while llist != None:
        llist = llist.next
        if count < positionFromTail:
            count += 1
        else:
            pointer_node = pointer_node.next

    return pointer_node.data


# This one works
def getNode(llist, positionFromTail):
    pointer1 = llist
    pointer2 = llist

    for i in range(positionFromTail):
        pointer1 = pointer1.next

    while pointer1.next != None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer2.data


def removeDuplicates(llist):
    if llist is None:
        llist

    new_head = llist

    while new_head.next != None:
        if new_head.data == new_head.next.data:
            new_head.next = new_head.next.next
        else:
            new_head = new_head.next

    return llist


def has_cycle(head):
    if head is None: return False

    fast = head.next
    slow = head

    while fast != None and fast.next != None and slow != None:
        if fast == slow:
            return 1
        else:
            fast = fast.next.next
            slow = slow.next
    return False


def findMergeNode(head1, head2):
    head1_current = head1
    head2_current = head2

    while head1_current != head2_current:
        if head1_current.next == None:
            head1_current = head2
        else:
            head1_current = head1_current.next

        if head2_current.next == None:
            head2_current = head1
        else:
            head2_current = head2_current.next

    return head1_current.data


# Doubly linked list
def sortedInsert(llist, data):
    # node = DoublyLinkedListNode(data)

    node = data
    if llist is None:
        llist = node

    elif data < llist.data:
        node.next = llist
        llist.prev = node
        llist = node

    else:
        current = llist
        while current.next != None and current.data < data:
            current = current.next

        if current.next == None and current.data < data:
            current.next = node
            node.prev = current
        else:
            node_previous = current.prev
            node_previous.next = node
            node.prev = node_previous
            node.next = current
            current.prev = node
    return llist


# Doubly linked list
def reverse(llist):
    if llist is None: return llist

    current = llist
    new_head = llist

    while current is not None:
        prev = current.prev
        current.prev = current.next
        current.next = prev
        new_head = current
        current = current.prev

    return new_head







def testSlice():
    st = "test"
    return st[2:] + st[:2]


def testArray():
    st = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
    for a, b, k in st:
        print(f"a{a}")
        print(f'b{b}')
        print(f'k{k}')


def dataTest():
    lulli = 5
    lulli = "-@"

    print(lulli)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataTest()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
