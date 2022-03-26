
message = list(input().replace(" ", ""))
k = int(input())


print([chr(ord(i) + k) for i in message])

