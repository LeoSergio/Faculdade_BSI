import 'package:flutter/material.dart';
import '../../models/alerta_dengue.dart';

class AlertaCard extends StatelessWidget {
  final AlertaDengue alerta;

  const AlertaCard({super.key, required this.alerta});

  static const _cores = {
    1: Color(0xFF2E7D32),
    2: Color(0xFFF9A825),
    3: Color(0xFFE65100),
    4: Color(0xFFC62828),
  };
  static const _textos = {
    1: 'Baixo',
    2: 'Moderado',
    3: 'Alto',
    4: 'Muito Alto',
  };

  @override
  Widget build(BuildContext context) {
    final cor = _cores[alerta.nivelAlerta] ?? Colors.grey;
    final texto = _textos[alerta.nivelAlerta] ?? 'Sem dados';

    return Card(
      margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 5),
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12),
        side: BorderSide(color: cor.withOpacity(0.4), width: 1.2),
      ),
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
        child: Row(
          children: [
            // Indicador de nível colorido
            Container(
              width: 4,
              height: 48,
              decoration: BoxDecoration(
                color: cor,
                borderRadius: BorderRadius.circular(4),
              ),
            ),
            const SizedBox(width: 12),

            // Datas e casos
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    alerta.periodoFormatado,
                    style: Theme.of(context).textTheme.titleSmall?.copyWith(
                          fontWeight: FontWeight.w700,
                        ),
                  ),
                  const SizedBox(height: 3),
                  Text(
                    'Notificados: ${alerta.casosNotificados}  •  Estimativa: ${alerta.casosEstimados}',
                    style: Theme.of(context).textTheme.bodySmall?.copyWith(
                          color: Theme.of(context).colorScheme.onSurfaceVariant,
                        ),
                  ),
                ],
              ),
            ),

            // Chip de risco
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
              decoration: BoxDecoration(
                color: cor.withOpacity(0.12),
                borderRadius: BorderRadius.circular(20),
                border: Border.all(color: cor.withOpacity(0.4)),
              ),
              child: Text(
                texto,
                style: TextStyle(
                  color: cor,
                  fontWeight: FontWeight.w700,
                  fontSize: 12,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}