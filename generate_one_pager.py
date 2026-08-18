import os
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)
from reportlab.graphics.shapes import Drawing, Circle, String, Rect, Line, Group

def build_pdf():
    local_pdf = r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\riviera-maya-payments\CARIBE_MEXICANO_SMART_PAY_ONE_PAGER.pdf"
    
    # Page setup - Letter: 612 x 792 pt. Margins: 20 pt
    doc = SimpleDocTemplate(
        local_pdf,
        pagesize=letter,
        leftMargin=22,
        rightMargin=22,
        topMargin=18,
        bottomMargin=18
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    header_title_style = ParagraphStyle(
        'HeaderTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=19,
        textColor=colors.HexColor('#0F172A')
    )
    
    header_sub_style = ParagraphStyle(
        'HeaderSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#475569')
    )
    
    badge_style = ParagraphStyle(
        'Badge',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#0284C7'),
        alignment=2
    )
    
    kpi_num_style = ParagraphStyle(
        'KpiNum',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=16,
        textColor=colors.HexColor('#0F172A'),
        alignment=1
    )
    
    kpi_label_style = ParagraphStyle(
        'KpiLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=8.5,
        textColor=colors.HexColor('#0284C7'),
        alignment=1
    )
    
    kpi_sub_style = ParagraphStyle(
        'KpiSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.5,
        leading=7.5,
        textColor=colors.HexColor('#64748B'),
        alignment=1
    )
    
    sec_title_style = ParagraphStyle(
        'SecTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.HexColor('#0F172A')
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#334155')
    )
    
    body_bold_style = ParagraphStyle(
        'BodyBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#0F172A')
    )
    
    th_style = ParagraphStyle(
        'TH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=8.5,
        textColor=colors.white
    )
    
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#64748B'),
        alignment=1
    )

    story = []
    
    # -------------------------------------------------------------
    # 1. HEADER BLOCK
    # -------------------------------------------------------------
    header_left = [
        Paragraph("<b>CARIBE MEXICANO SMART PAY</b>", header_title_style),
        Paragraph("Ecosistema Transaccional A2A & Pagos Transfronterizos · <b>FETUR Quintana Roo</b>", header_sub_style)
    ]
    header_right = [
        Paragraph("<b>REGULACIÓN CNBV / BANXICO (SPEI)</b><br/><font color='#64748B'>Alianza Estratégica FETUR Nacional & Agregador Aliado</font>", badge_style)
    ]
    
    header_table = Table([[header_left, header_right]], colWidths=[380, 188])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 6))
    
    # -------------------------------------------------------------
    # 2. KPI CARDS (4 Highlights)
    # -------------------------------------------------------------
    card1 = [
        Paragraph("$1,113M USD", kpi_num_style),
        Paragraph("DERRAMA SUDAMÉRICA", kpi_label_style),
        Paragraph("Brasil, Colombia, Argentina, Perú", kpi_sub_style)
    ]
    card2 = [
        Paragraph("0% CONTRACARGOS", kpi_num_style),
        Paragraph("PAGO IRREVOCABLE A2A", kpi_label_style),
        Paragraph("Cero fraude ni clonación de tarjeta", kpi_sub_style)
    ]
    card3 = [
        Paragraph("< 3 SEGUNDOS", kpi_num_style),
        Paragraph("LIQUIDACIÓN DIRECTA SPEI", kpi_label_style),
        Paragraph("Pesos limpios a la CLABE bancaria", kpi_sub_style)
    ]
    card4 = [
        Paragraph("$3.5M A $11M USD", kpi_num_style),
        Paragraph("PISO CONSERVADOR (1%-3%)", kpi_label_style),
        Paragraph("Captura ágil con 175 comercios clave", kpi_sub_style)
    ]
    
    kpi_table = Table([[card1, card2, card3, card4]], colWidths=[140, 142, 142, 144])
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#E2E8F0')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(kpi_table)
    story.append(Spacer(1, 7))
    
    # -------------------------------------------------------------
    # 3. VENN DIAGRAM BLOCK (3 Intersecting Circles of Value)
    # -------------------------------------------------------------
    story.append(Paragraph("<b>1. DIAGRAMA DE VENN: CONVERGENCIA ESTRATÉGICA DE VALOR</b>", sec_title_style))
    story.append(Spacer(1, 3))
    
    # Drawing Venn Diagram: 3 circles
    # Center points:
    # Circle Top (FETUR): x=95, y=85, r=38
    # Circle Bottom-Left (Comercios): x=68, y=45, r=38
    # Circle Bottom-Right (Agregador): x=122, y=45, r=38
    d = Drawing(190, 130)
    d.add(Rect(0, 0, 190, 130, fillColor=colors.HexColor('#F8FAFC'), strokeColor=colors.HexColor('#CBD5E1'), strokeWidth=0.5, rx=6, ry=6))
    
    # Circle 1: FETUR (Top, Sky Blue)
    d.add(Circle(95, 82, 38, fillColor=colors.HexColor('#BAE6FD'), strokeColor=colors.HexColor('#0284C7'), strokeWidth=1.5))
    # Circle 2: COMERCIOS (Bottom Left, Amber/Warm)
    d.add(Circle(68, 48, 38, fillColor=colors.HexColor('#FEF08A'), strokeColor=colors.HexColor('#CA8A04'), strokeWidth=1.5))
    # Circle 3: AGREGADOR / ETHOSPAY (Bottom Right, Emerald/Teal)
    d.add(Circle(122, 48, 38, fillColor=colors.HexColor('#A7F3D0'), strokeColor=colors.HexColor('#059669'), strokeWidth=1.5))
    
    # Labels inside circles
    d.add(String(95, 106, "1. FETUR & Q. ROO", fontName="Helvetica-Bold", fontSize=5.5, textAnchor="middle", fillColor=colors.HexColor('#0369A1')))
    d.add(String(95, 98, "• Turismo Inteligente", fontName="Helvetica", fontSize=4.5, textAnchor="middle", fillColor=colors.HexColor('#075985')))
    d.add(String(95, 91, "• $1,113M USD Derrama", fontName="Helvetica", fontSize=4.5, textAnchor="middle", fillColor=colors.HexColor('#075985')))

    d.add(String(48, 48, "2. COMERCIOS", fontName="Helvetica-Bold", fontSize=5.5, textAnchor="middle", fillColor=colors.HexColor('#854D0E')))
    d.add(String(48, 41, "• 0% Contracargos", fontName="Helvetica", fontSize=4.5, textAnchor="middle", fillColor=colors.HexColor('#713F12')))
    d.add(String(48, 34, "• Zero Hardware", fontName="Helvetica", fontSize=4.5, textAnchor="middle", fillColor=colors.HexColor('#713F12')))

    d.add(String(142, 48, "3. AGREGADOR", fontName="Helvetica-Bold", fontSize=5.5, textAnchor="middle", fillColor=colors.HexColor('#065F46')))
    d.add(String(142, 41, "• Licencia CNBV", fontName="Helvetica", fontSize=4.5, textAnchor="middle", fillColor=colors.HexColor('#064E3B')))
    d.add(String(142, 34, "• Riel STP / SPEI", fontName="Helvetica", fontSize=4.5, textAnchor="middle", fillColor=colors.HexColor('#064E3B')))

    # Center Intersection (The Sweet Spot)
    d.add(Circle(95, 58, 14, fillColor=colors.HexColor('#0F172A'), strokeColor=colors.HexColor('#38BDF8'), strokeWidth=1))
    d.add(String(95, 62, "SMART PAY", fontName="Helvetica-Bold", fontSize=5, textAnchor="middle", fillColor=colors.HexColor('#38BDF8')))
    d.add(String(95, 54, "SPEED TO CASH", fontName="Helvetica-Bold", fontSize=4, textAnchor="middle", fillColor=colors.white))

    desc_cell = [
        Paragraph("<b>1. CÍRCULO AZUL: FETUR & LA REGIÓN (DEMANDA Y SOBERANÍA)</b><br/>"
                  "• Frena la fuga de +$40M USD en comisiones bancarias tradicionales al extranjero.<br/>"
                  "• Implementa la <i>Estrategia Nacional de Turismo Inteligente</i> con data de consumo en el Hub.", body_style),
        Spacer(1, 2.5),
        Paragraph("<b>2. CÍRCULO AMARILLO: EL COMERCIO / SOCIO (OPERACIÓN EN MOSTRADOR)</b><br/>"
                  "• <b>0% Contracargos:</b> Transferencia irrevocable cuenta a cuenta A2A (Pix, Nequi, CoDi).<br/>"
                  "• <b>Zero Costo Fijo:</b> Cobra desde celular (Web POS) o acrílico QR de mesa sin comprar terminales.<br/>"
                  "• <b>Ahorro del 50%:</b> Tasa neta mucho menor al 3.6% de agregadores tradicionales (Clip).", body_style),
        Spacer(1, 2.5),
        Paragraph("<b>3. CÍRCULO VERDE: AGREGADOR & INFRAESTRUCTURA (ETHOSPAY / 8B / STP)</b><br/>"
                  "• <b>Cero CAC:</b> Adquisición masiva institucional de 175 comercios sin fuerza de ventas de calle.<br/>"
                  "• <b>Monetización Transaccional & Crédito:</b> Pone a producir la licencia de Agregador CNBV y usa la data de ventas diarias para colocar crédito de capital de trabajo a hoteles de alto ticket.", body_style),
        Spacer(1, 2.5),
        Paragraph("<b>🎯 INTERSECCIÓN CENTRAL: CARIBE MEXICANO SMART PAY</b><br/>"
                  "Conecta la demanda de 850,000 turistas sudamericanos con el mostrador del hotel y la tubería bancaria regulada en un piloto ágil de 30 días.", body_bold_style)
    ]
    
    venn_table = Table([[d, desc_cell]], colWidths=[195, 373])
    venn_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(venn_table)
    story.append(Spacer(1, 7))
    
    # -------------------------------------------------------------
    # 4. WIN-WIN-WIN ALIGNMENT MATRIX
    # -------------------------------------------------------------
    story.append(Paragraph("<b>2. MATRIZ DE INTERESES & ALINEACIÓN TRILATERAL</b>", sec_title_style))
    story.append(Spacer(1, 3))
    
    headers = [
        Paragraph("<b>STAKEHOLDER</b>", th_style),
        Paragraph("<b>INTERÉS GENUINO</b>", th_style),
        Paragraph("<b>SOLUCIÓN CON SMART PAY</b>", th_style),
        Paragraph("<b>BENEFICIO TANGIBLE</b>", th_style)
    ]
    
    row_fetur = [
        Paragraph("<b>FETUR Nacional & Q. Roo</b>", body_bold_style),
        Paragraph("Liderazgo en Turismo Inteligente, seguridad jurídica y valor a afiliados.", body_style),
        Paragraph("Ecosistema institucional de cobro A2A respaldado por Banco de México y CNBV.", body_style),
        Paragraph("Posicionamiento nacional, fidelización de socios y analítica de gasto turístico.", body_style)
    ]
    
    row_socio = [
        Paragraph("<b>Socio / Comercio</b><br/>(Hoteles / Restaurantes)", body_bold_style),
        Paragraph("Cobrar fácil al turista extranjero, liquidez inmediata y cero pérdidas por fraude.", body_style),
        Paragraph("Acrílico QR de mesa y Web POS móvil con dispersión directa a su CLABE bancaria.", body_style),
        Paragraph("0% contracargos, liquidación en 3 segundos y aumento en ventas de LATAM.", body_style)
    ]
    
    row_ethos = [
        Paragraph("<b>Agregador Aliado</b><br/>(EthosPay / FinTech)", body_bold_style),
        Paragraph("Procesar alto volumen rápido, rentabilizar licencia CNBV y colocar crédito.", body_style),
        Paragraph("Canal B2B concentrado en FETUR (sin fuerza de ventas de calle) y data de ventas.", body_style),
        Paragraph("Cero CAC, millones en TPV turística y colocación de crédito de nómina/capital.", body_style)
    ]
    
    matrix_table = Table([headers, row_fetur, row_socio, row_ethos], colWidths=[105, 148, 165, 150])
    matrix_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 3.5),
        ('RIGHTPADDING', (0,0), (-1,-1), 3.5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
    ]))
    story.append(matrix_table)
    story.append(Spacer(1, 7))
    
    # -------------------------------------------------------------
    # 5. ROADMAP PILOTO 30 DÍAS
    # -------------------------------------------------------------
    story.append(Paragraph("<b>3. PLAN DE EJECUCIÓN INMEDIATO (PILOTO DE 30 DÍAS — SPEED TO REVENUE)</b>", sec_title_style))
    story.append(Spacer(1, 3))
    
    p1 = [
        Paragraph("<b>FASE 1: DÍAS 1 - 10</b>", ParagraphStyle('PTitle', fontName='Helvetica-Bold', fontSize=7, textColor=colors.HexColor('#0284C7'))),
        Paragraph("<b>Comisión de Innovación:</b> Emisión de circular formal de FETUR y selección de los primeros 25-50 comercios ancla (Cancún, Playa 5ta Ave, Tulum, Cozumel).", body_style)
    ]
    p2 = [
        Paragraph("<b>FASE 2: DÍAS 11 - 20</b>", ParagraphStyle('PTitle', fontName='Helvetica-Bold', fontSize=7, textColor=colors.HexColor('#059669'))),
        Paragraph("<b>Onboarding & Kits:</b> Registro digital simplificado (CLABE + RFC) y entrega de kits de cobro (Acrílicos QR de mesa / Web POS en celular).", body_style)
    ]
    p3 = [
        Paragraph("<b>FASE 3: DÍAS 21 - 30</b>", ParagraphStyle('PTitle', fontName='Helvetica-Bold', fontSize=7, textColor=colors.HexColor('#D97706'))),
        Paragraph("<b>Go-Live & Métricas:</b> Primeros cobros en vivo con turistas de Brasil y Colombia; medición de volumen para escalamiento a los 175 comercios.", body_style)
    ]
    
    roadmap_table = Table([[p1, p2, p3]], colWidths=[189, 189, 190])
    roadmap_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 3.5),
        ('RIGHTPADDING', (0,0), (-1,-1), 3.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(roadmap_table)
    story.append(Spacer(1, 6))
    
    # -------------------------------------------------------------
    # 6. FOOTER
    # -------------------------------------------------------------
    footer_text = Paragraph(
        "<b>Documento Ejecutivo de Trabajo · Sesión de Trabajo Presidencia & Dirección Ejecutiva FETUR Nacional · Agosto 2026</b>",
        footer_style
    )
    story.append(footer_text)

    # Build Document
    doc.build(story)
    print("One-Pager with Venn Diagram built successfully at:", local_pdf)
    
    # Copy to downloads
    d1 = r"C:\Users\Antonio\OneDrive\Downloads\CARIBE_MEXICANO_SMART_PAY_ONE_PAGER_EJECUTIVO.pdf"
    d2 = r"C:\Users\Antonio\Downloads\CARIBE_MEXICANO_SMART_PAY_ONE_PAGER_EJECUTIVO.pdf"
    
    try:
        shutil.copyfile(local_pdf, d1)
        print("Copied to OneDrive:", d1)
    except Exception as e:
        print("Could not copy to OneDrive:", e)
        
    try:
        shutil.copyfile(local_pdf, d2)
        print("Copied to Downloads:", d2)
    except Exception as e:
        print("Could not copy to Downloads:", e)

if __name__ == "__main__":
    build_pdf()
