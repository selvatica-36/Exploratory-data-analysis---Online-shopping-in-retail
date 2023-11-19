from scipy import stats
from statsmodels.graphics.gofplots import qqplot
import missingno as msno
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns


class DataFrameInfo:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def _get_slice(self, columns=None):
        if columns is not None:
            try:
                if isinstance(columns, list): # slice by column names
                    columns = [col.lower() for col in columns]
                    return self.df[columns]
                elif isinstance(columns, str): #choose one column only, allows for string outside list
                    columns = columns.lower()
                    return self.df[[columns]]
                elif isinstance(columns, tuple) and len(columns) == 2 and all(isinstance(col, int) for col in columns):
                    return self.df.iloc[:, columns[0]:columns[1] + 1]
                else:
                    raise ValueError
            except KeyError as ke:
                print(f"KeyError: you need to provide a valid column name: {ke}")
            except ValueError as ve:
                print(f"ERROR: Invalid columns parameter. Use a list of valid column names formatted as strings, or a numerical interval formatted as a tuple e.g. (0,3): {ve}")
            except AttributeError as ae:
                print(f"ERROR: Invalid columns parameter. Use a list of valid column names formatted as strings, or a numerical interval formatted as a tuple e.g. (0,3): {ae}")
        else:
            return self.df
    def extract_column_names(self, columns=None):
        subset = self._get_slice(columns)
        return list(subset.columns)
    def data_types_columns(self, columns=None):
        subset = self._get_slice(columns)
        return subset.dtypes
    def info_columns(self, columns=None):
        subset = self._get_slice(columns)
        return subset.info()
    def extract_statistical_values(self, columns=None):
        subset = self._get_slice(columns)
        return subset.describe()
    def show_distinct_values(self,columns=None):
        subset = self._get_slice(columns)
        for column in subset:
            try:
                print(f"Unique values in {column}:", np.sort(self.df[column].unique()))
            except TypeError:
                print(f"Unique values in {column}:", self.df[column].unique())
    def count_distinct_values(self, columns=None):
        subset = self._get_slice(columns)
        distinct_counts = pd.DataFrame({
            'column': subset.columns,
            'distinct_values_count': [subset[column].nunique() for column in subset.columns]
        })
        distinct_counts.set_index(['column'], inplace=True)
        return distinct_counts
    def print_shape(self, columns=None):
        subset = self._get_slice(columns)
        print("DataFrame Shape:", subset.shape)
    def generate_null_counts(self, columns=None):
        subset = self._get_slice(columns)
        null_counts = subset.isnull().sum()
        null_percentages = (null_counts / len(subset)) * 100
        null_info = pd.DataFrame({
            'null_count': null_counts,
            'null_percentage': null_percentages
        })
        return null_info
    def extract_numeric_features(self):
        numeric_features = self.df.select_dtypes(include = np.number)
        return numeric_features
    def extract_categorical_features(self, numeric_features=None):
        if numeric_features is not None:
            categorical_features = [col for col in self.df.columns if col not in numeric_features]
            return categorical_features
        else:
            numeric_features = self.extract_numeric_features()
            categorical_features = [col for col in self.df.columns if col not in numeric_features]
            return categorical_features
    def print_summary_statistics(self, column_name):
            print(f"The mode of the distribution is {self.df[column_name].mode()[0]}")
            print(f"The mean of the distribution is {self.df[column_name].mean()}")
            print(f"The median of the distribution is {self.df[column_name].median()}")


