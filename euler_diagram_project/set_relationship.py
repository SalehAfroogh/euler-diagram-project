class SetRelationshipEvaluator:
    def check_relationship(self, set_a: set, set_b: set) -> str:
        if set_a.issubset(set_b):
            return "All A are B"
        elif set_b.issubset(set_a):
            return "All B are A"
        elif set_a.isdisjoint(set_b):
            return "No A is B"
        elif set_a & set_b:  # There is an intersection
            if set_a - set_b and set_b - set_a:  # Some elements of A are not in B, and some elements of B are not in A
                return "Some A is not B"
            return "Some A is B"  # Pure intersection case
        else:
            return "Unknown relationship"
