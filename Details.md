┌─────────────┐   ┌───────────────┐   ┌────────────┐   ┌────────────┐
│ Log Sources │ → │ Ingestion API │ → │ Log Parser │ → │ Data Store │
└─────────────┘   └───────────────┘   └────────────┘   └─────┬──────┘
                                                            │
                                      ┌─────────────────────▼────────────────────┐
                                      │ Indexer / Search Engine (e.g., OpenSearch│
                                      └─────────────────────┬────────────────────┘
                                                            │
        ┌───────────────┐   ┌──────────────────────┐    ┌───▼────┐
        │ Alert Engine  │   │ Visualization Engine │    │  Auth  │
        └───────────────┘   └──────────────────────┘    └────────┘

--------------------------------------------------------------------------------------------------

siem-system/
│
├── main.py                         # Entrypoint for FastAPI app
├── config/
│   ├── settings.py                 # Load env/config using pydantic.BaseSettings
│   └── logging_config.yaml         # Central logging configuration
│
├── ingestion/                      # Log ingestion via API and syslog
│   ├── __init__.py
│   ├── api_receiver.py             # FastAPI routes for receiving logs via POST
│   ├── syslog_receiver.py          # TCP/UDP syslog listener using socketserver
│   └── agent_handler.py            # Parser for logs from forwarders like Fluent Bit
│
├── parser/                         # Log normalization/parsing layer
│   ├── __init__.py
│   ├── models/
│   │   ├── base_log.py             # Base log Pydantic model
│   │   └── firewall_log.py         # Example: firewall log schema
│   ├── normalizer.py               # Standardizes incoming raw logs
│   └── enrichers.py                # Add metadata (e.g., geo IP, threat intel)
│
├── storage/                        # Database and raw log storage
│   ├── __init__.py
│   ├── db.py                       # SQLAlchemy engine/session
│   ├── models/
│   │   ├── base.py                 # Base SQLAlchemy declarative base
│   │   └── log_event.py            # Log event DB model
│   ├── crud.py                     # CRUD utilities
│   └── clickhouse_writer.py        # Optional: log writer to ClickHouse
│
├── search/                         # Search/index APIs
│   ├── __init__.py
│   ├── opensearch_client.py        # Connects to OpenSearch
│   ├── indexer.py                  # Indexes normalized logs
│   └── query_engine.py             # Executes search queries
│
├── alerting/                       # Rule engine and notifications
│   ├── __init__.py
│   ├── scheduler.py                # Uses APScheduler or Celery
│   ├── rule_engine.py              # Match rules against new logs
│   ├── rules.yaml                  # Declarative rules (e.g., if src_ip == 'x.x.x.x')
│   └── notifiers/
│       ├── email.py                # Send alert emails
│       └── slack.py                # Slack webhook integration
│
├── dashboard/                      # Visualization and frontend API
│   ├── __init__.py
│   ├── routes.py                   # FastAPI routes for dashboards
│   └── visualizer.py               # Logic to generate summary charts (Plotly)
│
├── auth/                           # User management and auth
│   ├── __init__.py
│   ├── auth.py                     # JWT handling, login logic
│   └── users.py                    # User DB model and CRUD
│
├── tests/                          # Unit and integration tests
│   ├── test_ingestion.py
│   ├── test_alerting.py
│   ├── test_parser.py
│   └── test_end_to_end.py          # Simulate entire pipeline
│
├── utils/                          # Utility functions/helpers
│   ├── log_utils.py                # Structured logger
│   ├── geoip.py                    # Geolocation utility
│   └── validators.py               # Custom field validators
│
├── .env                            # Environment variables
├── requirements.txt                # Pip requirements
├── Dockerfile                      # Docker build for backend
└── docker-compose.yml              # Full stack config (API, DB, OpenSearch)
