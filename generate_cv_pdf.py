import os
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
import fitz  # PyMuPDF to verify and render preview

def generate_resume():
    local_pdf = r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\riviera-maya-payments\Antonio_Gutierrez_Jimenez_CV_Fintech_AE.pdf"
    downloads_pdf = r"C:\Users\Antonio\Downloads\Antonio_Gutierrez_Jimenez_CV_Fintech_AE.pdf"
    
    # Letter size: 612 x 792 pt. Margins: 28 pt left/right, 24 pt top/bottom
    doc = SimpleDocTemplate(
        local_pdf,
        pagesize=letter,
        leftMargin=28,
        rightMargin=28,
        topMargin=24,
        bottomMargin=24
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Corporate Palette
    COLOR_PRIMARY = colors.HexColor('#0F172A')     # Deep Navy Slate (#0F172A)
    COLOR_ACCENT = colors.HexColor('#0284C7')      # Ocean Fintech Blue (#0284C7)
    COLOR_TEXT = colors.HexColor('#1E293B')        # Dark Charcoal (#1E293B)
    COLOR_MUTED = colors.HexColor('#475569')       # Slate Muted (#475569)
    COLOR_BORDER = colors.HexColor('#CBD5E1')      # Border (#CBD5E1)
    
    # Paragraph Styles
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16.5,
        leading=18.5,
        textColor=COLOR_PRIMARY,
        spaceAfter=3
    )
    
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.2,
        leading=11.5,
        textColor=COLOR_ACCENT,
        spaceAfter=4
    )
    
    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.0,
        leading=10.5,
        textColor=COLOR_MUTED
    )
    
    section_title_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=11,
        textColor=COLOR_PRIMARY,
        spaceBefore=0,
        spaceAfter=0
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.9,
        leading=10.6,
        textColor=COLOR_TEXT,
        alignment=4 # Justified
    )
    
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.4,
        leading=10.5,
        textColor=COLOR_PRIMARY
    )
    
    job_meta_style = ParagraphStyle(
        'JobMeta',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.6,
        leading=10,
        textColor=COLOR_MUTED,
        alignment=2 # Right aligned
    )
    
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.4,
        textColor=COLOR_TEXT,
        leftIndent=11,
        firstLineIndent=-11,
        alignment=4 # Justified
    )
    
    edu_title_style = ParagraphStyle(
        'EduTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.0,
        leading=10.2,
        textColor=COLOR_PRIMARY
    )
    
    edu_sub_style = ParagraphStyle(
        'EduSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.8,
        textColor=COLOR_MUTED
    )
    
    cert_item_style = ParagraphStyle(
        'CertItem',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.8,
        textColor=COLOR_TEXT,
        leftIndent=9,
        firstLineIndent=-9
    )

    story = []
    
    # 1. HEADER
    story.append(Paragraph("ANTONIO GUTIÉRREZ JIMÉNEZ", name_style))
    story.append(Paragraph("Senior B2B Sales Executive | Fintech, Merchant Acquiring & Payment Infrastructure", title_style))
    
    contact_text = (
        "Cancún, Quintana Roo, Mexico &nbsp;•&nbsp; "
        "+52 998 119 1903 &nbsp;•&nbsp; "
        "<font color='#0284C7'>antoniogtzjimenez@gmail.com</font> &nbsp;•&nbsp; "
        "<font color='#0284C7'>linkedin.com/in/agjbusiness/</font>"
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_PRIMARY, spaceBefore=1, spaceAfter=6))
    
    def add_section_header(title):
        story.append(Paragraph(title.upper(), section_title_style))
        story.append(HRFlowable(width="100%", thickness=0.6, color=COLOR_BORDER, spaceBefore=2, spaceAfter=5))
        
    # 2. PROFESSIONAL SUMMARY
    add_section_header("Professional Summary")
    summary_p = (
        "High-performing <b>B2B Sales Executive</b> with <b>5+ years of track record</b> driving commercial revenue, "
        "outbound hunting, and scaling merchant acquiring and payment technology (PayTech) solutions across Mexico and LATAM. "
        "Proven consultative hunter managing full-cycle sales for Mid-Market & Enterprise accounts, delivering <b>$69M+ MXN (~$3.8M+ USD)</b> "
        "in cumulative transactional volume. Strong domain expertise in payment gateways, POS/SmartPOS infrastructure, API/ISV integrations, "
        "and resolving transactional frictions for high-volume merchants with international customer exposure. Co-founder of an active regional "
        "community of 500+ payments and fintech professionals."
    )
    story.append(Paragraph(summary_p, body_style))
    story.append(Spacer(1, 6))
    
    # 3. CORE COMPETENCIES & EXPERTISE
    add_section_header("Core Competencies & Expertise")
    skills_data = [
        [
            Paragraph("• <b>Payment Tech & Acquiring:</b> Gateways, SmartPOS, multi-currency processing, interchange & fees, fraud mitigation.", body_style),
            Paragraph("• <b>Consultative Sales & Hunting:</b> End-to-end B2B sales cycles, cold outbound prospecting, C-Level/CFO discovery, pipeline hygiene.", body_style)
        ],
        [
            Paragraph("• <b>API & ISV Partnerships:</b> Commercial negotiations & technical integrations with ERP, PMS, and Point of Sale systems.", body_style),
            Paragraph("• <b>SalesTech & Revenue Ops:</b> Power BI transactional monitoring, Power Automate workflow automation, Salesforce, CRM forecasting.", body_style)
        ]
    ]
    skills_table = Table(skills_data, colWidths=[275, 281])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 6))
    
    # 4. PROFESSIONAL EXPERIENCE
    add_section_header("Professional Experience")
    
    # --- Job 1: LATAM Payments & eCommerce ---
    j1_header = [
        [
            Paragraph("<b>Co-Founder</b> | <font color='#0284C7'><b>LATAM Payments & eCommerce</b></font>", job_title_style),
            Paragraph("05/2024 – Present | LATAM · Remote", job_meta_style)
        ]
    ]
    t1 = Table(j1_header, colWidths=[376, 180])
    t1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t1)
    story.append(Paragraph(
        "• Co-founded and coordinate an active professional community of <b>500+ digital payments, acquiring, and fintech specialists</b> across Mexico and LATAM, analyzing regional payment rails, emerging fintech infrastructure, and cross-border settlement trends.",
        bullet_style
    ))
    story.append(Spacer(1, 5))
    
    # --- Job 2: Fiserv ---
    j2_header = [
        [
            Paragraph("<b>Business Advisor</b> | <font color='#0284C7'><b>Fiserv</b></font>", job_title_style),
            Paragraph("02/2025 – 10/2025 | Cancún, Mexico", job_meta_style)
        ]
    ]
    t2 = Table(j2_header, colWidths=[376, 180])
    t2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t2)
    story.append(Paragraph(
        "• Managed commercial retention, portfolio expansion, and churn mitigation for an active portfolio of <b>80+ high-volume corporate merchants</b> across hospitality, retail, and commercial services.",
        bullet_style
    ))
    story.append(Paragraph(
        "• Designed and deployed a dynamic <b>Month-over-Month (MoM) transactional monitoring model in Power BI</b>, identifying cross-sell opportunities and optimizing data-driven commercial decisions.",
        bullet_style
    ))
    story.append(Paragraph(
        "• Developed an automated merchant reactivation workflow integrating Power Automate and Salesforce, generating an average of <b>+15 qualified monthly pipeline opportunities</b> from banking alliance referrals.",
        bullet_style
    ))
    story.append(Spacer(1, 5))
    
    # --- Job 3: Clip ---
    j3_header = [
        [
            Paragraph("<b>Commercial Advisor – Middle Market / High Potential</b> | <font color='#0284C7'><b>Clip</b></font>", job_title_style),
            Paragraph("07/2021 – 02/2025 | Cancún, Mexico", job_meta_style)
        ]
    ]
    t3 = Table(j3_header, colWidths=[376, 180])
    t3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t3)
    story.append(Paragraph(
        "• <b>Top Performer & Quota Overachievement:</b> Ranked in the <b>Top 12% nationally (#22 out of 184 executives)</b> in H1 2022; consistently exceeded monthly transactional quotas by <b>over 280% ($2.8M to $5.8M MXN average vs. $1.0M goal)</b>, earning 3rd place on the national performance podium.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Portfolio Volume & Deal Efficiency:</b> Built a consolidated portfolio yielding <b>$69.0M+ MXN (~$3.8M+ USD) in cumulative TPV</b>, with <b>75.3% self-generated via outbound hunting</b>. Achieved an average TPV per deal of $555K MXN (60% above segment benchmark).",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>High-Volume Enterprise Closings:</b> Successfully prospected and closed top regional accounts with high tourist/international customer inflows and multi-currency volume, including a luxury yacht charter ($14.5M MXN YTD TPV) and an adventure tourism operator ($20.0M MXN YTD TPV).",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>API & ISV Integrations:</b> Led complex commercial and technical integration negotiations with key software platforms (Bistrosoft, Profitroom, Odoo ERP), reducing merchant operational friction and securing near-zero client churn.",
        bullet_style
    ))
    story.append(Spacer(1, 5))
    
    # --- Job 4: JTI ---
    j4_header = [
        [
            Paragraph("<b>Account Executive · Southeast & Bajío</b> | <font color='#0284C7'><b>Japan Tobacco International (JTI)</b></font>", job_title_style),
            Paragraph("07/2018 – 12/2020 | Cancún & Aguascalientes, Mexico", job_meta_style)
        ]
    ]
    t4 = Table(j4_header, colWidths=[376, 180])
    t4.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t4)
    story.append(Paragraph(
        "• Led territorial Key Account Management (KAM) in the HORECA sector, achieving <b>+40% growth in Share of Opportunity</b> in Cancún and Riviera Maya vs. prior year.",
        bullet_style
    ))
    story.append(Paragraph(
        "• Expanded active commercial client base by <b>+35%</b>, negotiating direct distribution agreements with <b>100+ premium hotels and international hospitality chains</b>. Coordinated a 3-person field sales team in Bajío.",
        bullet_style
    ))
    story.append(Spacer(1, 6))
    
    # 5. EDUCATION & CONTINUOUS TRAINING
    add_section_header("Education & Continuous Training")
    
    edu_cell = [
        Paragraph("<b>Bachelor's Degree in Commercial Relations</b>", edu_title_style),
        Paragraph("<b>Licenciatura en Relaciones Comerciales (Titulado)</b>", edu_sub_style),
        Paragraph("Instituto Politécnico Nacional (IPN) — Mexico | 2014 – 2018", edu_sub_style)
    ]
    
    cert_cell = [
        Paragraph("• <b>McKinsey Forward Program</b> (McKinsey.org · 120h) — Adaptive leadership & problem solving.", cert_item_style),
        Paragraph("• <b>Growth 101</b> (Kurios · 30h) — B2B growth and rapid experimentation frameworks.", cert_item_style),
        Paragraph("• <b>Mastering Ventas</b> (Sales Professional · 70h) — B2B sales playbooks & SalesTech automation.", cert_item_style),
        Paragraph("• <b>SDR Course – First Meeting</b> (LATAM SDR Leaders · 16h) — Outbound cold prospecting.", cert_item_style)
    ]
    
    edu_table = Table([[edu_cell, cert_cell]], colWidths=[240, 316])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(edu_table)

    # Build PDF
    doc.build(story)
    
    # Verify Page count with PyMuPDF
    pdf_doc = fitz.open(local_pdf)
    page_count = len(pdf_doc)
    print(f"Generated Local PDF: {local_pdf}")
    print(f"Page Count: {page_count}")
    
    # Copy to Downloads
    shutil.copyfile(local_pdf, downloads_pdf)
    print(f"Copied to Downloads: {downloads_pdf}")
    
    # Render preview image of page 1
    page = pdf_doc.load_page(0)
    pix = page.get_pixmap(dpi=150)
    preview_path = r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\riviera-maya-payments\Antonio_Gutierrez_Jimenez_CV_Preview.png"
    pix.save(preview_path)
    print(f"Preview image saved: {preview_path}")

if __name__ == '__main__':
    generate_resume()
