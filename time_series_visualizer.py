import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class TimeSeriesVisualizer:
    def __init__(self, df):
        self.df = df

    def draw_line_plot(self):
        """Función para dibujar el gráfico de líneas."""
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.lineplot(data=self.df, x='year', y='value', ax=ax)
        ax.set_title('Line Plot')
        ax.set_xlabel('Year')
        ax.set_ylabel('Page Views')
        plt.show()

    def draw_bar_plot(self):
        """Función para dibujar el gráfico de barras."""
        # Agrupar los datos por mes y sumar los valores
        fig, ax = plt.subplots(figsize=(10, 5))
        df_bar = self.df.groupby(['month'])['value'].sum().reset_index()
        
        # Graficar las barras
        sns.barplot(data=df_bar, x='month', y='value', ax=ax)

        # Usamos abreviaturas de los meses
        months_abbrev = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        ax.set_xticklabels(months_abbrev, rotation=45)

        # Retornar las leyendas
        return [item.get_text() for item in ax.get_xticklabels()]

    def draw_box_plot(self):
        """Función para dibujar el gráfico de box plot."""
        fig, ax1 = plt.subplots(figsize=(10, 5))
        df_box = self.df[['year', 'month', 'value']]
        
        # Graficar el box plot
        sns.boxplot(data=df_box, x='year', y='value', ax=ax1)

        # Establecer los meses abreviados en las etiquetas para el eje X
        months_abbrev = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        # Aquí se asegura de que las etiquetas se apliquen correctamente en el eje X
        ax1.set_xticks(range(12))  # Establecer los ticks en las posiciones correctas
        ax1.set_xticklabels(months_abbrev, rotation=45)  # Establecer las etiquetas de los meses

        # Retornar las leyendas
        return [item.get_text() for item in ax1.get_xticklabels()]
