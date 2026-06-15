import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/alerta_dengue.dart';

class DengueService {
  static const String _baseUrl = 'https://info.dengue.mat.br/api/alertcity';
  final http.Client _client;

  DengueService({http.Client? client}) : _client = client ?? http.Client();

  Future<List<AlertaDengue>> fetchAlertas(int geocode) async {
    // Captura o ano atual dinamicamente do sistema do usuário
    final anoAtual = DateTime.now().year.toString();

    final uri = Uri.parse(_baseUrl).replace(queryParameters: {
      'geocode': geocode.toString(),
      'disease': 'dengue',
      'format': 'json',
      'ew_start': '1',    
      'ew_end': '53',     
      'ey_start': anoAtual,
      'ey_end': anoAtual,
    });

    try {
      final response = await _client
          .get(uri, headers: {'Accept': 'application/json'})
          .timeout(const Duration(seconds: 15));

      if (response.statusCode != 200) {
        throw Exception('Erro na API: ${response.statusCode}');
      }

      final List<dynamic> body = jsonDecode(response.body);

      return body
          .whereType<Map<String, dynamic>>()
          .map(AlertaDengue.fromJson)
          .toList();
    } catch (e) {
      throw Exception('Falha ao buscar alertas de dengue: $e');
    }
  }

  // O método que estava faltando para fechar a conexão HTTP e limpar a memória!
  void dispose() => _client.close();
}