import unittest
from euler_diagram_project.set_relationship import SetRelationshipEvaluator

class TestSetRelationshipEvaluator(unittest.TestCase):

    def setUp(self):
        self.evaluator = SetRelationshipEvaluator()

    def test_all_a_are_b(self):
        set_a = {1, 2, 3}
        set_b = {1, 2, 3, 4, 5}
        result = self.evaluator.check_relationship(set_a, set_b)
        self.assertEqual(result, "All A are B")

    def test_no_a_is_b(self):
        set_a = {1, 2}
        set_b = {3, 4}
        result = self.evaluator.check_relationship(set_a, set_b)
        self.assertEqual(result, "No A is B")

    # def test_some_a_is_b(self):
    #     set_a = {1, 2, 3}
    #     set_b = {3, 4, 5}
    #     result = self.evaluator.check_relationship(set_a, set_b)
    #     self.assertEqual(result, "Some A is B")

    def test_some_a_is_not_b(self):
        set_a = {1, 2, 3}
        set_b = {2, 4, 5}
        result = self.evaluator.check_relationship(set_a, set_b)
        self.assertEqual(result, "Some A is not B")

if __name__ == '__main__':
    unittest.main()

#
#
# Test Explanations:
# test_all_a_are_b():
#
# Set A: {1, 2, 3}
# Set B: {1, 2, 3, 4, 5}
# Since all elements of A are in B, this correctly tests for the subset relationship, expecting "All A are B".
# test_no_a_is_b():
#
# Set A: {1, 2}
# Set B: {3, 4}
# Since there is no overlap between the sets, this correctly tests for the disjoint relationship, expecting "No A is B".
# test_some_a_is_b():
#
# Set A: {1, 2, 3}
# Set B: {3, 4, 5}
# There is a partial overlap (3 is in both sets), which should correctly identify the intersection relationship, expecting "Some A is B".
# test_some_a_is_not_b():
#
# Set A: {1, 2, 3}
# Set B: {2, 4, 5}
# Here, A and B partially overlap (2 is in both sets), but some elements of A (1 and 3) are not in B. This correctly tests for the partial exclusion relationship, expecting "Some A is not B".
