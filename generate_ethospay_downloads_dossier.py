import os
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
)

def build_pdf():
    downloads_dir = r"C:\Users\Antonio\Downloads"
    pdf_path = os.path.join(downloads_dir, "Briefing_Ejecutivo_EthosPay_OnePager.pdf")
    workspace_pdf = r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\riviera-maya-payments\Briefing_Ejecutivo_EthosPay_OnePager.pdf"
    
    # 612 x 792 pt, margins 20 pt
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=20,
        rightMargin=20,
        topMargin=16,
        bottomMargin=16
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Typography Styles
    title_style = ParagraphStyle(
        'MainTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor('#0F172A')
    )
    
    subtitle_style = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#475569')
    )
    
    badge_style = ParagraphStyle(
        'BadgeStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9,
        textColor=colors.HexColor('#059669'),
        alignment=2
    )
    
    section_heading = ParagraphStyle(
        'SectionH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10,
        textColor=colors.HexColor('#1E293B')
    )
    
    kpi_num_style = ParagraphStyle(
        'KpiNum',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=15,
        textColor=colors.HexColor('#0F172A'),
        alignment=1
    )
    
    kpi_label_style = ParagraphStyle(
        'KpiLabel',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#475569'),
        alignment=1
    )
    
    body_style = ParagraphStyle(
        'BodyP',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#334155')
    )
    
    body_bold = ParagraphStyle(
        'BodyBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#0F172A')
    )
    
    tbl_header = ParagraphStyle(
        'TblH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=8.5,
        textColor=colors.HexColor('#FFFFFF')
    )
    
    tbl_cell = ParagraphStyle(
        'TblC',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#1E293B')
    )
    
    source_style = ParagraphStyle(
        'SourceP',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=5.8,
        leading=7.2,
        textColor=colors.HexColor('#64748B')
    )
    
    story = []
    
    # 1. HEADER
    header_data = [
        [
            Paragraph("<b>ETHOSPAY × FETUR QUINTANA ROO</b><br/><font color='#0284C7'>Alianza Adquirente Zero-Hardware | Corredor Transfronterizo de Pagos</font>", title_style),
            Paragraph("<b>MEMORÁNDUM CONFIDENCIAL</b><br/>Fecha: Agosto 2026<br/>Sede: Cancún / Riviera Maya", badge_style)
        ]
    ]
    t_header = Table(header_data, colWidths=[400, 172])
    t_header.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINEBELOW', (0,0), (-1,-1), 1.5, colors.HexColor('#0284C7')),
    ]))
    story.append(t_header)
    story.append(Spacer(1, 6))
    
    # 2. KPI CARDS (BENTO GRID)
    kpi_data = [
        [
            Paragraph("<font color='#DC2626'><b>40% - 50%</b></font>", kpi_num_style),
            Paragraph("<font color='#059669'><b>+37%</b></font>", kpi_num_style),
            Paragraph("<font color='#0284C7'><b>1.5% - 2.5%</b></font>", kpi_num_style),
            Paragraph("<font color='#7C3AED'><b>-30% / +75%</b></font>", kpi_num_style)
        ],
        [
            Paragraph("<b>Rechazo en TPVs Tradicionales</b><br/>Filtros antifraude en tarjetas de Brasil, Argentina y Colombia", kpi_label_style),
            Paragraph("<b>Incremento Real en Ingresos</b><br/>Ventas adicionales comprobadas al habilitar Pix y APMs (EBANX)", kpi_label_style),
            Paragraph("<b>Spread FX Neto Retenido</b><br/>Margen cambiario puro para EthosPay sin pagar tasas de intercambio", kpi_label_style),
            Paragraph("<b>Muerte del Efectivo</b><br/>Caída de retiros en cajeros (-30%) y explosión del QR (+75%)", kpi_label_style)
        ]
    ]
    t_kpi = Table(kpi_data, colWidths=[143, 143, 143, 143])
    t_kpi.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#FEF2F2')),
        ('BACKGROUND', (1,0), (1,-1), colors.HexColor('#ECFDF5')),
        ('BACKGROUND', (2,0), (2,-1), colors.HexColor('#F0F9FF')),
        ('BACKGROUND', (3,0), (3,-1), colors.HexColor('#F5F3FF')),
        ('BOX', (0,0), (0,-1), 0.5, colors.HexColor('#FECACA')),
        ('BOX', (1,0), (1,-1), 0.5, colors.HexColor('#A7F3D0')),
        ('BOX', (2,0), (2,-1), 0.5, colors.HexColor('#BAE6FD')),
        ('BOX', (3,0), (3,-1), 0.5, colors.HexColor('#DDD6FE')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_kpi)
    story.append(Spacer(1, 6))
    
    # 3. COMPARATIVE TABLE: TRADITIONAL ACQUIRERS VS ETHOSPAY
    story.append(Paragraph("<b>1. LA OPORTUNIDAD: EL ARBITRAJE FRENTE A LOS ADQUIRENTES TRADICIONALES</b>", section_heading))
    story.append(Spacer(1, 3))
    
    comp_data = [
        [
            Paragraph("<b>Dimensión Estratégica</b>", tbl_header),
            Paragraph("<b>Adquirentes Tradicionales / TPVs Legacy</b>", tbl_header),
            Paragraph("<b>Propuesta EthosPay × FETUR (Next-Gen)</b>", tbl_header)
        ],
        [
            Paragraph("<b>Aprobación de Pagos LATAM</b>", tbl_cell),
            Paragraph("<b>20% - 45%</b> (55% de rechazos por filtros offshore)", tbl_cell),
            Paragraph("<b>>98% de Aprobación</b> vía Pix, APMs y Biometría nativa", tbl_cell)
        ],
        [
            Paragraph("<b>Modelo de Ingreso y Margen</b>", tbl_cell),
            Paragraph("MDR diluido por tasas de intercambio de bancos extranjeros", tbl_cell),
            Paragraph("<b>100% Spread FX Neto (1.5% - 2.5%)</b> libre de intercambio", tbl_cell)
        ],
        [
            Paragraph("<b>Infraestructura & Costo (CAC)</b>", tbl_cell),
            Paragraph("Alto: Compra, subsidio, logística y mantenimiento de hardware", tbl_cell),
            Paragraph("<b>Zero-Hardware:</b> Activación en 2 min vía QR dinámico / API", tbl_cell)
        ],
        [
            Paragraph("<b>Riesgo Operativo (Fraude)</b>", tbl_cell),
            Paragraph("Alto riesgo de contracargos (*Chargebacks*) en tarjetas", tbl_cell),
            Paragraph("<b>Cero Contracargos:</b> Autorización biométrica irrevocable", tbl_cell)
        ]
    ]
    t_comp = Table(comp_data, colWidths=[120, 226, 226])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#FFFFFF')),
        ('BACKGROUND', (0,2), (-1,2), colors.HexColor('#F8FAFC')),
        ('BACKGROUND', (0,3), (-1,3), colors.HexColor('#FFFFFF')),
        ('BACKGROUND', (0,4), (-1,4), colors.HexColor('#F8FAFC')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_comp)
    story.append(Spacer(1, 6))
    
    # 4. TWO COLUMNS: BUSINESS MODEL & 60-DAY PILOT
    story.append(Paragraph("<b>2. ARQUITECTURA DE NEGOCIO Y PLAN DE PILOTO (60 DÍAS)</b>", section_heading))
    story.append(Spacer(1, 3))
    
    col_left = [
        Paragraph("<b>Ventajas Clave para EthosPay:</b>", body_bold),
        Paragraph("• <b>Captura de Spread Cambiario:</b> Al procesar vía rieles directos (Pix/APMs), EthosPay retiene el diferencial cambiario limpio entre divisas locales y MXN/USD.", body_style),
        Paragraph("• <b>Acceso Cautivo FETUR:</b> Afiliación directa sin costo comercial en frío a empresas turísticas (tours náuticos, agencias receptivas, beach clubs).", body_style),
        Paragraph("• <b>Flujos B2B Mayoristas:</b> Liquidación de reservas hoteleras internacionales en minutos vs. los 42-66 días del sistema bancario tradicional (Dasbanq).", body_style),
    ]
    
    col_right = [
        Paragraph("<b>Hoja de Ruta del Piloto Controlado:</b>", body_bold),
        Paragraph("• <b>Fase 1 (Semanas 1-2):</b> Integración API y generación de QR dinámico multi-país con pasarela EthosPay.", body_style),
        Paragraph("• <b>Fase 2 (Semanas 3-6):</b> Despliegue en <b>50 a 100 comercios piloto</b> de alta densidad turística de FETUR en Cancún y Playa del Carmen.", body_style),
        Paragraph("• <b>Fase 3 (Semanas 7-8):</b> Medición de tasa de aprobación (>98%), volumen procesado y escalamiento al universo de +15,000 comercios.", body_style),
    ]
    
    t_split = Table([[col_left, col_right]], colWidths=[286, 286])
    t_split.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#F8FAFC')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (0,0), 0.5, colors.HexColor('#E2E8F0')),
        ('BOX', (1,0), (1,0), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_split)
    story.append(Spacer(1, 6))
    
    # 5. SOURCES & COMPLIANCE FOOTER
    story.append(Paragraph("<b>3. FUENTES Y RESPALDO EMPÍRICO DE LA INDUSTRIA</b>", section_heading))
    story.append(Spacer(1, 2))
    
    sources_text = (
        "<b>Fuentes Verificadas:</b> "
        "<b>[1] EBANX / GlobeNewswire:</b> +37% revenue lift & +25% client growth con Pix en comercio transfronterizo. "
        "<b>[2] Rapyd / PayRetailers 2026:</b> 40%-55% tasa de rechazo bancario en compras internacionales LATAM. "
        "<b>[3] Condusef México:</b> 28%-30% de no autorización en transacciones digitales y filtros antifraude. "
        "<b>[4] Nuvei Tourism Report:</b> $117B en pérdidas globales en turismo por rechazo de pagos; 13% cambia de proveedor. "
        "<b>[5] Banco Central de la República Argentina (BCRA):</b> Caída del -30% en uso de cajeros y auge de +75.4% en pagos con QR. "
        "<b>[6] Dasbanq 2025/2026:</b> 77% de empresas reportan retrasos de 42 a 66 días en pagos transfronterizos bancarios tradicionales."
    )
    t_sources = Table([[Paragraph(sources_text, source_style)]], colWidths=[572])
    t_sources.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_sources)
    
    doc.build(story)
    
    # Copy to workspace
    shutil.copyfile(pdf_path, workspace_pdf)
    print(f"PDF successfully created at: {pdf_path}")
    print(f"PDF backup in workspace: {workspace_pdf}")

if __name__ == "__main__":
    build_pdf()
