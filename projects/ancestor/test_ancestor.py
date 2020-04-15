import unittest
from ancestor import earliest_ancestor

class Test(unittest.TestCase):

    '''
       10     15
     /       / \
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
	   / \   \ / \
	  12  13  14  16
	   \
	    17
    '''
    # def test_earliest_ancestor(self):
    #     test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    #     self.assertEqual(earliest_ancestor(test_ancestors, 1), 10)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 2), -1)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 3), 10)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 4), -1)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 5), 4)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 6), 10)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 7), 4)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 8), 4)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 9), 4)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 10), -1)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 11), -1)
    def test_earliest_ancestor(self):
        test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1),
							(15,4), (15,11), (6,12), (6,13), (7,14) , (9,14) , (9,16) , (12,17)]
        self.assertEqual(earliest_ancestor(test_ancestors, 1), 10)
        self.assertEqual(earliest_ancestor(test_ancestors, 16), 15)
        self.assertEqual(earliest_ancestor(test_ancestors, 6), 15)

if __name__ == '__main__':
    print("\n\n\n\n\n\n BEGIN")
    unittest.main()