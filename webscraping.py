import bs4
import requests

basic_url = 'http://books.toscrape.com/catalogue/page-{}.html'

#list of 4 or 5 star titles
high_rated_titles = []

for page in range(1,51):

    #make soup on each page
    url_page = basic_url.format(page)
    result = requests.get(url_page)
    soup = bs4.BeautifulSoup(result.text,'html.parser')

    #Get data of books
    books = soup.select('.product_pod')

    for book in books:

        #check for 4 or 5 star
        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) != 0:

            #Store title in variable
            book_title = book.select('a')[1]['title']

            #add to list
            high_rated_titles.append(book_title)
for b in high_rated_titles:
    print(b)

