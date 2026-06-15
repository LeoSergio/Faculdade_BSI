import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import '../viewmodels/alertas_viewmodel.dart';
import 'widgets/alerta_card.dart';
import 'widgets/resumo_card.dart';

class HomeScreen extends HookWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final vm = useMemoized(() => AlertasViewModel());
    final state = useValueListenable(vm.state);
    final municipioAtual = useValueListenable(vm.municipioSelecionado);

    useEffect(() {
      vm.carregarAlertas();
      return vm.dispose;
    }, []);

    return Scaffold(
      backgroundColor: Theme.of(context).colorScheme.surface,
      appBar: _buildAppBar(context, vm, municipioAtual),
      body: _buildBody(context, state, vm),
    );
  }

  PreferredSizeWidget _buildAppBar(
    BuildContext context,
    AlertasViewModel vm,
    int municipioAtual,
  ) {
    return AppBar(
      backgroundColor: Theme.of(context).colorScheme.surface,
      elevation: 0,
      scrolledUnderElevation: 1,
      toolbarHeight: 64,
      title: Row(
        children: [
          Container(
            width: 34,
            height: 34,
            decoration: BoxDecoration(
              color: Theme.of(context).colorScheme.primary,
              borderRadius: BorderRadius.circular(9),
            ),
            child: const Icon(Icons.radar_rounded, color: Colors.white, size: 19),
          ),
          const SizedBox(width: 10),
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: [
              Text('RadarSUS',
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.w800,
                        letterSpacing: -0.4,
                      )),
              Text('Vigilância Epidemiológica',
                  style: Theme.of(context).textTheme.labelSmall?.copyWith(
                        color: Theme.of(context).colorScheme.onSurfaceVariant,
                      )),
            ],
          ),
        ],
      ),
      actions: [
        Padding(
          padding: const EdgeInsets.only(right: 12),
          child: DropdownButtonHideUnderline(
            child: DropdownButton<int>(
              value: municipioAtual,
              borderRadius: BorderRadius.circular(10),
              icon: Icon(Icons.location_on_rounded,
                  color: Theme.of(context).colorScheme.primary),
              items: AlertasViewModel.municipios.entries
                  .map((e) => DropdownMenuItem(
                        value: e.key,
                        child: Text(e.value,
                            style: Theme.of(context)
                                .textTheme
                                .bodyMedium
                                ?.copyWith(fontWeight: FontWeight.w600)),
                      ))
                  .toList(),
              onChanged: (val) {
                if (val != null) vm.alterarMunicipio(val);
              },
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildBody(
    BuildContext context,
    AlertasState state,
    AlertasViewModel vm,
  ) {
    return Center(
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 700),
        child: switch (state) {
          AlertasInicial() => const SizedBox.shrink(),
          AlertasCarregando() => const Center(child: CircularProgressIndicator()),
          AlertasCarregados(:final alertas, :final resumo) => alertas.isEmpty
              ? _buildVazio(context)
              : RefreshIndicator(
                  onRefresh: vm.carregarAlertas,
                  child: CustomScrollView(
                    slivers: [
                      SliverToBoxAdapter(
                        child: ResumoCard(
                          resumo: resumo,
                          nomeMunicipio: AlertasViewModel
                              .municipios[vm.municipioSelecionado.value]!,
                        ),
                      ),
                      SliverToBoxAdapter(
                        child: Padding(
                          padding: const EdgeInsets.fromLTRB(16, 16, 16, 4),
                          child: Text(
                            'HISTÓRICO SEMANAL',
                            style: Theme.of(context)
                                .textTheme
                                .labelSmall
                                ?.copyWith(
                                  letterSpacing: 1.2,
                                  color: Theme.of(context)
                                      .colorScheme
                                      .onSurfaceVariant,
                                ),
                          ),
                        ),
                      ),
                      SliverList.builder(
                        itemCount: alertas.length,
                        itemBuilder: (_, i) => AlertaCard(alerta: alertas[i]),
                      ),
                      const SliverPadding(padding: EdgeInsets.only(bottom: 24)),
                    ],
                  ),
                ),
          AlertasErro(:final mensagem) => _buildErro(context, mensagem, vm),
        },
      ),
    );
  }

  Widget _buildVazio(BuildContext context) => Center(
        child: Column(mainAxisSize: MainAxisSize.min, children: [
          Icon(Icons.inbox_rounded,
              size: 48, color: Theme.of(context).colorScheme.outlineVariant),
          const SizedBox(height: 12),
          Text('Nenhum alerta encontrado',
              style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                    color: Theme.of(context).colorScheme.onSurfaceVariant,
                  )),
        ]),
      );

  Widget _buildErro(
    BuildContext context,
    String mensagem,
    AlertasViewModel vm,
  ) =>
      Center(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 32),
          child: Column(mainAxisSize: MainAxisSize.min, children: [
            Icon(Icons.wifi_off_rounded,
                size: 48, color: Theme.of(context).colorScheme.error),
            const SizedBox(height: 12),
            Text('Falha na conexão',
                style: Theme.of(context)
                    .textTheme
                    .titleMedium
                    ?.copyWith(fontWeight: FontWeight.w700)),
            const SizedBox(height: 6),
            Text(mensagem,
                textAlign: TextAlign.center,
                style: Theme.of(context).textTheme.bodySmall?.copyWith(
                      color: Theme.of(context).colorScheme.onSurfaceVariant,
                    )),
            const SizedBox(height: 20),
            FilledButton.icon(
              onPressed: vm.carregarAlertas,
              icon: const Icon(Icons.refresh_rounded),
              label: const Text('Tentar novamente'),
            ),
          ]),
        ),
      );
}
