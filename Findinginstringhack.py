def count_substring(string, sub_string):
    c=0
    a=True
    while True:
        if (string.count(sub_string) >0):
            c=c+1
        else:
            False
    
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)