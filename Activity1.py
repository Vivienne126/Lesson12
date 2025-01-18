n=input("Enter your word")
char=input("Enter your letter")
i=0
count=0

while (i<len(n)):
    if (n[i]==char):
        count=count+1
    i=i+1

print("The word count is" , count)