class AlertaDengue {
  final int _semanaEpidemiologica;
  final int _casosNotificados;
  final int _casosEstimados;
  final int _nivelAlerta;

  const AlertaDengue({
    required int semanaEpidemiologica,
    required int casosNotificados,
    required int casosEstimados,
    required int nivelAlerta,
  })  : _semanaEpidemiologica = semanaEpidemiologica,
        _casosNotificados = casosNotificados,
        _casosEstimados = casosEstimados,
        _nivelAlerta = nivelAlerta;

  int get semanaEpidemiologica => _semanaEpidemiologica;
  int get casosNotificados => _casosNotificados;
  int get casosEstimados => _casosEstimados;
  int get nivelAlerta => _nivelAlerta;

  String get semanaFormatada {
    final str = _semanaEpidemiologica.toString();
    if (str.length == 6) return 'Semana ${str.substring(4, 6)} de ${str.substring(0, 4)}';
    return str;
  }

  String get periodoFormatado {
    final str = _semanaEpidemiologica.toString();
    if (str.length != 6) return str;
    final ano = int.parse(str.substring(0, 4));
    final semana = int.parse(str.substring(4, 6));
    DateTime primeiroDia = DateTime(ano, 1, 1);
    int diasParaDomingo = (7 - (primeiroDia.weekday % 7)) % 7;
    DateTime primeiroDomingo = primeiroDia.add(Duration(days: diasParaDomingo));
    DateTime inicio = primeiroDomingo.add(Duration(days: (semana - 1) * 7));
    DateTime fim = inicio.add(const Duration(days: 6));
    String pad(int n) => n.toString().padLeft(2, '0');
    return '${pad(inicio.day)}/${pad(inicio.month)} a ${pad(fim.day)}/${pad(fim.month)}';
  }

  factory AlertaDengue.fromJson(Map<String, dynamic> json) {
    return AlertaDengue(
      semanaEpidemiologica: (json['SE'] as num?)?.toInt() ?? 0,
      casosNotificados: (json['casos'] as num?)?.toInt() ?? 0,
      casosEstimados: (json['casos_est'] as num?)?.toInt() ?? 0,
      nivelAlerta: (json['nivel'] as num?)?.toInt() ?? 1,
    );
  }
}

class ResumoDengue {
  final AlertaDengue ultimaSemana;
  final int totalCasosAno;
  final int semanasPicoNivel;
  final TendenciaCasos tendencia;

  const ResumoDengue({
    required this.ultimaSemana,
    required this.totalCasosAno,
    required this.semanasPicoNivel,
    required this.tendencia,
  });

  factory ResumoDengue.calcular(List<AlertaDengue> alertas) {
    if (alertas.isEmpty) {
      return ResumoDengue(
        ultimaSemana: AlertaDengue(
          semanaEpidemiologica: 0,
          casosNotificados: 0,
          casosEstimados: 0,
          nivelAlerta: 1,
        ),
        totalCasosAno: 0,
        semanasPicoNivel: 0,
        tendencia: TendenciaCasos.estavel,
      );
    }
    final ordenados = List<AlertaDengue>.from(alertas)
      ..sort((a, b) => a.semanaEpidemiologica.compareTo(b.semanaEpidemiologica));
    final ultima = ordenados.last;
    final total = ordenados.fold(0, (s, a) => s + a.casosNotificados);
    final pico = ordenados.where((a) => a.nivelAlerta >= 3).length;
    TendenciaCasos tendencia = TendenciaCasos.estavel;
    if (ordenados.length >= 6) {
      final recentes = ordenados.sublist(ordenados.length - 3);
      final anteriores = ordenados.sublist(ordenados.length - 6, ordenados.length - 3);
      final mediaRecente = recentes.fold(0, (s, a) => s + a.casosNotificados) / 3;
      final mediaAnterior = anteriores.fold(0, (s, a) => s + a.casosNotificados) / 3;
      if (mediaAnterior == 0) {
        tendencia = TendenciaCasos.estavel;
      } else if (mediaRecente > mediaAnterior * 1.15) {
        tendencia = TendenciaCasos.subindo;
      } else if (mediaRecente < mediaAnterior * 0.85) {
        tendencia = TendenciaCasos.descendo;
      }
    }
    return ResumoDengue(
      ultimaSemana: ultima,
      totalCasosAno: total,
      semanasPicoNivel: pico,
      tendencia: tendencia,
    );
  }
}

enum TendenciaCasos { subindo, descendo, estavel }
