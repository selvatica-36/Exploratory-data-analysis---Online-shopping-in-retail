from info_extractor import DataFrameInfo
from scipy.stats import chi2_contingency, normaltest
from typing import List
import pandas as pd


class StatisticalTests(DataFrameInfo):


    def __init__(self, dataframe):
        self.df = dataframe.copy()

    # NOTE Really like the method though 
    def chi_square_test(self, independent_variable: str, dependant_variables: List[str]) -> float:
        """
        Perform chi-square test between two categorical variables.

        Parameters:
        - independent_variable (str): Name of the independent variable.
        - dependent_variables (List[str]): List of dependent variables to test against the independent variable.

        Returns:
        - float: p-value of the chi-square test.

        """
        # Only between categorical variables
        chi_sq_test_df = self.df.copy()
        chi_sq_test_df[independent_variable] = chi_sq_test_df[independent_variable].isnull()
        # Step 2: Crosstab the new column with B
        if len(dependant_variables) > 3:
            for column in dependant_variables:
                contingency_table = pd.crosstab(chi_sq_test_df[independent_variable], chi_sq_test_df[column])
                # Step 3: Perform chi-squared test
                chi2, p, dof, expected = chi2_contingency(contingency_table)
                if p < 0.05:
                    print(f"Chi-square test for missing values in {independent_variable} against {column} column: ")
                    print(f"p-value = {p}: Significant")
                    return p
                elif p == 0.05:
                    print(f"Chi-square test for missing values in {independent_variable} against {column} column: ")
                    print(f"p-value = {p}: Likely not significant")
                    return p
        elif len(dependant_variables) <= 3:
            for column in dependant_variables:
                contingency_table = pd.crosstab(chi_sq_test_df[independent_variable], chi_sq_test_df[column])
                # Step 3: Perform chi-squared test
                chi2, p, dof, expected = chi2_contingency(contingency_table)
                print(f"Chi-square test for missing values in {independent_variable} against {column} column: ")
                print(f"p-value = {p}")
                return p
            
    def K2_test(self, column_name): # Test for normality in continuous variables
        stat, p = normaltest(self.df[column_name], nan_policy='omit')
        print('Statistics=%.3f, p=%.3f' % (stat, p))