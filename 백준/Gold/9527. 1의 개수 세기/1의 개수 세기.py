def count_ones(n):
    total = 0
    for i in range(60):  # 최대 2^60 > 10^18
        cycle_len = 1 << (i + 1)
        full_cycles = (n + 1) // cycle_len
        remainder = (n + 1) % cycle_len

        ones_from_cycles = full_cycles * (1 << i)
        ones_from_remainder = max(0, remainder - (1 << i))

        total += ones_from_cycles + ones_from_remainder
    return total

A, B = map(int, input().split())
print(count_ones(B) - count_ones(A - 1))
