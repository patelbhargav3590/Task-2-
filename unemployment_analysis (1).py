import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

class UnemploymentAnalyzer:
    """
    A class to analyze unemployment data and generate insights
    """
    
    def __init__(self, filepath):
        """Initialize the analyzer with a dataset"""
        self.df = pd.read_csv(filepath)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df = self.df.sort_values('Date')
        
    def display_info(self):
        """Display basic information about the dataset"""
        print("=" * 60)
        print("UNEMPLOYMENT ANALYSIS DATASET OVERVIEW")
        print("=" * 60)
        print(f"\nDataset Shape: {self.df.shape}")
        print(f"\nColumn Names:\n{self.df.columns.tolist()}")
        print(f"\nFirst Few Rows:\n{self.df.head()}")
        print(f"\nData Types:\n{self.df.dtypes}")
        print(f"\nMissing Values:\n{self.df.isnull().sum()}")
        print(f"\nBasic Statistics:\n{self.df.describe()}")
        
    def analyze_trends(self):
        """Analyze unemployment trends over time"""
        print("\n" + "=" * 60)
        print("UNEMPLOYMENT RATE TRENDS")
        print("=" * 60)
        
        unemployment_col = 'Unemployment_Rate'
        if unemployment_col in self.df.columns:
            print(f"\nHighest Unemployment Rate: {self.df[unemployment_col].max():.2f}%")
            print(f"Lowest Unemployment Rate: {self.df[unemployment_col].min():.2f}%")
            print(f"Average Unemployment Rate: {self.df[unemployment_col].mean():.2f}%")
            print(f"Median Unemployment Rate: {self.df[unemployment_col].median():.2f}%")
            print(f"Standard Deviation: {self.df[unemployment_col].std():.2f}%")
            
            # Year-over-year analysis
            self.df['Year'] = self.df['Date'].dt.year
            print(f"\nUnemployment by Year:")
            print(self.df.groupby('Year')[unemployment_col].agg(['min', 'max', 'mean']))
        
    def analyze_covid_impact(self):
        """Analyze the impact of COVID-19 on unemployment"""
        print("\n" + "=" * 60)
        print("COVID-19 IMPACT ANALYSIS")
        print("=" * 60)
        
        unemployment_col = 'Unemployment_Rate'
        if unemployment_col in self.df.columns:
            # Pre-COVID (before March 2020)
            pre_covid = self.df[self.df['Date'] < '2020-03-01'][unemployment_col]
            # COVID period (March 2020 onwards)
            covid_period = self.df[self.df['Date'] >= '2020-03-01'][unemployment_col]
            
            if len(pre_covid) > 0:
                print(f"\nPre-COVID Average Rate (before March 2020): {pre_covid.mean():.2f}%")
                print(f"COVID Period Average Rate (March 2020 onwards): {covid_period.mean():.2f}%")
                
                if len(covid_period) > 0:
                    increase = covid_period.max() - pre_covid.mean()
                    print(f"\nMaximum Increase from Pre-COVID Baseline: {increase:.2f}%")
                    print(f"Peak Unemployment during COVID: {covid_period.max():.2f}%")
        
    def plot_unemployment_trend(self, save_path='unemployment_trend.png'):
        """Plot unemployment rate over time"""
        unemployment_col = 'Unemployment_Rate'
        if unemployment_col in self.df.columns:
            plt.figure(figsize=(14, 7))
            plt.plot(self.df['Date'], self.df[unemployment_col], linewidth=2, color='#E74C3C')
            plt.axvline(x=pd.to_datetime('2020-03-01'), color='red', linestyle='--', 
                       label='COVID-19 Start', alpha=0.7)
            plt.fill_between(self.df['Date'], self.df[unemployment_col], alpha=0.3, color='#E74C3C')
            
            plt.title('Unemployment Rate Trend Over Time', fontsize=16, fontweight='bold')
            plt.xlabel('Date', fontsize=12)
            plt.ylabel('Unemployment Rate (%)', fontsize=12)
            plt.legend(fontsize=11)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"\n✓ Trend plot saved as '{save_path}'")
            plt.show()
    
    def plot_monthly_distribution(self, save_path='unemployment_distribution.png'):
        """Plot distribution of unemployment rates"""
        unemployment_col = 'Unemployment_Rate'
        if unemployment_col in self.df.columns:
            fig, axes = plt.subplots(1, 2, figsize=(14, 5))
            
            # Histogram
            axes[0].hist(self.df[unemployment_col], bins=30, color='#3498DB', edgecolor='black', alpha=0.7)
            axes[0].set_title('Distribution of Unemployment Rates', fontsize=12, fontweight='bold')
            axes[0].set_xlabel('Unemployment Rate (%)')
            axes[0].set_ylabel('Frequency')
            axes[0].grid(True, alpha=0.3)
            
            # Box plot
            axes[1].boxplot(self.df[unemployment_col], vert=True)
            axes[1].set_title('Box Plot of Unemployment Rates', fontsize=12, fontweight='bold')
            axes[1].set_ylabel('Unemployment Rate (%)')
            axes[1].grid(True, alpha=0.3)
            
            plt.tight_layout()
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Distribution plot saved as '{save_path}'")
            plt.show()
    
    def plot_yearly_comparison(self, save_path='unemployment_yearly.png'):
        """Compare unemployment rates across years"""
        unemployment_col = 'Unemployment_Rate'
        if unemployment_col in self.df.columns:
            self.df['Year'] = self.df['Date'].dt.year
            
            plt.figure(figsize=(12, 6))
            for year in self.df['Year'].unique():
                year_data = self.df[self.df['Year'] == year]
                plt.plot(year_data['Date'], year_data[unemployment_col], 
                        marker='o', label=str(year), linewidth=2)
            
            plt.title('Unemployment Rate Comparison by Year', fontsize=14, fontweight='bold')
            plt.xlabel('Month')
            plt.ylabel('Unemployment Rate (%)')
            plt.legend(loc='best')
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Yearly comparison plot saved as '{save_path}'")
            plt.show()
    
    def generate_report(self):
        """Generate a complete analysis report"""
        print("\n" + "=" * 60)
        print("COMPLETE UNEMPLOYMENT ANALYSIS REPORT")
        print("=" * 60)
        print(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        self.display_info()
        self.analyze_trends()
        self.analyze_covid_impact()
        
        print("\n" + "=" * 60)
        print("Generating Visualizations...")
        print("=" * 60)
        
        self.plot_unemployment_trend()
        self.plot_monthly_distribution()
        self.plot_yearly_comparison()
        
        print("\n" + "=" * 60)
        print("ANALYSIS COMPLETE!")
        print("=" * 60)


if __name__ == "__main__":
    # Initialize the analyzer
    analyzer = UnemploymentAnalyzer('unemployment_data.csv')
    
    # Generate comprehensive report
    analyzer.generate_report()
