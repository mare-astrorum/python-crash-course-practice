import unittest

import python_repos

class PythonReposTestCase(unittest.TestCase):
    """Tests for the python_repos.py."""

    def test_status_code(self):
        """Is the status code 200?"""
        status_code = python_repos.r.status_code
        self.assertEqual(status_code, 200)

    def test_items_returned(self):
        """Are the items returned a number?"""
        items_returned = len(python_repos.response_dict['items'])
        self.assertTrue(items_returned, int)

    def test_number_repos(self):
        """Is the number of repos returned larger than 10?"""
        number_repos = python_repos.response_dict['total_count']
        self.assertNotIn(number_repos, range(0,11))
