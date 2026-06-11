import 'package:flutter/foundation.dart';
import '../models/noticia.dart';
import '../services/ibge_service.dart';

sealed class NoticiasState {
  const NoticiasState();
}

class NoticiasInicial extends NoticiasState {
  const NoticiasInicial();
}

class NoticiasCarregando extends NoticiasState {
  const NoticiasCarregando();
}

class NoticiasCarregadas extends NoticiasState {
  final List<Noticia> noticias;
  const NoticiasCarregadas(this.noticias);
}

class NoticiasErro extends NoticiasState {
  final String mensagem;
  const NoticiasErro(this.mensagem);
}

class NoticiasViewModel {
  final IbgeService _service;

  final ValueNotifier<NoticiasState> state =
      ValueNotifier(const NoticiasInicial());

  final ValueNotifier<int> quantidadeSelecionada = ValueNotifier(10);

  NoticiasViewModel({IbgeService? service})
      : _service = service ?? IbgeService();

  static const List<int> opcoesQuantidade = [5, 10, 20, 50];

  Future<void> carregarNoticias() async {
    state.value = const NoticiasCarregando();
    try {
      final noticias = await _service.fetchNoticias(
        quantidade: quantidadeSelecionada.value,
      );
      state.value = NoticiasCarregadas(noticias);
    } on IbgeServiceException catch (e) {
      state.value = NoticiasErro(e.message);
    } catch (e) {
      state.value = NoticiasErro('Erro inesperado: $e');
    }
  }

  Future<void> alterarQuantidade(int novaQuantidade) async {
    quantidadeSelecionada.value = novaQuantidade;
    await carregarNoticias();
  }

  void dispose() {
    state.dispose();
    quantidadeSelecionada.dispose();
    _service.dispose();
  }
}
