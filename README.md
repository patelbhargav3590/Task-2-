# Unemployment Analysis with Python 📊

A comprehensive data science project analyzing unemployment trends, with special focus on COVID-19 impact on the job market.

---

## 📋 Project Overview

Unemployment is a critical economic indicator measured by the **unemployment rate** - the percentage of people who are unemployed as part of the total labor force. This project analyzes unemployment data spanning from 2018 to 2024, with particular emphasis on the sharp increase during the COVID-19 pandemic.

### Key Objectives:
- Analyze historical unemployment trends
- Identify patterns and seasonal variations
- Assess the impact of COVID-19 on unemployment
- Generate insightful visualizations
- Provide actionable insights for economic analysis

---

## 📊 Dataset Information

**File:** `unemployment_data.csv`

### Columns:
| Column | Description | Data Type |
|--------|-------------|-----------|
| Date | Month and year of record | DateTime |
| Unemployment_Rate | Percentage of unemployed people | Float |
| Total_Workforce | Total labor force count | Integer |
| Unemployed_Count | Number of unemployed people | Integer |
| Country | Country name | String |

### Dataset Characteristics:
- **Time Period:** January 2018 - June 2024
- **Frequency:** Monthly
- **Records:** 78 observations
- **Country:** United States

### Key Statistics:
- **Highest Unemployment Rate:** 14.7% (April 2020)
- **Lowest Unemployment Rate:** 3.4% (Multiple months in 2023)
- **Average Rate:** 5.47%
- **Pre-COVID Average:** 3.73%
- **COVID Period Average:** 6.85%

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/unemployment-analysis.git
cd unemployment-analysis
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required packages**
```bash
pip install -r requirements.txt
```

---

## 📦 Dependencies

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
```

**Install all dependencies:**
```bash
pip install -r requirements.txt
```

---

## 💻 Usage

### Running the Analysis

```bash
python unemployment_analysis.py
```

This will generate:
1. **Console Output:** Detailed statistical analysis
2. **Visualizations:**
   - `unemployment_trend.png` - Time series trend with COVID marker
   - `unemployment_distribution.png` - Histogram and box plot
   - `unemployment_yearly.png` - Year-over-year comparison

### Example Code

```python
from unemployment_analysis import UnemploymentAnalyzer

# Initialize analyzer
analyzer = UnemploymentAnalyzer('unemployment_data.csv')

# Display dataset overview
analyzer.display_info()

# Analyze trends
analyzer.analyze_trends()

# Analyze COVID impact
analyzer.analyze_covid_impact()

# Generate visualizations
analyzer.plot_unemployment_trend()
analyzer.plot_monthly_distribution()
analyzer.plot_yearly_comparison()

