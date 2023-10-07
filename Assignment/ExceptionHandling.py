#division by zero, mismatch datatype and all other exception can be handled 
try:
    a = int(input())
    b = int(input())
    print(f"a/b is {a/b}")
except Exception as e:
    print(f"Exception occurs for {e}")
finally:
    print("We can use this block to do anything which we required to do\nLike closing the file, DBconnection etc")
