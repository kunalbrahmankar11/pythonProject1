f=open("demo.txt","w")
f.write("whops! i ahave deleted content")
f.close()

f=open("demo.txt","r")
print(f.read())