import os
import sys
import shutil
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        width, height = landscape(A4)
        
        # Executive Dark Navy Left Panel
        rail_width = 220
        self.setFillColor(colors.HexColor('#0F172A'))
        self.rect(0, 0, rail_width, height, fill=True, stroke=False)
        
        # Blue Accent Line
        self.setFillColor(colors.HexColor('#2563EB'))
        self.rect(rail_width, 0, 3, height, fill=True, stroke=False)
        
        # Left Panel Branding
        self.setFillColor(colors.HexColor('#94A3B8'))
        self.setFont("Helvetica-Bold", 9)
        self.drawString(28, height - 45, "FETUR · SECTUR QROO")
        
        self.setFillColor(colors.HexColor('#FFFFFF'))
        self.setFont("Helvetica-Bold", 15)
        self.drawString(28, height - 85, "CARIBE MEXICANO")
        self.setFillColor(colors.HexColor('#93C5FD'))
        self.drawString(28, height - 105, "SMART PAY")
        
        self.setFillColor(colors.HexColor('#94A3B8'))
        self.setFont("Helvetica", 8.5)
        self.drawString(28, height - 130, "Infraestructura LATAM (PIX/Nequi/Yape)")
        
        # Author bottom left
        self.setFillColor(colors.HexColor('#FFFFFF'))
        self.setFont("Helvetica-Bold", 9.5)
        self.drawString(28, 55, "Antonio Gutiérrez")
        self.setFillColor(colors.HexColor('#94A3B8'))
        self.setFont("Helvetica", 8.5)
        self.drawString(28, 40, "Comisión Innovación (FETUR)")
        
        # Footer
        self.setFillColor(colors.HexColor('#475569'))
        self.setFont("Helvetica", 8.5)
        self.drawString(245, 18, "DOCUMENTO EJECUTIVO DE ESTRATEGIA Y FINANZAS — CONFIDENCIAL")
        self.drawRightString(width - 25, 18, f"Diapositiva {self._pageNumber} de {page_count}")


