x = input("File Name: ").strip().casefold()

if x.endswith(".gif"):
    print("image/gif")
elif x.endswith(".jpg"):
    print("image/jpeg")
elif x.endswith(".jpeg"):
    print("image/jpeg")
elif x.endswith(".png"):
    print("image/png")
elif x.endswith(".pdf"):
    print("application/pdf")
elif x.endswith(".txt"):
    print("text/plain")
elif x.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
