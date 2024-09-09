# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
#
# # Set up Selenium WebDriver (Assuming you have ChromeDriver installed)
# driver = webdriver.Chrome(executable_path='path_to_chromedriver')  # Replace with the path to your chromedriver
#
# # URL of IMDb's top-rated movies page
# url = "https://www.imdb.com/chart/top"
#
# # Load the page
# driver.get(url)
#
# # Allow some time for the page to load completely
# time.sleep(3)
#
# # Parse page source using BeautifulSoup
# soup = BeautifulSoup(driver.page_source, 'html.parser')
#
# # Close the browser window
# driver.quit()
#
# # Find the section that contains the movie data
# movies = soup.find_all('td', class_='titleColumn')
# ratings = soup.find_all('td', class_='ratingColumn imdbRating')
#
# # Extract movie titles, ranks, years, and ratings
# top_movies = []
# for i in range(len(movies)):
#     title = movies[i].a.text
#     year = movies[i].span.text.strip('()')
#     rank = movies[i].get_text(strip=True).split('.')[0]
#     rating = ratings[i].strong.text
#     top_movies.append({
#         'rank': rank,
#         'title': title,
#         'year': year,
#         'rating': rating
#     })
#
# # Print the extracted movie data
# for movie in top_movies[:10]:  # Adjust the range as needed
#     print(f"Rank: {movie['rank']} | Title: {movie['title']} ({movie['year']}) | Rating: {movie['rating']}")
