// test/viewmodels/noticias_viewmodel_test.dart
// Testa as transições de estado do ViewModel sem envolver widgets.

import 'dart:convert';
import 'package:flutter_test/flutter_test.dart';
import 'package:http/http.dart' as http;
import 'package:http/testing.dart';
import 'package:radar_sus/services/ibge_service.dart';
import 'package:radar_sus/viewmodels/noticias_viewmodel.dart';

IbgeService _serviceComResposta(String body, int status) {
  final client = MockClient(
    (_) async => http.Response(
      body,
      status,
      headers: {'content-type': 'application/json'},
    ),
  );
  return IbgeService(client: client);
}

const _jsonDuasNoticias = '''{
  "count": 2,
  "items": [
    {
      "titulo": "Notícia A",
      "introducao": "Texto A",
      "link": "https://ibge.gov.br/a",
      "data_publicacao": "01/06/2024 00:00:00"
    },
    {
      "titulo": "Notícia B",
      "introducao": "Texto B",
      "link": "https://ibge.gov.br/b",
      "data_publicacao": "02/06/2024 00:00:00"
    }
  ]
}''';

void main() {
  group('NoticiasViewModel', () {
    test('estado inicial deve ser NoticiasInicial', () {
      final vm = NoticiasViewModel(
        service: _serviceComResposta(_jsonDuasNoticias, 200),
      );
      expect(vm.state.value, isA<NoticiasInicial>());
      vm.dispose();
    });

    test('deve transitar para NoticiasCarregadas após sucesso', () async {
      final vm = NoticiasViewModel(
        service: _serviceComResposta(_jsonDuasNoticias, 200),
      );

      await vm.carregarNoticias();

      expect(vm.state.value, isA<NoticiasCarregadas>());
      final carregadas = vm.state.value as NoticiasCarregadas;
      expect(carregadas.noticias.length, 2);
      expect(carregadas.noticias[0].titulo, 'Notícia A');
      vm.dispose();
    });

    test('deve transitar para NoticiasErro em resposta 500', () async {
      final vm = NoticiasViewModel(
        service: _serviceComResposta('erro', 500),
      );

      await vm.carregarNoticias();

      expect(vm.state.value, isA<NoticiasErro>());
      vm.dispose();
    });

    test('alterarQuantidade deve atualizar quantidadeSelecionada e recarregar', () async {
      final vm = NoticiasViewModel(
        service: _serviceComResposta(_jsonDuasNoticias, 200),
      );

      await vm.alterarQuantidade(20);

      expect(vm.quantidadeSelecionada.value, 20);
      expect(vm.state.value, isA<NoticiasCarregadas>());
      vm.dispose();
    });

    test('opcoesQuantidade deve conter os valores esperados', () {
      expect(NoticiasViewModel.opcoesQuantidade, containsAll([5, 10, 20, 50]));
    });
  });
}