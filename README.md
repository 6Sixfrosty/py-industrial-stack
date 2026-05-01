# py-industrial-stack

Simulação da camada de edge computing de uma fábrica, do sensor até o painel na TV do chão de fábrica.

## Visão Geral

Projeto que simula em Python uma arquitetura industrial real de edge computing — onde os dados dos sensores são coletados via OPC UA, processados e classificados localmente, armazenados no MySQL e exibidos em painéis Grafana nas TVs da fábrica para os operadores, em tempo real, sem depender de nuvem.

## Arquitetura

```
┌──────────────────────────────────────────────┐
│           CHÃO DE FÁBRICA / OT SIMULADO      │
│                                              │
│  CLP Virtual Python                          │
│  - Simula sensores industriais               │
│  - Gera valores com random e threading       │
│                                              │
│  OPC UA Server                               │
│  - Expõe as tags do CLP na rede              │
│  - Permite leitura e escrita via OPC UA      │
└──────────────────────┬───────────────────────┘
                       │ OPC UA Read / Write
                       ▼
┌──────────────────────────────────────────────┐
│                EDGE COMPUTING                │
│                                              │
│  Edge Collector                              │
│  - Conecta no OPC UA Server                  │
│  - Coleta as tags industriais                │
│                                              │
│  Edge Data Processing                        │
│  - Trata os dados coletados                  │
│  - Classifica: NORMAL / ALERTA / CRÍTICO     │
│  - Prepara os dados para armazenamento       │
│                                              │
│  Edge Data Work Center                       │
│  - Organiza logs, status e operações         │
└──────────────────────┬───────────────────────┘
                       │ Dados tratados
                       ▼
┌──────────────────────────────────────────────┐
│                    MYSQL                     │
│  - Armazena dados brutos e processados       │
│  - Guarda histórico e eventos                │
└──────────────────────┬───────────────────────┘
                       │ Consultas SQL
                       ▼
┌──────────────────────────────────────────────┐
│               GRAFANA — TV DA FÁBRICA        │
│  - Exibe painéis industriais em tempo real   │
│  - Mostra temperatura, status e alertas      │
│  - Visualização local para os operadores     │
│  - Roda na edge, sem depender de nuvem       │
└──────────────────────────────────────────────┘
```

## Stack

- Python — CLP virtual, OPC UA server e edge computing
- Docker — containerização de todos os serviços
- MySQL — armazenamento local dos dados
- Grafana — painel industrial exibido nas TVs da fábrica
- OPC UA — protocolo de comunicação industrial


## Módulos

- clp/        → CLP virtual com sensores simulados
- opc-ua/     → servidor OPC UA que expõe as tags na rede
- edge/       → coleta, processamento e classificação dos dados
- database/   → schema e migrations do MySQL
- docs/       → diagramas e documentação da arquitetura


## Objetivo

Estudar e demonstrar na prática os conceitos de edge computing industrial — processamento local de dados de sensores, comunicação via OPC UA e visualização em tempo real no chão de fábrica, sem dependência de nuvem.
## Objetivo

Estudar e demonstrar na prática os conceitos de edge computing industrial — processamento local de dados de sensores, comunicação via OPC UA e visualização em tempo real no chão de fábrica, sem dependência de nuvem.
