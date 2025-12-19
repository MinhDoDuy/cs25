#3 File Extensions
filename = input("File name: ").strip()
if filename.endswith("gif"):
    print("image/gif")
elif filename.endswith("jpeg") or filename.endswith("jpg"):
    print("image/jpeg")
elif filename.endswith("png"):
    print("image/png")
elif filename.endswith("pdf"):
    print("application/pdf")
elif filename.endswith("txt"):
    print("text/txt")
elif filename.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream ")