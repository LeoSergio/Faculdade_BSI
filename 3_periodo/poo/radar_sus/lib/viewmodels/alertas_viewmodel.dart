import 'package:flutter/foundation.dart';
import '../models/alerta_dengue.dart';
import '../services/dengue_service.dart';

sealed class AlertasState {}
class AlertasInicial extends AlertasState {}
class AlertasCarregando extends AlertasState {}
class AlertasCarregados extends AlertasState {
  final List<AlertaDengue> alertas;
  final ResumoDengue resumo;
  AlertasCarregados({required this.alertas, required this.resumo});
}
class AlertasErro extends AlertasState {
  final String mensagem;
  AlertasErro(this.mensagem);
}

class AlertasViewModel {
  final _service = DengueService();

  static const Map<int, String> municipios = {
    2408102: 'Natal',
    2402006: 'Caicó',
    2411205: 'Santa Cruz',
  };

  final state = ValueNotifier<AlertasState>(AlertasInicial());
  final municipioSelecionado = ValueNotifier<int>(2408102);

  void alterarMunicipio(int codigoIBGE) {
    if (municipioSelecionado.value == codigoIBGE) return;
    municipioSelecionado.value = codigoIBGE;
    carregarAlertas();
  }

  Future<void> carregarAlertas() async {
    state.value = AlertasCarregando();
    try {
      final alertas = await _service.fetchAlertas(municipioSelecionado.value);
      alertas.sort((a, b) =>
          b.semanaEpidemiologica.compareTo(a.semanaEpidemiologica));
      final resumo = ResumoDengue.calcular(alertas);
      state.value = AlertasCarregados(alertas: alertas, resumo: resumo);
    } catch (e) {
      state.value = AlertasErro(e.toString());
    }
  }

  void dispose() {
    state.dispose();
    municipioSelecionado.dispose();
    _service.dispose();
  }
}
