# IBM Employee Attrition Analysis

## Dataset Overview

The dataset encompasses 1470 entries, each representing an individual employee, and 35 columns that provide various details about them. Below is a succinct description of each column:

- **Age**: Age of the employee.
- **Attrition**: Indicates whether the employee left the company or not (Yes/No).
- **BusinessTravel**: Frequency of business travel (Non-Travel, Travel_Rarely, Travel_Frequently).
- **DailyRate**: Daily rate of payment for the employee.
- **Department**: Department in which the employee works (e.g., Sales, Research & Development).
- **DistanceFromHome**: Distance from the employee's home to work.
- **Education**: Educational level of the employee.
- **EducationField**: Field of study of the employee (e.g., Life Sciences, Medical).
- **EmployeeCount**: Constant value of 1 across all entries, likely non-informative.
- **EmployeeNumber**: Unique identifier assigned to each employee.
- **EnvironmentSatisfaction**: Employee's rating of their environment satisfaction.
- **Gender**: Gender of the employee (Male/Female).
- **HourlyRate**: Hourly rate of payment for the employee.
- **JobInvolvement**: Employee's job involvement rating.
- **JobLevel**: Level of the employee's job.
- **JobRole**: Employee's role within the company (e.g., Sales Executive, Research Scientist).
- **JobSatisfaction**: Employee's job satisfaction rating.
- **MaritalStatus**: Marital status of the employee (Single, Married, Divorced).
- **MonthlyIncome**: Monthly income of the employee.
- **MonthlyRate**: Monthly rate of the employee.
- **NumCompaniesWorked**: Number of companies the employee has worked for.
- **Over18**: Whether the employee is over 18 years of age (Y/N).
- **OverTime**: Whether the employee works overtime or not (Yes/No).
- **PercentSalaryHike**: Percentage increase in salary.
- **PerformanceRating**: Employee's performance rating.
- **RelationshipSatisfaction**: Employee's relationship satisfaction rating.
- **StandardHours**: Constant value of 80 across all entries, likely non-informative.
- **StockOptionLevel**: Level of the employee’s stock option.
- **TotalWorkingYears**: Total number of working years of the employee.
- **TrainingTimesLastYear**: Number of training sessions attended last year.
- **WorkLifeBalance**: Employee's work-life balance rating.
- **YearsAtCompany**: Number of years the employee has worked for the company.
- **YearsInCurrentRole**: Number of years in the current role.
- **YearsSinceLastPromotion**: Number of years since last promotion.
- **YearsWithCurrManager**: Number of years with the current manager.

## Potential Use-Cases

This dataset could serve various analytic purposes like understanding factors contributing to employee attrition, analyzing variables influencing job satisfaction, or investigating the effect of different variables on employees’ monthly income, among other potential analyses.

## Analysis Overview

In the analysis, the target variable was balanced post-identification and handling of outliers using the Windsorized method. Following this, a correlation analysis was conducted, succeeded by train-test split of the data. Two initial models, Logistic Regression and Decision Tree, were developed, which identified the need for data scaling prior to constructing forecasting models. Consequently, Standard Scaler and SMOTE were employed, and various models like Logistic Regression, Decision Tree, RandomForest, AdaBoost, Bagging, and XGBC were evaluated. The XGBC model was identified to perform optimally for the considered IBM dataset.

## Visual Insights

<img width="1055" alt="257909299-857108d0-9d7f-4db2-a32b-332b71063265" src="https://github.com/K-Majeti/Python-Projects/assets/136497111/1dd1b799-94ef-4680-876f-c9292e9f3714">


From the comparison of box plot diagrams, it is evident that Random Forest and XGBC emerge as superior models. However, upon inspecting train and test scores of both Random Forest and XGBC, it is observed that the XGBC model demonstrates superior performance on both train and test data, establishing it as the preferred model.
