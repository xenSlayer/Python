'''
This script is written by XenSlayer
This simple program scraps online websites[onefootball, premierleague.com, goal.com, footlive.com] to fetch English premier league table data
The data obtained is saved in a csv file
Re-use and improvement of the code is well appreciated

#peace :)

'''
import requests
from bs4 import BeautifulSoup
import csv

team_name = []
team_played = []
team_points = []
game_won = []
data = []
game_drawn = []
game_lost = []
gf_ga = []
goaldiff = []

r = requests.get('https://onefootball.com/en/competition/premier-league-9?variable=20200111').text
r = BeautifulSoup(r, 'lxml')

r2 = requests.get('https://www.premierleague.com/tables').text
r2 = BeautifulSoup(r2, 'lxml')


r3 = requests.get('https://www.goal.com/en-in/premier-league/table/2kwbbcootiqqgmrzs6o5inle5').text
r3 = BeautifulSoup(r3, 'lxml')


r4 = requests.get('http://www.footlive.com/table-standings/england/barclays-premiership/').text
r4 = BeautifulSoup(r4, 'lxml')



with open('Pl_standing.csv', 'w', newline='') as file:

    write = csv.writer(file)
    write.writerow(['#','Teams','P','W','D','L','GF-GA','GD','Pts'])
    write.writerow('')
    count = int(1)
    w = 1
    d = 2
    l = 3
    gfga = 4


    for i in r.find_all('div', class_='team-name d-block flex-grow-1 text-ellipsis'):
        page = i.text
        team_name.append(page)


    for i in r2.find_all('td', class_='points'):
        points = i.text
        team_points.append(points)
        team_points = team_points[0:20]

    for played in r3.find_all('td', class_="p0c-competition-tables__matches-played"):
        played = played.text
        team_played.append(played)

    for i in r4.find_all('div', style='width:50px;text-align:center;line-height:20px;'):
        i = i.text
        data.append(i)


    try:
        for i in range(0, len(data)):
            draw = data[d]
            game_drawn.append(draw)
            d += 6
    except Exception as error:
        er = 0

    try:
        for i in range(0, len(data)):
            won = data[w]
            game_won.append(won)
            w += 6
    except Exception as e:
        er = 0

    try:
        for i in range(0, len(data)):
            lost = data[l]
            game_lost.append(lost)
            l += 6
    except Exception as e:
        er = 0

    try:
        for i in range(0, len(data)):
            gfga_ = data[gfga]
            gf_ga.append(gfga_)
            gfga += 6
    except Exception as e:
        er = 0

    for i in range(0, len(gf_ga)):
        s = 0
        t = 1
        gf = gf_ga[i]
        gf = gf.split("-", 2)
        gd = int(int(gf[0]) - int(gf[1]))
        goaldiff.append(gd)

    for (i, j, k, l, m, n, o, p) in (zip(team_name, team_played, game_won, game_drawn, game_lost, gf_ga, goaldiff, team_points)):
        write.writerow([count, i, j, k, l, m, n, o, p])
        count += 1

    write.writerow(' ')
    write.writerow(['P = Played'])
    write.writerow(['W = Won'])
    write.writerow(['D = Drawn'])
    write.writerow(['L = Lost'])
    write.writerow(['GF = Goals For'])
    write.writerow(['GA = Goals Against'])
    write.writerow(['GD = Goal Difference'])
    write.writerow(['Pts = Points'])
print('******Table Updated******')
