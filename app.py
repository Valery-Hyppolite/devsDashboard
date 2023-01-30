from flask import Flask, render_template
import os, requests, json
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
from utils import getData

load_dotenv()
env_path = Path(".")/'.flaskenv'
load_dotenv(dotenv_path=env_path)


app = Flask(__name__)

URL = os.environ.get('API_URL')

@app.route('/')
def home():
    response = requests.get(url=f'{URL}/projects')
    response_profiles = requests.get(url=f'{URL}/profiles')
    response.raise_for_status()
    response_profiles.raise_for_status()

    projects = response.json()
    profiles = response_profiles.json()
    totalUsers = len(profiles)
    data = getData(projects=projects)
    return render_template ('dashboard.html', projects=projects, data=data, profiles=profiles, totalUsers=totalUsers)

@app.route('/projects')
def projects():
    response = requests.get(url=f'{URL}/projects')
    response.raise_for_status()
    projects = response.json()

    data = getData(projects=projects)
    return render_template('projects.html', projects=projects, data=data)

@app.route('/project/<project_id>', methods=['GET'])
def project(project_id):
    response = requests.get(url=f'{URL}/project/{project_id}')
    response.raise_for_status()
    project = response.json()

    return render_template('project.html', project=project)

@app.route('/users')
def users():
    response = requests.get(url=f'{URL}/profiles')
    response_projects = requests.get(url=f'{URL}/projects')
    response.raise_for_status()
    response_projects.raise_for_status()

    profiles = response.json()
    projects = response_projects.json()

    totalUsers = len(profiles)
    data = getData(projects=projects)
    return render_template('users.html', data=data, totalUsers=totalUsers, profiles=profiles)

@app.route('/profile/<profile_id>', methods=['GET'])
def profile(profile_id):
    response = requests.get(url=f'{URL}/profile/{profile_id}')
    response_projects = requests.get(url=f'{URL}/projects')
    response.raise_for_status()
    response_projects.raise_for_status()

    profile = response.json()
    projects_list = response_projects.json()

    allProjects = []

    for project in projects_list:
        if project['owner']['id'] == profile_id:
            #print(f"profile id: {profile_id}, project id: {project['id']}")
            allProjects.append(project)
    projects = allProjects

    data = getData(projects=projects)
    
    return render_template('user.html', profile=profile, projects=projects, data=data)

if __name__ == '__main__':
    app.run()

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)