import 'package:flutter_test/flutter_test.dart';
import 'package:radar_sus/main.dart';

void main() {
  testWidgets('App inicializa sem erros', (WidgetTester tester) async {
    await tester.pumpWidget(const RadarSusApp());
    expect(find.byType(RadarSusApp), findsOneWidget);
  });
}
