from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Fetch the webpage
driver.get('https://www.iplt20.com/matches/fixtures')

# Get the page source after JavaScript has been executed
html_page = driver.page_source

# html_page=requests.get('https://www.iplt20.com/matches/fixtures')
soup = BeautifulSoup(html_page, 'lxml')
# print(soup)
schedule = soup.find_all('li', class_='ng-scope')
# print(schedule[0].prettify())

def entire_schedule():
    result = ""
    for item in schedule:
        home_team_div = item.find('div', class_='vn-shedTeam')
        away_team_div = item.find('div', class_='vn-shedTeam vn-team-2')
        if home_team_div and away_team_div:
            home_team = home_team_div.find('h3').text.strip()
            away_team = away_team_div.find('h3').text.strip()
            match_date_time = item.find('div', class_='vn-matchDateTime w20 tl pr50').text.strip()
            match_number = item.find('span', class_='vn-matchOrder ng-binding ng-scope').text.strip()
            location = item.find('p', class_='ng-binding').text.strip()
            tickets = item.find('a', class_='buyTicketsIcon')['href']
            result += f"""
            <div class='match-card'>
                <p class='match-time'>{match_date_time}</p>
                <h3>{match_number}: {home_team} vs {away_team}</h3>
                <p class='location'>📍 {location}</p>
                <a href='{tickets}' class='ticket-link'>Buy Tickets →</a>
            </div>
            """
    return result

def favorite_team_schedule(fav_team):
    result = ""
    for item in schedule:
        home_team_div = item.find('div', class_='vn-shedTeam')
        away_team_div = item.find('div', class_='vn-shedTeam vn-team-2')
        if home_team_div and away_team_div:
            home_team = home_team_div.find('h3').text.strip()
            away_team = away_team_div.find('h3').text.strip()
            if home_team == fav_team or away_team == fav_team:
                match_date_time = item.find('div', class_='vn-matchDateTime w20 tl pr50').text.strip()
                match_number = item.find('span', class_='vn-matchOrder ng-binding ng-scope').text.strip()
                location = item.find('p', class_='ng-binding').text.strip()
                tickets = item.find('a', class_='buyTicketsIcon')['href']
                result += f"""
            <div class='match-card'>
                <p class='match-time'>{match_date_time}</p>
                <h3>{match_number}: {home_team} vs {away_team}</h3>
                <p class='location'>📍 {location}</p>
                <a href='{tickets}' class='ticket-link'>Buy Tickets →</a>
            </div>
            """
    return result

def favorite_team_home_schedule(fav_team):
    result = ""
    for item in schedule:
        home_team_div = item.find('div', class_='vn-shedTeam')
        away_team_div = item.find('div', class_='vn-shedTeam vn-team-2')
        if home_team_div and away_team_div:
            home_team = home_team_div.find('h3').text.strip()
            if home_team == fav_team:
                away_team = away_team_div.find('h3').text.strip()
                match_date_time = item.find('div', class_='vn-matchDateTime w20 tl pr50').text.strip()
                match_number = item.find('span', class_='vn-matchOrder ng-binding ng-scope').text.strip()
                location = item.find('p', class_='ng-binding').text.strip()
                tickets = item.find('a', class_='buyTicketsIcon')['href']
                result += f"""
            <div class='match-card'>
                <p class='match-time'>{match_date_time}</p>
                <h3>{match_number}: {home_team} vs {away_team}</h3>
                <p class='location'>📍 {location}</p>
                <a href='{tickets}' class='ticket-link'>Buy Tickets →</a>
            </div>
            """
    return result

def favorite_team_away_schedule(fav_team):
    result = ""
    for item in schedule:
        home_team_div = item.find('div', class_='vn-shedTeam')
        away_team_div = item.find('div', class_='vn-shedTeam vn-team-2')
        if home_team_div and away_team_div:
            away_team = away_team_div.find('h3').text.strip()
            if away_team == fav_team:
                home_team = home_team_div.find('h3').text.strip()
                match_date_time = item.find('div', class_='vn-matchDateTime w20 tl pr50').text.strip()
                match_number = item.find('span', class_='vn-matchOrder ng-binding ng-scope').text.strip()
                location = item.find('p', class_='ng-binding').text.strip()
                tickets = item.find('a', class_='buyTicketsIcon')['href']
                result += f"""
            <div class='match-card'>
                <p class='match-time'>{match_date_time}</p>
                <h3>{match_number}: {home_team} vs {away_team}</h3>
                <p class='location'>📍 {location}</p>
                <a href='{tickets}' class='ticket-link'>Buy Tickets →</a>
            </div>
            """
    return result

