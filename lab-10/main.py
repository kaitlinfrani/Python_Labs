# -*- coding: utf-8 -*-
"""
Kaitlin Frani
CPSC 223P-01
Wed Apr 21, 2021
kaitlinfrani@csu.fullerton.edu
"""

#LAB 4/21
#going to process an API Response
#going to write a program to automatically issue an API call and process the results
#by identifying the most starred Python projects on GitHub

#Part 1
import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

hders = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=hders)
#status code of 200 means successful request
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()

# Process results.
print(response_dict.keys())

#Part 2
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
repo_names, stars = [], []
#same as this^.. just initializes two variables in one line rather than separate
#stars = []
       
"""
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")

for key in sorted(repo_dict.keys()):
    print(key)

print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")
"""
for repo_dict in repo_dicts:
       repo_names.append(repo_dict['name'])
       stars.append(repo_dict['stargazers_count'])
# Make visualization.
data = [{
       'type': 'bar',
       'x': repo_names,
       'y': stars,
       'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
    }]

my_layout = {
       'title': 'Most-Starred Python Projects on GitHub',
       'xaxis': {'title': 'Repository'},
       'yaxis': {'title': 'Stars'},
    }

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='python_repos.html')

