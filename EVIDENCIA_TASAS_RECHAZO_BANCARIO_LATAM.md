# Compendio de Evidencia Empírica: Tasas de Rechazo Cross-Border en Turismo y Comercio LATAM ➔ México

Este documento reúne la recopilación de datos duros, benchmarks de procesadores de pago (EBANX, Rapyd, PayRetailers, Kushki, Nuvei, Yuno) y fuentes regulatorias (Condusef, Banco Central do Brasil) sobre la fricción y tasas de no autorización de pagos transfronterizos procedentes de Sudamérica hacia México.

---

## 1. Métricas Macroeconómicas y Benchmarks de la Industria

### A. Comercio Electrónico y Pagos con Tarjeta en México (CONDUSEF)
* **Tasa de No Autorización General:** En México, la **Condusef** reporta que entre el **28% y el 30%** de todas las solicitudes de compra en comercio electrónico con tarjetas de crédito y débito son rechazadas o no autorizadas ([Condusef Estadísticas](https://www.condusef.gob.mx/?p=estadisticas)).
* **Impacto:** Casi 3 de cada 10 intentos de compra digital en México son declinados antes de llegar a la liquidación.

### B. Pérdidas en el Sector Turismo Global (Nuvei)
* Un estudio global de la fintech **Nuvei** revela el impacto directo de los rechazos en la conversión turística ([Consumotic / Nuvei Report](https://consumotic.mx/ecommerce/medios_de_pago/sector-turismo-enfrentaria-perdidas-millonarias-por-rechazo-de-tarjetas-de-credito/)):
  * **13% de los viajeros** cambian de proveedor cuando su tarjeta es declinada.
  * **5% de los viajeros** abandonan la compra por completo.
  * Pérdidas estimadas de hasta **$117 mil millones de dólares** anuales en turismo y aerolíneas por declinaciones de pago.

### C. Falla de Procesamiento Transfronterizo Tradicional (Kushki, Rapyd, EBANX)
* Las pasarelas de pago explican que el problema **no radica en la red bancaria mexicana**, sino en los **filtros preventivos antifraude de los bancos emisores extranjeros** y la falta de interoperabilidad de adquirencia local ([Kushki / Milenio](https://www.milenio.com/negocios/politicas-autorizacion-fallas-rechazos-bancarios-e-commerce)).
* **Tasa de Rechazo Histórica Promedio en LATAM (Cross-Border):** **30% al 50%** ([Rapyd Research](https://www.rapyd.net/blog/payment-processing-decline-rates-in-latam/), [PayRetailers Cross-Border Guide](https://www.payretailers.com/en/blog/cross-border-payments-in-latin-america-a-complete-guide-for-merchants-2026), [Yuno Payment Declines](https://y.uno/es/blog/payment-declines)).

---

## 2. Radiografía de Rechazos por País de Origen

```
┌────────────────────────────────────────────────────────────────────────┐
│        TASAS DE RECHAZO TRANSFRONTERIZO PROMEDIO (LATAM ➔ MÉXICO)      │
├───────────────┬──────────────────────────┬─────────────────────────────┤
│ País          │ Tasa de Rechazo Promedio │ Tipo de Tarjeta Crítica     │
├───────────────┼──────────────────────────┼─────────────────────────────┤
│ 🇦🇷 Argentina │ 45% - 55%                │ Crédito y Débito restringido│
│ 🇨🇴 Colombia  │ 35% - 40%                │ Débito / Alertas Antifraude │
│ 🇵🇪 Perú      │ 35% - 40%                │ Débito / Falta de 3DS       │
│ 🇧🇷 Brasil    │ 30% - 35%                │ Tarjetas Domésticas (Elo)   │
└───────────────┴──────────────────────────┴─────────────────────────────┘
```

---

## 3. Desglose de Motivos Técnicos y Macroeconómicos por País

### 🇦🇷 Argentina (Rechazo: 45% - 55%)
1. **Restricciones de Divisas y Cepo Cambiario:**
   * Políticas monetarias estrictas: los bancos emisores rechazan de inmediato cargos internacionales si el titular supera cupos mensuales o límites fiscales de compra en el exterior.
2. **Bloqueo Nativo de Débito:**
   * Las tarjetas de débito argentinas vienen bloqueadas por defecto para consumos transfronterizos, requiriendo desbloqueo previo en home banking.

---

### 🇨🇴 Colombia (Rechazo: 35% - 40%)
1. **Falsos Positivos Antifraude (Card-Not-Present):**
   * Bancos como Bancolombia o Davivienda aplican modelos de IA hipersensibles debido al alto volumen de fraude transfronterizo en la región ([La Nota Económica](https://lanotaeconomica.com.co/movidas-empresarial/nuevo-estudio-sobre-el-fraude-en-el-comercio-electronico-alerta-sobre-perdidas-por-chargeback-en-colombia-us48-millones-en-2026/)).
   * Cargos directos desde México son marcados como "sospechosos" y bloqueados preventivamente.
2. **Falta de Homologación de Tarjetas de Débito:**
   * Gran volumen de cuentas maestras operan con tarjetas débito sin habilitación internacional para pasarelas extranjeras ([Ingenico LatAm FAQ](https://ingenico.com/latam-es/faq/why-transaction-declined)).

---

### 🇧🇷 Brasil (Rechazo: 30% - 35%)
1. **Tarjetas de Uso Exclusivo Nacional (Sin Co-badging):**
   * Millones de plásticos emitidos por neobancos o banderas domésticas (*Elo, Hipercard*) carecen de habilitación internacional multidivisa. Al intentar procesar en MXN/USD en terminales mexicanas, el clearing falla.
2. **Cultura de Pagos Instantáneos (Pix) y Parcelas:**
   * El 85%+ de los usuarios bancarizados operan vía Pix. Forzarlos al plástico tradicional resulta en fricción, límites insuficientes en crédito o abandono total de la transacción ([Mexico Business News](https://mexicobusiness.news/finance/news/instant-payments-reshape-latam-banking-competition-study)).

---

### 🇵🇪 Perú (Rechazo: 35% - 40%)
1. **Dependencia Extrema del Débito:**
   * La penetración de tarjetas de crédito es de apenas ~11% ([Trustonic LatAm Study](https://www.trustonic.com/la-es/opinion/disminuye-tarjetas-credito-latam/)). Las transacciones de débito rebotan por fluctuación cambiaria inmediata (USD/MXN a PEN) o falta de saldo líquido.
2. **Fricción de Autenticación 3D Secure (3DS):**
   * Los emisores peruanos exigen 3DS obligatorio. Si el comercio mexicano no tiene activado el protocolo 3DS v2, la transacción es cancelada automáticamente.

---

## 4. Implicación Estratégica para el Proyecto Riviera Maya SmartPay

| Enfoque Tradicional (Ej. Clip / Bancos TPVs) | Enfoque SmartPay (APMs / Local-to-Local / QR) |
| :--- | :--- |
| **Pérdida del 30% al 50% de las ventas** de visitantes de LATAM por rechazo emisor. | **Tasa de aprobación >99%** al procesar vía rieles locales (Pix, PSE, Yape/Plin, Stablecoins). |
| **Cero trazabilidad:** El comercio no sabe por qué la tarjeta no pasó y asume que el cliente no tiene fondos. | **Confirmación biométrica instantánea:** El cliente autoriza en su propia app bancaria. |
| **Riesgo de fraude y contracargos** asumido por el comercio o pasarela. | **Cero riesgo de contracargo (*Zero Chargebacks*)** y liquidación garantizada. |
| **CAC elevado:** Obligación de vender hardware físico TPV. | **Zero-Hardware:** Despliegue inmediato vía código QR impreso o en pantalla. |
