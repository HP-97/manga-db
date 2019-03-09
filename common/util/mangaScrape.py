import requests
import bs4
import datetime
import arrow


"""
13/02/2019 - This script will be scraping from multiple websites to gather information about specific manga.
"""

"""
START: These functions apply to jaiminisbox.com 
"""
def get_latest_chapter(soup_item):
    item = soup_item.find("div", {"class": "element"}) # Finds the 1st entry in the list of manga chapters.
    url = item.find("a").get("href").split('/')
    return int(url[-2])

"""
END: jaiminisbox.com 
"""

"""
START: These functions apply to myanimelist.net 

14/02/2019 - This function 'soup_item.find_all("div", {"class": "spaceit"})' traverses through the volumes, chapters, status, publish dates, genres, authors and serialization sections.
"""
def get_genres(soup_item):
    genre_list = []
    for item in soup_item.find_all("div", {"class": "spaceit"}):
        if item.find("span").text == "Genres:":
            genre_list = item.text.split()[1:-1]
            break
    return genre_list

def get_title(url):
    full_title = url.split("/")[-1]
    split_title =  full_title.split("_")
    final_title = ""
    for item in split_title:
        final_title = final_title + item + " "
    return final_title

def get_author(soup_item):
    final_author = ""
    for item in soup_item.find_all("div"):
        try:
            if item.find("span").text == "Authors:":
                author_list = item.text.split()[1:3]
                for item in author_list:
                    final_author = final_author + item + " "
                break
        except AttributeError:
            pass # Move on to next <div> tag.

    final_author = final_author.strip() # remove trailing whitespace
    return final_author

def get_release_date(soup_item):
    final_release_date = ""
    for item in soup_item.find_all("div"):
        try:
            if item.find("span").text == "Published:":
                pub_list = item.text.split()[1:4]
                for item in pub_list:
                    final_release_date = final_release_date + item + " "
                break
        except AttributeError:
            pass  # Move on to next <div> tag.
    final_release_date = final_release_date.strip()
    return final_release_date

def get_pub_status(soup_item): # TODO: Incomplete function
    genre_list = []
    for item in soup_item.find_all("div", {"class": "spaceit"}):
        if item.find("span").text == "Status:":
            genre_list = item.text.split()
            break
    return genre_list[1]
"""
END: myanimelist.com 
"""

def retrieve_data(url_1, url_2):
    manga_details = {}  # Contains information on the manga where key = attribute and value = attribute_val.

    res = requests.get(url_1)
    res.raise_for_status()
    mangaSoup = bs4.BeautifulSoup(res.text, "html.parser")

    manga_details["latest chapter"] = get_latest_chapter(mangaSoup)

    res_2 = requests.get(url_2)
    res_2.raise_for_status()
    malSoup = bs4.BeautifulSoup(res_2.text, "html.parser")

    manga_details["genres"] = get_genres(malSoup)
    manga_details["title"] = get_title(url_2)
    manga_details["author"] = get_author(malSoup)
    manga_details["release date"] = get_release_date(malSoup)
    manga_details["pub status"] = get_pub_status(malSoup)

    manga_details["date uploaded"] = arrow.now().format('DD/MM/YYYY')
    manga_details["url chapter"] = url_1
    manga_details["url metadata"] = url_2

    return manga_details

if __name__ == "__main__":
    # "https://jaiminisbox.com/reader/series/one-piece-2/"
    curr_dict = retrieve_data("https://jaiminisbox.com/reader/series/we-can-t-study", "https://myanimelist.net/manga/103890/Bokutachi_wa_Benkyou_ga_Dekinai")
    print(curr_dict)