class DataTransform:
        def __init__(self, dataframe):
            self.df = dataframe.copy()

        def convert_to_type(self, column_name, data_type, ignore_errors = True):
                data_type = data_type.lower()
                if ignore_errors == True:
                    try:
                        if data_type == 'datetime':
                            self.df[column_name] = pd.to_datetime(self.df[column_name], errors = 'coerce')
                        elif data_type == 'date':
                            self.df[column_name] = pd.to_datetime(self.df[column_name], errors = 'coerce')
                        elif data_type == 'categorical':
                            self.df[column_name] = pd.Categorical(self.df[column_name])
                        elif data_type == 'str':
                            self.df[column_name] = self.df[column_name].astype(str, errors='ignore')
                        elif data_type == 'float' or data_type == 'float64':
                            self.df[column_name] = self.df[column_name].astype(float, errors='ignore')
                        elif data_type == 'int' or data_type == 'int64':
                            self.df[column_name] = self.df[column_name].astype(int, errors='ignore')
                        elif data_type == 'bool':
                            self.df[column_name] = self.df[column_name].astype(bool, errors='ignore')
                        else:
                            print(f"Error: data type {data_type} not supported. Check docstrings or call help for more information.")
                    except Exception as e:
                        print(f"Error converting column '{column_name}' to type '{data_type}': {e}")
                    return self.df.copy()
                elif ignore_errors == False:
                    try:
                        if data_type == 'datetime':
                            self.df[column_name] = pd.to_datetime(self.df[column_name])
                        elif data_type == 'date':
                            self.df[column_name] = pd.to_datetime(self.df[column_name])
                        elif data_type == 'timedelta':
                            self.df[column_name] = pd.to_timedelta(self.df[column_name])
                        elif data_type == 'categorical':
                            self.df[column_name] = pd.Categorical(self.df[column_name])
                        elif data_type == 'str':
                            self.df[column_name] = self.df[column_name].astype(str)
                        elif data_type == 'float' or data_type == 'float64':
                            self.df[column_name] = self.df[column_name].astype(float)
                        elif data_type == 'int' or data_type == 'int64':
                            self.df[column_name] = self.df[column_name].astype(int)
                        elif data_type == 'bool':
                            self.df[column_name] = self.df[column_name].astype(bool)
                        else:
                            print(f"Error converting column '{column_name}' to type '{data_type}': {e}")
                    except Exception as e:
                        print(f"Error converting column '{column_name}' to type '{data_type}': {e}")
                    return self.df.copy()
                else:
                    print("Error: the parameter 'ignore_errors' is a bool and can only be True or False.")

        def convert_month_to_period(self, column_name):
            try:
                self.df[column_name] = self.df[column_name].astype(str)
                self.df['month'] = self.df['month'].str.lower()
                month_map = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'june': 6,
                            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
                self.df[column_name] = self.df[column_name].map(month_map)
                self.df[column_name] = pd.to_datetime(self.df[column_name], format='%m', errors='coerce').dt.to_period('M')
            except Exception as e:
                print(f"Error converting 'month' column to period: {e}")
            return self.df.copy()

        def convert_columns(self, column_list, data_type, ignore_errors=True):
            for column in column_list:
                self.convert_to_type(column, data_type, ignore_errors)
            return self.df.copy()
        
        def impute_nulls_with_median(self, columns_list):
                for column in columns_list:
                    self.df[column] = self.df[column].fillna(self.df[column].median())
                return self.df
        def impute_nulls_with_mean(self, columns_list):
                for column in columns_list:
                    self.df[column] = self.df[column].fillna(self.df[column].mean())
                return self.df
        def impute_nulls_with_mode(self, columns_list):
                for column in columns_list:
                    self.df[column] = self.df[column].fillna(self.df[column].mode()[0])
                return self.df
        def plot_log_transform(self, column_list):
            for col in column_list:
                log_col = self.df[col].map(lambda i: np.log(i) if i > 0 else 0)
                t=sns.histplot(log_col,label="Skewness: %.2f"%(log_col.skew()), kde=True )
                t.legend()
                t.title(f"{col}")
        def log_transform(self, column_list):
            for col in column_list:
                self.df[col] = self.df[col].map(lambda i: np.log(i) if i > 0 else 0)
        def plot_boxcox_transform(self, column_list):
            for col in column_list:
                boxcox_population = self.df[col]
                boxcox_population= stats.boxcox(boxcox_population)
                boxcox_population= pd.Series(boxcox_population[0])
                t=sns.histplot(boxcox_population,label="Skewness: %.2f"%(boxcox_population.skew()) )
                t.legend()
        def boxcox_transform(self, column_list):
            for col in column_list:
                self.df[col]= stats.boxcox(self.df[col])    
        def plot_yeo_johnson_transform(self, column_list):
            for col in column_list:
                yeojohnson_population = self.df[col]
                yeojohnson_population = stats.yeojohnson(yeojohnson_population)
                yeojohnson_population= pd.Series(yeojohnson_population[0])
                t=sns.histplot(yeojohnson_population,label="Skewness: %.2f"%(yeojohnson_population.skew()) )
                t.legend()
        def yeo_johnson_transform(self, column_list):
            for col in column_list:
                self.df[col] = stats.yeojohnson(self.df[col])

            
class StatisticalTests(DataFrameInfo):
    def __init__(self, dataframe):
        self.df = dataframe.copy()
        
    def chi_square_test(self, column_1, column_list): # Only between categorical variables
        chi_sq_test_df = self.df.copy()
        chi_sq_test_df[column_1] = chi_sq_test_df[column_1].isnull()
        # Step 2: Crosstab the new column with B
        if len(column_list) > 3:
            for column in column_list:
                contingency_table = pd.crosstab(chi_sq_test_df[column_1], chi_sq_test_df[column])
                # Step 3: Perform chi-squared test
                chi2, p, dof, expected = chi2_contingency(contingency_table)
                if p < 0.05:
                    print(f"Chi-square test for missing values in {column_1} against {column} column: ")
                    print(f"p-value = {p}: Significant")
                    return p
                elif p == 0.05:
                    print(f"Chi-square test for missing values in {column_1} against {column} column: ")
                    print(f"p-value = {p}: Likely not significant")
                    return p
        elif len(column_list) <= 3:
            for column in column_list:
                contingency_table = pd.crosstab(chi_sq_test_df[column_1], chi_sq_test_df[column])
                # Step 3: Perform chi-squared test
                chi2, p, dof, expected = chi2_contingency(contingency_table)
                print(f"Chi-square test for missing values in {column_1} against {column} column: ")
                print(f"p-value = {p}")
                return p
    def K2_test(self, column_name): # Test for normality in continuous variables
        stat, p = normaltest(self.df[column_name], nan_policy='omit')
        print('Statistics=%.3f, p=%.3f' % (stat, p))



class Plotter(StatisticalTests):
    def __init__(self,dataframe):
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
        corr = self.df.select_dtypes(include = np.number).corr()
        mask = np.zeros_like(corr, dtype=np.bool_)
        mask[np.triu_indices_from(mask)] = True
        # set thins up for plotting
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
        f = pd.melt(self.df, value_vars=categorical_features)
        g = sns.FacetGrid(f, col='variable',  col_wrap=3, sharex=False, sharey=False)
        g = g.map(self.count_plot, 'value')
  
    


    
    

    

    

        