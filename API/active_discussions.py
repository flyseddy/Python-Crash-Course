"""
Author: Sedrick Thomas
Created at: April 2020
17-2 Active Discussions
-Make a bar chart showing the most active discussions currently happening on
Hacker News
"""

import requests
import json

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status Code: {r.status_code}")

# Process the information about each submission
submission_ids = r.json()
y_list, x_list = [], []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f"id: {submission_id}\t Status: {r.status_code}")
    response_dict = r.json()

    # Values for the graph
    try:
        title = response_dict['title']
        comments = response_dict['descendants']
        discussion_url = response_dict['url']
        label_link = f"<a href='{discussion_url}'>{title}</a>"
    except KeyError:
        pass

    # Add values to the list
    y_list.append(comments)
    x_list.append(label_link)

    # Make visualization
    data = [{
        'type': 'bar',
        'x': x_list,
        'y': y_list,
        'marker': {
            'color': 'rgb(0, 0, 175)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]
    my_layout = {
        'title': 'Most Commented Posts on Hacker News',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Discussions',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
        'yaxis': {
            'title': 'Comments',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
    }
# Plots the data
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='comments.html')
