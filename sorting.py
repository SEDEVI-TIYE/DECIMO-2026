import pygame
import random
import sys

pygame.init()

# Configuración
WIDTH, HEIGHT = 1000, 600
ARRAY_SIZE = 100
MIN_VALUE = 10
MAX_VALUE = 500

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 120, 255)
YELLOW = (255, 255, 0)
PURPLE = (180, 0, 255)
BACKGROUND = (25, 25, 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer PRO")
font = pygame.font.SysFont('Arial', 20)
small_font = pygame.font.SysFont('Arial', 16)

clock = pygame.time.Clock()
speed = 60

def generate_array():
    return [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(ARRAY_SIZE)]

def draw_array(array, colors={}, moves=0):
    screen.fill(BACKGROUND)
    bar_width = (WIDTH - 20) // len(array)

    for i, val in enumerate(array):
        color = colors.get(i, WHITE)
        pygame.draw.rect(screen, color,
                         (10 + i * bar_width, HEIGHT - val, bar_width - 1, val))

    screen.blit(font.render(f"{current_algorithm}", True, WHITE), (10, 10))
    screen.blit(font.render(f"Moves: {moves}", True, YELLOW), (10, 40))
    screen.blit(font.render(f"Speed: {speed}", True, BLUE), (10, 70))

    controls = [
        "1 Bubble", "2 Selection", "3 Insertion",
        "4 Merge", "5 Quick", "6 Shell", "7 Radix",
        "R Reset | SPACE Start | ↑↓ Speed"
    ]

    for i, t in enumerate(controls):
        screen.blit(small_font.render(t, True, WHITE), (WIDTH - 220, 10 + i * 20))

    pygame.display.update()

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# =========================
# SORTING GENERATORS
# =========================

def bubble_sort(arr):
    moves = 0
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            check_quit()
            moves += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                moves += 1
            yield arr, {j: RED, j+1: RED}, moves
    yield arr, {i: GREEN for i in range(n)}, moves


def selection_sort(arr):
    moves = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            check_quit()
            moves += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
            yield arr, {i: PURPLE, j: RED, min_idx: YELLOW}, moves
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        moves += 1
    yield arr, {i: GREEN for i in range(n)}, moves


def insertion_sort(arr):
    moves = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            check_quit()
            arr[j+1] = arr[j]
            j -= 1
            moves += 1
            yield arr, {j: RED, i: BLUE}, moves
        arr[j+1] = key
        moves += 1
    yield arr, {i: GREEN for i in range(len(arr))}, moves


def merge_sort(arr):
    moves = 0

    def merge(arr, left, mid, right):
        nonlocal moves
        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < len(left_part) and j < len(right_part):
            check_quit()
            moves += 1
            colors = {x: YELLOW for x in range(left, mid + 1)}
            colors.update({x: PURPLE for x in range(mid + 1, right + 1)})
            colors[k] = RED
            yield arr, colors, moves
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1
        while i < len(left_part):
            check_quit()
            arr[k] = left_part[i]
            i += 1
            k += 1
            moves += 1
            yield arr, {k - 1: RED}, moves
        while j < len(right_part):
            check_quit()
            arr[k] = right_part[j]
            j += 1
            k += 1
            moves += 1
            yield arr, {k - 1: RED}, moves

    def sort(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            yield from sort(arr, left, mid)
            yield from sort(arr, mid + 1, right)
            yield from merge(arr, left, mid, right)

    yield from sort(arr, 0, len(arr) - 1)
    yield arr, {i: GREEN for i in range(len(arr))}, moves


def quick_sort(arr):
    moves = 0

    def partition(low, high):
        nonlocal moves
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            check_quit()
            moves += 1
            yield arr, {high: PURPLE, j: RED}, moves
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                moves += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        moves += 1
        yield arr, {i + 1: PURPLE}, moves
        partition.last_pi = i + 1

    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            gen = partition(low, high)
            for state in gen:
                yield state
            pi = partition.last_pi
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

    yield arr, {i: GREEN for i in range(len(arr))}, moves


def shell_sort(arr):
    moves = 0
    gap = len(arr) // 2

    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                check_quit()
                arr[j] = arr[j - gap]
                j -= gap
                moves += 1
                yield arr, {j: RED, i: BLUE}, moves
            arr[j] = temp
        gap //= 2

    yield arr, {i: GREEN for i in range(len(arr))}, moves


def counting_sort_radix(arr, exp, moves):
    output = [0] * len(arr)
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in reversed(range(len(arr))):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]
        moves += 1
        yield arr, {i: YELLOW}, moves

    return moves


def radix_sort(arr):
    moves = 0
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        gen = counting_sort_radix(arr, exp, moves)
        for state in gen:
            yield state
        exp *= 10

    yield arr, {i: GREEN for i in range(len(arr))}, moves


# =========================
# MAIN LOOP
# =========================

array = generate_array()
current_algorithm = "None"
sorting = False
generator = None
moves = 0

while True:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                speed += 10
            if event.key == pygame.K_DOWN:
                speed = max(10, speed - 10)

            if not sorting:
                if event.key == pygame.K_r:
                    array = generate_array()
                    current_algorithm = "None"
                    generator = None
                    moves = 0

                if event.key == pygame.K_1:
                    current_algorithm = "Bubble Sort"
                    generator = bubble_sort(array)

                if event.key == pygame.K_2:
                    current_algorithm = "Selection Sort"
                    generator = selection_sort(array)

                if event.key == pygame.K_3:
                    current_algorithm = "Insertion Sort"
                    generator = insertion_sort(array)

                if event.key == pygame.K_4:
                    current_algorithm = "Merge Sort"
                    generator = merge_sort(array)

                if event.key == pygame.K_5:
                    current_algorithm = "Quick Sort"
                    generator = quick_sort(array)

                if event.key == pygame.K_6:
                    current_algorithm = "Shell Sort"
                    generator = shell_sort(array)

                if event.key == pygame.K_7:
                    current_algorithm = "Radix Sort"
                    generator = radix_sort(array)

                if event.key == pygame.K_SPACE and generator:
                    sorting = True

    if sorting and generator:
        try:
            array, colors, moves = next(generator)
        except StopIteration:
            sorting = False

        draw_array(array, colors, moves)
    else:
        draw_array(array, moves=moves)