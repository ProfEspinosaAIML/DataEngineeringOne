# Data Engineering & EDA Workshop

## Objective

You will practice hands-on data engineering by:

- Connecting to a free cloud SQL database
- Collecting, cleaning, transforming, and scaling real data using Python and Pandas
- Conducting exploratory data analysis (EDA)
- Creating and explaining insightful visualizations

---

# Instructions

## Part 1: Data Collection & Database Connection

### Create a Free SQL Database

Use **Neon.tech** to set up a free PostgreSQL database (no payment required).

Create a table named `employees` with the following columns:

- `employee_id` (integer, primary key)
- `name` (string)
- `position` (string, IT-related job titles)
- `start_date` (date, between 2015 and 2024)
- `salary` (integer, $60,000–$200,000)

### Generate & Populate Data

- Generate at least 50 synthetic records using Python and the Faker library.
- Insert the data into your cloud database.

### Connect and Load Data

Using Python, `psycopg2`, and Pandas:

1. Connect to your cloud database.
2. Query the entire `employee` table and load the data into a Pandas DataFrame.
3. Display the first few rows using `df.head()`.

---

## Part 2: Exploratory Data Analysis (EDA)

### Explain Each EDA Step in Markdown

Use markdown cells in your notebook to explain:

#### Data Collection
- Where and how you sourced your data.

#### Data Cleaning
- How you checked for missing or incorrect values.

#### Data Transformation
- Any new columns or changes you made (e.g., extracting year, normalizing job titles).

#### Feature Engineering
- Any derived columns (e.g., years of service).

#### Scaling
- Apply scaling or normalization to salary or other numeric columns as appropriate.

### Show Descriptive Statistics

Use:

- `df.info()`
- `df.describe()`
- `df.isnull().sum()`
- Other relevant EDA methods

---

## Part 3: Visualization Challenges

### Standard Visualization

Create a grouped bar chart that displays the average salary by position and start year (see sample code and screenshot from class).

### Advanced Visualization Challenge

Create a more complex dataset by merging or joining additional information.

You can:

- Generate a second table (e.g., departments with department names, locations, budgets, etc.) and join it with employee data.
- Create a project assignment table and analyze the distribution of salaries or years of service by project or department.

### Produce an Advanced Visualization

Examples:

- Heatmap of average salary by department and position.
- Scatter plot with trendline.
- Multi-facet bar chart showing salary trends by department and year.

### Explain Insights

Write a markdown section explaining the main findings from each visualization.

---

## Submission

### Deliverables

- Well-commented Jupyter Notebook (uploaded to GitHub or LMS)
- All steps clearly explained in Markdown
- At least two visualizations:
  - One standard visualization as demonstrated in class
  - One advanced visualization using a more complex dataset you construct

---

# Example Notebook Outline

```markdown
# Data Engineering & EDA Workshop

## 1. Data Collection
*(How you set up the database and collected data)*

## 2. Data Cleaning
*(Show missing value checks, corrections, etc.)*

## 3. Data Transformation & Feature Engineering
*(Explain derived features, e.g., years of service)*

## 4. Scaling
*(Show normalization/scaling of numeric columns)*

## 5. Visualization 1: Average Salary by Position and Start Year
*(Include code and chart, explain findings)*

## 6. Visualization 2: [Your Advanced Chart Here]
*(Show how you constructed/joined new data, explain your chart)*

## 7. Insights & Conclusions
*(Discuss what you learned from the analysis and visualizations)*
```

---

# Part 4: Rubric

| Criteria | Points |
|-----------|--------|
| Database setup & data loading | 1 |
| Data cleaning & transformation | 1 |
| EDA steps are clearly explained | 1 |
| Standard visualization completed | 1 |
| Advanced visualization (complex data) | 2 |
| **Total** | **6** |

---

# Part 5: Late Delivery

- A 20% penalty will be applied to any late delivery up to 24 hours after the due date.
- A 40% penalty will be applied to any late delivery between 24 and 48 hours after the due date.
- A score of 0 points will be assigned if the project is not submitted.
