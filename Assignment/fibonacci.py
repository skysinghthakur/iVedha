n = int(input("Enter the length for FB list: "))
dp = []
if n == 1:
    dp = [0]
elif n > 1:
    dp = [0, 1]
for i in range(2,n):
    dp.append(dp[i-1]+dp[i-2])

print(f"Series is: {dp}")