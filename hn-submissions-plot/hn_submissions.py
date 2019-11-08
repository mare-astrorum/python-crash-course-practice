import requests

from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])

# Create values for a pygal plot.
names, plot_dicts = [], []
for dict in submission_dicts:
    name = dict['title']
    names.append(name)

for dict in submission_dicts:
    plot_dict = {
        'value': dict['comments'],
        'xlink': dict['link'],
    }
    plot_dicts.append(plot_dict)


# Make visualization.
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most active current Hacker News discussions'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('hn_repos.svg')