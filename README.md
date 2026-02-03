Project Overview

This project focuses on the comprehensive Exploratory Data Analysis (EDA) and Feature Engineering of a dataset containing TED Talks information. The primary goal is to analyze audience engagement by unpacking complex, nested sentiment data and examining how various factors—such as speaker occupation and talk duration—influence viewership over time.

Key Objectives

Data Wrangling & Cleaning: Standardizing the dataset, identifying duplicate entries (specifically within talk titles), and ensuring data consistency across multiple variables.

Sentiment Unpacking: Transforming nested dictionary structures within the ‘ratings’ column into a flat, tabular format. This involves mapping diverse audience reactions (e.g., Funny, Courageous, Informative) into individual numerical features.

Performance Metrics: Calculating and visualizing engagement ratios, such as views per presentation, to identify high-impact years and trends.

Correlation Analysis: Identifying relationships between different user sentiments and metadata to understand what drives a "viral" or highly-rated presentation.

Technical Methodology

The analysis is performed using Python and the Pandas library, leveraging efficient data manipulation techniques:

Parsing: Converting raw string representations into structured Python objects using ast.literal_eval.

Vectorization: Utilizing .itertuples() and direct column access to optimize processing speed during data transformation.

Data Integration: Executing complex merge and join operations to consolidate metadata with the newly generated sentiment features.

Statistical Summary: Generating descriptive statistics to provide a high-level overview of the sentiment distribution across the entire TED library.
