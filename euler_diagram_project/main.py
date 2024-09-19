from euler_diagram_project.set_relationship import SetRelationshipEvaluator
from euler_diagram_project.diagram_visualizer import DiagramVisualizer
from euler_diagram_project.utils import load_sets_from_file, pretty_print_result


def main():
    # Load the sets from a text file
    set_a, set_b = load_sets_from_file("sample_sets.txt")

    # Evaluate the relationship
    evaluator = SetRelationshipEvaluator()
    relationship = evaluator.check_relationship(set_a, set_b)

    # Print the result:
    pretty_print_result(relationship)

    # Visualize the result
    visualizer = DiagramVisualizer()
    visualizer.plot_diagram(set_a, set_b, relationship)


if __name__ == "__main__":
    main()
