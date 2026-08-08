import os
import sys
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
        
        # Draw Navy Chrome Left Rail
        rail_width = 220
        self.setFillColor(colors.HexColor('#1F2A44'))
        self.rect(0, 0, rail_width, height, fill=True, stroke=False)
        
        # Draw Accent Green Line
        self.setFillColor(colors.HexColor('#00E676'))
        self.rect(rail_width, 0, 6, height, fill=True, stroke=False)
        
        # Draw Rail Branding Text
        self.setFillColor(colors.HexColor('#00E676'))
        self.setFont("Helvetica-Bold", 10)
        self.drawString(30, height - 50, "FETUR · SECTUR QROO")
        
        self.setFillColor(colors.HexColor('#FFFFFF'))
        self.setFont("Helvetica-Bold", 16)
        self.drawString(30, height - 90, "CARIBE MEXICANO")
        self.drawString(30, height - 110, "SMART PAY")
        
        self.setFillColor(colors.HexColor('#94A3B8'))
        self.setFont("Helvetica", 9)
        self.drawString(30, height - 135, "Infraestructura LATAM (PIX/Nequi/Yape)")
        
        # Author info bottom left
        self.setFillColor(colors.HexColor('#FFFFFF'))
        self.setFont("Helvetica-Bold", 10)
        self.drawString(30, 60, "Antonio Gutiérrez")
        self.setFillColor(colors.HexColor('#94A3B8'))
        self.setFont("Helvetica", 9)
        self.drawString(30, 45, "Comisión Innovación (FETUR)")
        
        # Footer page counter & confidential mark
        self.setFillColor(colors.HexColor('#64748B'))
        self.setFont("Helvetica", 9)
        self.drawString(245, 20, "DOCUMENTO EJECUTIVO DE ESTRATEGIA Y FINANZAS")
        self.drawRightString(width - 30, 20, f"Diapositiva {self._pageNumber} de {page_count}")


