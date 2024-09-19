import unittest
from unittest.mock import patch, MagicMock
from euler_diagram_project.diagram_visualizer import DiagramVisualizer


class TestDiagramVisualizer(unittest.TestCase):

    def setUp(self):
        self.visualizer = DiagramVisualizer()

    @patch("matplotlib.pyplot.savefig")
    def test_plot_diagram(self, mock_savefig):
        # Mock the savefig method to prevent actual file creation
        set_a = {1, 2, 3}
        set_b = {3, 4, 5}
        relationship = "Some A is B"

        # Mock plt.show to prevent actual display during tests
        with patch("matplotlib.pyplot.show"):
            self.visualizer.plot_diagram(set_a, set_b, relationship)

        # Check if savefig was called with the correct filename
        mock_savefig.assert_called_once_with("visuals/Some A is B.png")


if __name__ == '__main__':
    unittest.main()
