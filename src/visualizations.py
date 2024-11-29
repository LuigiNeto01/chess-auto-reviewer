import plotly.express as px
import plotly.graph_objects as go

def plot_rating_evolution(df_filtered):
    fig = px.line(df_filtered, x='Timestamp', y='User Rating', markers=True, title='Evolução do Rating', template='plotly_dark')
    fig.update_traces(line=dict(color='#00CC96'))
    return fig

def plot_precision_evolution(df_filtered):
    fig = px.line(df_filtered, x='Timestamp', y='Precision', markers=True, title='Evolução da Precisão', template='plotly_dark')
    fig.update_traces(line=dict(color='#FFA15A'))
    return fig

def plot_victory_distribution(df_filtered):
    victory_counts = df_filtered['Victory'].value_counts().rename(index={1: 'Vitórias', 0: 'Derrotas'}).reset_index()
    victory_counts.columns = ['Resultado', 'Quantidade']
    fig = px.pie(victory_counts, names='Resultado', values='Quantidade', title='Vitórias vs Derrotas', template='plotly_dark', color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def plot_stats_bar_chart(stats_df):
    color_map = {
        'Brilhante': '#26c2a3',
        'Excelente': '#749bbf',
        'Melhor': '#81b64c',
        'Ótimo': '#81b64c',
        'Bom': '#95b776',
        'Livro': '#d5a47d',
        'Imprecisão': '#f7c631',
        'Erro': '#ffa459',
        'Chance Perdida': '#ff7769',   
        'Capivarada': '#fa412d'         
    }
    fig = px.bar(
        stats_df, 
        x='Estatística', 
        y='Total', 
        title='Total por Estatística', 
        template='plotly_dark', 
        color='Estatística', 
        color_discrete_map=color_map
    )
    fig.update_layout(xaxis_tickangle=0)
    return fig

def plot_winrate_by_opening(openings_winrate):
    fig = px.bar(openings_winrate, x='Opening', y='Taxa de Vitória (%)', title='Taxa de Vitória por Abertura', template='plotly_dark', color='Taxa de Vitória (%)', color_continuous_scale='Blues')
    fig.update_layout(xaxis_tickangle=0)
    return fig

def plot_rating_by_opening(df_filtered):
    fig = px.line(df_filtered, x='Timestamp', y='User Rating', color='Opening', title='Evolução do Rating por Abertura', template='plotly_dark')
    return fig

def plot_stats_radar_chart(stats_means):
    categories = list(stats_means.index)
    values = stats_means.values.flatten().tolist()
    values += values[:1]  # Fechar o gráfico

    fig = go.Figure(data=go.Scatterpolar(
            r=values,
            theta=categories + [categories[0]],
            fill='toself',
            marker=dict(color='#AB63FA')
        ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(values)]
            )),
        showlegend=False,
        template='plotly_dark',
        title='Perfil Médio das Estatísticas'
    )
    return fig
