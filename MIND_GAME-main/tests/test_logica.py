from src.config import CAMINHO_RECORDE, CAMINHO_SPRITES, PASTA_PROJETO
from src.dados import carregar_recorde, salvar_recorde
from src.logic import (
    atualizar_pontuacao,
    atualizar_vidas,
    esta_morto,
    jogo_concluido,
    verificar_resposta,
)


def test_caminhos_do_projeto_nao_dependem_do_diretorio_atual(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)

    assert CAMINHO_RECORDE == PASTA_PROJETO / "data" / "recorde.txt"
    assert CAMINHO_SPRITES == PASTA_PROJETO / "assets" / "imagens" / "spritesheet.bmp"
    assert CAMINHO_RECORDE.is_file()
    assert isinstance(carregar_recorde(CAMINHO_RECORDE), int)
    assert CAMINHO_SPRITES.is_file()


def test_verificar_resposta():
    pergunta = {"correta": 1}

    assert verificar_resposta(pergunta, 1) is True
    assert verificar_resposta(pergunta, 0) is False


def test_atualizar_pontuacao_por_dificuldade():
    assert atualizar_pontuacao(10, True, "Difícil") == 40
    assert atualizar_pontuacao(10, False, "Difícil") == 10


def test_atualizar_vidas_e_verificar_derrota():
    vidas = atualizar_vidas(1, False)

    assert vidas == 0
    assert esta_morto(vidas) is True


def test_jogo_concluido():
    assert jogo_concluido(20, 20) is True
    assert jogo_concluido(19, 20) is False


def test_recorde_pode_ser_salvo_e_carregado(tmp_path):
    caminho = tmp_path / "recorde.txt"

    salvar_recorde(caminho, 120)

    assert carregar_recorde(caminho) == 120
