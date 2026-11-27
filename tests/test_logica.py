# ==============================================================================
# ARQUIVO: tests/test_logica.py
# O QUE FAZ: Suíte de testes automatizados com pytest para validar funções
#            utilitárias, regras da partida, transição de estados, caminhos,
#            persistência do recorde e integridade do banco de perguntas.
# ESTÁ LINCADO COM:
#   - src/config.py, src/dados.py, src/funcoes.py, src/logic.py, src/questions.py, src/jogo.py
# ==============================================================================

# Importações dos módulos do projeto que serão testados.
from src.config import CAMINHO_RECORDE, CAMINHO_SPRITES, PASTA_PROJETO
from src.dados import carregar_recorde, salvar_recorde
from src.funcoes import calcular_pontos, jogador_perdeu, limitar_valor
from src.logic import (
    atualizar_pontuacao,
    atualizar_vidas,
    esta_morto,
    jogo_concluido,
    verificar_resposta,
)
from src.questions import PERGUNTAS
from src import jogo


# ==============================================================================
# TESTES DAS FUNÇÕES UTILITÁRIAS (src/funcoes.py)
# ==============================================================================

def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


# ==============================================================================
# TESTES DAS REGRAS DO JOGO (src/logic.py)
# ==============================================================================

def test_verificar_resposta():
    """Deve retornar True apenas para o indice da alternativa correta."""
    pergunta = {"correta": 2}
    assert verificar_resposta(pergunta, 2) is True
    assert verificar_resposta(pergunta, 0) is False


def test_atualizar_pontuacao_por_dificuldade():
    """Deve somar 10, 20 ou 30 pontos no acerto e manter ao errar."""
    assert atualizar_pontuacao(0, True, "Fácil") == 10
    assert atualizar_pontuacao(10, True, "Média") == 30
    assert atualizar_pontuacao(30, True, "Difícil") == 60
    assert atualizar_pontuacao(60, False, "Difícil") == 60


def test_atualizar_vidas_e_condicao_de_derrota():
    """Deve reduzir uma vida ao errar e indicar derrota ao zerar."""
    assert atualizar_vidas(3, True) == 3
    vidas = atualizar_vidas(1, False)
    assert vidas == 0
    assert esta_morto(vidas) is True
    assert esta_morto(1) is False


def test_jogo_concluido():
    """Deve concluir somente quando o indice atingir o total de perguntas."""
    assert jogo_concluido(29, 30) is False
    assert jogo_concluido(30, 30) is True


# ==============================================================================
# TESTES DO FLUXO DE ESTADOS APÓS O FEEDBACK (src/jogo.py)
# ==============================================================================

def test_avancar_apos_feedback_continua_para_proxima_pergunta():
    """Depois do feedback, a partida deve avançar quando ainda houver vidas e perguntas."""
    estado, indice, recorde = jogo.avancar_apos_feedback(4, 30, 3, 50, 160)
    assert (estado, indice, recorde) == (jogo.JOGANDO, 5, 160)


def test_avancar_apos_feedback_encerra_e_salva_novo_recorde(monkeypatch):
    """A vitória deve encerrar a partida e persistir apenas um recorde maior."""
    # 'monkeypatch' substitui salvar_recorde temporariamente para não alterar data/recorde.txt real.
    gravados = []
    monkeypatch.setattr(jogo, "salvar_recorde", lambda caminho, pontos: gravados.append(pontos))

    estado, indice, recorde = jogo.avancar_apos_feedback(29, 30, 1, 180, 160)

    assert (estado, indice, recorde) == (jogo.FIM, 29, 180)
    assert gravados == [180]


def test_avancar_apos_feedback_encerra_derrota_sem_substituir_recorde(monkeypatch):
    """A derrota encerra a partida e não grava uma pontuação menor que o recorde."""
    # Verifica que, ao perder com pontuação menor que o recorde atual, nada é gravado em disco.
    gravados = []
    monkeypatch.setattr(jogo, "salvar_recorde", lambda caminho, pontos: gravados.append(pontos))

    estado, indice, recorde = jogo.avancar_apos_feedback(2, 30, 0, 40, 160)

    assert (estado, indice, recorde) == (jogo.FIM, 2, 160)
    assert gravados == []


# ==============================================================================
# TESTES DE CAMINHOS E PERSISTÊNCIA DE RECORDE (src/config.py e src/dados.py)
# ==============================================================================

def test_caminhos_independem_do_diretorio_atual(monkeypatch, tmp_path):
    """Os caminhos de dados e assets devem continuar validos fora da pasta raiz."""
    # Simula execução a partir de uma pasta temporária para confirmar que os caminhos absolutos continuam válidos.
    monkeypatch.chdir(tmp_path)
    assert CAMINHO_RECORDE.startswith(PASTA_PROJETO)
    assert CAMINHO_SPRITES.startswith(PASTA_PROJETO)
    assert isinstance(carregar_recorde(CAMINHO_RECORDE), int)


def test_salvar_e_carregar_recorde(tmp_path):
    """Deve salvar o recorde criando pastas se necessario e ignorar arquivos invalidos."""
    # 'tmp_path' cria uma pasta temporária isolada que o pytest limpa depois do teste.
    caminho = tmp_path / "subpasta" / "recorde.txt"
    assert salvar_recorde(caminho, 240) is True
    assert carregar_recorde(caminho) == 240

    # Testa fallback para 0 quando o arquivo contém texto inválido ou número negativo.
    caminho.write_text("invalido", encoding="utf-8")
    assert carregar_recorde(caminho) == 0

    caminho.write_text("-15", encoding="utf-8")
    assert carregar_recorde(caminho) == 0

    # Testa fallback para 0 quando o arquivo ainda não existe.
    assert carregar_recorde(tmp_path / "inexistente.txt") == 0


# ==============================================================================
# TESTE DE INTEGRIDADE DO BANCO DE PERGUNTAS (src/questions.py)
# ==============================================================================

def test_banco_de_perguntas_valido():
    """Todas as perguntas devem possuir campos obrigatorios, 3 opcoes e resposta valida."""
    # Garante exatamente 30 perguntas com IDs sequenciais de 1 a 30.
    assert len(PERGUNTAS) == 30
    assert [pergunta["id"] for pergunta in PERGUNTAS] == list(range(1, 31))
    campos = {"id", "enunciado", "alternativas", "correta", "categoria", "dificuldade", "explicacao"}
    for pergunta in PERGUNTAS:
        assert campos.issubset(pergunta.keys())
        assert len(pergunta["alternativas"]) == 3
        assert pergunta["correta"] in (0, 1, 2)
        assert pergunta["dificuldade"] in ("Fácil", "Média", "Difícil")
