# ==============================================================================
# PROJETO OLIV.IA - MÓDULO JURIX
# Script de Analytics e Inteligência de Dados
# Grupo 7 - FIAP
# ==============================================================================

# Instalação e Carregamento de Pacotes (Descomente se necessário)
# install.packages("ggplot2")
# install.packages("dplyr")
library(ggplot2)
library(dplyr)

# ------------------------------------------------------------------------------
# 1. SIMULAÇÃO DE DADOS (MOCK DATABASE)
# Como o banco de dados é criptografado/remoto, simulamos aqui uma extração CSV
# ------------------------------------------------------------------------------
set.seed(123) # Para reprodutibilidade

areas <- c("Trabalhista", "Cível", "Família", "Consumidor", "Penal")
sentimentos <- c("Calmo", "Ansioso", "Nervoso", "Desesperado", "Agressivo")
urgencias <- c("Baixa", "Média", "Alta")

# Criando 200 casos simulados processados pela Oliv.ia
dados_jurix <- data.frame(
  id_caso = 1:200,
  area_direito = sample(areas, 200, replace = TRUE, prob = c(0.3, 0.2, 0.2, 0.2, 0.1)),
  sentimento_cliente = sample(sentimentos, 200, replace = TRUE),
  urgencia = sample(urgencias, 200, replace = TRUE),
  tempo_triagem_ia_seg = runif(200, min = 20, max = 120), # Segundos
  tempo_resolucao_dias = NA # Será calculado com base no sentimento
)

# Lógica de Negócio: Clientes 'Agressivos' ou 'Desesperados' tendem a casos mais complexos/lentos
dados_jurix <- dados_jurix %>%
  mutate(tempo_resolucao_dias = case_when(
    sentimento_cliente == "Agressivo" ~ runif(n(), 100, 300),
    sentimento_cliente == "Desesperado" ~ runif(n(), 80, 200),
    TRUE ~ runif(n(), 30, 120)
  ))

# ------------------------------------------------------------------------------
# 2. VISUALIZAÇÃO DE DADOS (INSIGHTS)
# ------------------------------------------------------------------------------

# GRÁFICO 1: Relação Sentimento x Tempo de Resolução
# Insight: Mostra porque a triagem emocional é vital para a gestão
g1 <- ggplot(dados_jurix, aes(x=reorder(sentimento_cliente, tempo_resolucao_dias, FUN=median), 
                        y=tempo_resolucao_dias, fill=sentimento_cliente)) +
  geom_boxplot() +
  labs(title = "Impacto Emocional na Duração do Processo",
       subtitle = "Insight: Casos 'Agressivos' têm maior variabilidade e duração",
       x = "Sentimento Detectado pela IA",
       y = "Dias até Resolução",
       fill = "Sentimento") +
  theme_minimal()

print(g1)

# GRÁFICO 2: Volume de Urgência por Área
g2 <- ggplot(dados_jurix, aes(x=area_direito, fill=urgencia)) +
  geom_bar(position="fill") +
  labs(title = "Distribuição de Urgência por Área Jurídica",
       subtitle = "Área Trabalhista apresenta maior volume de alta urgência",
       x = "Área do Direito",
       y = "Proporção",
       fill = "Nível de Urgência") +
  theme_minimal() +
  scale_fill_brewer(palette = "Reds")

print(g2)

# ------------------------------------------------------------------------------
# 3. CONCLUSÃO ESTATÍSTICA
# ------------------------------------------------------------------------------
summary_stats <- dados_jurix %>%
  group_by(sentimento_cliente) %>%
  summarise(media_dias = mean(tempo_resolucao_dias),
            total_casos = n())

print("--- Tabela Resumo para o Gestor ---")
print(summary_stats)