def generate_pdf():
    onedrive_path = r"C:\Users\Antonio\OneDrive\Downloads"
    pdf_filename_corp = "PRESENTACION_EJECUTIVA_CORPORATIVA.pdf"
    target_pdf = os.path.join(onedrive_path, pdf_filename_corp)
    
    doc = SimpleDocTemplate(
        target_pdf,
        pagesize=landscape(A4),
        leftMargin=245,
        rightMargin=25,
        topMargin=32,
        bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'SlideTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=17,
        leading=21,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=12
    )
    
    tag_style = ParagraphStyle(
        'SlideTag',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10,
        textColor=colors.HexColor('#475569'),
        spaceAfter=4
    )
    
    card_label_style = ParagraphStyle(
        'CardLabel',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=4
    )
    
    card_desc_style = ParagraphStyle(
        'CardDesc',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#334155')
    )

    source_style = ParagraphStyle(
        'SourceDesc',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#475569')
    )

    story = []
    
    # ------------------ SLIDE 1: DERRAMA ECONÓMICA ------------------
    story.append(Paragraph("01 · CONTEXTO DE MERCADO Y DERRAMA ECONÓMICA", tag_style))
    story.append(Paragraph("Quintana Roo lidera la recepción de turismo sudamericano en México con una derrama en sitio de $1,113 Millones de Dólares", title_style))
    
    data_s1 = [
        [
            Paragraph("<b>380,000 Turistas</b><br/><font color='#1E3A8A'><b>🇨🇴 Colombia</b></font>", card_label_style),
            Paragraph("<b>160,000 Turistas</b><br/><font color='#0D9488'><b>🇦🇷 Argentina</b></font>", card_label_style)
        ],
        [
            Paragraph("Gasto en sitio: <b>$1,039.55 USD/estancia</b>.<br/>Derrama total: <b>$395.0M USD</b>.", card_desc_style),
            Paragraph("Gasto en sitio: <b>$1,125.75 USD/estancia</b>.<br/>Derrama total: <b>$180.1M USD</b>.", card_desc_style)
        ],
        [
            Paragraph("<b>150,000 Turistas</b><br/><font color='#312E81'><b>🇧🇷 Brasil</b></font>", card_label_style),
            Paragraph("<b>135,000 Turistas</b><br/><font color='#B45309'><b>🇵🇪 Perú</b></font>", card_label_style)
        ],
        [
            Paragraph("Gasto en sitio: <b>$1,209.00 USD/estancia</b>.<br/>Derrama total: <b>$181.35M USD</b>.", card_desc_style),
            Paragraph("Gasto en sitio: <b>$980.00 USD/estancia</b>.<br/>Derrama total: <b>$132.3M USD</b>.", card_desc_style)
        ]
    ]
    
    t1 = Table(data_s1, colWidths=[260, 260])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFFFF')),
        ('BOX', (0,0), (0,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,0), (1,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (0,2), (0,3), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,2), (1,3), 1, colors.HexColor('#E2E8F0')),
        ('LINEABOVE', (0,0), (0,0), 3, colors.HexColor('#1E3A8A')),
        ('LINEABOVE', (1,0), (1,0), 3, colors.HexColor('#0D9488')),
        ('LINEABOVE', (0,2), (0,2), 3, colors.HexColor('#312E81')),
        ('LINEABOVE', (1,2), (1,2), 3, colors.HexColor('#B45309')),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('BOTTOMPADDING', (0,2), (-1,2), 2),
    ]))
    
    story.append(t1)
    story.append(Spacer(1, 15))
    story.append(Paragraph("📌 <b>FUENTES OFICIALES CORROBORABLES:</b> DATATUR (Secretaría de Turismo de México) · SECTUR Quintana Roo · 8B World PTE (Market Report 2025) · Statista Oct 2024.", source_style))
    story.append(PageBreak())

    # ------------------ SLIDE 2: ADOPCIÓN DE QR Y BANCOS CENTRALES ------------------
    story.append(Paragraph("02 · ADOPCIÓN DE QR Y REGULACIÓN DE BANCOS CENTRALES", tag_style))
    story.append(Paragraph("El 65% de los turistas sudamericanos no usa tarjeta bancaria en el exterior por impuestos y comisiones bancarias", title_style))
    
    data_qr_banks = [
        [
            Paragraph("<b>155 Millones Users</b><br/><font color='#1E3A8A'><b>🇧🇷 Brasil · Banco Central (BCB)</b></font>", card_label_style),
            Paragraph("<b>31% e-Wallets</b><br/><font color='#0D9488'><b>🇦🇷 Argentina · AFIP & BCRA</b></font>", card_label_style)
        ],
        [
            Paragraph("Red <b>PIX del Banco Central do Brasil</b> (155M usuarios activos).<br/>El 85% de brasileños paga con QR para eludir el <b>3.5% de Impuesto IOF</b> que les cobra su gobierno. Proyección 2029: <b>$862.5B USD (CAGR 28.9%)</b>.", card_desc_style),
            Paragraph("Red de <b>eWallets CBU/CVU</b> (31% adopción eWallets, 10% transferencias).<br/>Evitan tarjeta de crédito para eludir el <b>15% al 25% AFIP</b> ('Dólar Tarjeta'). Proyección 2028: <b>$140.8B USD (CAGR 15.9%)</b>.", card_desc_style)
        ],
        [
            Paragraph("<b>&gt;40M Txs / Día</b><br/><font color='#312E81'><b>🇵🇪 Perú · Banco Central (BCRP)</b></font>", card_label_style),
            Paragraph("<b>&gt;78% Adultos</b><br/><font color='#B45309'><b>🇨🇴 Colombia · SFC</b></font>", card_label_style)
        ],
        [
            Paragraph("Interoperabilidad obligatoria <b>Yape & Plin</b>.<br/>El 68% no usa tarjeta de crédito en el extranjero por temor a altas tasas de interés y prefieren pago por QR.", card_desc_style),
            Paragraph("Red <b>Nequi & DaviPlata</b> (Superfinanciera SFC).<br/>Prevalencia masiva de pagos digitales mediante llaves QR de transferencia instantánea sin costo.", card_desc_style)
        ]
    ]
    
    t_qr = Table(data_qr_banks, colWidths=[260, 260])
    t_qr.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFFFF')),
        ('BOX', (0,0), (0,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,0), (1,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (0,2), (0,3), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,2), (1,3), 1, colors.HexColor('#E2E8F0')),
        ('LINEABOVE', (0,0), (0,0), 3, colors.HexColor('#1E3A8A')),
        ('LINEABOVE', (1,0), (1,0), 3, colors.HexColor('#0D9488')),
        ('LINEABOVE', (0,2), (0,2), 3, colors.HexColor('#312E81')),
        ('LINEABOVE', (1,2), (1,2), 3, colors.HexColor('#B45309')),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('BOTTOMPADDING', (0,2), (-1,2), 2),
    ]))
    
    story.append(t_qr)
    story.append(Spacer(1, 15))
    story.append(Paragraph("📌 <b>FUENTES REGULATORIAS & CONSULTORÍA:</b> Banco Central do Brasil (BCB) · AFIP Argentina · 8B World PTE (LPM Adoption Report 2025) · Statista (Oct 2024).", source_style))
    story.append(PageBreak())

    # ------------------ SLIDE 3: TAM / SAM / SOM DESGLOSADO ------------------
    story.append(Paragraph("03 · MODELO FINANCIERO TAM / SAM / SOM DESGLOSADO", tag_style))
    story.append(Paragraph("Desglose del Mercado Total (TAM $1,113M USD), Atendible (SAM $350.6M USD) y Captación Piso (SOM $3.5M USD)", title_style))
    
    data_tam_sam_som = [
        [
            Paragraph("<b>DESGLOSE POR PAÍS DE ORIGEN</b>", card_label_style),
            Paragraph("<b>TAM (Gasto Sitio)</b>", card_label_style),
            Paragraph("<b>SAM (31.5% Dig.)</b>", card_label_style),
            Paragraph("<b>SOM (Piso 1%)</b>", card_label_style)
        ],
        [
            Paragraph("🇨🇴 <b>Colombia (380k Turistas)</b>", card_desc_style),
            Paragraph("$395.00 M USD", card_desc_style),
            Paragraph("$124.40 M USD", card_desc_style),
            Paragraph("<b>$1,244,000 USD</b>", card_desc_style)
        ],
        [
            Paragraph("🇧🇷 <b>Brasil (150k Turistas)</b>", card_desc_style),
            Paragraph("$181.35 M USD", card_desc_style),
            Paragraph("$57.12 M USD", card_desc_style),
            Paragraph("<b>$571,200 USD</b>", card_desc_style)
        ],
        [
            Paragraph("🇦🇷 <b>Argentina (160k Turistas)</b>", card_desc_style),
            Paragraph("$180.12 M USD", card_desc_style),
            Paragraph("$56.74 M USD", card_desc_style),
            Paragraph("<b>$567,400 USD</b>", card_desc_style)
        ],
        [
            Paragraph("🇵🇪 <b>Perú (135k Turistas)</b>", card_desc_style),
            Paragraph("$132.30 M USD", card_desc_style),
            Paragraph("$41.67 M USD", card_desc_style),
            Paragraph("<b>$416,700 USD</b>", card_desc_style)
        ],
        [
            Paragraph("🌎 <b>Otros LATAM (Chile/Uruguay/etc)</b>", card_desc_style),
            Paragraph("$224.43 M USD", card_desc_style),
            Paragraph("$70.67 M USD", card_desc_style),
            Paragraph("<b>$706,700 USD</b>", card_desc_style)
        ],
        [
            Paragraph("<b>TOTAL QUINTANA ROO</b>", card_label_style),
            Paragraph("<b>$1,113.20 M USD</b>", card_label_style),
            Paragraph("<b>$350.60 M USD</b>", card_label_style),
            Paragraph("<b>$3,506,000 USD</b>", card_label_style)
        ]
    ]
    
    t_tss = Table(data_tam_sam_som, colWidths=[180, 110, 110, 120])
    t_tss.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#FFFFFF')),
        ('BACKGROUND', (0,1), (-1,-2), colors.HexColor('#FFFFFF')),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#E2E8F0')),
        ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    
    story.append(t_tss)
    story.append(Spacer(1, 12))
    story.append(Paragraph("📌 <b>DESGLOSE POR MUNICIPIO EN QROO (SOM PISO $3.5M USD):</b> Cancún/Benito Juárez: <b>$1.23M USD (40 txs/día)</b> · Playa del Carmen/Solidaridad: <b>$1.05M USD (35 txs/día)</b> · Tulum: <b>$0.77M USD (25 txs/día)</b> · Cozumel/Isla Mujeres: <b>$0.45M USD (13 txs/día)</b>.", source_style))
    story.append(PageBreak())

    # ------------------ SLIDE 4: TEMPORALIDADES ------------------
    story.append(Paragraph("04 · TEMPORALIDADES DE VIAJE Y CONTRA-CICLO ESTACIONAL", tag_style))
    story.append(Paragraph("El turismo sudamericano genera picos de afluencia durante la temporada baja norteamericana (Junio a Agosto)", title_style))
    
    data_s2_season = [
        [
            Paragraph("<b>🇨🇴 Colombia (380k Turistas)</b><br/><font color='#1E3A8A'><b>Junio - Julio & Octubre</b></font>", card_label_style),
            Paragraph("<b>🇧🇷 Brasil (150k Turistas)</b><br/><font color='#312E81'><b>Julio, Diciembre & Feb/Mar</b></font>", card_label_style)
        ],
        [
            Paragraph("• Vacaciones de mitad de año (Junio/Julio).<br/>• Semana de Receso escolar (Octubre).<br/>• Fiestas de fin de año (Diciembre/Enero).", card_desc_style),
            Paragraph("• Vacaciones de invierno austral (Julio).<br/>• Fiestas y verano del hemisferio sur (Dic/Ene).<br/>• Semana de Carnaval (Febrero/Marzo).", card_desc_style)
        ],
        [
            Paragraph("<b>🇦🇷 Argentina (160k Turistas)</b><br/><font color='#0D9488'><b>Enero - Febrero & Julio</b></font>", card_label_style),
            Paragraph("<b>🇵🇪 Perú (135k Turistas)</b><br/><font color='#B45309'><b>Julio - Agosto & Enero/Feb</b></font>", card_label_style)
        ],
        [
            Paragraph("• Verano austral principal (Enero/Febrero).<br/>• Receso escolar de invierno (Julio).<br/>• Escapadas de fin de año (Nov/Dic).", card_desc_style),
            Paragraph("• Fiestas Patrias peruanas (28-29 de Julio).<br/>• Vacaciones escolares de invierno (Julio/Ago).<br/>• Receso de verano (Enero/Febrero).", card_desc_style)
        ]
    ]
    
    t_season = Table(data_s2_season, colWidths=[260, 260])
    t_season.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFFFF')),
        ('BOX', (0,0), (0,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,0), (1,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (0,2), (0,3), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,2), (1,3), 1, colors.HexColor('#E2E8F0')),
        ('LINEABOVE', (0,0), (0,0), 3, colors.HexColor('#1E3A8A')),
        ('LINEABOVE', (1,0), (1,0), 3, colors.HexColor('#312E81')),
        ('LINEABOVE', (0,2), (0,2), 3, colors.HexColor('#0D9488')),
        ('LINEABOVE', (1,2), (1,2), 3, colors.HexColor('#B45309')),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('BOTTOMPADDING', (0,2), (-1,2), 2),
    ]))
    
    story.append(t_season)
    story.append(Spacer(1, 15))
    story.append(Paragraph("📌 <b>IMPACTO ESTRATÉGICO DE ESTACIONALIDAD:</b> Mientras el flujo de EE.UU. cae entre Mayo y Agosto, los 4 mercados sudamericanos tienen sus picos máximos de vacaciones familiares en Junio, Julio y Agosto, equilibrando la ocupación hotelera de Quintana Roo.", source_style))
    story.append(PageBreak())

    # ------------------ SLIDE 5: DIAGRAMA DE FLUJO DE PAGO EN 6 PASOS ------------------
    story.append(Paragraph("05 · ARQUITECTURA Y DIAGRAMA DE TRANSACCIÓN EN 6 PASOS", tag_style))
    story.append(Paragraph("Diagrama de Pago QR: Transacción iniciada en sitio por el comercio y procesada en &lt;3 segundos vía SPEI", title_style))
    
    data_diagram_flow = [
        [
            Paragraph("<b>PASO 1: COMERCIO (QROO)</b>", card_label_style),
            Paragraph("<b>PASO 2: TURISTA LATAM</b>", card_label_style),
            Paragraph("<b>PASO 3: SMART HUB (FETUR)</b>", card_label_style)
        ],
        [
            Paragraph("Muestra el <b>QR de Mostrador/Mesa</b> (Dinámico con monto o Estático de caja).", card_desc_style),
            Paragraph("Escanea el QR usando su <b>App Bancaria Nativa</b> (PIX, Nequi, Yape, eWallet).", card_desc_style),
            Paragraph("Enruta a la red bancaria de origen y calcula el tipo de cambio FX instantáneo.", card_desc_style)
        ],
        [
            Paragraph("<b>PASO 6: NOTIFICACIÓN (&lt;3s)</b>", card_label_style),
            Paragraph("<b>PASO 5: BANCO COMERCIO</b>", card_label_style),
            Paragraph("<b>PASO 4: BANCO ORIGEN</b>", card_label_style)
        ],
        [
            Paragraph("Comercio recibe <b>confirmación en &lt;3 seg</b> vía WhatsApp/SMS o ticket impreso.", card_desc_style),
            Paragraph("Acreditación automática en <b>Pesos Mexicanos (MXN)</b> vía SPEI en su cuenta.", card_desc_style),
            Paragraph("Debita automáticamente en la cuenta local del turista (Reales/Pesos Col/Soles).", card_desc_style)
        ]
    ]
    
    t_diag = Table(data_diagram_flow, colWidths=[173, 173, 173])
    t_diag.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFFFF')),
        ('BOX', (0,0), (0,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,0), (1,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (2,0), (2,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (0,2), (0,3), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,2), (1,3), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (2,2), (2,3), 1, colors.HexColor('#E2E8F0')),
        ('LINEABOVE', (0,0), (0,0), 3, colors.HexColor('#1E3A8A')),
        ('LINEABOVE', (1,0), (1,0), 3, colors.HexColor('#0D9488')),
        ('LINEABOVE', (2,0), (2,0), 3, colors.HexColor('#2563EB')),
        ('LINEABOVE', (0,2), (0,2), 3, colors.HexColor('#059669')),
        ('LINEABOVE', (1,2), (1,2), 3, colors.HexColor('#312E81')),
        ('LINEABOVE', (2,2), (2,2), 3, colors.HexColor('#B45309')),
        ('PADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('BOTTOMPADDING', (0,2), (-1,2), 2),
    ]))
    
    story.append(t_diag)
    story.append(Spacer(1, 12))
    story.append(Paragraph("📌 <b>ESTÁNDARES DE ARQUITECTURA:</b> Estándar de Comunicación EMVCo QR Code · Regulación de Pagos Electrónicos Banco de México (SPEI) · Enrutamiento Certificado ISO 8583.", source_style))
    story.append(PageBreak())

    # ------------------ SLIDE 6: MATRIZ DE ESCENARIOS Y SUPUESTOS ------------------
    story.append(Paragraph("06 · MODELO DE ESCENARIOS Y SUPUESTOS DE ADOPCIÓN", tag_style))
    story.append(Paragraph("Análisis de Sensibilidad: El proyecto genera desde $3.1M USD (piso) hasta $23.25M USD en función de la adopción", title_style))
    
    data_scenarios_cards = [
        [
            Paragraph("<b>$3.10M USD</b><br/><font color='#1E3A8A'><b>🟢 Escenario Conservador</b></font>", card_label_style),
            Paragraph("<b>$10.85M USD</b><br/><font color='#0D9488'><b>🔵 Escenario Moderado</b></font>", card_label_style),
            Paragraph("<b>$23.25M USD</b><br/><font color='#312E81'><b>🟣 Escenario Optimista</b></font>", card_label_style)
        ],
        [
            Paragraph("20% Afiliación FETUR (100 Comercios) · 1 cobro/día.", card_desc_style),
            Paragraph("35% Afiliación FETUR (175 Comercios) · 2 cobros/día.", card_desc_style),
            Paragraph("50% Afiliación FETUR (250 Comercios) · 3 cobros/día.", card_desc_style)
        ]
    ]
    t_scen_cards = Table(data_scenarios_cards, colWidths=[173, 173, 173])
    t_scen_cards.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFFFF')),
        ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#E2E8F0')),
        ('LINEABOVE', (0,0), (0,0), 3, colors.HexColor('#1E3A8A')),
        ('LINEABOVE', (1,0), (1,0), 3, colors.HexColor('#0D9488')),
        ('LINEABOVE', (2,0), (2,0), 3, colors.HexColor('#312E81')),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_scen_cards)
    story.append(Spacer(1, 10))

    data_scenarios = [
        [
            Paragraph("<b>Escenario de Adopción</b>", card_label_style),
            Paragraph("<b>% Afiliación (Base 500)</b>", card_label_style),
            Paragraph("<b>Txs / Día / Comercio ($85 Ticket)</b>", card_label_style),
            Paragraph("<b>Txs Diarias Estado</b>", card_label_style),
            Paragraph("<b>Volumen Anual (USD)</b>", card_label_style)
        ],
        [
            Paragraph("🟢 <b>Conservador (Piso 1% SAM)</b>", card_desc_style),
            Paragraph("<b>20% (100 Comercios)</b>", card_desc_style),
            Paragraph("1 cobro / día", card_desc_style),
            Paragraph("100 txs / día", card_desc_style),
            Paragraph("<b>$3,102,500 USD (~$3.1M)</b>", card_desc_style)
        ],
        [
            Paragraph("🔵 <b>Moderado (Base 2.5% SAM)</b>", card_desc_style),
            Paragraph("<b>35% (175 Comercios)</b>", card_desc_style),
            Paragraph("2 cobros / día", card_desc_style),
            Paragraph("350 txs / día", card_desc_style),
            Paragraph("<b>$10,858,750 USD (~$10.8M)</b>", card_desc_style)
        ],
        [
            Paragraph("🟣 <b>Optimista (Escalado 5% SAM)</b>", card_desc_style),
            Paragraph("<b>50% (250 Comercios)</b>", card_desc_style),
            Paragraph("3 cobros / día", card_desc_style),
            Paragraph("750 txs / día", card_desc_style),
            Paragraph("<b>$23,268,750 USD (~$23.2M)</b>", card_desc_style)
        ]
    ]
    
    t_scen = Table(data_scenarios, colWidths=[140, 95, 105, 80, 100])
    t_scen.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#FFFFFF')),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#FFFFFF')),
        ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    
    story.append(t_scen)
    story.append(Spacer(1, 8))
    story.append(Paragraph("📌 <b>SUPUESTOS CLAVE DEL MODELO DE NEGOCIO:</b> Base de 500 comercios de FETUR en Cancún, Playa del Carmen, Tulum y Cozumel · Ticket promedio de $85 USD · Modelo Zero-Device sin costo de infraestructura para el afiliado.", source_style))
    story.append(PageBreak())

    # ------------------ SLIDE 7: PROPUESTA DE FASES DE DESPLIEGUE ------------------
    story.append(Paragraph("07 · PROPUESTA DE FASES Y OPCIONES DE DESPLIEGUE", tag_style))
    story.append(Paragraph("Propuesta de implementación gradual a 45 días para la validación, prueba piloto y lanzamiento oficial", title_style))
    
    data_s5 = [
        [
            Paragraph("<b>Fase 1 (Días 1 - 15)</b><br/><font color='#1E3A8A'><b>Convocatoria & Afiliación Voluntaria</b></font>", card_label_style),
            Paragraph("<b>Fase 2 (Días 16 - 30)</b><br/><font color='#0D9488'><b>Piloto Técnico & Integración Software</b></font>", card_label_style)
        ],
        [
            Paragraph("Presentación de la circular de adhesión a los primeros 100 comercios de mayor afluencia sudamericana.", card_desc_style),
            Paragraph("Despliegue de señalética QR de mostrador y pruebas de integración con el software de caja de los comercios.", card_desc_style)
        ],
        [
            Paragraph("<b>Fase 3 (Días 31 - 45)</b><br/><font color='#312E81'><b>Lanzamiento Institucional Estatal</b></font>", card_label_style),
            Paragraph("<b>Fase 4 (Días 46+)</b><br/><font color='#B45309'><b>Evaluación & Réplica ASETUR</b></font>", card_label_style)
        ],
        [
            Paragraph("Presentación formal ante medios con SECTUR Quintana Roo y la Comisión de Innovación de FETUR.", card_desc_style),
            Paragraph("Revisión del volumen procesado y análisis de expansión a otros polos turísticos (Los Cabos / Puerto Vallarta).", card_desc_style)
        ]
    ]
    
    t5 = Table(data_s5, colWidths=[260, 260])
    t5.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFFFF')),
        ('BOX', (0,0), (0,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,0), (1,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (0,2), (0,3), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,2), (1,3), 1, colors.HexColor('#E2E8F0')),
        ('LINEABOVE', (0,0), (0,0), 3, colors.HexColor('#1E3A8A')),
        ('LINEABOVE', (1,0), (1,0), 3, colors.HexColor('#0D9488')),
        ('LINEABOVE', (0,2), (0,2), 3, colors.HexColor('#312E81')),
        ('LINEABOVE', (1,2), (1,2), 3, colors.HexColor('#B45309')),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('BOTTOMPADDING', (0,2), (-1,2), 2),
    ]))
    
    story.append(t5)
    story.append(Spacer(1, 15))
    story.append(Paragraph("📌 <b>HOJA DE RUTA PROPUESTA:</b> Plan sujeto a retroalimentación y aprobación de la Asamblea Directiva de FETUR y SECTUR Quintana Roo.", source_style))

    # Build PDF
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF Corporativo sobrio con escenarios y espacio optimizado generado en: {target_pdf}")

if __name__ == "__main__":
    generate_pdf()