# Generate complete report
analyzer.generate_report()
```

---

## 📈 Key Findings

### Pre-COVID Period (2018-2019)
- Stable unemployment rates between 3.5% - 4.1%
- Average rate: **3.73%**
- Shows healthy labor market conditions
- Slight seasonal variations observed

### COVID-19 Impact (March 2020 onwards)
- **Sharp spike to 14.7%** in April 2020
- Peak represents **3.97% increase** from pre-COVID baseline
- Rapid recovery visible from May 2020 onwards
- Returned to normal levels by mid-2021

### Post-COVID Recovery (2021-2024)
- Gradual stabilization around 3.5% - 4.0%
- Labor market recovery to pre-pandemic levels
- Low unemployment indicates strong job market

---

## 📊 Visualizations Generated

### 1. **Unemployment Trend Over Time**
- Line chart showing historical trends
- COVID-19 onset marked with vertical reference line
- Clearly shows the spike and recovery pattern

### 2. **Distribution Analysis**
- Histogram showing frequency distribution
- Box plot revealing quartiles and outliers
- Helps identify normal vs. anomalous periods

### 3. **Yearly Comparison**
- Multi-year line chart
- Shows evolution across different years
- Identifies seasonal patterns

---

## 📁 Project Structure

```
unemployment-analysis/
│
├── unemployment_analysis.py       # Main analysis script
├── unemployment_data.csv          # Dataset
├── requirements.txt              # Dependencies
├── README.md                     # This file
│
├── outputs/                      # Generated outputs
│   ├── unemployment_trend.png
│   ├── unemployment_distribution.png
│   └── unemployment_yearly.png
│
└── .gitignore
```

---

## 🔍 Code Breakdown

### UnemploymentAnalyzer Class

**Key Methods:**

1. **`__init__(filepath)`**
   - Loads and initializes the dataset
   - Sorts data chronologically

2. **`display_info()`**
   - Shows dataset overview
   - Displays shape, columns, data types
   - Lists missing values and statistics

3. **`analyze_trends()`**
   - Calculates max, min, average rates
   - Performs year-over-year analysis
   - Identifies statistical patterns

4. **`analyze_covid_impact()`**
   - Compares pre-COVID vs COVID periods
   - Quantifies the impact in percentage terms
   - Shows recovery trajectory

5. **`plot_unemployment_trend()`**
   - Creates time series visualization
   - Marks COVID-19 onset
   - Saves as PNG file

6. **`plot_monthly_distribution()`**
   - Generates histogram and box plot
   - Identifies outliers
   - Shows data distribution

7. **`plot_yearly_comparison()`**
   - Compares unemployment across years
   - Shows seasonal variations
   - Saves comparison chart

8. **`generate_report()`**
   - Orchestrates all analysis steps
   - Generates complete report
   - Creates all visualizations

---

## 💡 Analysis Insights

### Questions This Project Answers:

1. **How much did unemployment increase during COVID-19?**
   - Increased from ~3.7% to peak of 14.7%

2. **How long did the recovery take?**
   - Recovered to pre-pandemic levels by mid-2021 (approximately 12-15 months)

3. **Are there seasonal patterns?**
   - Some months show slight variations in unemployment rate

4. **What is the current unemployment trend?**
   - Stabilized around 4% as of June 2024

---

## 🛠️ Customization

### Modify for Different Datasets:

```python
# Update column name if different
unemployment_col = 'YourUnemploymentColumnName'

# Change visualization style
sns.set_style("darkgrid")  # Try: whitegrid, darkgrid, dark, white, ticks

# Adjust COVID period dates
covid_start = '2020-03-01'  # Modify as needed

# Change output resolution
plt.savefig('filename.png', dpi=600)  # 600 DPI for high quality
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Add new analysis features
- Improve documentation

### Steps to contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📚 Learning Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Guide](https://seaborn.pydata.org/tutorial.html)
- [Data Science with Python](https://www.python.org/about/gettingstarted/)

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- Internship: [Company Name]

---

## 🙏 Acknowledgments

- Data sources: U.S. Bureau of Labor Statistics
- Inspiration: COVID-19 economic impact analysis
- Libraries: Pandas, Matplotlib, Seaborn

---

## 📞 Support

For questions or issues, please:
- Open an issue on GitHub
- Contact the project maintainer
- Check existing documentation

---

## 📅 Project Timeline

| Phase | Duration | Status |
|-------|----------|--------|
| Data Collection | 2 weeks | ✅ Complete |
| Data Cleaning | 1 week | ✅ Complete |
| Analysis | 2 weeks | ✅ Complete |
| Visualization | 1 week | ✅ Complete |
| Documentation | 1 week | ✅ Complete |

---

## 🎯 Future Enhancements

- [ ] Add state-level unemployment analysis
- [ ] Implement predictive models
- [ ] Create interactive dashboard
- [ ] Add demographic breakdown
- [ ] Compare with other countries
- [ ] Integrate real-time data updates

---

**Last Updated:** June 2026

**Project Status:** Active ✅

---

Made with ❤️ for data science enthusiasts
