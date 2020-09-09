'''
Example tests using standard documentation
https://docs.python.org/3/library/unittest.html
'''

import unittest

# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])

#         with self.assertRaises(TypeError):
#             s.split(2)

#     def test_in(self):
#         s = 'Lambda School rocks!'
#         self.assertTrue('L' in s)
#         self.assertIn('L', s)

from oop_examples import Simulator
import numpy as np

class TestMazeMethods(unittest.TestCase):
    def setUp(self):
        self.sim = Simulator()

    def test_next_move_exit(self):
        '''
        Tests to make sure that the bot can find the exit
        '''
        inputGrid = [
                    ['#', 'e', '#'],
                    ['-', 'b', '-'],
                    ['-', '-', '-']
                    ]
        grids = [np.rot90(inputGrid,rotation) for rotation in np.arange(4)]
        directions = ['UP','LEFT','DOWN','RIGHT']
        for count, grid in enumerate(grids):
            self.assertEqual(self.sim.nextMove(grid), directions[count])

    def test_next_move_wall(self):
        '''Tests to make sure that the bot can find the wall'''
        inputGrid = [
                    ['#', '#', '#'],
                    ['-', 'b', '-'],
                    ['-', '-', '-']
                    ]
        grids = [np.rot90(inputGrid,rotation) for rotation in np.arange(4)]
        directions = ['RIGHT','UP','LEFT','DOWN']
        for count, grid in enumerate(grids):
            self.assertEqual(self.sim.nextMove(grid), directions[count])

    def test_next_move_blocked(self):
        '''Tests to make sure that the bot can move with a block in front'''
        inputGrid = [
                    ['-', '#', '-'],
                    ['-', 'b', '-'],
                    ['-', '-', '-']
                    ]
        grids = [np.rot90(inputGrid,rotation) for rotation in np.arange(4)]
        directions = ['RIGHT','UP','UP','UP']
        for count, grid in enumerate(grids):
            self.assertEqual(self.sim.nextMove(grid), directions[count])

    def test_next_move_final_boss(self):
        '''Tests to make sure that the bot can escape a trap'''
        inputGrid = [
                    ['#', '#', '#'],
                    ['#', 'b', '#'],
                    ['#', '-', '#']
                    ]
        grids = [np.rot90(inputGrid,rotation) for rotation in np.arange(4)]
        directions = ['DOWN','RIGHT','UP','LEFT']
        for count, grid in enumerate(grids):
            self.assertEqual(self.sim.nextMove(grid), directions[count])

if __name__ == '__main__':
    unittest.main()