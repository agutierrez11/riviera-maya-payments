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
        self.drawString(245, 25, "DOCUMENTO CONFIDENCIAL ESTATAL DE PAGO RECEPTIVO TURÍSTICO")
        self.drawRightString(width - 30, 25, f"Diapositiva {self._pageNumber} de {page_count}")


def generate_pdf():
    downloads_path = r"C:\Users\Antonio\Downloads"
    onedrive_path = r"C:\Users\Antonio\OneDrive\Downloads"
    pdf_filename = "CARIBE_MEXICANO_SMART_PAY_PRESENTACION_EJECUTIVA.pdf"
    
    target_pdf = os.path.join(downloads_path, pdf_filename)
    target_onedrive_pdf = os.path.join(onedrive_path, pdf_filename)
    
    doc = SimpleDocTemplate(
        target_pdf,
        pagesize=landscape(A4),
        leftMargin=245,
        rightMargin=30,
        topMargin=40,
        bottomMargin=50
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'SlideTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1F2A44'),
        spaceAfter=15
    )
    
    tag_style = ParagraphStyle(
        'SlideTag',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.HexColor('#00C853'),
        spaceAfter=5
    )
    
    card_label_style = ParagraphStyle(
        'CardLabel',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=4
    )
    
    card_desc_style = ParagraphStyle(
        'CardDesc',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#334155')
    )

    story = []
    
    # ------------------ SLIDE 1 ------------------
    story.append(Paragraph("01 · CONTEXTO DE MERCADO Y DERRAMA", tag_style))
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
        ('BACKGROUND', (0,0), (0,1), colors.HexColor('#F8FAFC')),
        ('BACKGROUND', (1,0), (1,1), colors.HexColor('#F8FAFC')),
        ('BACKGROUND', (0,2), (0,3), colors.HexColor('#F8FAFC')),
        ('BACKGROUND', (1,2), (1,3), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (0,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,0), (1,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (0,2), (0,3), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,2), (1,3), 1, colors.HexColor('#E2E8F0')),
        ('LINELEFT', (0,0), (0,1), 4, colors.HexColor('#00C853')),
        ('LINELEFT', (1,0), (1,1), 4, colors.HexColor('#00E5FF')),
        ('LINELEFT', (0,2), (0,3), 4, colors.HexColor('#A855F7')),
        ('LINELEFT', (1,2), (1,3), 4, colors.HexColor('#FF9100')),
        ('PADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('BOTTOMPADDING', (0,2), (-1,2), 2),
    ]))
    
    story.append(t1)
    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>Nota de Exposición:</b> <i>Quintana Roo concentra el 46% de todo el volumen de gasto en sitio de turistas sudamericanos en México.</i>", card_desc_style))
    story.append(PageBreak())
    
    # ------------------ SLIDE 2 ------------------
    story.append(Paragraph("02 · HÁBITOS DE PAGO Y SOBRECOSTOS IMPOSITIVOS", tag_style))
    story.append(Paragraph("El 65% de los turistas sudamericanos evita usar tarjetas tradicionales por comisiones e impuestos en sus países", title_style))
    
    data_s2 = [
        [
            Paragraph("<b>🇧🇷 Brasil — Red PIX (>65,000M Txs/Año)</b>", card_label_style),
            Paragraph("<b>🇦🇷 Argentina — eWallets & CBU (62% Adopción)</b>", card_label_style)
        ],
        [
            Paragraph("El 85% prefiere pagar con PIX para eludir el <b>3.5% de Impuesto IOF</b> que cobra su gobierno al usar tarjeta en México.", card_desc_style),
            Paragraph("Los argentinos evitan la tarjeta de crédito para eludir el <b>15% al 25% de recargo impositivo AFIP</b> ('Dólar Tarjeta').", card_desc_style)
        ],
        [
            Paragraph("<b>🇵🇪 Perú — Yape & Plin (>40M Txs/Día)</b>", card_label_style),
            Paragraph("<b>🇨🇴 Colombia — Nequi & DaviPlata (>78% Adultos)</b>", card_label_style)
        ],
        [
            Paragraph("El 68% de los viajeros peruanos no utiliza tarjeta de crédito por temor a altas tasas de interés bancarias.", card_desc_style),
            Paragraph("Prevalencia masiva de pagos mediante llaves digitales y códigos QR de transferencia instantánea.", card_desc_style)
        ]
    ]
    
    t2 = Table(data_s2, colWidths=[260, 260])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (0,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,0), (1,1), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (0,2), (0,3), 1, colors.HexColor('#E2E8F0')),
        ('BOX', (1,2), (1,3), 1, colors.HexColor('#E2E8F0')),
        ('LINELEFT', (0,0), (0,1), 4, colors.HexColor('#00C853')),
        ('LINELEFT', (1,0), (1,1), 4, colors.HexColor('#3B82F6')),
        ('LINELEFT', (0,2), (0,3), 4, colors.HexColor('#A855F7')),
        ('LINELEFT', (1,2), (1,3), 4, colors.HexColor('#EC4899')),
        ('PADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('BOTTOMPADDING', (0,2), (-1,2), 2),
    ]))
    
    story.append(t2)
    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>Nota de Exposición:</b> <i>Pagar con el QR nativo de su país es su hábito cotidiano número uno y les ahorra sobrecostos.</i>", card_desc_style))
    story.append(PageBreak())

    # ------------------ SLIDE 3 ------------------
    story.append(Paragraph("03 · ARQUITECTURA ZERO-DEVICE & ZERO-ERP", tag_style))
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
        ('PADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
    ]))
    
    story.append(t3)
    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>Nota de Exposición:</b> <i>Despliegue ultrarrápido sin costo de compra ni mantenimiento de terminales bancarias.</i>", card_desc_style))
    story.append(PageBreak())

    # ------------------ SLIDE 4 ------------------
    story.append(Paragraph("04 · PLAN DE NEGOCIO Y METAS DE PISO FINANCIERO", tag_style))
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
        ('PADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('BOTTOMPADDING', (0,2), (-1,2), 2),
    ]))
    
    story.append(t4)
    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>Nota de Exposición:</b> <i>Métrica de piso hiper-alcanzable (apenas el 4.9% del flujo diario de pasajeros sudamericanos).</i>", card_desc_style))
    story.append(PageBreak())

    # ------------------ SLIDE 5 ------------------
    story.append(Paragraph("05 · CRONOGRAMA DE EJECUCIÓN Y PRÓXIMOS PASOS", tag_style))
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
        ('PADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('BOTTOMPADDING', (0,2), (-1,2), 2),
    ]))
    
    story.append(t5)
    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>Mesa Abierta:</b> <i>Quedamos a su disposición para coordinar la circular de adhesión y la fecha de la rueda de prensa estatal.</i>", card_desc_style))

    # Build PDF with custom NumberedCanvas
    doc.build(story, canvasmaker=NumberedCanvas)
    
    # Copy to OneDrive Downloads as backup
    if os.path.exists(downloads_path):
        import shutil
        shutil.copy(target_pdf, target_onedrive_pdf)
        print(f"PDF exitosamente guardado en:\n1. {target_pdf}\n2. {target_onedrive_pdf}")

if __name__ == "__main__":
    generate_pdf()
