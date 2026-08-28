import streamlit as st

# ==========================================
# MENU LATERAL (DESIGN DA PÁGINA)
# ==========================================
st.sidebar.header("🎨 Personalizar Visual")

# Seletores de cores e fontes para o usuário
cor_fundo = st.sidebar.color_picker("Cor do Fundo", "#F0F2F6")
cor_texto = st.sidebar.color_picker("Cor do Texto", "#000000")
cor_topicos = st.sidebar.color_picker("Cor dos Títulos", "#005C99")
fonte = st.sidebar.selectbox("Estilo da Fonte", ["sans-serif", "Arial", "Courier New", "Georgia", "Verdana"])

# Aplicação das escolhas usando CSS customizado "forçado"
estilo_css = f"""
<style>
    /* Fundo da aplicação */
    [data-testid="stAppViewContainer"] {{
        background-color: {cor_fundo} !important;
    }}
    /* Fundo do cabeçalho superior (para não ficar uma faixa branca) */
    [data-testid="stHeader"] {{
        background-color: transparent !important;
    }}
    /* Cor do texto geral e fonte */
    p, span, label, div {{
        color: {cor_texto} !important;
        font-family: {fonte} !important;
    }}
    /* Cor e fonte dos títulos */
    h1, h2, h3, h4, h5, h6 {{
        color: {cor_topicos} !important;
        font-family: {fonte} !important;
    }}
</style>
"""
st.markdown(estilo_css, unsafe_allow_html=True)


# ==========================================
# CÓDIGO DO SISTEMA DE DOAÇÕES
# ==========================================

# Inicializa o "banco de dados" na memória da sessão do usuário
if 'estoque' not in st.session_state:
    st.session_state.estoque = {}

# Configuração visual do título da página
st.title("📦 Sistema Solidário de Doações")
st.write("Bem-vindo ao portal de controle de estoque da ONG.")

st.divider() # Cria uma linha separadora visual

# SESSÃO 1: CADASTRO DE DOAÇÕES
st.header("➕ Cadastrar Nova Doação")

col1, col2 = st.columns(2)
with col1:
    novo_item = st.text_input("Nome do Item:", placeholder="Ex: Arroz, Leite")
with col2:
    nova_qtd = st.number_input("Quantidade:", min_value=1, step=1)

if st.button("Adicionar ao Estoque"):
    if novo_item:
        item_padronizado = novo_item.strip().upper()
        if item_padronizado in st.session_state.estoque:
            st.session_state.estoque[item_padronizado] += nova_qtd
        else:
            st.session_state.estoque[item_padronizado] = nova_qtd
        st.success(f"Sucesso! {nova_qtd} de '{item_padronizado}' cadastrado.")
    else:
        st.warning("Por favor, digite o nome do item.")

st.divider()

# SESSÃO 2: VISUALIZAÇÃO DO ESTOQUE
st.header("📋 Estoque Atual")
if not st.session_state.estoque:
    st.info("O estoque está vazio no momento.")
else:
    dados_tabela = {"Item": list(st.session_state.estoque.keys()), 
                    "Quantidade": list(st.session_state.estoque.values())}
    st.table(dados_tabela)

st.divider()

# SESSÃO 3: SAÍDA/ENTREGA DE DOAÇÕES
st.header("➖ Retirar Doação (Entrega)")
if st.session_state.estoque:
    item_retirar = st.selectbox("Selecione o item para retirar:", list(st.session_state.estoque.keys()))
    qtd_retirar = st.number_input("Quantidade a retirar:", min_value=1, step=1, key="retirar")
    
    if st.button("Confirmar Retirada"):
        if qtd_retirar <= st.session_state.estoque[item_retirar]:
            st.session_state.estoque[item_retirar] -= qtd_retirar
            st.success(f"Retirada confirmada! Restam {st.session_state.estoque[item_retirar]}.")
            
            if st.session_state.estoque[item_retirar] == 0:
                del st.session_state.estoque[item_retirar]
                st.rerun() 
        else:
            st.error("Erro: Quantidade solicitada é maior que o estoque disponível!")
else:
    st.write("Não há itens no estoque para retirar.")
