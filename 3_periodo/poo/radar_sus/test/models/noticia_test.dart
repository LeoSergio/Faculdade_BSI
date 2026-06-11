// test/models/noticia_test.dart
// Testa o encapsulamento e o parsing do modelo Noticia.

import 'package:flutter_test/flutter_test.dart';
import 'package:radar_sus/models/noticia.dart';

void main() {
  group('Noticia.fromJson', () {
    test('deve criar objeto corretamente a partir de JSON válido', () {
      final json = {
        'titulo': 'Vacinação contra dengue avança no Brasil',
        'introducao': 'O Ministério da Saúde reportou aumento na cobertura.',
        'link': 'https://ibge.gov.br/noticias/123',
        'data_publicacao': '15/03/2024 10:30:00',
      };

      final noticia = Noticia.fromJson(json);

      expect(noticia.titulo, 'Vacinação contra dengue avança no Brasil');
      expect(noticia.introducao, 'O Ministério da Saúde reportou aumento na cobertura.');
      expect(noticia.link, 'https://ibge.gov.br/noticias/123');
      expect(noticia.publicadaEm, DateTime(2024, 3, 15));
    });

    test('deve usar valores padrão quando campos ausentes', () {
      final noticia = Noticia.fromJson({});

      expect(noticia.titulo, 'Sem título');
      expect(noticia.introducao, '');
      expect(noticia.link, '');
      expect(noticia.publicadaEm, DateTime(2000));
    });

    test('deve retornar DateTime(2000) para data malformada', () {
      final json = {
        'titulo': 'Teste',
        'introducao': '',
        'link': '',
        'data_publicacao': 'data-invalida',
      };

      final noticia = Noticia.fromJson(json);
      expect(noticia.publicadaEm, DateTime(2000));
    });

    test('toString deve conter titulo e data', () {
      final noticia = Noticia(
        titulo: 'Saúde Pública',
        introducao: '',
        link: '',
        publicadaEm: DateTime(2024, 1, 10),
      );

      expect(noticia.toString(), contains('Saúde Pública'));
      expect(noticia.toString(), contains('2024-01-10'));
    });
  });
}