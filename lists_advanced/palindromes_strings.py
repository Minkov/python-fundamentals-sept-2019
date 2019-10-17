words = input().split(' ')
palindrome = input()

palindromes = [word for word in words if word == word[::-1]]
palindrome_count = palindromes.count(palindrome)

print(palindromes)
print(f"Fund palindrome {palindrome_count} times")


