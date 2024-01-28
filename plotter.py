from scipy import stats
from statsmodels.graphics.gofplots import qqplot
from statistical_tests import StatisticalTests
import missingno as msno
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Plotter(StatisticalTests):


    def __init__(self, dataframe):
        self.df = dataframe.copy()
        
    def discrete_probability_distribution(self, column_name, **kwargs):
        plt.rc("axes.spines", top=False, right=False)
        sns.set_style(style='darkgrid', rc=None)
        probs = self.df[column_name].value_counts(normalize=True)
        # Create bar plot
        dpd = sns.barplot(y=probs.values, x=probs.index)
        dpd.set_xticklabels(dpd.get_xticklabels(), rotation=45, ha='right')
        plt.xlabel('Values')
        plt.ylabel('Probability')
        plt.title('Discrete Probability Distribution')
        plt.show()

    def continuous_probability_distribution(self, column_name, column_list=None):
        if column_list is not None:
            for col in column_list:
                sns.histplot(self.df[col], kde=True, color='blue', stat="probability", bins=30)
                super().print_summary_statistics(col)
        else:
            sns.histplot(self.df[column_name], kde=True, color='blue', stat="probability", bins=30)
            super().print_summary_statistics(column_name)

    def correlation_heatmap(self, column_list):
        sns.heatmap(self.df[column_list].corr(), annot=True, cmap='coolwarm')

    def correlation_matrix_df(self):
        corr = self.df.select_dtypes(include=np.number).corr()
        mask = np.zeros_like(corr, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        cmap = sns.diverging_palette(220, 10, as_cmap=True)
        # Draw the heatmap
        sns.heatmap(corr, mask=mask, 
                    square=True, linewidths=.5, annot=True, cmap=cmap)
        plt.yticks(rotation=0)
        plt.title('Correlation Matrix of all Numerical Variables')
        plt.show()

    def qqplot(self,column_list):
        for column in column_list:
            qqplot(self.df[column], scale=1 ,line='q')

    def nulls_dataframe_plot(self):
        msno.matrix(self.df)

    def pair_correlations_grid(self, numeric_features=None):
        if numeric_features is not None:
            sns.pairplot(self.df[numeric_features])
        else:
            numeric_features = super().extract_numeric_features()
            sns.pairplot(self.df[numeric_features])

    def numeric_distributions_grid(self, numeric_features=None, kde=True):
        if numeric_features is not None:
            sns.set(font_scale=0.7)
            f = pd.melt(self.df, value_vars=numeric_features)
            g = sns.FacetGrid(f, col="variable",  col_wrap=3, sharex=False, sharey=False)
            g = g.map(sns.histplot, "value", kde=kde)
        else:
            numeric_features = super().extract_numeric_features()
            sns.set(font_scale=0.7)
            f = pd.melt(self.df, value_vars=numeric_features)
            g = sns.FacetGrid(f, col="variable",  col_wrap=3, sharex=False, sharey=False)
            g = g.map(sns.histplot, "value", kde=kde)

    def count_plot(self, x, **kwargs):
        sns.countplot(x=x)
        x=plt.xticks(rotation=90)

    def count_plots_grid(self, categorical_features):
        figure = pd.melt(self.df, value_vars=categorical_features)
        grid = sns.FacetGrid(figure, col='variable',  col_wrap=3, sharex=False, sharey=False)
        grid = grid.map(self.count_plot, 'value')

    def plot_log_transform(self, col):
        nonzero_values = self.df[col][self.df[col] != 0]
        log_col = nonzero_values.map(lambda i: np.log(i) if i > 0 else 0)
        figure = sns.histplot(log_col,label="Skewness: %.2f"%(log_col.skew()), kde=True)
        figure.legend()
    
    def plot_boxcox_transform(self, col):
        boxcox_population = self.df[col]
        boxcox_population= stats.boxcox(boxcox_population)
        boxcox_population= pd.Series(boxcox_population[0])
        figure = sns.histplot(boxcox_population,label="Skewness: %.2f"%(boxcox_population.skew()))
        figure.legend()
    
    def plot_yeo_johnson_transform(self, col):
        nonzero_values = self.df[col][self.df[col] != 0]
        yeojohnson_population = stats.yeojohnson(nonzero_values)
        yeojohnson_population= pd.Series(yeojohnson_population[0])
        figure = sns.histplot(yeojohnson_population,label="Skewness: %.2f"%(yeojohnson_population.skew()))
        figure.legend()