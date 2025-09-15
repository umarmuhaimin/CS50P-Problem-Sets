# Option 1 :
def main():
    extensions = input("File name: ").strip().lower()
    if gif_extension(extensions):
        print("image/gif")
    elif jpg_extension(extensions):
        print("image/jpeg")
    elif jpeg_extension(extensions):
        print("image/jpeg")
    elif png_extension(extensions):
        print("image/png")
    elif pdf_extension(extensions):
        print("application/pdf")
    elif txt_extension(extensions):
        print("text/plain")
    elif zip_extension(extensions):
        print("application/zip")
    else:
        print("application/octet-stream")



def gif_extension(ext):
    return ext.endswith(".gif")

def jpg_extension(ext):
    return ext.endswith(".jpg")

def jpeg_extension(ext):
    return ext.endswith(".jpeg")

def png_extension(ext):
    return ext.endswith(".png")

def pdf_extension(ext):
    return ext.endswith(".pdf")

def txt_extension(ext):
    return ext.endswith(".txt")

def zip_extension(ext):
    return ext.endswith(".zip")


main()


# Option 2 : Simplified, no need additional functions.
def main():
    extensions = input("File name: ").strip().lower()
    if extensions.endswith(".gif"):
        print("image/gif")
    elif extensions.endswith(".jpg") or extensions.endswith(".jpeg"):
        print("image/jpeg")
    elif extensions.endswith(".png"):
        print("image/png")
    elif extensions.endswith(".pdf"):
        print("application/pdf")
    elif extensions.endswith(".txt"):
        print("text/plain")
    elif extensions.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()


# use return .endswith() function if the correct answer for the case/task ends with a certain letters or words.