def optimal_task(tasks):
    
    op_tasks = list()
    # Sort Array
    sorted_tasks = sorted(tasks)
    
    # Pick first and last
    i = 0
    j = len(sorted_tasks) - 1

    while i <= j :
        op_tasks.append((sorted_tasks[i],sorted_tasks[j]))
        i += 1
        j -= 1
    return op_tasks

def optimal_task_python(tasks):
    tasks = sorted(tasks)

    # ~ is bitwise complement operator
    for x in range(len(A) // 2):
        print(A[x], A[~x])

    return tasks

A = [6, 3, 2, 7, 5, 5, 3, 9]
# workers = 3

print(optimal_task(A, workers))
optimal_task_python(A)