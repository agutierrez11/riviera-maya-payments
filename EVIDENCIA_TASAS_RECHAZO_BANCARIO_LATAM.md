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

### C. Falla de Procesamiento Transfronterizo Tradicional (Rapyd, Kushki, EBANX)
* **Offshore vs. Local Acquiring (Rapyd Global Insights):**
  * Las pasarelas de pago offshore/cross-border tradicionales sufren tasas de aprobación de apenas **20% a 45%** (tasas de rechazo de hasta 55%-80%), mientras que la adquirencia local o APMs alcanzan **60% a 80%+** ([Rapyd Decline Rates in LATAM](https://www.rapyd.net/blog/payment-processing-decline-rates-in-latam/)).
  * **Fraude y Falsos Positivos:** El fraude drena casi el **20% de los ingresos de eCommerce en LATAM** (el doble del promedio global). En Brasil, los rechazos por sospecha de fraude alcanzan el **5%** (vs 2.6% global).
  * **Fragmentación de Pasarelas:** En la región operan más de 80 gateways con tasas de autorización sumamente dispares (algunas caen a **16.3%**).

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

## 3. Evidencia Macro: La Muerte del Efectivo vs. El Auge del QR (BCRA / Cámara Argentina Fintech)

Datos oficiales del **Banco Central de la República Argentina (BCRA)** analizados por **Mariano Agustín Giraffa** (Director de Medios de Pago @ Cámara Argentina Fintech):

* **Explosión de Pagos con QR:** **+75.4% interanual en operaciones** (108.2 millones de transacciones) y **+67.4% en volumen real** descontada la inflación ($2.6 billones de pesos).
* **Desplome de Cajeros Automáticos (ATMs):** Las extracciones en efectivo cayeron **-30% interanual**.
* **Comportamiento por Ticket Promedio:**
  * **Extracción en Cajero:** ~$107,000 ARS (baja frecuencia, montos altos por necesidad/emergencia).
  * **Pago con QR:** ~$24,000 ARS (alta frecuencia, micropagos y consumo diario en comercios).
* **Tesis Central de Mercado:**
  > *"Lo que pierde terreno no es la tarjeta frente al QR: es el efectivo frente a todo lo demás."*
* **Infraestructura Interoperable en Escala:** 90 billeteras digitales interoperables, 62 aceptadores de Pagos con Transferencia (PCT) y 219 PSPs registrados.

---

## 4. Desglose de Motivos Técnicos y Macroeconómicos por País

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

## 5. La Fricción en la Cadena B2B Turística y Corporativa (Dasbanq Market Insights)

El problema transfronterizo no solo afecta al turista individual (B2C), sino que paraliza la cadena de suministro B2B entre agencias emisoras en Sudamérica y operadores receptivos/hoteles en México ([Dasbanq Cross-Border Report](https://www.linkedin.com/company/dasbanq/)):

* **77% de las empresas en LATAM** reportan pagos internacionales demorados o bloqueados (frente al 51% previo).
* **Términos de pago extendidos:** El promedio de liquidación regional subió a **59 días**, con **retrasos promedio de 42 días** en el clearing bancario tradicional.
* **Términos más largos por país:** Brasil enfrenta los plazos de liquidación transfronteriza más largos de la región (**66 días promedio**).
* **Crisis de Liquidez de Divisas:** En mercados como Bolivia y Argentina, los bancos comerciales rechazan transferencias en USD sin explicación debido a la escasez de reservas, dejando a agencias de viaje y mayoristas imposibilitados para prepagar hoteles o tours en México mediante SWIFT tradicional.
* **Mercado Objetivo:** Mientras el mercado de pagos digitales en LATAM supera los **$300 mil millones de USD para 2027**, la infraestructura bancaria tradicional sigue operando con tecnologías heredadas lentas y costosas.

---

## 6. El Paradigma FinTech 2026: "Poliamor Financiero", Biometría Multimodal y Stablecoins (Bianca Prieto / Tech Lawyer Analysis)

La evolución de los medios de pago en 2026 marca el fin definitivo de la hegemonía del plástico físico y la terminal TPV rígida, dando paso a tres pilares estructurales:

### A. "Poliamor Financiero" y Diversidad de Rieles
* El consumidor y turista moderno no depende de un solo plástico bancario; exige coexistencia de **Billeteras Digitales (>60% penetración global)**, **Pagos Instantáneos A2A (Pix, SPEI, Transferencias 3.0)**, **Stablecoins respaldadas (USDC de Circle, Paxos)** y tarjetas tokenizadas.
* Forzar a un turista a pagar exclusivamente con tarjeta física deslizada en una terminal genera fricción inmediata y abandono.

### B. Biometría Multimodal y Passkeys (Visa / Mastercard Standards)
* La autenticación ha migrado hacia el estándar de **Visa Payment Passkey** y biometría multimodal (*FaceID, huella, liveness detection, comportamiento*).
* **Impacto en Aprobación:** Al validar biométricamente en el dispositivo del usuario, se eliminan los falsos positivos por sospecha de fraude y se neutraliza el miedo del turista a la clonación física (*skimming*) en destinos turísticos.

### C. Convergencia FinTech + Stablecoins Reguladas
* Integración de rieles *on-chain* (USDC, protocolos cross-chain) con autenticación biométrica *off-chain*: transferencias transfronterizas instantáneas, de bajo costo y con liquidación inmediata en moneda local (MXN) para los comercios receptores.

---

## 7. Cuadro Comparativo: El Modelo TPV Tradicional (Clip) vs. Ecosistema SmartPay 2026

| Dimensión | Modelo TPV Tradicional (Clip / Adquirentes Legacy) | Ecosistema SmartPay Riviera Maya (2026) |
| :--- | :--- | :--- |
| **Arquitectura de Pago** | Monolítica: Tarjeta física + PIN / Chip en hardware propietario. | **Multimodal / "Poliamor Financiero":** QR dinámico, Pix, APMs, Stablecoins (USDC), Passkeys. |
| **Tasa de Rechazo Turística** | **30% al 50% de rechazos** en plásticos de LATAM por filtros emisores. | **>99% de aprobación** mediante autorización biométrica y rieles locales. |
| **Costo y Tiempo de Despliegue** | **Alto CAC:** Venta, subsidio y logística de hardware físico ($500-$1,500 MXN/TPV). | **Zero-Hardware:** Despliegue en 2 minutos vía software, pantalla o QR impreso. |
| **Seguridad para el Turista** | Fricción y desconfianza por riesgo de clonación/estafas en destino. | **Zero-Trust / Biometría Nativa:** El turista jamás suelta su tarjeta ni datos bancarios. |
| **Liquidación B2B** | **42 a 66 días** en transferencias bancarias internacionales (SWIFT). | **Liquidación instantánea** (minutos) entre agencias, DMCs y hoteles. |
---

## 8. Directorio de Fuentes Oficiales y Enlaces Verificados

### A. Impacto Económico de Pix y Recuperación de Ingresos (+37%)
1. **EBANX / GlobeNewswire:** [*Adding Pix lifts global merchant revenue by up to 37% in Brazil*](https://www.globenewswire.com/news-release/2024/08/07/2926122/0/en/Adding-Pix-lifts-global-merchant-revenue-by-up-to-37-in-Brazil-reveals-new-EBANX-data.html)
2. **EBANX Beyond Borders Report:** [*Global Hub de Pagos Transfronterizos en LATAM*](https://www.ebanx.com/en/beyond-borders/)
3. **EBANX Press Room:** [*Stripe users can now accept Pix via EBANX*](https://business.ebanx.com/en/press-room/press-releases/stripe-users-can-now-accept-pix-in-brazil-via-ebanx)
4. **Emerald Insight:** [*Fast payment, credit and bank diversification: the impact of Pix*](https://www.emerald.com/insight/content/doi/10.1108/RAUSP-07-2023-0130/full/html)

### B. Casos Reales de Pix en Turismo Internacional Fuera de Brasil
1. **kamiPay Argentina:** [*Solución de Cobro con Pix en Turismo y Comercios en Argentina*](https://kamipay.io/es/cobrar-pix-argentina/)
2. **Mercado Pago:** [*Cobro a Turistas Brasileños con QR Pix en Terminales Point*](https://www.mercadolibre.com.ar/ayuda/point-cobrar-con-qr-pix_30628)
3. **Rapyd Blog:** [*What is Pix and How Does it Work for Global Merchants*](https://www.rapyd.net/blog/what-is-pix/)

### C. Benchmarks de Rechazos Bancarios y Fricción Transfronteriza
1. **Rapyd:** [*Why Payment Processing Decline Rates Are So High in LATAM*](https://www.rapyd.net/blog/payment-processing-decline-rates-in-latam/)
2. **PayRetailers:** [*Cross-Border Payments in Latin America: Complete Guide 2026*](https://www.payretailers.com/en/blog/cross-border-payments-in-latin-america-a-complete-guide-for-merchants-2026)
3. **Yuno Payments:** [*Análisis de Declinaciones y Rechazos en Pasarelas LATAM*](https://y.uno/es/blog/payment-declines)
4. **Kushki / Milenio:** [*Políticas de autorización y fallas en rechazos bancarios e-commerce*](https://www.milenio.com/negocios/politicas-autorizacion-fallas-rechazos-bancarios-e-commerce)

### D. Pérdidas en Turismo y Estadísticas Oficiales
1. **Nuvei / Consumotic:** [*Sector turismo enfrentaría pérdidas de $117B por rechazo de tarjetas*](https://consumotic.mx/ecommerce/medios_de_pago/sector-turismo-enfrentaria-perdidas-millonarias-por-rechazo-de-tarjetas-de-credito/)
2. **CONDUSEF México:** [*Estadísticas de Compras y Rechazos en Comercio Electrónico*](https://www.condusef.gob.mx/?p=estadisticas)
3. **Banco Central do Brasil:** [*Portal Oficial y Datos de Operación de Pix*](https://www.bcb.gov.br/estabilidadefinanceira/pix)
4. **Cámara Argentina Fintech:** [*Informe de Pagos Minoristas del BCRA*](https://www.linkedin.com/company/camara-argentina-de-fintech/)
5. **Trustonic:** [*Disminución de penetración de tarjetas de crédito y auge de APMs en LATAM*](https://www.trustonic.com/la-es/opinion/disminuye-tarjetas-credito-latam/)
6. **Mexico Business News:** [*Instant Payments Reshape LATAM Banking Competition*](https://mexicobusiness.news/finance/news/instant-payments-reshape-latam-banking-competition-study)
