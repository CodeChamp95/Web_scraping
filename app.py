from flask import Flask, render_template, request
from ipl import entire_schedule, favorite_team_schedule, favorite_team_home_schedule, favorite_team_away_schedule, specific_match, search_by_location, search_by_dateTime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule():
    choice = int(request.form['choice'])
    if choice == 1:
        result = entire_schedule()
    elif choice == 2:
        fav_team = request.form['fav_team']
        result = favorite_team_schedule(fav_team)
    elif choice == 3:
        fav_team = request.form['fav_team']
        result = favorite_team_home_schedule(fav_team)
    elif choice == 4:
        fav_team = request.form['fav_team']
        result = favorite_team_away_schedule(fav_team)
    elif choice == 5:
        home_team = request.form['home_team']
        away_team = request.form['away_team']
        result = specific_match(home_team, away_team)
    elif choice == 6:
        location = request.form['location']
        result = search_by_location(location)
    elif choice == 7:
        date_time = request.form['date_time']
        result = search_by_dateTime(date_time)
    else:
        result = "Invalid choice"
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)