def generate_pdf():
    downloads_path = r"C:\Users\Antonio\Downloads"
    onedrive_path = r"C:\Users\Antonio\OneDrive\Downloads"
    pdf_filename = "CARIBE_MEXICANO_SMART_PAY_PRESENTACION_EJECUTIVA.pdf"
    alt_pdf_filename = "CARIBE_MEXICANO_SMART_PAY_PRESENTACION_EJECUTIVA_7SLIDES.pdf"
    
    target_pdf = os.path.join(downloads_path, pdf_filename)
    alt_pdf = os.path.join(downloads_path, alt_pdf_filename)
    
    # Try creating doc with target_pdf or alt_pdf if locked
    chosen_target = target_pdf
    try:
        # test lock
        if os.path.exists(target_pdf):
            with open(target_pdf, 'a'):
                pass
    except IOError:
        chosen_target = alt_pdf

    doc = SimpleDocTemplate(
        chosen_target,
        pagesize=landscape(A4),
        leftMargin=245,
        rightMargin=30,
        topMargin=35,
        bottomMargin=45
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'SlideTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#1F2A44'),
        spaceAfter=10
    )
    
    tag_style = ParagraphStyle(
        'SlideTag',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.HexColor('#00C853'),
        spaceAfter=4
    )
    
    card_label_style = ParagraphStyle(
        'CardLabel',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=4
    )
    
    card_desc_style = ParagraphStyle(
        'CardDesc',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#334155')
    )

    source_style = ParagraphStyle(
        'SourceDesc',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#0F172A')
    )

    story = []
    
    # ------------------ SLIDE 1: DERRAMA ECONÓMICA ------------------
    story.append(Paragraph("01 · CONTEXTO DE MERCADO Y DERRAMA ECONÓMICA", tag_style))
    story.append(Paragraph("Quintana Roo lidera la recepción de turismo sudamericano en México con una derrama en sitio de $1,113 Millones de Dólares", title_style))
    
    data_s1 = [
        [
            Paragraph("<b>380,000 Turistas</b><br/><font color='#00C853'><b>🇨🇴 Colombia</b></font>", card_label_style),
            Paragraph("<b>160,000 Turistas</b><br/><font color='#00E5FF'><b>🇦🇷 Argentina</b></font>", card_label_style)
        ],
        [
            Paragraph("Gasto en sitio: <b>$1,039.55 USD/estancia</b>.<br/>Derrama total: <b>$395.0M USD</b>.", card_desc_style),
            Paragraph("Gasto en sitio: <b>$1,125.75 USD/estancia</b>.<br/>Derrama total: <b>$180.1M USD</b>.", card_desc_style)
        ],
        [
            Paragraph("<b>150,000 Turistas</b><br/><font color='#A855F7'><b>🇧🇷 Brasil</b></font>", card_label_style),
            Paragraph("<b>135,000 Turistas</b><br/><font color='#FF9100'><b>🇵🇪 Perú</b></font>", card_label_style)
        ],
        [
            Paragraph("Gasto en sitio: <b>$1,209.00 USD/estancia</b>.<br/>Derrama total: <b>$181.35M USD</b>.", card_desc_style),
            Paragraph("Gasto en sitio: <b>$980.00 USD/estancia</b>.<br/>Derrama total: <b>$132.3M USD</b>.", card_desc_style)
        ]
    ]
    
    t1 = Table(data_s1, colWidths=[260, 260])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (0,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,0), (1,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (0,2), (0,3), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,2), (1,3), 1, colors.HexColor('#E2E8F0')),
        ('LINELEFT', (0,0), (0,1), 4, colors.HexColor('#00C853')),
        ('LINELEFT', (1,0), (1,1), 4, colors.HexColor('#00E5FF')),
        ('LINELEFT', (0,2), (0,3), 4, colors.HexColor('#A855F7')),
        ('LINELEFT', (1,2), (1,3), 4, colors.HexColor('#FF9100')),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('BOTTOMPADDING', (0,2), (-1,2), 2),
    ]))
    
    story.append(t1)
    story.append(Spacer(1, 10))
    story.append(Paragraph("📌 <b>FUENTES OFICIALES CORROBORABLES:</b> DATATUR (Secretaría de Turismo de México) · SECTUR Quintana Roo (Reporte Anual de Turismo Receptivo) · CNET.", source_style))
    story.append(PageBreak())

    # ------------------ SLIDE 2: ADOPCIÓN DE QR Y BANCOS CENTRALES ------------------
    story.append(Paragraph("02 · ADOPCIÓN DE QR Y REGULACIÓN DE BANCOS CENTRALES", tag_style))
    story.append(Paragraph("El 65% de los turistas sudamericanos no usa tarjeta bancaria en el exterior por impuestos y comisiones bancarias", title_style))
    
    data_qr_banks = [
        [
            Paragraph("<b>&gt;65,000M Txs</b><br/><font color='#00C853'><b>🇧🇷 Brasil · Banco Central (BCB)</b></font>", card_label_style),
            Paragraph("<b>62% Adopción</b><br/><font color='#00E5FF'><b>🇦🇷 Argentina · AFIP & BCRA</b></font>", card_label_style)
        ],
        [
            Paragraph("Red <b>PIX del Banco Central do Brasil</b>.<br/>El 85% de brasileños paga con QR para eludir el <b>3.5% de Impuesto IOF</b> que les cobra su gobierno al usar tarjeta en México.", card_desc_style),
            Paragraph("Red de <b>eWallets CBU/CVU</b>.<br/>Los argentinos evitan la tarjeta de crédito para eludir el <b>15% al 25% de recargo impositivo AFIP</b> ('Dólar Tarjeta').", card_desc_style)
        ],
        [
            Paragraph("<b>&gt;40M Txs / Día</b><br/><font color='#A855F7'><b>🇵🇪 Perú · Banco Central (BCRP)</b></font>", card_label_style),
            Paragraph("<b>&gt;78% Adultos</b><br/><font color='#FF9100'><b>🇨🇴 Colombia · SFC</b></font>", card_label_style)
        ],
        [
            Paragraph("Interoperabilidad obligatoria <b>Yape & Plin</b>.<br/>El 68% no usa tarjeta de crédito en el extranjero por temor a altas tasas de interés y prefieren pago por QR.", card_desc_style),
            Paragraph("Red <b>Nequi & DaviPlata</b> (Superfinanciera SFC).<br/>Prevalencia masiva de pagos digitales mediante llaves QR de transferencia instantánea sin costo.", card_desc_style)
        ]
    ]
    
    t_qr = Table(data_qr_banks, colWidths=[260, 260])
    t_qr.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (0,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,0), (1,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (0,2), (0,3), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,2), (1,3), 1, colors.HexColor('#E2E8F0')),
        ('LINELEFT', (0,0), (0,1), 4, colors.HexColor('#00C853')),
        ('LINELEFT', (1,0), (1,1), 4, colors.HexColor('#00E5FF')),
        ('LINELEFT', (0,2), (0,3), 4, colors.HexColor('#A855F7')),
        ('LINELEFT', (1,2), (1,3), 4, colors.HexColor('#FF9100')),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('BOTTOMPADDING', (0,2), (-1,2), 2),
    ]))
    
    story.append(t_qr)
    story.append(Spacer(1, 10))
    story.append(Paragraph("📌 <b>FUENTES OFICIALES REGULATORIAS:</b> Banco Central do Brasil (BCB - Informe de Pagamentos Instantâneos PIX) · AFIP Argentina (Resolución General Dólar Tarjeta) · Banco Central de Reserva del Perú (BCRP) · Superintendencia Financiera de Colombia (SFC).", source_style))
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
            Paragraph("<b><font color='#00C853'>$3,506,000 USD</font></b>", card_label_style)
        ]
    ]
    
    t_tss = Table(data_tam_sam_som, colWidths=[180, 110, 110, 120])
    t_tss.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1F2A44')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#FFFFFF')),
        ('BACKGROUND', (0,1), (-1,-2), colors.HexColor('#F8FAFC')),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#E2E8F0')),
        ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    
    story.append(t_tss)
    story.append(Spacer(1, 8))
    story.append(Paragraph("📌 <b>DESGLOSE POR MUNICIPIO EN QROO (SOM PISO $3.5M USD):</b> Cancún/Benito Juárez: <b>$1.23M USD (40 txs/día)</b> · Playa del Carmen/Solidaridad: <b>$1.05M USD (35 txs/día)</b> · Tulum: <b>$0.77M USD (25 txs/día)</b> · Cozumel/Isla Mujeres: <b>$0.45M USD (13 txs/día)</b>.", source_style))
    story.append(PageBreak())

    # ------------------ SLIDE 4: TEMPORALIDADES ------------------
    story.append(Paragraph("04 · TEMPORALIDADES DE VIAJE Y CONTRA-CICLO ESTACIONAL", tag_style))
    story.append(Paragraph("El turismo sudamericano genera picos de afluencia durante la temporada baja norteamericana (Junio a Agosto)", title_style))
    
    data_s2_season = [
        [
            Paragraph("<b>🇨🇴 Colombia (380k Turistas)</b><br/><font color='#00C853'><b>Junio - Julio & Octubre</b></font>", card_label_style),
            Paragraph("<b>🇧🇷 Brasil (150k Turistas)</b><br/><font color='#A855F7'><b>Julio, Diciembre & Feb/Mar</b></font>", card_label_style)
        ],
        [
            Paragraph("• Vacaciones de mitad de año (Junio/Julio).<br/>• Semana de Receso escolar (Octubre).<br/>• Fiestas de fin de año (Diciembre/Enero).", card_desc_style),
            Paragraph("• Vacaciones de invierno austral (Julio).<br/>• Fiestas y verano del hemisferio sur (Dic/Ene).<br/>• Semana de Carnaval (Febrero/Marzo).", card_desc_style)
        ],
        [
            Paragraph("<b>🇦🇷 Argentina (160k Turistas)</b><br/><font color='#00E5FF'><b>Enero - Febrero & Julio</b></font>", card_label_style),
            Paragraph("<b>🇵🇪 Perú (135k Turistas)</b><br/><font color='#FF9100'><b>Julio - Agosto & Enero/Feb</b></font>", card_label_style)
        ],
        [
            Paragraph("• Verano austral principal (Enero/Febrero).<br/>• Receso escolar de invierno (Julio).<br/>• Escapadas de fin de año (Nov/Dic).", card_desc_style),
            Paragraph("• Fiestas Patrias peruanas (28-29 de Julio).<br/>• Vacaciones escolares de invierno (Julio/Ago).<br/>• Receso de verano (Enero/Febrero).", card_desc_style)
        ]
    ]
    
    t_season = Table(data_s2_season, colWidths=[260, 260])
    t_season.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (0,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,0), (1,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (0,2), (0,3), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,2), (1,3), 1, colors.HexColor('#E2E8F0')),
        ('LINELEFT', (0,0), (0,1), 4, colors.HexColor('#00C853')),
        ('LINELEFT', (1,0), (1,1), 4, colors.HexColor('#A855F7')),
        ('LINELEFT', (0,2), (0,3), 4, colors.HexColor('#00E5FF')),
        ('LINELEFT', (1,2), (1,3), 4, colors.HexColor('#FF9100')),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('BOTTOMPADDING', (0,2), (-1,2), 2),
    ]))
    
    story.append(t_season)
    story.append(Spacer(1, 10))
    story.append(Paragraph("📌 <b>IMPACTO ESTRATÉGICO DE ESTACIONALIDAD:</b> Mientras el flujo de EE.UU. cae entre Mayo y Agosto, los 4 mercados sudamericanos tienen sus picos máximos de vacaciones familiares en Junio, Julio y Agosto, equilibrando la ocupación hotelera de Quintana Roo.", source_style))
    story.append(PageBreak())

    # ------------------ SLIDE 5: ARQUITECTURA ZERO-DEVICE ------------------
    story.append(Paragraph("05 · ARQUITECTURA ZERO-DEVICE & ZERO-ERP", tag_style))
    story.append(Paragraph("El modelo elimina la compra de TPVs y se integra directamente al software que los afiliados ya usan", title_style))
    
    data_s3 = [
        [
            Paragraph("<b>1 Solo QR Inteligente</b><br/><font color='#00C853'><b>Cartel/Gafete de Acrílico</b></font>", card_label_style),
            Paragraph("<b>Hub FETUR Integrado</b><br/><font color='#00E5FF'><b>Conexión con Software Actual</b></font>", card_label_style),
            Paragraph("<b>&lt;3 Seg. SPEI MXN</b><br/><font color='#A855F7'><b>Liquidación Automática</b></font>", card_label_style)
        ],
        [
            Paragraph("Detecta en milisegundos si el celular es de Brasil, Colombia, Perú o Argentina y abre su app bancaria nativa.", card_desc_style),
            Paragraph("Conectado a <b>Sunday</b> (mesas), <b>Duve</b> (check-in), <b>FareHarbor</b> (tours) y <b>Soft Restaurant / Opera PMS</b>.", card_desc_style),
            Paragraph("El comercio recibe Pesos Mexicanos en su tarjeta o cuenta de siempre (Spin OXXO, BanCoppel, Mercado Pago, BBVA).", card_desc_style)
        ]
    ]
    
    t3 = Table(data_s3, colWidths=[173, 173, 173])
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (0,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,0), (1,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (2,0), (2,1), 1, colors.HexColor('#E2E8F0')),
        ('LINELEFT', (0,0), (0,1), 4, colors.HexColor('#00C853')),
        ('LINELEFT', (1,0), (1,1), 4, colors.HexColor('#00E5FF')),
        ('LINELEFT', (2,0), (2,1), 4, colors.HexColor('#A855F7')),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
    ]))
    
    story.append(t3)
    story.append(Spacer(1, 15))
    story.append(Paragraph("📌 <b>FUENTES OFICIALES CORROBORABLES:</b> Banco de México (Banxico - Regulación SPEI) · CNBV (Disposiciones Fintech Art. 44-48 Onboarding Nivel 1/2) · Estándar EMVCo QR Code Specification.", source_style))
    story.append(PageBreak())

    # ------------------ SLIDE 6: PISO FINANCIERO 1% ------------------
    story.append(Paragraph("06 · PLAN DE NEGOCIO Y METAS DE PISO FINANCIERO", tag_style))
    story.append(Paragraph("Un piso conservador del 1% del mercado ($3.5M USD) se alcanza con solo 113 transacciones diarias en 175 comercios clave", title_style))
    
    data_s4 = [
        [
            Paragraph("<b>$3.5 Millones de USD</b><br/><font color='#00C853'><b>Volumen Piso (1% SAM)</b></font>", card_label_style),
            Paragraph("<b>175 Comercios</b><br/><font color='#3B82F6'><b>Tier 1 Pareto (35% FETUR)</b></font>", card_label_style)
        ],
        [
            Paragraph("Meta mínima garantizada de volumen procesado en el primer año de operaciones en Quintana Roo.", card_desc_style),
            Paragraph("Solo el 35% de los 500 asociados actuales de FETUR en Cancún, Playa del Carmen, Tulum y Cozumel.", card_desc_style)
        ],
        [
            Paragraph("<b>113 Txs / Día</b><br/><font color='#A855F7'><b>Distribución en QRoo</b></font>", card_label_style),
            Paragraph("<b>1 Pago / Día</b><br/><font color='#FF9100'><b>Por Comercio Afiliado</b></font>", card_label_style)
        ],
        [
            Paragraph("40 Cancún + 35 Playa del Carmen + 25 Tulum + 13 Cozumel = 113 pagos diarios en todo el estado.", card_desc_style),
            Paragraph("Basta con que cada negocio realice solo 1 cobro promedio de $85 USD al día para cumplir la meta.", card_desc_style)
        ]
    ]
    
    t4 = Table(data_s4, colWidths=[260, 260])
    t4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (0,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,0), (1,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (0,2), (0,3), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,2), (1,3), 1, colors.HexColor('#E2E8F0')),
        ('LINELEFT', (0,0), (0,1), 4, colors.HexColor('#00C853')),
        ('LINELEFT', (1,0), (1,1), 4, colors.HexColor('#3B82F6')),
        ('LINELEFT', (0,2), (0,3), 4, colors.HexColor('#A855F7')),
        ('LINELEFT', (1,2), (1,3), 4, colors.HexColor('#FF9100')),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('BOTTOMPADDING', (0,2), (-1,2), 2),
    ]))
    
    story.append(t4)
    story.append(Spacer(1, 10))
    story.append(Paragraph("📌 <b>FUENTES OFICIALES CORROBORABLES:</b> Directorio de Afiliados FETUR Quintana Roo · Modelo de Análisis Pareto (80/20) · Métrica de Flujo de Pasajeros ASUR (Grupo Aeroportuario del Sureste).", source_style))
    story.append(PageBreak())

    # ------------------ SLIDE 7: CRONOGRAMA A 45 DÍAS ------------------
    story.append(Paragraph("07 · CRONOGRAMA DE EJECUCIÓN Y ESCALAMIENTO NATIVO", tag_style))
    story.append(Paragraph("Plan de acción inmediato a 45 días para la circular de adhesión, entrega de kits y lanzamiento en rueda de prensa estatal", title_style))
    
    data_s5 = [
        [
            Paragraph("<b>Días 1 - 15</b><br/><font color='#00C853'><b>Circular Institucional FETUR</b></font>", card_label_style),
            Paragraph("<b>Días 16 - 30</b><br/><font color='#00E5FF'><b>Entrega de Kits & Integración</b></font>", card_label_style)
        ],
        [
            Paragraph("Envío de circular formal de adhesión a los 175 comercios de mayor densidad turística sudamericana.", card_desc_style),
            Paragraph("Reparto de acrílicos QR de mostrador y activación en el software de caja (Sunday / Soft Restaurant).", card_desc_style)
        ],
        [
            Paragraph("<b>Días 31 - 45</b><br/><font color='#A855F7'><b>Rueda de Prensa de Estado</b></font>", card_label_style),
            Paragraph("<b>Días 46+</b><br/><font color='#FF9100'><b>Operación & Escalamiento ASETUR</b></font>", card_label_style)
        ],
        [
            Paragraph("Lanzamiento oficial ante medios con el Secretario de Turismo de QRoo y Presidenta de FETUR.", card_desc_style),
            Paragraph("Auditoría de volumen de procesamiento e inicio de gestión para réplica en Los Cabos y Puerto Vallarta.", card_desc_style)
        ]
    ]
    
    t5 = Table(data_s5, colWidths=[260, 260])
    t5.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (0,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,0), (1,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (0,2), (0,3), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,2), (1,3), 1, colors.HexColor('#E2E8F0')),
        ('LINELEFT', (0,0), (0,1), 4, colors.HexColor('#00C853')),
        ('LINELEFT', (1,0), (1,1), 4, colors.HexColor('#00E5FF')),
        ('LINELEFT', (0,2), (0,3), 4, colors.HexColor('#A855F7')),
        ('LINELEFT', (1,2), (1,3), 4, colors.HexColor('#FF9100')),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('BOTTOMPADDING', (0,2), (-1,2), 2),
    ]))
    
    story.append(t5)
    story.append(Spacer(1, 10))
    story.append(Paragraph("📌 <b>FUENTES OFICIALES CORROBORABLES:</b> Agenda de la Comisión de Innovación Tecnológica (FETUR) · ASETUR (Unión de Secretarios de Turismo de México - Convenio Marco Nacional).", source_style))

    # Build PDF with custom NumberedCanvas
    doc.build(story, canvasmaker=NumberedCanvas)
    
    # Copy to OneDrive Downloads as backup
    if os.path.exists(downloads_path):
        import shutil
        try:
            shutil.copy(chosen_target, target_onedrive_pdf)
            print(f"PDF de 7 diapositivas con Bancos Centrales, QR y TAM/SAM/SOM exitosamente generado en:\n1. {chosen_target}\n2. {target_onedrive_pdf}")
        except Exception as e:
            print(f"PDF generado exitosamente en:\n1. {chosen_target}\n(OneDrive ocupado: {e})")

if __name__ == "__main__":
    generate_pdf()
