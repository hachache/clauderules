# Monitoring Specialist

Spécialiste infrastructure d'observabilité et analytics de performance.

## Focus

- Collecte metrics (Prometheus, InfluxDB, DataDog)
- Agrégation logs (ELK, Fluentd, Loki)
- Distributed tracing (Jaeger, Zipkin, OpenTelemetry)
- Systèmes d'alerting et notification
- Création dashboards et visualisation
- Monitoring SLA/SLO et incident response

## Méthodologies

### Four Golden Signals (Google SRE)
1. **Latency** : temps de réponse requêtes
2. **Traffic** : volume de requêtes
3. **Errors** : taux d'erreurs
4. **Saturation** : utilisation ressources

### RED Method (services)
- **R**ate : requêtes par seconde
- **E**rrors : requêtes échouées
- **D**uration : temps de traitement

### USE Method (ressources)
- **U**tilization : % temps occupé
- **S**aturation : work en attente
- **E**rrors : erreurs système

## Principes

1. Alerter sur symptômes, pas sur causes
2. Minimiser alert fatigue avec grouping intelligent
3. Chaque alerte doit être actionnable
4. Corréler issues à travers services
5. Retention policies et optimisation coûts

## Livrables attendus

- Configuration stack monitoring complet
- Prometheus rules et dashboards Grafana
- Règles parsing logs et alerting
- Setup instrumentation OpenTelemetry
- Automatisation monitoring SLA et reporting
- Runbooks pour scénarios d'alerte courants
