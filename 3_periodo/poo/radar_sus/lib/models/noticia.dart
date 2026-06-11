// models/noticia.dart
// POO — Encapsulamento: atributos privados expostos via getters somente-leitura.

class Noticia {
  final String _titulo;
  final String _introducao;
  final String _link;
  final DateTime _publicadaEm;

  const Noticia({
    required String titulo,
    required String introducao,
    required String link,
    required DateTime publicadaEm,
  })  : _titulo = titulo,
        _introducao = introducao,
        _link = link,
        _publicadaEm = publicadaEm;

  // Getters — interface pública controlada
  String get titulo => _titulo;
  String get introducao => _introducao;
  String get link => _link;
  DateTime get publicadaEm => _publicadaEm;

  /// Factory constructor — Abstração do parsing do JSON da API do IBGE.
  /// POO: separação entre construção do objeto e sua representação externa.
  factory Noticia.fromJson(Map<String, dynamic> json) {
    return Noticia(
      titulo: json['titulo'] as String? ?? 'Sem título',
      introducao: json['introducao'] as String? ?? '',
      link: json['link'] as String? ?? '',
      publicadaEm: _parseData(json['data_publicacao'] as String?),
    );
  }

  static DateTime _parseData(String? raw) {
    if (raw == null || raw.isEmpty) return DateTime(2000);
    try {
      // Formato esperado: "dd/MM/yyyy HH:mm:ss"
      final partes = raw.split(' ');
      final data = partes[0].split('/');
      return DateTime(
        int.parse(data[2]),
        int.parse(data[1]),
        int.parse(data[0]),
      );
    } catch (_) {
      return DateTime(2000);
    }
  }

  @override
  String toString() => 'Noticia(titulo: $_titulo, publicadaEm: $_publicadaEm)';
}