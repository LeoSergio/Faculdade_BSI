import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/noticia.dart';

class IbgeService {
  static const String _baseUrl =
      'https://servicodados.ibge.gov.br/api/v3/noticias/';

  // Termos de busca: saúde com foco no RN.
  // A API não tem filtro por estado — usamos busca combinada como proxy.
  // Quando não há resultados do RN, retorna notícias nacionais de saúde.
  static const List<String> _termosPrimarios = [
    'saude rio grande do norte',
    'saude RN',
    'saude nordeste',
  ];
  static const String _termoFallback = 'saude';

  final http.Client _client;

  IbgeService({http.Client? client}) : _client = client ?? http.Client();

  Future<List<Noticia>> fetchNoticias({int quantidade = 10}) async {
    // Tenta busca regionalizada primeiro
    for (final termo in _termosPrimarios) {
      final resultado = await _buscar(termo, quantidade);
      if (resultado.isNotEmpty) return resultado;
    }
    // Fallback: saúde nacional
    return _buscar(_termoFallback, quantidade);
  }

  Future<List<Noticia>> _buscar(String busca, int quantidade) async {
    final uri = Uri.parse(_baseUrl).replace(queryParameters: {
      'busca': busca,
      'qtd': quantidade.toString(),
    });

    try {
      final response = await _client
          .get(uri, headers: {'Accept': 'application/json'})
          .timeout(const Duration(seconds: 15));

      if (response.statusCode != 200) {
        throw IbgeServiceException(
          'Resposta inesperada da API: ${response.statusCode}',
        );
      }

      final Map<String, dynamic> body =
          jsonDecode(response.body) as Map<String, dynamic>;

      final List<dynamic> itens = body['items'] as List<dynamic>? ?? [];

      return itens
          .whereType<Map<String, dynamic>>()
          .map(Noticia.fromJson)
          .toList();
    } on IbgeServiceException {
      rethrow;
    } catch (e) {
      throw IbgeServiceException('Falha ao buscar notícias: $e');
    }
  }

  void dispose() => _client.close();
}

class IbgeServiceException implements Exception {
  final String message;
  const IbgeServiceException(this.message);

  @override
  String toString() => 'IbgeServiceException: $message';
}