def specific_match(home_team_param, away_team_param):
    result = ""
    for item in schedule:
        home_team_div = item.find('div', class_='vn-shedTeam')
        away_team_div = item.find('div', class_='vn-shedTeam vn-team-2')
        if home_team_div and away_team_div:
            home_team = home_team_div.find('h3').text.strip()
            away_team = away_team_div.find('h3').text.strip()
            if home_team == home_team_param and away_team == away_team_param:
                match_date_time = item.find('div', class_='vn-matchDateTime w20 tl pr50').text.strip()
                match_number = item.find('span', class_='vn-matchOrder ng-binding ng-scope').text.strip()
                location = item.find('p', class_='ng-binding').text.strip()
                tickets = item.find('a', class_='buyTicketsIcon')['href']
                result += f"""
            <div class='match-card'>
                <p class='match-time'>{match_date_time}</p>
                <h3>{match_number}: {home_team} vs {away_team}</h3>
                <p class='location'>📍 {location}</p>
                <a href='{tickets}' class='ticket-link'>Buy Tickets →</a>
            </div>
            """
    return result

def search_by_location(Location):
    result = ""
    for item in schedule:
        location = item.find('p', class_='ng-binding').text.strip()
        if location == Location:
            home_team_div = item.find('div', class_='vn-shedTeam')
            away_team_div = item.find('div', class_='vn-shedTeam vn-team-2')
            if home_team_div and away_team_div:
                home_team = home_team_div.find('h3').text.strip()
                away_team = away_team_div.find('h3').text.strip()
                match_date_time = item.find('div', class_='vn-matchDateTime w20 tl pr50').text.strip()
                match_number = item.find('span', class_='vn-matchOrder ng-binding ng-scope').text.strip()
                tickets = item.find('a', class_='buyTicketsIcon')['href']
                result += f"""
            <div class='match-card'>
                <p class='match-time'>{match_date_time}</p>
                <h3>{match_number}: {home_team} vs {away_team}</h3>
                <p class='location'>📍 {location}</p>
                <a href='{tickets}' class='ticket-link'>Buy Tickets →</a>
            </div>
            """
    return result

def search_by_dateTime(dateTime):
    result = ""
    for item in schedule:
        match_date_time = item.find('div', class_='vn-matchDateTime w20 tl pr50').text.strip()
        if match_date_time == dateTime:
            home_team_div = item.find('div', class_='vn-shedTeam')
            away_team_div = item.find('div', class_='vn-shedTeam vn-team-2')
            if home_team_div and away_team_div:
                home_team = home_team_div.find('h3').text.strip()
                away_team = away_team_div.find('h3').text.strip()
                match_number = item.find('span', class_='vn-matchOrder ng-binding ng-scope').text.strip()
                location = item.find('p', class_='ng-binding').text.strip()
                tickets = item.find('a', class_='buyTicketsIcon')['href']
                result += f"""
            <div class='match-card'>
                <p class='match-time'>{match_date_time}</p>
                <h3>{match_number}: {home_team} vs {away_team}</h3>
                <p class='location'>📍 {location}</p>
                <a href='{tickets}' class='ticket-link'>Buy Tickets →</a>
            </div>
            """
    return result

# choice=int(input("Enter your choice:\n1. Entire Schedule\n2. Search by favorite team\n3. Search by favorite team home matches\n4. Search by favorite team away matches\n5. Search by specific match\n6. Search by location\n7. Search by date and time\n"))
# if(choice==1):
#     entire_schedule()
# elif(choice==2):
#     fav_team=input("Enter your favorite team: ")
#     favorite_team_schedule(fav_team)
# elif(choice==3):
#     fav_team=input("Enter your favorite team: ")
#     favorite_team_home_schedule(fav_team)
# elif(choice==4):
#     fav_team=input("Enter your favorite team: ")
#     favorite_team_away_schedule(fav_team)
# elif(choice==5):
#     home_team=input("Enter the home team: ")
#     away_team=input("Enter the away team: ")
#     specific_match(home_team,away_team)
# elif(choice==6):
#     Location=input("Enter the location: ")
#     search_by_location(Location)
# elif(choice==7):
#     dateTime=input("Enter the date and time: ")
#     search_by_dateTime(dateTime)
