def main():
    n = int(input())
    a = list(input().split())
    b = input()

    ans = None 
    for i in a:
        if i > b:
            ans = i
            break
    if ans is not None:
        print(ans)
    else:
        print(a[0])

    

main()