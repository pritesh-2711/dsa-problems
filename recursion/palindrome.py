def is_palindrome(s: str, left: int, right: int) -> bool:
    if left >= right:
        return True
    if s[left] == s[right]:
        return is_palindrome(s, left + 1, right - 1)
    return False

# Example usage:
s = "racecar"
print(is_palindrome(s, 0, len(s) - 1))  # Output: True

s = "racecars"
print(is_palindrome(s, 0, len(s) - 1))  # Output: False