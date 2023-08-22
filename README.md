# Chain Weighted Real GDP Calculator
### Video Demo: https://youtu.be/jviFJCeBntI
## Background
#### I am currently studying economics and data science in college. This led me to a realization: I wanted to take advantage of my insights from economics with coding skills to create a tool that could enhance my learning experience. In the realm of macroeconomics, I focused on the concept of Real GDP, which gauges the growth of a country's total economic output while factoring out inflation. An approach to refine the accuracy of measuring real GDP growth involves the utilization of the chain weighted method. This method computes the geometric average of real GDP growth rates. Despite its capacity to yield more precise results, employing this method is tedious and a minor miscalculation could potentially disrupt the entire process. My struggles centered around grappling with practice problems, as uncertainty loomed over the accuracy of my final calculations as answers were not provided. In light of these challenges, I took the initiative to develop a computational tool that calculates chain weighted real GDP. This tool not only empowers users to verify the correctness of their calculations, but also facilitates the derivation of a more precise real GDP figure.

## Functions and Classes
#### Within the project.py, I created a Data_Storage class that enables users to input and retain data pertaining to production quantities, sales figures, and individual product costs. Given the prerequisite that the year, product name, and product number remain consistent across years for accurate real GDP computation, I devised functions external to the class to extract these essential variables. Step-by-step calculations follow the setter and getter functions. These computations are ultimately summarized within the calculator function, culminating in a comprehensive summary.

## How to Find Chain Weighted Real GDP
#### For the computation of chain weighted real GDP, an initial step entails determining the real GDP for each year using the respective year's costs, as well as the real GDP using the costs from another year. The year for which the prices are used is designated as the "base year." Once these calculations yield four distinct real GDP values, the subsequent task involves evaluating the real GDP growth between two specific years. This is achieved by dividing the real GDP of the second year by that of the first year, with both years referencing the same base year. Deriving the chain weighted real GDP growth factor involves multiplying the two growth rates and then calculating the square root of the resulting product. With this chain weighted real GDP growth factor in hand, one can proceed to ascertain the chain weighted real GDP for each year. This process entails multiplying the real GDP of the first year (computed using the first year as the base) by the chain weighted growth factor. Similarly, the chain weighted real GDP for the second year is determined by dividing the real GDP of the second year (based on the second year's prices) by the chain weighted growth factor. This reciprocal relationship facilitates the calculation of the chain weighted real GDP for both years.

## Summary
#### As evident, the procedure is notably intricate and laborious. Having a software application that arranges the data systematically within a table, thereby enabling users to visually comprehend the information, coupled with its ability to perform the intricate calculations, maximizes the ability for the program to assist the user. This tool would not only facilitate students in cross-verifying their practice exercises, but also considerably simplify the tasks of users seeking chain weighted real GDP values for specific products.
