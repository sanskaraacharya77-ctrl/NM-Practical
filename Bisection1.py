def f(x):
    return x**3 - x - 2


def bisection_method(a, b, tolerance, max_iterations):
    if f(a) * f(b) >= 0:
        print("Bisection method fails, f(a) and f(b) must have opposite signs.")
        return None

    print("Iteration \t a \t\t b \t\t c \t\t f(c)")

    for i in range(1, max_iterations + 1):
        c = (a + b) / 2
        print(f"{i} \t\t{a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}")

        if abs(f(c)) < tolerance:
            print("\nRoot found:", c)
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("\nAppropriate root after max iteration:", c)
    return c


a = float(input("Enter lower bound a: "))
b = float(input("Enter upper bound b: "))
tolerance = float(input("Enter tolerance: "))
max_iterations = int(input("Enter maximum iterations: "))

bisection_method(a, b, tolerance, max_iterations)