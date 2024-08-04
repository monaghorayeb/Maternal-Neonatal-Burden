import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Burden of Maternal and Neonatal Deaths in the World Dashboard")

# Burden in 2021
graph_url1 = "https://ihmeuw.org/6hmv"
st.markdown(f'<iframe src="{graph_url1}" width="100%" height="600px"></iframe>', unsafe_allow_html=True)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Barplot 1: Maternal death by region
data1 = pd.read_csv("maternal-deaths-number-by-region.csv")

regions = ['North America (WB)', 'Europe and Central Asia (WB)', 'Middle East and North Africa (WB)', 'Latin America and Caribbean (WB)', 
           'East Asia and Pacific (WB)', 'South Asia (WB)', 'Sub-Saharan Africa (WB)']

filtered_data = data1[data1['Entity'].isin(regions)]

fig = px.bar(
    filtered_data,
    x = 'Year',
    y = 'Number of maternal deaths',
    color = 'Entity',
    title='Number of Maternal Deaths by Region from 2000 to 2020',
    barmode='stack'
)

fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Number of Maternal Deaths',
    legend_title='Region',
    hovermode='x unified',
    font=dict(
    family="Times New Roman",
    size=18
    ),
    title=dict(
        font=dict(
            family="Times New Roman",
            size=24
        )
    ),
    xaxis=dict(
        title=dict(
            font=dict(
                family="Times New Roman",
                size=16
            )
        ),
        tickfont=dict(
            family="Times New Roman",
            size=14
        )
    ),
    yaxis=dict(
        title=dict(
            font=dict(
                family="Times New Roman",
                size=16
            )
        ),
        tickfont=dict(
            family="Times New Roman",
            size=14
        )
    ),
    legend=dict(
        title=dict(
            font=dict(
                family="Times New Roman",
                size=14
            )
        ),
        font=dict(
            family="Times New Roman",
            size=16
        )
    )
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Map 1: Number of maternal deaths in the world in 2020
data2 = pd.read_csv("number-of-maternal-deaths.csv")

data_2020 = data2[data2['Year'] == 2020]

max_value = data_2020['Number of maternal deaths'].quantile(0.95)

map_fig1 = px.choropleth(
    data_2020,
    locations="Entity",
    locationmode="country names",
    color="Number of maternal deaths",
    hover_name="Entity",
    color_continuous_scale=px.colors.sequential.YlOrRd,
    range_color=(0, max_value),
    title='Number of Maternal Deaths, 2020'
)

map_fig1.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='equirectangular'
    ),
    coloraxis_colorbar=dict(
        title="Number of Maternal Deaths",
        ticks="outside",
        tickfont=dict(
            family="Times New Roman",
            size=14
        ),
        titlefont=dict(
            family="Times New Roman",
            size=20
        )
    ),
    font=dict(
        family="Times New Roman",
        size=16
    ),
    title=dict(
        font=dict(
            family="Times New Roman",
            size=26
        )
    ),
    xaxis=dict(
        title=dict(
            font=dict(
                family="Times New Roman",
                size=14
            )
        ),
        tickfont=dict(
            family="Times New Roman",
            size=14
        )
    ),
    yaxis=dict(
        title=dict(
            font=dict(
                family="Times New Roman",
                size=14
            )
        ),
        tickfont=dict(
            family="Times New Roman",
            size=14
        )
    ),
    legend=dict(
        title=dict(
            font=dict(
                family="Times New Roman",
                size=12
            )
        ),
        font=dict(
            family="Times New Roman",
            size=14
        )
    )
)

st.plotly_chart(map_fig1, use_container_width=True)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

data9 = pd.read_csv("lifetime-risk-of-maternal-region.csv")

data9['Label'] = '1 in ' + data9['2020'].astype(str)

bar_fig3 = px.bar(
  data9, 
  x='2020', 
  y='Region', 
  orientation='h', 
  text='Label', 
  color='2020',
  color_continuous_scale='deep',
  labels={'2020': 'Ratio', 'Region': 'Region'},
  title='Risk Levels by Region')

bar_fig3.update_traces(textposition='outside')

