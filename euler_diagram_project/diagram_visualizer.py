import os
import matplotlib.pyplot as plt
from matplotlib_venn import venn2


class DiagramVisualizer:
    def plot_diagram(self, set_a: set, set_b: set, relationship: str):
        # Ensure 'visuals/' directory exists
        if not os.path.exists('visuals'):
            os.makedirs('visuals')

        # Plot the Venn diagram
        plt.figure(figsize=(5, 5))
        venn2([set_a, set_b], set_labels=('A', 'B'))
        plt.title(f"Relationship: {relationship}")

        # Save the diagram to the 'visuals/' folder
        plt.savefig(f"visuals/{relationship}.png")
        plt.show()
