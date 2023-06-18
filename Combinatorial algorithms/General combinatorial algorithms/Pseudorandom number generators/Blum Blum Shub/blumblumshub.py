def blum_blum_shub(seed, n):
    p = 1009  # A large prime number
    q = 3643  # Another large prime number
    m = p * q  # Modulus for generating random bits
    x = seed  # Initial seed value
    result = []

    for _ in range(n):
        x = (x * x) % m  # Calculate next value using the formula

        # Extract the least significant bit as a random bit
        bit = x % 2
        result.append(bit)

    return result

# Example usage
random_bits = blum_blum_shub(12345, 10)
print(random_bits)
