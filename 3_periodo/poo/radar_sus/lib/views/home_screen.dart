import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import '../viewmodels/noticias_viewmodel.dart';
import 'widgets/noticia_card.dart';

class HomeScreen extends HookWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final vm = useMemoized(() => NoticiasViewModel());
    final state = useValueListenable(vm.state);
    final quantidade = useValueListenable(vm.quantidadeSelecionada);

    useEffect(() {
      vm.carregarNoticias();
      return vm.dispose;
    }, []);

    return Scaffold(
      backgroundColor: Theme.of(context).colorScheme.surface,
      appBar: _buildAppBar(context, vm, quantidade),
      body: _buildBody(context, state, vm),
    );
  }

  PreferredSizeWidget _buildAppBar(
    BuildContext context,
    NoticiasViewModel vm,
    int quantidade,
  ) {
    return AppBar(
      backgroundColor: Theme.of(context).colorScheme.surface,
      elevation: 0,
      scrolledUnderElevation: 1,
      title: Row(
        children: [
          Container(
            width: 32,
            height: 32,
            decoration: BoxDecoration(
              color: Theme.of(context).colorScheme.primary,
              borderRadius: BorderRadius.circular(8),
            ),
            child: const Icon(
              Icons.radar_rounded,
              color: Colors.white,
              size: 18,
            ),
          ),
          const SizedBox(width: 10),
          Text(
            'RadarSUS',
            style: Theme.of(context).textTheme.titleLarge?.copyWith(
                  fontWeight: FontWeight.w800,
                  letterSpacing: -0.5,
                ),
          ),
          const SizedBox(height: 2),
          Text(
            'Saúde • Rio Grande do Norte',
            style: TextStyle(
              fontSize: 11,
              color: Theme.of(context).colorScheme.onSurfaceVariant,
            ),
          ),
        ],
      ),
      actions: [
        Padding(
          padding: const EdgeInsets.only(right: 12),
          child: DropdownButtonHideUnderline(
            child: DropdownButton<int>(
              value: quantidade,
              borderRadius: BorderRadius.circular(10),
              items: NoticiasViewModel.opcoesQuantidade
                  .map(
                    (q) => DropdownMenuItem(
                      value: q,
                      child: Text(
                        '$q notícias',
                        style: Theme.of(context).textTheme.bodyMedium,
                      ),
                    ),
                  )
                  .toList(),
              onChanged: (val) {
                if (val != null) vm.alterarQuantidade(val);
              },
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildBody(
    BuildContext context,
    NoticiasState state,
    NoticiasViewModel vm,
  ) {
    return switch (state) {
      NoticiasInicial() => const SizedBox.shrink(),
      NoticiasCarregando() => const Center(
          child: CircularProgressIndicator(),
        ),
      NoticiasCarregadas(:final noticias) => noticias.isEmpty
          ? _buildVazio(context)
          : RefreshIndicator(
              onRefresh: vm.carregarNoticias,
              child: ListView.builder(
                padding: const EdgeInsets.only(top: 8, bottom: 24),
                itemCount: noticias.length,
                itemBuilder: (_, index) => NoticiaCard(
                  noticia: noticias[index],
                  onTap: () {},
                ),
              ),
            ),
      NoticiasErro(:final mensagem) => _buildErro(context, mensagem, vm),
    };
  }

  Widget _buildVazio(BuildContext context) {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(
            Icons.inbox_rounded,
            size: 48,
            color: Theme.of(context).colorScheme.outlineVariant,
          ),
          const SizedBox(height: 12),
          Text(
            'Nenhuma notícia encontrada',
            style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                  color: Theme.of(context).colorScheme.onSurfaceVariant,
                ),
          ),
        ],
      ),
    );
  }

  Widget _buildErro(
    BuildContext context,
    String mensagem,
    NoticiasViewModel vm,
  ) {
    return Center(
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 32),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              Icons.wifi_off_rounded,
              size: 48,
              color: Theme.of(context).colorScheme.error,
            ),
            const SizedBox(height: 12),
            Text(
              'Não foi possível carregar',
              style: Theme.of(context).textTheme.titleMedium?.copyWith(
                    fontWeight: FontWeight.w700,
                  ),
            ),
            const SizedBox(height: 6),
            Text(
              mensagem,
              textAlign: TextAlign.center,
              style: Theme.of(context).textTheme.bodySmall?.copyWith(
                    color: Theme.of(context).colorScheme.onSurfaceVariant,
                  ),
            ),
            const SizedBox(height: 20),
            FilledButton.icon(
              onPressed: vm.carregarNoticias,
              icon: const Icon(Icons.refresh_rounded),
              label: const Text('Tentar novamente'),
            ),
          ],
        ),
      ),
    );
  }
}
