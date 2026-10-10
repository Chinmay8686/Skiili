def classifyTriangle(a: int, b: int, c: int) -> str:
    # Check for invalid side lengths or triangle inequality violation
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"
    
    # Check for Equilateral triangle
    if a == b == c:
        return "Equilateral"
    
    # Check if all three sides are different
    all_different = (a != b and b != c and a != c)
    
    if all_different:
        # Sort sides to verify Pythagorean theorem (x^2 + y^2 = z^2)
        sides = sorted([a, b, c])
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            return "Right Scalene"
        else:
            return "Scalene"
    else:
        # If not equilateral and not all different, exactly two sides are equal
        return "Isosceles"