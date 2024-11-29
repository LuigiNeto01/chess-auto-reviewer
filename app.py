import streamlit as st
from src.data_loader import load_data
from src.data_processing import filter_data
from src.visualizations import (
    plot_rating_evolution,
    plot_precision_evolution,
    plot_victory_distribution,
    plot_stats_bar_chart,
    plot_winrate_by_opening,
    plot_rating_by_opening,
    plot_stats_radar_chart
)
from src.match_adder import adicionar_partida

# Configurar a página
st.set_page_config(page_title='Dashboard de Partidas de Xadrez', layout='wide')

# Carregar os dados
df = load_data('data/matchs.json')

# Navegação entre páginas
paginas = ['Home', 'Dashboard']
escolha = st.sidebar.selectbox('Selecione a página', paginas)

if escolha == 'Home':
    # Código para a página Home
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Adicionar Nova Partida</h1>", unsafe_allow_html=True)
    url = st.text_input('Insira a URL da partida:')
    if st.button('Adicionar Partida'):
        if url:
            adicionar_partida(url) # Ainda eh necessario implementar o codigo que o libniz vai fazer
        else:
            st.warning('Por favor, insira uma URL.')
else:
    # Código para a página Dashboard
    st.sidebar.header('Filtros')

    # Filtro por período de tempo
    min_date = df['Timestamp'].min()
    max_date = df['Timestamp'].max()
    date_range = st.sidebar.date_input('Selecione o período', [min_date.date(), max_date.date()])

    # Filtro por tipo de partida
    type_match_options = df['Type Match'].unique()
    selected_type_matches = st.sidebar.multiselect('Tipo de Partida', type_match_options, default=type_match_options)

    # Filtro por vitória ou derrota
    victory_options = ['Vitória', 'Derrota']
    selected_victory = st.sidebar.multiselect('Resultado', victory_options, default=victory_options)

    # Mapear seleção de vitória para valores numéricos
    victory_mapping = {'Vitória': 1, 'Derrota': 0}
    selected_victory_values = [victory_mapping[v] for v in selected_victory]

    # Filtro por aberturas
    opening_options = df['Opening'].unique()
    selected_openings = st.sidebar.multiselect('Aberturas', opening_options, default=opening_options)

    # Aplicar filtros
    df_filtered = filter_data(df, date_range, selected_type_matches, selected_victory_values, selected_openings)

    # Título do dashboard
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Dashboard de Partidas de Xadrez</h1>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # Seção de resumo geral
    st.markdown("## Resumo Geral")
    col1, col2, col3 = st.columns(3)
    col1.metric('Total de Partidas', len(df_filtered))
    col2.metric('Vitórias', df_filtered['Victory'].sum())
    col3.metric('Taxa de Vitória (%)', f"{(df_filtered['Victory'].mean() * 100):.2f}%")

    st.markdown("<hr>", unsafe_allow_html=True)

    # Gráficos
    st.markdown("### Evolução do Rating do Usuário")
    fig = plot_rating_evolution(df_filtered)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Evolução da Precisão")
    fig = plot_precision_evolution(df_filtered)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Distribuição de Vitórias e Derrotas")
    fig = plot_victory_distribution(df_filtered)
    st.plotly_chart(fig, use_container_width=True)

    # Estatísticas das partidas
    st.markdown("### Estatísticas das Partidas")
    stats_columns = ['Brilliant', 'Excellent', 'Better', 'Great', 'Good', 'Book', 'Inaccuracy', 'Error', 'Missed Chance', 'Capybara']

    # Verificando se todas as colunas existem no DataFrame
    missing_columns = [col for col in stats_columns if col not in df_filtered.columns]
    if missing_columns:
        st.error(f"As seguintes colunas estão ausentes no DataFrame: {missing_columns}")
    else:
        # Somando os valores das colunas especificadas
        stats_df = df_filtered[stats_columns].sum().reset_index()
        stats_df.columns = ['Estatística', 'Total']

        # Mapeando nomes em inglês para português
        translation_map = {
            'Brilliant': 'Brilhante',
            'Excellent': 'Excelente',
            'Better': 'Melhor',
            'Great': 'Ótimo',
            'Good': 'Bom',
            'Book': 'Livro',
            'Inaccuracy': 'Imprecisão',
            'Error': 'Erro',
            'Missed Chance': 'Chance Perdida',
            'Capybara': 'Capivarada'
        }
        stats_df['Estatística'] = stats_df['Estatística'].map(translation_map)

        fig = plot_stats_bar_chart(stats_df)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Taxa de Vitória por Abertura")
    openings_winrate = df_filtered.groupby('Opening')['Victory'].mean().reset_index()
    openings_winrate['Taxa de Vitória (%)'] = openings_winrate['Victory'] * 100
    fig = plot_winrate_by_opening(openings_winrate)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Evolução do Rating por Abertura")
    fig = plot_rating_by_opening(df_filtered)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Perfil Médio das Estatísticas")
    stats_means = df_filtered[stats_columns].mean()
    fig = plot_stats_radar_chart(stats_means)
    st.plotly_chart(fig, use_container_width=True)

    # Tabela detalhada das partidas filtradas
    st.markdown("### Detalhes das Partidas Filtradas")
    st.dataframe(df_filtered.style.format({"Precision": "{:.2f}%", "User Rating": "{:.0f}"}))
