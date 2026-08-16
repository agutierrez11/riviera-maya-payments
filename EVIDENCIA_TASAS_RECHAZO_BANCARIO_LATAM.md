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

## 6. Implicación Estratégica para el Proyecto Riviera Maya SmartPay

| Enfoque Tradicional (Ej. Clip / Bancos TPVs / SWIFT) | Enfoque SmartPay (APMs / Local-to-Local / Stablecoins / QR) |
| :--- | :--- |
| **Pérdida del 30% al 50% de las ventas B2C** de visitantes de LATAM por rechazo emisor. | **Tasa de aprobación >99%** al procesar vía rieles locales (Pix, PSE, Yape/Plin, Stablecoins). |
| **42 a 66 días de retraso** en pagos B2B entre agencias mayoristas de LATAM y hoteles/DMCs en México. | **Liquidación B2B en minutos** vía rieles directos / stablecoins, eliminando el riesgo cambiario. |
| **Cero trazabilidad:** El comercio no sabe por qué la tarjeta no pasó y asume que el cliente no tiene fondos. | **Confirmación biométrica instantánea:** El cliente autoriza en su propia app bancaria. |
| **Riesgo de fraude y contracargos** asumido por el comercio o pasarela. | **Cero riesgo de contracargo (*Zero Chargebacks*)** y liquidación garantizada. |
| **CAC elevado:** Obligación de vender hardware físico TPV. | **Zero-Hardware:** Despliegue inmediato vía código QR impreso o en pantalla. |
