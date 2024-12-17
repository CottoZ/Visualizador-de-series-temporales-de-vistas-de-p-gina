import unittest
import pandas as pd
from time_series_visualizer import TimeSeriesVisualizer

class BarPlotTestCase(unittest.TestCase):
    def setUp(self):
        # Crear un DataFrame de ejemplo con los meses abreviados
        data = {
            'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            'year': [2020] * 12,
            'value': [100, 200, 150, 175, 120, 180, 130, 160, 140, 110, 90, 100]
        }
        self.df = pd.DataFrame(data)
        self.visualizer = TimeSeriesVisualizer(self.df)

    def test_bar_plot_legend_labels(self):
        # Esperamos que los meses abreviados estén en las leyendas
        expected = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        actual = self.visualizer.draw_bar_plot()
        self.assertEqual(actual, expected, "Expected bar plot legend labels to be months of the year.")

class BoxPlotTestCase(unittest.TestCase):
    def setUp(self):
        # Crear un DataFrame de ejemplo con los meses abreviados
        data = {
            'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            'year': [2020] * 12,
            'value': [100, 200, 150, 175, 120, 180, 130, 160, 140, 110, 90, 100]
        }
        self.df = pd.DataFrame(data)
        self.visualizer = TimeSeriesVisualizer(self.df)

    def test_box_plot_labels(self):
        # Esperamos que los meses abreviados estén en las etiquetas
        expected = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        actual = self.visualizer.draw_box_plot()
        self.assertEqual(actual, expected, "Expected box plot 2 secondary labels to be months.")

if __name__ == '__main__':
    unittest.main()
