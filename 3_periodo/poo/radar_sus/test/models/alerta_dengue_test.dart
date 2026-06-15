import 'package:flutter_test/flutter_test.dart';
// Ajuste o caminho abaixo conforme o nome do seu pacote principal (ex: radar_sus)
import 'package:radar_sus/models/alerta_dengue.dart'; 

void main() {
  group('AlertaDengue Model |', () {
    test('Deve extrair os dados corretamente de um JSON válido e arredondar decimais', () {
      // Simula o JSON problemático da API (com casos_est vindo como double)
      final jsonApi = {
        "SE": 202401,
        "casos": 15,
        "casos_est": 15.8, // <-- O decimal que quebrou o app antes
        "nivel": 2
      };

      final alerta = AlertaDengue.fromJson(jsonApi);

      expect(alerta.semanaEpidemiologica, 202401);
      expect(alerta.casosNotificados, 15);
      expect(alerta.casosEstimados, 15); // Deve ter sido convertido/truncado para int
      expect(alerta.nivelAlerta, 2);
    });

    test('Deve formatar a semana epidemiológica corretamente', () {
      final alerta = AlertaDengue(
        semanaEpidemiologica: 202412,
        casosNotificados: 0,
        casosEstimados: 0,
        nivelAlerta: 1,
      );

      expect(alerta.semanaFormatada, 'Semana 12 de 2024');
    });

    test('Deve lidar com JSON vazio usando valores padrão', () {
      final jsonVazio = <String, dynamic>{};
      final alerta = AlertaDengue.fromJson(jsonVazio);

      expect(alerta.semanaEpidemiologica, 0);
      expect(alerta.casosNotificados, 0);
      expect(alerta.casosEstimados, 0);
      expect(alerta.nivelAlerta, 1);
    });
  });
}