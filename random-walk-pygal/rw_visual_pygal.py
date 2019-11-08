import pygal

from random_walk_pygal import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    scatter = pygal.XY()
    scatter.add('Random Walk', rw.coordinate_list)
    scatter.add('Start', [(0,0)])
    scatter.add('End', [rw.coordinate_list[-1]])
    scatter.render_to_file('scatter.svg')

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