bar_fig3.update_layout(
    font=dict(family="Times New Roman", size=18),
    title=dict(font=dict(family="Times New Roman", size=24)),
    xaxis=dict(
        title='Number',
        titlefont=dict(family="Times New Roman", size=20),
        tickfont=dict(family="Times New Roman", size=16)
    ),
    yaxis=dict(
        title='Region',
        titlefont=dict(family="Times New Roman", size=20),
        tickfont=dict(family="Times New Roman", size=16),
        categoryorder='total ascending'
    ),
    coloraxis_colorbar=dict(
        title="Risk Level",
        ticks="outside",
        tickfont=dict(family="Times New Roman", size=14),
        titlefont=dict(family="Times New Roman", size=20)
    ),
    showlegend=False,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, t=60, b=0)
)

st.plotly_chart(bar_fig3, use_container_width=True)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

data11 = pd.read_csv("causes-of-maternal death.csv")

pie_fig2 = px.pie(
    data11,
    names='Cause',
    values='Count',
    title='Causes of Maternal Death',
    color_discrete_sequence=px.colors.sequential.Sunsetdark
)

pie_fig2.update_traces(
    textposition='outside', 
    textinfo='percent+label', 
    pull=[0.1]*len(data11),
    textfont_size=13
)

pie_fig2.update_layout(
    showlegend=False,
    font=dict(family="Times New Roman", size=18),
    title=dict(font=dict(family="Times New Roman", size=24)),
    annotations=[
        dict(
            text='*Nearly all (99 per cent) of abortion deaths are due to unsafe abortions.<br>'
                 '**Includes deaths due to obstructed labour or anaemia.<br>'
                 '*** Indirect causes are medical causes such as pre-existing conditions aggravated by pregnancy.',
            x=0.5,
            y=-0.30,
            showarrow=False,
            font=dict(family="Times New Roman", size=14),
            xref='paper',
            yref='paper',
            align='center'
        )
    ]
)

st.plotly_chart(pie_fig2, use_container_width=True)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Scatter Plot: Relation between Maternal Mortality and GDP
data4 = pd.read_csv("maternal-mortality-ratio-vs-gdp-per-capita.csv")

scatter_fig = px.scatter(
    data4,
    x='GDP per capita ($)',
    y='Maternal Mortality Ratio',  
    color='Continent',  
    hover_name='Entity',  
    animation_frame='Year',  
    log_x=True,  
    title='Maternal Mortality Ratio vs. GDP per Capita'
)

scatter_fig.update_layout(
    xaxis_title='GDP per capita',
    yaxis_title='Maternal mortality ratio',
    legend_title='Region',
    font=dict(
        family="Times New Roman",
        size=18
    ),
    title=dict(
        font=dict(
            family="Times New Roman",
            size=24
        )
    ),
    xaxis=dict(
        title=dict(
            font=dict(
                family="Times New Roman",
                size=20
            )
        ),
        tickfont=dict(
            family="Times New Roman",
            size=16
        ),
        tickformat = ',.0f'
    ),
    yaxis=dict(
        title=dict(
            font=dict(
                family="Times New Roman",
                size=20
            )
        ),
        tickfont=dict(
            family="Times New Roman",
            size=16
        )
    ),
    legend=dict(
        title=dict(
            font=dict(
                family="Times New Roman",
                size=18
            )
        ),
        font=dict(
            family="Times New Roman",
            size=16
        )
    )
)

scatter_fig.update_traces(marker=dict(size=8))
st.plotly_chart(scatter_fig, use_container_width=True)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Pie chart 1: Income level vs Maternal Deaths
data5 = pd.read_csv("maternal-deaths-by-income-group.csv")

income_groups = ["High-income countries", "Upper-middle-income countries", "Lower-middle-income countries", "Low-income countries"]

income_data = data5[data5['Entity'].isin(income_groups)]
years = income_data['Year'].unique()

selected_year = st.selectbox("Select Year", years)

year_data = income_data[income_data['Year'] == selected_year]

pie_fig = px.pie(
    year_data,
    names='Entity', 
    values='Number of maternal deaths', 
    title=f'Maternal Death by Income Level in {selected_year}'
)

# Customize the layout with Times New Roman font and larger text size
pie_fig.update_layout(
    font=dict(
        family="Times New Roman",
        size=18
    ),
    title=dict(
        font=dict(
            family="Times New Roman",
            size=24
        )
    ),
    legend=dict(
        title=dict(
            font=dict(
                family="Times New Roman",
                size=18
            )
        ),
        font=dict(
            family="Times New Roman",
            size=16
        )
    )
)

st.plotly_chart(pie_fig, use_container_width=True)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
data10 = pd.read_csv("lifetime-risk-of-maternal-income.csv")

