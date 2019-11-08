from random import choice


class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, num_points=2000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = 0
        self.y_values = 0

        self.first_coordinate = (0,0)
        self.coordinate_list = [self.first_coordinate]

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step



    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        iter = 1
        while iter < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            self.x_values = self.x_values + x_step
            self.y_values = self.y_values + y_step

            coordinates = (self.x_values, self.y_values)
            self.coordinate_list.append(coordinates)

            iter += 1










