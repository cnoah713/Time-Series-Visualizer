import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col = 'date', parse_dates = True)
# Clean data
df = df[(df.value < df.value.quantile(0.975)) & (df.value > df.value.quantile(0.025)) ]


def draw_line_plot():
    # Create a function that generates a line plot of the data
  fig = plt.figure()
  plt.plot(df.index, df.value)
  plt.xlabel('Date')
  plt.ylabel('Page Views')
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')





    # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar['year'] = df_bar.index.year
  df_bar['month'] = df_bar.index.month_name()
  df_bar = df_bar.groupby(['year','month'])['value'].mean().round()
  df_bar = df_bar.reset_index()
  df_bar = df_bar.rename(columns={"value": "Average Page Views"})
    # Draw bar plot
  fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
  ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")
  chart = sns.barplot(data = df_bar, x = 'year', y = 'Average Page Views', hue = 'month', palette = "tab10")
  handles, labels = plt.gca().get_legend_handles_labels()
  months_order = ['January','February','March','April','May','June','July','August','September','October','November','December']
  plt.legend([handles[labels.index(label)] for label in months_order], months_order)
  ax.set_xlabel('Years')
  




    # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) =plt.subplots(1,2, figsize = (20,10))
    sns.boxplot(data = df_box, x ='year', y ='value', ax = ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug','Sep','Oct','Nov','Dec']
    sns.boxplot(data = df_box, x = 'month', y = 'value',order = months_order, ax = ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