data10['Label'] = '1 in ' + data10['Risk'].astype(str)

bar_fig3 = px.bar(
  data10, 
  x='Risk', 
  y='Income', 
  orientation='h', 
  text='Label', 
  color='Risk',
  color_continuous_scale='deep',
  labels={'Risk': 'Ratio', 'Income': 'Income'},
  title='Risk Levels by Income group')

bar_fig3.update_traces(textposition='outside')

bar_fig3.update_layout(
    font=dict(family="Times New Roman", size=18),
    title=dict(font=dict(family="Times New Roman", size=24)),
    xaxis=dict(
        title='Number',
        titlefont=dict(family="Times New Roman", size=20),
        tickfont=dict(family="Times New Roman", size=16)
    ),
    yaxis=dict(
        title='Region',
        titlefont=dict(family="Times New Roman", size=20),
        tickfont=dict(family="Times New Roman", size=16),
        categoryorder='total ascending'
    ),
    coloraxis_colorbar=dict(
        title="Risk Level",
        ticks="outside",
        tickfont=dict(family="Times New Roman", size=14),
        titlefont=dict(family="Times New Roman", size=20)
    ),
    showlegend=False,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, t=60, b=0)
)

st.plotly_chart(bar_fig3, use_container_width=True)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Boxplot 1: Risk Factors in Maternal Deaths
data6 = pd.read_csv("riskfactors.csv")

# Extract the list of columns for comparison with Risk Level
columns = data6.columns.tolist()
columns.remove('RiskLevel')

selected_column = st.selectbox("Select Column to Compare with Risk Level", columns)

box_fig = px.box(
    data6,
    x='RiskLevel',
    y=selected_column,
    color='RiskLevel',
    title=f'Comparison of Risk Level with {selected_column}',
    template='plotly_white'
)

box_fig.update_layout(
    font=dict(
        family="Times New Roman",
        size=18
    ),
    title=dict(
        font=dict(
            family="Times New Roman",
            size=24
        )
    ),
    xaxis=dict(
        title='Risk Level',
        titlefont=dict(
            family="Times New Roman",
            size=20
        ),
        tickfont=dict(
            family="Times New Roman",
            size=16
        )
    ),
    yaxis=dict(
        title=selected_column,
        titlefont=dict(
            family="Times New Roman",
            size=20
        ),
        tickfont=dict(
            family="Times New Roman",
            size=16
        )
    ),
    legend=dict(
        title=dict(
            font=dict(
                family="Times New Roman",
                size=18
            )
        ),
        font=dict(
            family="Times New Roman",
            size=16
        )
    )
)

st.plotly_chart(box_fig, use_container_width=True)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Figure 2: Share of women visited by Professionals
data7 = pd.read_csv("share-of-mothers-receiving-antenatal-visits.csv")

filtered_data = data7[data7['Year'] <= 2021]

sorted_data = filtered_data.sort_values(['Entity', 'Year'], ascending=[True, False])

latest_year_data = sorted_data.drop_duplicates(subset='Entity', keep='first')

# Create the choropleth map
map_fig2 = px.choropleth(
    latest_year_data,
    locations="Entity",
    locationmode="country names",
    color="Pregnant women receiving prenatal care (%)",
    hover_name="Entity",
    hover_data=["Year"],
    color_continuous_scale=px.colors.sequential.Turbo_r,    
    range_color=(0, 100),
    title='Share of Mothers Visited by a Health Professional During Pregnancy'
)


map_fig2.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='equirectangular'
    ),
    coloraxis_colorbar=dict(
        title="Percentage",
        ticks="outside"
    ),
    font=dict(
        family="Times New Roman",
        size=18
    ),
    title=dict(
        font=dict(
            family="Times New Roman",
            size=24
        )
    )
)

st.plotly_chart(map_fig2, use_container_width=True)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

data8 = pd.read_csv("antenatal-care-4times.csv")

df_melted = data8.melt(id_vars=["Region"], value_vars=["2012", "2022"], var_name="Year", value_name="Percentage")

color_map = {
    "2012": "green",
    "2022": "orange"
}

bar_fig2 = px.bar(
    df_melted,
    x='Region',
    y='Percentage',
    color='Year',
    barmode='group',
    title='Antenatal Care in 2012 and 2022',
    color_discrete_map=color_map
)

