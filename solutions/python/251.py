def queue_time(customers, n):
    from collections import deque
    queue = deque(customers)
    checkout_tills = [0] * n
    time = 0
    while True:
        vacant = 0
        for index, _ in enumerate(checkout_tills):
            if checkout_tills[index] > 0:
                checkout_tills[index] -= 1
            if checkout_tills[index] == 0:
                if len(queue) > 0:
                    checkout_tills[index] = queue.popleft()
                else:
                    vacant += 1
        if vacant == n:
            break
        else:
            time += 1
    return time