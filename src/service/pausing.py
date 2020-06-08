from urllib.request import Request
import urllib, os
import requests

url = "http://quatest1.com.vn/images/PHP-DocumentFull.pdf"


# if os.path.exists(dlFile):
#     outputFile = open(dlFile, "ab")
#     existSize = os.path.getsize(dlFile)
#     # If the file exists, then only download the remainder
#     Request.add_header("Range", "bytes=%s-" % (existSize))
# else:
#     outputFile = open(dlFile, "wb")

def main_func():
    full_file_name = url.split("/")[-1]
    file_name = full_file_name.split(".")[0]
    extension = full_file_name.split(".")[-1]

    req = Request(url)
    req.add_header("apikey", "xxx")
    response = urllib.request.urlopen(req)

    with open("downloaded/{0}.{1}".format(file_name, extension), "wb") as downloaded_file:
        data = response.read()
        downloaded_file.write(data)


if __name__ == '__main__':
    main_func()