bar_fig2.update_layout(
    xaxis_title='Region',
    yaxis_title='Percentage',
    font=dict(
        family="Times New Roman",
        size=18
    ),
    title=dict(
        font=dict(
            family="Times New Roman",
            size=24
        )
    ),
    xaxis=dict(
        titlefont=dict(
            size=18
        ),
        tickfont=dict(
            size=14
        )
    ),
    yaxis=dict(
        titlefont=dict(
            size=18
        ),
        tickfont=dict(
            size=14
        )
    )
)

st.plotly_chart(bar_fig2, use_container_width=True)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

data12 = pd.read_csv("maternal-mortality-vs-neonatal-mortality.csv")

data_2020 = data12[data12['Year'] == 2020]

scatter_fig2 = px.scatter(
    data_2020,
    x='Neonatal mortality rate',
    y='Maternal mortality ratio',
    color='Maternal mortality ratio',
    color_continuous_scale='Viridis',
    title='Maternal Mortality Ratio vs. Neonatal Mortality, 2020',
    labels={'Neonatal mortality rate': 'Neonatal mortality rate (%)', 'Maternal mortality ratio': 'Maternal mortality ratio'}
)

scatter_fig2.update_layout(
    font=dict(
        family="Times New Roman",
        size=18
    ),
    title=dict(
        font=dict(
            family="Times New Roman",
            size=24
        )
    ),
    xaxis=dict(
        title='Neonatal mortality rate (%)',
        titlefont=dict(
            family="Times New Roman",
            size=20
        ),
        tickfont=dict(
            family="Times New Roman",
            size=16
        )
    ),
    yaxis=dict(
        title='Maternal mortality ratio',
        titlefont=dict(
            family="Times New Roman",
            size=20
        ),
        tickfont=dict(
            family="Times New Roman",
            size=16
        )
    ),
    coloraxis_colorbar=dict(
        title="Maternal mortality ratio",
        ticks="outside",
        tickfont=dict(
            family="Times New Roman",
            size=14
        ),
        titlefont=dict(
            family="Times New Roman",
            size=20
        )
    )
)

# Display the plot
st.plotly_chart(scatter_fig2, use_container_width=True)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

data13 = pd.read_csv("number-of-neonatal-deaths.csv")

regions = [
    'East Asia and Pacific (UNICEF)', 
    'Europe and Central Asia (UNICEF)', 
    'Latin America and Caribbean (UNICEF)', 
    'Middle East and North Africa (UNICEF)', 
    'North America', 
    'South Asia (WB)', 
    'Sub-Saharan Africa (SDG)'
]

filtered_data = data13[data13['Entity'].isin(regions)]

filtered_data['Entity'] = filtered_data['Entity'].replace({
    'East Asia and Pacific (UNICEF)': 'East Asia and Pacific', 
    'Europe and Central Asia (UNICEF)': 'Europe and Central Asia', 
    'Latin America and Caribbean (UNICEF)': 'Latin America and Caribbean', 
    'Middle East and North Africa (UNICEF)': 'Middle East and North Africa', 
    'North America': 'North America', 
    'Sub-Saharan Africa (SDG)': 'Sub-Saharan Africa'
})

line_fig = px.line(
    filtered_data,
    x='Year',
    y='Number of deaths',
    color='Entity',
    title='Number of Deaths Across the Years by Region',
    markers = True
)

line_fig.update_layout(
    font=dict(
        family="Times New Roman",
        size=18
    ),
    title=dict(
        font=dict(
            family="Times New Roman",
            size=24
        )
    ),
    xaxis=dict(
        title='Year',
        titlefont=dict(
            family="Times New Roman",
            size=20
        ),
        tickfont=dict(
            family="Times New Roman",
            size=16
        )
    ),
    yaxis=dict(
        title='Number of Deaths',
        titlefont=dict(
            family="Times New Roman",
            size=20
        ),
        tickfont=dict(
            family="Times New Roman",
            size=16
        )
    ),
    legend=dict(
        title=dict(
            font=dict(
                family="Times New Roman",
                size=18
            )
        ),
        font=dict(
            family="Times New Roman",
            size=16
        )
    )
)

st.plotly_chart(line_fig, use_container_width=True)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Load the dataset
data15 = pd.read_csv("neonatal-death-causes.csv")

melted_data = data15.melt(id_vars=["Entity"], var_name="Cause", value_name="Count")

world_data = melted_data[melted_data["Entity"] == "World"]

world_data = world_data.sort_values(by="Count", ascending=False)

