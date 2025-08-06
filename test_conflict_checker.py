import unittest
from conflict_checker import query_deconfliction

class TestConflictDetection(unittest.TestCase):

    def setUp(self):
        self.primary = {
            "id": "primary",
            "waypoints": [
                {"pos": [50, 50, 30], "t": [100, 110]},
                {"pos": [60, 50, 30], "t": [110, 120]},
            ]
        }

        self.conflicting_sim = [
            {
                "id": "sim_1",
                "waypoints": [
                    {"pos": [51, 50, 30], "t": [105, 115]},  # spatial and temporal overlap
                    {"pos": [70, 50, 30], "t": [120, 130]},
                ]
            }
        ]

        self.clear_sim = [
            {
                "id": "sim_2",
                "waypoints": [
                    {"pos": [100, 100, 30], "t": [105, 115]},  # far away
                    {"pos": [110, 100, 30], "t": [120, 130]},
                ]
            }
        ]

    def test_conflict_detected(self):
        result = query_deconfliction(self.primary, self.conflicting_sim)
        self.assertEqual(result['status'], 'conflict')
        self.assertTrue(len(result['conflicts']) > 0)

    def test_no_conflict_detected(self):
        result = query_deconfliction(self.primary, self.clear_sim)
        self.assertEqual(result['status'], 'clear')
        self.assertEqual(len(result['conflicts']), 0)

if __name__ == '__main__':
    unittest.main()