def char_to_point(c, a, b, p):
    # ASCII representation of the character
    x = ord(c)
    # Try possible y values until we find one that fits the curve
    # This might not be the most efficient way, but it's simple
    for y in range(p):
        if (y * y - x * x * x - a * x - b) % p == 0:
            return (x, y)    
    # If no y value fits the curve, raise an exception
    raise ValueError(f"No point on the curve corresponds to character '{c}'")


# Test
print(char_to_point('A', 2, 2, 17))