bar_fig = px.bar(
    world_data,
    x="Count",
    y="Cause",
    orientation='h',
    title="Neonatal Deaths by Cause in the World in 2021",
    template='plotly_white',
    color_discrete_sequence=px.colors.sequential.Sunset
)

bar_fig.update_layout(
    font=dict(
        family="Times New Roman",
        size=18
    ),
    title=dict(
        font=dict(
            family="Times New Roman",
            size=24
        )
    ),
    xaxis=dict(
        title="Number of Deaths",
        titlefont=dict(
            family="Times New Roman",
            size=20
        ),
        tickfont=dict(
            family="Times New Roman",
            size=16
        ),
    ),
    yaxis=dict(
        title="",
        titlefont=dict(
            family="Times New Roman",
            size=20
        ),
        tickfont=dict(
            family="Times New Roman",
            size=16
        )
    ),
    showlegend=False
)

st.plotly_chart(bar_fig, use_container_width=True)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Map 3: Stillbirths in countries
data11 = pd.read_csv("stillbirth-rate.csv")

latest_year_data = data11.sort_values(['Entity', 'Year'], ascending=[True, False]).drop_duplicates(subset='Entity', keep='first')

# Create the choropleth map
map_fig3 = px.choropleth(
    latest_year_data,
    locations="Entity",
    locationmode="country names",
    color="Still Birth Rate",
    hover_name="Entity",
    hover_data=["Year"],
    color_continuous_scale=px.colors.sequential.PuRd,
    range_color=(latest_year_data["Still Birth Rate"].min(), latest_year_data["Still Birth Rate"].max()),
    title='Still Birth Rate in the world'
)

map_fig3.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='equirectangular'
    ),
    coloraxis_colorbar=dict(
        title="Stillbirth Rate",
        ticks="outside"
    ),
    font=dict(
        family="Times New Roman",
        size=18
    ),
    title=dict(
        font=dict(
            family="Times New Roman",
            size=24
        )
    )
)

st.plotly_chart(map_fig3, use_container_width=True)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
st.image("Screenshot 2024-08-03 142425.jpg", caption="Stillbirths and Delivery", use_column_width=True)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

data14 = pd.read_csv("sdg-target-on-child-mortality.csv")

data_2021 = data14[data14['Year'] == 2021]

data_2021['Target Status'] = data_2021['Deaths per 100 live births - Indicator: Under-five mortality rate'].apply(lambda x: 'Target met' if x < 1.4 else 'Still to meet')

map_fig4 = px.choropleth(
    data_2021,
    locations="Entity",
    locationmode="country names",
    color="Target Status",
    hover_name="Entity",
    hover_data=["Deaths per 100 live births - Indicator: Under-five mortality rate"],
    title='Has country already reached SDG target on infant mortality? 2021',
    color_discrete_map={
        'Target met': 'rgb(255, 255, 0)',
        'Still to meet': 'rgb(255, 105, 180)',
        'No data': 'rgb(221, 221, 221)'
    }
)

map_fig4.update_layout(
    font=dict(
        family="Times New Roman",
        size=18
    ),
    title=dict(
        font=dict(
            family="Times New Roman",
            size=24
        )
    ),
    legend=dict(
        title=dict(
            text="Target Status",
            font=dict(
                family="Times New Roman",
                size=18
            )
        ),
        font=dict(
            family="Times New Roman",
            size=16
        )
    )
)

st.plotly_chart(map_fig4, use_container_width=True)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

data16 = pd.read_csv("sdg-target-on-maternal-mortality.csv")

data_2020 = data16[data16['Year'] == 2020]

data_2020['Target Status'] = data_2020['Estimated maternal mortality ratio'].apply(lambda x: 'Target met' if x < 70 else 'Still to meet')

map_fig5 = px.choropleth(
    data_2020,
    locations="Entity",
    locationmode="country names",
    color="Target Status",
    hover_name="Entity",
    color_discrete_map={
        'Target met': 'purple',
        'Still to meet': 'orange'
    },
    title='Has country already reached SDG target on maternal mortality? 2020'
)

map_fig5.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='equirectangular'
    ),
    coloraxis_colorbar=dict(
        title="",
        ticks="outside"
    ),
    font=dict(
        family="Times New Roman",
        size=18
    ),
    title=dict(
        font=dict(
            family="Times New Roman",
            size=24
        )
    )
)

st.plotly_chart(map_fig5, use_container_width=True)
