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


def test_avancar_apos_feedback_continua_para_proxima_pergunta():
    """Depois do feedback, a partida deve avançar quando ainda houver vidas e perguntas."""
    estado, indice, recorde = jogo.avancar_apos_feedback(4, 30, 3, 50, 160)
    assert (estado, indice, recorde) == (jogo.JOGANDO, 5, 160)


def test_avancar_apos_feedback_encerra_e_salva_novo_recorde(monkeypatch):
    """A vitória deve encerrar a partida e persistir apenas um recorde maior."""
    gravados = []
    monkeypatch.setattr(jogo, "salvar_recorde", lambda caminho, pontos: gravados.append(pontos))

    estado, indice, recorde = jogo.avancar_apos_feedback(29, 30, 1, 180, 160)

    assert (estado, indice, recorde) == (jogo.FIM, 29, 180)
    assert gravados == [180]


def test_avancar_apos_feedback_encerra_derrota_sem_substituir_recorde(monkeypatch):
    """A derrota encerra a partida e não grava uma pontuação menor que o recorde."""
    gravados = []
    monkeypatch.setattr(jogo, "salvar_recorde", lambda caminho, pontos: gravados.append(pontos))

    estado, indice, recorde = jogo.avancar_apos_feedback(2, 30, 0, 40, 160)

    assert (estado, indice, recorde) == (jogo.FIM, 2, 160)
    assert gravados == []


def test_caminhos_independem_do_diretorio_atual(monkeypatch, tmp_path):
    """Os caminhos de dados e assets devem continuar validos fora da pasta raiz."""
    monkeypatch.chdir(tmp_path)
    assert CAMINHO_RECORDE.startswith(PASTA_PROJETO)
    assert CAMINHO_SPRITES.startswith(PASTA_PROJETO)
    assert isinstance(carregar_recorde(CAMINHO_RECORDE), int)


def test_salvar_e_carregar_recorde(tmp_path):
    """Deve salvar o recorde criando pastas se necessario e ignorar arquivos invalidos."""
    caminho = tmp_path / "subpasta" / "recorde.txt"
    assert salvar_recorde(caminho, 240) is True
    assert carregar_recorde(caminho) == 240

    caminho.write_text("invalido", encoding="utf-8")
    assert carregar_recorde(caminho) == 0

    caminho.write_text("-15", encoding="utf-8")
    assert carregar_recorde(caminho) == 0

    assert carregar_recorde(tmp_path / "inexistente.txt") == 0


def test_banco_de_perguntas_valido():
    """Todas as perguntas devem possuir campos obrigatorios, 3 opcoes e resposta valida."""
    assert len(PERGUNTAS) == 30
    assert [pergunta["id"] for pergunta in PERGUNTAS] == list(range(1, 31))
    campos = {"id", "enunciado", "alternativas", "correta", "categoria", "dificuldade", "explicacao"}
    for pergunta in PERGUNTAS:
        assert campos.issubset(pergunta.keys())
        assert len(pergunta["alternativas"]) == 3
        assert pergunta["correta"] in (0, 1, 2)
        assert pergunta["dificuldade"] in ("Fácil", "Média", "Difícil")
