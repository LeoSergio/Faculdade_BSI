// views/widgets/noticia_card.dart
// POO — Herança e Reutilização: widget genérico que recebe um objeto Noticia
// e se adapta ao conteúdo — nunca conhece a origem dos dados.

import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import '../../models/noticia.dart';

class NoticiaCard extends StatelessWidget {
  final Noticia noticia;
  final VoidCallback? onTap;

  const NoticiaCard({
    super.key,
    required this.noticia,
    this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    final dataFormatada =
        DateFormat("dd 'de' MMMM 'de' yyyy", 'pt_BR').format(noticia.publicadaEm);

    return Card(
      margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12),
        side: BorderSide(
          color: Theme.of(context).colorScheme.outlineVariant,
        ),
      ),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Eyebrow — data de publicação
              Text(
                dataFormatada.toUpperCase(),
                style: Theme.of(context).textTheme.labelSmall?.copyWith(
                      color: Theme.of(context).colorScheme.primary,
                      letterSpacing: 1.2,
                      fontWeight: FontWeight.w600,
                    ),
              ),
              const SizedBox(height: 6),

              // Título
              Text(
                noticia.titulo,
                style: Theme.of(context).textTheme.titleMedium?.copyWith(
                      fontWeight: FontWeight.w700,
                      height: 1.3,
                    ),
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
              ),
              const SizedBox(height: 8),

              // Introdução
              Text(
                noticia.introducao,
                style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                      color: Theme.of(context).colorScheme.onSurfaceVariant,
                      height: 1.5,
                    ),
                maxLines: 3,
                overflow: TextOverflow.ellipsis,
              ),
              const SizedBox(height: 12),

              // Rodapé — link
              Row(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  Text(
                    'Ler no IBGE',
                    style: Theme.of(context).textTheme.labelMedium?.copyWith(
                          color: Theme.of(context).colorScheme.primary,
                          fontWeight: FontWeight.w600,
                        ),
                  ),
                  const SizedBox(width: 4),
                  Icon(
                    Icons.arrow_forward_rounded,
                    size: 14,
                    color: Theme.of(context).colorScheme.primary,
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}