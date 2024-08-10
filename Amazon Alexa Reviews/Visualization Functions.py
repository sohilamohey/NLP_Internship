import pandas as pd
import datetime as dt
import warnings

# Visualization
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.graph_objs as go
import plotly.offline as py
#sns.color_palette("dark:salmon_r", as_cmap=True)

# Sets a filter to ignore warnings using the 'ignore' parameter.
warnings.filterwarnings('ignore') 


# Draw Bar Chart
def draw_bar_chart(df, x, y, title, column_name, y_name):
    import plotly.express as px

    # Set a dark color palette directly within Plotly Express
    fig = px.bar(df, x=x, y=y, color_discrete_sequence=["darkred"], text=y, title=title)

    # Update layout for better appearance
    fig.update_layout(
        xaxis_title=column_name.capitalize(),
        yaxis_title=y_name.capitalize(),
        font=dict(size=14, family="Arial"),
        title_font=dict(size=18, family="Arial", color="black"),
        title_x=0.5  # Center the title
    )

    # Show the plot
    fig.show()
    
# Line chart
def DrawLineChart(df, x, y, title, xlabel, ylabel,  angle = 0):
    # Create a line plot trace
    trace = go.Scatter(
        x=df[x],
        y=df[y],
        mode='lines+markers',
        marker=dict(symbol='circle', size=8, color='lightcoral', line=dict(color='rgba(0,0,0,0)')),  # Use transparent line color
        line=dict(color='lightcoral', width=2),
        name='Line Plot'
    )
    # Create the layout
    layout = go.Layout(
        title=title,
        title_x=0.5,  # Title alignment to the center
        xaxis=dict(title=xlabel, tickfont=dict(size=10), showgrid=True, tickangle=angle),
        yaxis=dict(title=ylabel, tickfont=dict(size=13), showgrid=True),
        plot_bgcolor='white',
        showlegend=False,
        xaxis_showgrid=True,  # Show grid
        yaxis_showgrid=True,  # Show grid
    )
    # Create the figure
    fig = go.Figure(data=[trace], layout=layout)
    # Show the figure
    fig.show()
    
    
# Plot Missing Values to Unmissing in Spacific Column
def plot_missing(df, column):
    missing_data = df[column].isnull().sum()
    total_data = len(df)
    percentage_missing = (missing_data / total_data) * 100
    
    # Plotly bar plot
    fig = go.Figure(data=[
        go.Bar(x=[f"Missing {column}", f"Present {column}"],
               y=[missing_data, total_data - missing_data],
               marker_color='lightcoral')
    ])
    
    fig.update_layout(title=f"Percentage of Missing Values in {column}: {percentage_missing:.2f}%",
                      xaxis_title=column,
                      yaxis_title="Number of Values",
                      bargap=0.2)
    fig.show()     
    
    
#Histogram
def DrawHistogram(df, x, bins, xlabel, ylabel, title):
    # Plotting the histogram
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df[x], nbinsx=bins, marker_color='lightcoral'))
    # Update layout
    fig.update_layout(
        title=title,
        title_x=0.5,  # Title alignment to the center
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        xaxis=dict(tickfont=dict(size=12)),
        yaxis=dict(tickfont=dict(size=12)),
        bargap=0.05,
        plot_bgcolor='white',
        showlegend=False
    )
    fig.show()
    
    
# Draw Pie Chart
def draw_pie_chart_go(labels, values, title):
    colorscale = 'dark'
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title=title)
    fig.show()           