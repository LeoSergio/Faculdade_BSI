# 🏥 RadarSus

> Projeto de Extensão Universitária — Disciplina: Programação Orientada a Objetos  
> Curso: Bacharelado em Sistemas de Informação  
> Tema: **Letramento Digital na Saúde**

---

## 📋 Descrição

O **RadarSus** é um aplicativo móvel desenvolvido em Flutter que centraliza informações públicas de saúde na palma da mão do gestor municipal. O app consome a API pública do IBGE, filtrando notícias e estatísticas pelo tema saúde, e as apresenta em uma interface intuitiva e responsiva.

O projeto integra o programa de extensão **"Letramento Digital na Saúde"**, voltado para capacitar gestores de municípios como Caicó e Santa Cruz (RN) no uso de tecnologia digital como ferramenta de apoio à tomada de decisão em saúde pública.

---

## 🎯 Objetivos

- Demonstrar na prática os princípios de **Programação Orientada a Objetos** por meio de um produto funcional
- Oferecer aos gestores municipais acesso simplificado a dados oficiais do IBGE sobre saúde
- Introduzir competências digitais de forma orgânica, através da experiência de uso do aplicativo

---

## 🏗️ Arquitetura e POO na Prática

A estrutura do projeto foi desenhada para evidenciar os quatro pilares de POO:

```
lib/
├── main.dart
├── models/
│   └── noticia.dart              # Encapsulamento: atributos privados + getters
├── services/
│   └── ibge_service.dart         # Abstração: contrato de acesso à API
├── viewmodels/
│   └── noticias_viewmodel.dart   # Separação de responsabilidade com ValueNotifier
└── views/
    ├── home_screen.dart
    └── widgets/
        └── noticia_card.dart     # Reutilização: componente genérico
```

| Camada | Pilar de POO | Descrição |
|---|---|---|
| `models/` | **Encapsulamento** | Dados da API modelados como objetos com atributos controlados |
| `services/` | **Abstração** | Lógica de requisição HTTP isolada, expondo apenas o necessário |
| `viewmodels/` | **Polimorfismo** | Estado reativo desacoplado da interface visual |
| `widgets/` | **Herança** | Componentes que estendem widgets base do Flutter |

---

## ⚙️ Stack Técnica

| Tecnologia | Versão | Papel |
|---|---|---|
| Flutter | ≥ 3.x | Framework principal |
| Dart | ≥ 3.x | Linguagem |
| `http` | ^1.2.1 | Requisições HTTP assíncronas para a API do IBGE |
| `flutter_hooks` | ^0.20.5 | Gerência de estado reativa com `ValueNotifier` |

### Por que `ValueNotifier` em vez de BLoC ou MobX?

Para um projeto de prazo semestral, `ValueNotifier` + `flutter_hooks` entrega reatividade granular com zero dependências adicionais — apenas o widget que depende do estado é reconstruído. Isso respeita o princípio de escolher **a ferramenta mais simples que resolve o problema**, sem sacrificar a separação entre estado e UI.

---

## 🌐 API Utilizada

**IBGE — Agência de Notícias**  
`https://servicodados.ibge.gov.br/api/v3/noticias/?qtd=10&tipo=noticia`

- Pública e gratuita, sem necessidade de autenticação
- Filtrada pelo tema `saúde`
- Retorna notícias em formato JSON com título, introdução, link e data de publicação

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos

- Flutter SDK instalado (`flutter --version`)
- Android Studio **ou** VS Code com extensão Flutter
- Dispositivo físico ou emulador configurado

### Instalação

```bash
# 1. Clonar o repositório
git clone git@github.com:LeoSergio/Faculdade_BSI.git
cd Faculdade_BSI/poo/radar_sus

# 2. Instalar dependências
flutter pub get

# 3. Verificar ambiente
flutter doctor

# 4. Rodar o app
flutter run
```

---

## 📱 Funcionalidades do MVP

- [x] Listagem de notícias de saúde da API do IBGE
- [x] Filtro por quantidade de resultados via `DropdownButton`
- [x] Componentização genérica com `List<Map<String, dynamic>>`
- [x] Gerência de estado reativa sem `StatefulWidget`


---

## 📂 Contexto no Repositório

Este projeto faz parte do repositório geral da graduação em Sistemas de Informação:

```
Faculdade_BSI/
├── 1periodo/algoritmo/
├── 2periodo/
├── BD/
├── E.D/
├── FADA/
└── POO/
    └── RadarSus/   ← você está aqui
```

---

## 👤 Autor

**Leo Sergio**  
Bacharelado em Sistemas de Informação  
Universidade — NCaicó, RN  

[![GitHub](https://img.shields.io/badge/GitHub-LeoSergio-181717?style=flat&logo=github)](https://github.com/LeoSergio)

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](../../LICENSE) na raiz do repositório.