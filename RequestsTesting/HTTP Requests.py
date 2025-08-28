#This program is just trying to test out requests
import requests

def main():
    #writeHTMLFromLink("https://classroom.google.com/c/Nzc0NjY1OTM2NDIy", "physicsGoogleClassroom")
    #writeHTMLFromLink("https://www.deledao.com/", "deledao")

    printAllCookieInfo("https://www.deledao.com/", "googleClassroom")


def writeHTMLFromLink(url, file_name = "website"):
    response = requests.get(url)
    html_text = response.text

    with open(str(file_name) + ".html", "w") as file:
        file.write(html_text)


def printAllCookieInfo(url, file_name = "website"):
    cookies = requests.get(url).cookies
    print("Amount of cookies: " + str(len(cookies)))

    for cookie in cookies:
        cookieInfo = f"Name: {cookie.name}\nValue: {cookie.value}\nDomain: {cookie.domain}\nPath: {cookie.path}\nExpires: {cookie.expires}\n\n"
        print(cookieInfo)
        #file.writeLine(cookie)


main()