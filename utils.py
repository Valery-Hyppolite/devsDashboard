
from flask import Flask
from datetime import datetime

# @app.template_filter()
# def pretty_date(dttm):
#     return dttm.strftime("%m/%d")

def getData(projects):
    links = []
    demo = []
    vote = 0
    users = []

    for project in projects:
        if project['source_link']:
         links.append(project['source_link'])
        if project['demo_link']:
            demo.append(project['demo_link'])
        if project['vote_total']:
            vote += (project['vote_total'])
        if project['owner']['user']:
            users.append(project['owner']['user'])

    global total_links, demo_links, vote_total, total_users, total_projects

    total_projects = len(projects)
    demo_links = len(demo)
    total_links = len(links)
    vote_total = vote
    total_users = len((set(users)))
    print('total users:',total_users, 'userlist:', users)

    return total_users, vote_total, demo_links, total_links, total_projects