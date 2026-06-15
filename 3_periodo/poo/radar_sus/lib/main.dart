import 'package:flutter/material.dart';
import 'views/home_screen.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const RadarSusApp());
}

class RadarSusApp extends StatelessWidget {
  const RadarSusApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'RadarSUS',
      debugShowCheckedModeBanner: false,
      theme: _buildTheme(Brightness.light),
      darkTheme: _buildTheme(Brightness.dark),
      home: const HomeScreen(),
    );
  }

  ThemeData _buildTheme(Brightness brightness) {
    // Uma cor mais puxada para o universo de dados/vigilância (Azul Marinho)
    const seedColor = Color(0xFF005C8A);

    final colorScheme = ColorScheme.fromSeed(
      seedColor: seedColor,
      brightness: brightness,
    );

    return ThemeData(
      useMaterial3: true,
      colorScheme: colorScheme,
      fontFamily: 'Roboto',
      appBarTheme: AppBarTheme(
        centerTitle: false,
        backgroundColor: colorScheme.surface,
        foregroundColor: colorScheme.onSurface,
        titleTextStyle: TextStyle(
          fontFamily: 'Roboto',
          fontSize: 20,
          fontWeight: FontWeight.w800,
          color: colorScheme.onSurface,
          letterSpacing: -0.5,
        ),
      ),
      cardTheme: CardThemeData(
        elevation: 0,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
    );
  }
}