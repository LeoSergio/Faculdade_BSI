// test/services/ibge_service_test.dart
// Testa a camada de serviço sem fazer requisições reais à internet.
// POO: injeção de dependência — passamos um cliente HTTP falso (mock).

import 'dart:convert';
import 'package:flutter_test/flutter_test.dart';
import 'package:http/http.dart' as http;
import 'package:http/testing.dart';
import 'package:radar_sus/services/ibge_service.dart';

// JSON que simula a resposta real da API do IBGE
const _respostaValida = '''{
  "count": 2,
  "items": [
    {
      "titulo": "Notícia de saúde 1",
      "introducao": "Introdução da notícia 1.",
      "link": "https://ibge.gov.br/1",
      "data_publicacao": "10/01/2024 08:00:00"
    },
    {
      "titulo": "Notícia de saúde 2",
      "introducao": "Introdução da notícia 2.",
      "link": "https://ibge.gov.br/2",
      "data_publicacao": "11/01/2024 09:00:00"
    }
  ]
}''';

void main() {
  group('IbgeService.fetchNoticias', () {
    test('deve retornar lista de Noticia em resposta 200 válida', () async {
      final mockClient = MockClient((_) async => http.Response(
            _respostaValida,
            200,
            headers: {'content-type': 'application/json'},
          ));

      final service = IbgeService(client: mockClient);
      final noticias = await service.fetchNoticias(quantidade: 2);

      expect(noticias.length, 2);
      expect(noticias[0].titulo, 'Notícia de saúde 1');
      expect(noticias[1].link, 'https://ibge.gov.br/2');
    });

    test('deve lançar IbgeServiceException em resposta 500', () async {
      final mockClient = MockClient(
        (_) async => http.Response('Erro interno', 500),
      );

      final service = IbgeService(client: mockClient);

      expect(
        () => service.fetchNoticias(),
        throwsA(isA<IbgeServiceException>()),
      );
    });

    test('deve retornar lista vazia quando items está ausente', () async {
      final mockClient = MockClient(
        (_) async => http.Response(
          jsonEncode({'count': 0}),
          200,
          headers: {'content-type': 'application/json'},
        ),
      );

      final service = IbgeService(client: mockClient);
      final noticias = await service.fetchNoticias();

      expect(noticias, isEmpty);
    });

    test('deve lançar IbgeServiceException em falha de rede', () async {
      final mockClient = MockClient(
        (_) async => throw Exception('sem conexão'),
      );

      final service = IbgeService(client: mockClient);

      expect(
        () => service.fetchNoticias(),
        throwsA(isA<IbgeServiceException>()),
      );
    });
  });
}