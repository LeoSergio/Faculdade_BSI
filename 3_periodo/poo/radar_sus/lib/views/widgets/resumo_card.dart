// views/widgets/resumo_card.dart
// Painel executivo no topo da tela — o gestor vê o status atual em 3 segundos.
import 'package:flutter/material.dart';
import '../../models/alerta_dengue.dart';

class ResumoCard extends StatelessWidget {
  final ResumoDengue resumo;
  final String nomeMunicipio;

  const ResumoCard({
    super.key,
    required this.resumo,
    required this.nomeMunicipio,
  });

  static const _cores = {1: Color(0xFF2E7D32), 2: Color(0xFFF9A825), 3: Color(0xFFE65100), 4: Color(0xFFC62828)};
  static const _textos = {1: 'Risco Baixo', 2: 'Risco Moderado', 3: 'Risco Alto', 4: 'Risco Muito Alto'};
  static const _acoes = {
    1: 'Manter vigilância de rotina. Continuar ações preventivas e monitoramento semanal.',
    2: 'Intensificar fiscalização de focos. Acionar equipes de controle vetorial.',
    3: 'Ativar sala de situação municipal. Reforçar UBS e comunicar secretaria estadual.',
    4: 'EMERGÊNCIA — Acionar plano de contingência. Articular leitos e insumos com estado.',
  };
  static const _tendenciaIcone = {
    TendenciaCasos.subindo: Icons.trending_up_rounded,
    TendenciaCasos.descendo: Icons.trending_down_rounded,
    TendenciaCasos.estavel: Icons.trending_flat_rounded,
  };
  static const _tendenciaTexto = {
    TendenciaCasos.subindo: 'Em alta',
    TendenciaCasos.descendo: 'Em queda',
    TendenciaCasos.estavel: 'Estável',
  };

  @override
  Widget build(BuildContext context) {
    final nivel = resumo.ultimaSemana.nivelAlerta;
    final cor = _cores[nivel] ?? Colors.grey;
    final acao = _acoes[nivel] ?? '';

    return Container(
      margin: const EdgeInsets.fromLTRB(16, 12, 16, 4),
      decoration: BoxDecoration(
        color: cor.withOpacity(0.08),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: cor.withOpacity(0.4), width: 1.5),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Cabeçalho com nível atual
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
            decoration: BoxDecoration(
              color: cor,
              borderRadius: const BorderRadius.vertical(top: Radius.circular(14)),
            ),
            child: Row(
              children: [
                const Icon(Icons.shield_rounded, color: Colors.white, size: 20),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    '${_textos[nivel]} — $nomeMunicipio',
                    style: const TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.w700,
                      fontSize: 15,
                    ),
                  ),
                ),
                Text(
                  resumo.ultimaSemana.periodoFormatado,
                  style: const TextStyle(color: Colors.white70, fontSize: 11),
                ),
              ],
            ),
          ),

          // Métricas em linha
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 14, 16, 0),
            child: Row(
              children: [
                _Metrica(
                  rotulo: 'Casos (semana)',
                  valor: '${resumo.ultimaSemana.casosNotificados}',
                  icone: Icons.person_rounded,
                  cor: cor,
                ),
                _Metrica(
                  rotulo: 'Estimativa',
                  valor: '${resumo.ultimaSemana.casosEstimados}',
                  icone: Icons.analytics_rounded,
                  cor: cor,
                ),
                _Metrica(
                  rotulo: 'Total no ano',
                  valor: '${resumo.totalCasosAno}',
                  icone: Icons.calendar_month_rounded,
                  cor: cor,
                ),
                _MetricaTendencia(
                  tendencia: resumo.tendencia,
                  icone: _tendenciaIcone[resumo.tendencia]!,
                  texto: _tendenciaTexto[resumo.tendencia]!,
                ),
              ],
            ),
          ),

          // Orientação de ação
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 10, 16, 14),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Icon(Icons.assignment_late_rounded, size: 16, color: cor),
                const SizedBox(width: 6),
                Expanded(
                  child: Text(
                    acao,
                    style: TextStyle(
                      fontSize: 12,
                      color: cor.withOpacity(0.9),
                      fontWeight: FontWeight.w500,
                      height: 1.4,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _Metrica extends StatelessWidget {
  final String rotulo;
  final String valor;
  final IconData icone;
  final Color cor;

  const _Metrica({
    required this.rotulo,
    required this.valor,
    required this.icone,
    required this.cor,
  });

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Column(
        children: [
          Icon(icone, size: 18, color: cor),
          const SizedBox(height: 4),
          Text(valor,
              style: TextStyle(
                  fontSize: 16, fontWeight: FontWeight.w800, color: cor)),
          Text(rotulo,
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 10, color: Colors.grey[600])),
        ],
      ),
    );
  }
}

class _MetricaTendencia extends StatelessWidget {
  final TendenciaCasos tendencia;
  final IconData icone;
  final String texto;

  const _MetricaTendencia({
    required this.tendencia,
    required this.icone,
    required this.texto,
  });

  Color get _cor {
    return switch (tendencia) {
      TendenciaCasos.subindo => const Color(0xFFC62828),
      TendenciaCasos.descendo => const Color(0xFF2E7D32),
      TendenciaCasos.estavel => Colors.grey,
    };
  }

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Column(
        children: [
          Icon(icone, size: 18, color: _cor),
          const SizedBox(height: 4),
          Text(texto,
              style: TextStyle(
                  fontSize: 13, fontWeight: FontWeight.w800, color: _cor)),
          Text('Tendência',
              style: TextStyle(fontSize: 10, color: Colors.grey[600])),
        ],
      ),
    );
  }
}