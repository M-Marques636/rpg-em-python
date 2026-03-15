

def atacar(jogador, inimigo):
    
    dano = jogador.atacar()
    inimigo.receber_dano(dano)
    
    return dano
