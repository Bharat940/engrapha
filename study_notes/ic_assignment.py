"""
Indian Constitution (IT410) -- Assignment Answers (CO1-CO5)
UIT-RGPV (Autonomous) Bhopal | Semester IV | Session: Jan-June 2026
Run:    python ic_assignment_it410.py
Output: IC_Assignment_IT410.pdf
"""

from __future__ import annotations

import paperforge_notes as pn
import paperforge_diagrams as pd

# =============================================================================
#  THEME & GLOBAL FOOTER
# =============================================================================
pn.set_story([])
# Create print-optimized light theme using Times New Roman
# Create print-optimized light theme using Times New Roman (pure B&W, no greys, plain questions)
print_theme = pn.LIGHT.copy_with(
    name="Print Light",
    bg="#ffffff",
    surface="#ffffff",
    surface_alt="#ffffff",
    card_mid="#ffffff",
    text="#000000",
    text_dim="#000000",
    text_code="#000000",
    accent="#000000",
    accent2="#000000",
    accent_dim="#000000",
    accent_surface="#ffffff",
    cyan="#000000",
    green="#000000",
    green_bg="#ffffff",
    yellow="#000000",
    yellow_bg="#ffffff",
    red="#000000",
    red_bg="#ffffff",
    purple="#000000",
    purple_bg="#ffffff",
    white="#ffffff",
    border="#000000",
    table_hdr="#ffffff",
    table_bdr="#000000",
    code_bg="#ffffff",
    body_font="Times-Roman",
    heading_font="Times-Bold",
    size_body=10.0,
    size_question=12.0,
    double_page_border=True,
    page_border_margin=15.0,
    page_border_gap=3.0,
    page_border_color="#000000",
    show_headers=True,
    plain_questions=True,
)
pn.set_theme(print_theme)

pn.set_global_header(
    left="Indian Constitution",
    center="Semester –IV",
    right="Session-Jan-June 2026",
    y_offset=0.8,
    line_y_offset=0.85,
)

pn.set_global_footer(
    left="Name: Bharat Dangi",
    center="Enrollment no: 0101IT241013",
    show_page_num=True,
)

diag_theme = pd.DiagramTheme.from_notes_theme(pn.get_theme()).model_copy(
    update={
        "stack_colors": (
            "#ffffff",
            "#ffffff",
            "#ffffff",
            "#ffffff",
            "#ffffff",
            "#ffffff",
            "#ffffff",
        ),
        "stack_stroke": "#000000",
        "stack_text": "#000000",
        "stack_sublabel_text": "#000000",
        "bg": "#ffffff",
        "text": "#000000",
        "text_dim": "#000000",
        "surface": "#ffffff",
        "surface_alt": "#ffffff",
        "node_fill": "#ffffff",
        "node_stroke": "#000000",
        "node_text": "#000000",
        "edge_color": "#000000",
        "edge_label_color": "#000000",
        "line_color": "#000000",
        "font_name": "Times-Roman",
        "font_name_bold": "Times-Bold",
        "font_name_italic": "Times-Italic",
    }
)


# =============================================================================
#  COVER PAGE
# =============================================================================
pn.bookmark("Cover Page")
pn.suppress_header(page_only=True)
pn.suppress_footer(page_only=True)
pn.sp(15)

# Center the title card
pn.cover_card(
    "INDIAN CONSTITUTION -- ASSIGNMENT",
)
pn.sp(15)

# Centered logo
pn.image("RGPVLOGO.jpg", width=120, height=128)
pn.sp(20)

# Student details in a neat column format (borderless centered table)
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import ParagraphStyle

t_theme = pn.get_theme()
st_key = ParagraphStyle(
    "CoverKey",
    fontName="Times-Bold",
    fontSize=11,
    textColor=t_theme.rl(t_theme.text),
    alignment=2,  # Right aligned
)
st_val = ParagraphStyle(
    "CoverVal",
    fontName="Times-Roman",
    fontSize=11,
    textColor=t_theme.rl(t_theme.text),
    alignment=0,  # Left aligned
)

metadata = [
    [Paragraph("Name:", st_key), Paragraph("Bharat Dangi", st_val)],
    [Paragraph("Enrollment No.:", st_key), Paragraph("0101IT241013", st_val)],
    [Paragraph("Subject:", st_key), Paragraph("Indian Constitution", st_val)],
    [Paragraph("Subject Code:", st_key), Paragraph("IT-410", st_val)],
    [Paragraph("Instructor:", st_key), Paragraph("Dr Arpit Namdev", st_val)],
    [Paragraph("Batch:", st_key), Paragraph("2024-2028", st_val)],
    [Paragraph("Semester:", st_key), Paragraph("IVth Semester", st_val)],
    [Paragraph("Year:", st_key), Paragraph("IInd year", st_val)],
]

meta_table_style = TableStyle(
    [
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
    ]
)
meta_table = Table(metadata, colWidths=[150, 200], hAlign="CENTER")
meta_table.setStyle(meta_table_style)
pn.add(meta_table)

pn.sp(20)
pn.br()

pn.suppress_header(page_only=True)
pn.suppress_footer(page_only=True)
pn.toc(
    style="index",
    headers=["Q.no", "Question", "CO", "DOA", "DOS", "Page no", "Signature"],
    col_widths=["8%", "34%", "8%", "14%", "14%", "10%", "12%"],
    defaults={"doa": "/      /  2026", "dos": "18/06/2026"},
    hdr_bg_color="#ffffff",
    hdr_text_color="#000000",
)


# #############################################################################
#  ASSIGNMENT 1 -- CO1
# #############################################################################
pn.part_box("ASSIGNMENT 1 -- CO1: CONSTITUTION BASICS & STRUCTURE")

pn.bookmark(
    "Q1.1 -- What are the three lists under the Seventh Schedule of the Indian Constitution?"
)
pn.qbox(
    "Q1.1: What are the three lists under the Seventh Schedule of the Indian Constitution?"
)
pn.body(
    "The Seventh Schedule of the Constitution of India, in accordance with Article 246, distributes legislative powers between the Union government and the State governments. This distribution of power represents one of the core federal characteristics of the Indian polity. The schedule partitions legislative subjects into three distinct lists:"
)
pn.info_table(
    [
        "List Name",
        "Constitutional Provision",
        "Legislative Jurisdiction",
        "Number of Subjects",
        "Key Examples",
    ],
    [
        [
            "Union List (List I)",
            "Article 246(1)",
            "Exclusive power of Parliament",
            "Originally 97, now 100",
            "Defence, Foreign Affairs, Railways, Banking, Atomic Energy, Currency",
        ],
        [
            "State List (List II)",
            "Article 246(3)",
            "Exclusive power of State Legislatures",
            "Originally 66, now 61",
            "Police, Public Health, Sanitation, Agriculture, Local Government, Prisons",
        ],
        [
            "Concurrent List (List III)",
            "Article 246(2)",
            "Joint jurisdiction (Union & States)",
            "Originally 47, now 52",
            "Education, Forests, Marriage & Divorce, Trade Unions, Civil Procedure",
        ],
    ],
)
pn.section("Conflict Resolution and Doctrine of Repugnancy")
pn.body(
    "Under Article 254, if there is a conflict between a law enacted by Parliament and a law enacted by a State Legislature on a subject in the Concurrent List, the central law prevails. The state law becomes void to the extent of its repugnancy with the central law. However, if the state law has received the assent of the President of India, it may prevail in that particular state."
)
pn.section("Residuary Powers (Article 248)")
pn.body(
    "Subjects not explicitly mentioned in any of the three lists (such as Cyber Law, E-Commerce, and Artificial Intelligence) are classified as residuary powers. Article 248 vests the exclusive authority to legislate on residuary subjects solely in the Parliament of India, illustrating the unitary bias of the Indian federal structure."
)


pn.br()
pn.bookmark("Q1.2 -- Name the articles that deal with the Fundamental Duties.")
pn.qbox("Q1.2: Name the articles that deal with the Fundamental Duties.")
pn.body(
    "The Fundamental Duties of citizens are contained in <b>Part IV-A</b> of the Constitution of India, which consists of a single Article -- <b>Article 51A</b>. Unlike Fundamental Rights, these duties are non-justiciable in court, meaning a citizen cannot be directly punished by the judiciary for failing to perform them, unless there is a specific statutory law enacted by Parliament that penalizes such failure."
)
pn.section("Historical Evolution & Committees")
pn.bullet(
    [
        "<b>Swaran Singh Committee (1976):</b> Set up by the Congress Party during the National Emergency to make recommendations about fundamental duties. The committee suggested the inclusion of 8 duties, but the 42nd Amendment Act added 10 duties.",
        "<b>42nd Amendment Act, 1976:</b> Formally inserted Part IV-A and Article 51A into the Constitution, introducing the original 10 duties (clauses a to j).",
        "<b>86th Amendment Act, 2002:</b> Added the 11th duty under clause (k), which mandates parents or guardians to provide education opportunities to their children aged 6 to 14 years.",
        "<b>Verma Committee (1999):</b> Identified the existence of legal provisions for the implementation of some of the Fundamental Duties (e.g., Prevention of Insults to National Honour Act, Wildlife Protection Act, Representation of the People Act).",
    ]
)
pn.section("List of 11 Fundamental Duties under Article 51A")
pn.body("It shall be the duty of every citizen of India:")
pn.bullet(
    [
        "<b>(a)</b> To abide by the Constitution and respect its ideals and institutions, the National Flag and the National Anthem;",
        "<b>(b)</b> To cherish and follow the noble ideals which inspired our national struggle for freedom;",
        "<b>(c)</b> To uphold and protect the sovereignty, unity and integrity of India;",
        "<b>(d)</b> To defend the country and render national service when called upon to do so;",
        "<b>(e)</b> To promote harmony and the spirit of common brotherhood amongst all the people of India transcending religious, linguistic and regional or sectional diversities; to renounce practices derogatory to the dignity of women;",
        "<b>(f)</b> To value and preserve the rich heritage of our composite culture;",
        "<b>(g)</b> To protect and improve the natural environment including forests, lakes, rivers and wild life, and to have compassion for living creatures;",
        "<b>(h)</b> To develop the scientific temper, humanism and the spirit of inquiry and reform;",
        "<b>(i)</b> To safeguard public property and to abjure violence;",
        "<b>(j)</b> To strive towards excellence in all spheres of individual and collective activity so that the nation constantly rises to higher levels of endeavour and achievement;",
        "<b>(k)</b> Who is a parent or guardian to provide opportunities for education to his child or, as the case may be, ward between the age of six and fourteen years.",
    ]
)


pn.br()
pn.bookmark(
    "Q1.3 -- What is the article number that deals with the amendment procedure of the Indian constitution?"
)
pn.qbox(
    "Q1.3: What is the article number that deals with the amendment procedure of the Indian constitution?"
)
pn.body(
    "<b>Article 368</b> in <b>Part XX</b> of the Constitution of India vests the power in Parliament to amend the Constitution and lays down the detailed procedure for doing so. This article ensures that the Constitution remains a living document that can adapt to changing socio-economic and political realities, balancing the rigid and flexible characteristics of the state."
)
pn.section("Three Types of Amendment Procedures")
pn.body(
    "The amendment procedure under the Indian Constitution is categorized into three methods based on the significance of the provisions:"
)
pn.info_table(
    ["Amendment Type", "Scope / Application", "Voting Requirement", "Key Examples"],
    [
        [
            "Simple Majority of Parliament",
            "Provisions outside the scope of Article 368. Easy to amend.",
            "Majority of members present and voting in each House.",
            "Admission of new States, boundaries of existing States, citizenship acquisition.",
        ],
        [
            "Special Majority of Parliament",
            "Main amendment pathway under Article 368.",
            "50% of total membership of each House AND 2/3rd of members present and voting.",
            "Fundamental Rights, Directive Principles of State Policy (DPSP).",
        ],
        [
            "Special Majority + State Ratification",
            "Federally significant provisions under Article 368.",
            "Special majority of Parliament plus ratification by half of the State Legislatures.",
            "Election of the President, distribution of legislative powers, Article 368 itself.",
        ],
    ],
)
pn.section("Step-by-Step Amendment Bill Procedure")
pn.bullet(
    [
        "<b>Initiation:</b> An amendment bill can be introduced in either House of Parliament (Lok Sabha or Rajya Sabha) by any minister or private member, without requiring the prior permission of the President.",
        "<b>Passage:</b> The bill must be passed in each House by a special majority (or simple/state-ratified majority where applicable). There is no provision for a joint sitting in case of a deadlock between the two Houses.",
        "<b>Presidential Assent:</b> After being passed by both Houses (and ratified by states if required), the bill is presented to the President. Under the 24th Amendment Act of 1971, the President <i>must</i> give their assent and cannot withhold it or return the bill for reconsideration.",
    ]
)
pn.section("Limitations: The Basic Structure Doctrine")
pn.body(
    "In the landmark case of <b>Kesavananda Bharati v. State of Kerala (1973)</b>, the Supreme Court held that while Parliament has broad powers to amend any part of the Constitution under Article 368, it cannot alter or destroy its <i>Basic Structure</i>. Features like judicial review, supremacy of the Constitution, secularism, and federalism are immune to amendment."
)


pn.br()
pn.bookmark(
    "Q1.4 -- What are the three types of emergencies provided in the Indian Constitution?"
)
pn.qbox(
    "Q1.4: What are the three types of emergencies provided in the Indian Constitution?"
)
pn.body(
    "<b>Part XVIII</b> of the Constitution of India (Articles 352 to 360) contains the emergency provisions. These provisions enable the Central government to meet any abnormal situation effectively, turning the federal structure into a unitary one during times of crisis. The Constitution provides for three distinct types of emergencies:"
)
pn.info_table(
    [
        "Emergency Type",
        "Article",
        "Grounds for Proclamation",
        "Parliamentary Approval",
        "Duration & Effect",
    ],
    [
        [
            "National Emergency",
            "Article 352",
            "War, external aggression, or armed rebellion (amended by 44th Amendment from 'internal disturbance').",
            "Special majority in both Houses within 1 month.",
            "Indefinite (approved every 6 months). Suspends Article 19 automatically under Article 358.",
        ],
        [
            "President's Rule (State)",
            "Article 356",
            "Failure of constitutional machinery in a State (Article 356) or non-compliance with Union directions (Article 365).",
            "Simple majority in both Houses within 2 months.",
            "Maximum 3 years. Executive powers transfer to the Governor; state assembly is suspended or dissolved.",
        ],
        [
            "Financial Emergency",
            "Article 360",
            "Threat to the financial stability or credit of India or any part of its territory.",
            "Simple majority in both Houses within 2 months.",
            "Indefinite (does not require periodic renewal). Salaries of public officials (including judges) can be reduced.",
        ],
    ],
)
pn.section("Key Distinctions and Safeguards")
pn.bullet(
    [
        "<b>National Emergency (Art. 352):</b> Requires a written recommendation from the Cabinet (Prime Minister and other cabinet-rank ministers) to the President. This safeguard was introduced by the 44th Amendment Act of 1978 to prevent the unilateral proclamation of emergency.",
        "<b>President's Rule (Art. 356):</b> Often criticized for misuse by the ruling party at the Centre. In the <b>S.R. Bommai case (1994)</b>, the Supreme Court established guidelines, holding that the state assembly cannot be dissolved until Parliament approves the proclamation, and the proclamation is subject to judicial review.",
        "<b>Financial Emergency (Art. 360):</b> This is the only type of emergency that has never been declared in India since independence, even during the severe balance of payments crisis in 1991.",
    ]
)


pn.br()
pn.bookmark("Q1.5 -- List five salient features of the Indian Constitution.")
pn.qbox("Q1.5: List five salient features of the Indian Constitution.")
pn.body(
    "The Constitution of India is unique in its spirit and content. While it has borrowed features from various constitutions across the world, it is tailored to suit the specific socio-cultural realities of India. Below are five key salient features of the Indian Constitution explained in detail:"
)
pn.bullet(
    [
        "<b>1. Lengthiest Written Constitution:</b> It is the most detailed written constitution in the world. Originally in 1949, it had 395 Articles, 8 Schedules, and 22 Parts. Today, it has over 448 Articles, 12 Schedules, and 25 Parts. This detail is due to the vast geographical size of India, its cultural diversity, the inclusion of administrative details, and single constitutions for both the Union and the States (except historically Jammu & Kashmir).",
        "<b>2. Blend of Rigidity and Flexibility:</b> The Constitution is neither entirely rigid (like the US Constitution, which requires a very complex amendment process) nor entirely flexible (like the British Constitution, which can be amended by ordinary laws). Article 368 provides for three types of amendments, allowing some provisions to be amended by simple majority, others by special majority, and federally important ones by special majority plus state ratification.",
        "<b>3. Federal System with Unitary Bias:</b> The Constitution establishes a federal structure with a dual government polity, division of powers, written constitution, and supremacy of the constitution. However, it also contains strong unitary features such as a single constitution, single citizenship, appointment of State Governors by the President, all-India services (IAS, IPS), and emergency provisions. This has led scholars like K.C. Wheare to describe it as 'quasi-federal'.",
        "<b>4. Parliamentary Form of Government:</b> Modeled on the British Westminster system rather than the American presidential system. It is based on the principle of cooperation and coordination between the executive and legislative organs. Key features include the presence of nominal (President) and real (Prime Minister) executives, majority party rule, and collective responsibility of the executive (Council of Ministers) to the legislature (Lok Sabha).",
        "<b>5. Synthesis of Parliamentary Sovereignty and Judicial Supremacy:</b> It balances the British principle of parliamentary sovereignty (where parliament can make or unmake any law) and the American principle of judicial supremacy (where courts have the final power of judicial review). The Supreme Court of India can declare parliamentary laws unconstitutional through judicial review, but Parliament can amend major parts of the Constitution through Article 368 (limited by the Basic Structure Doctrine).",
    ]
)
pn.section("Additional Notable Features")
pn.body(
    "Other prominent characteristics include an integrated and independent judiciary (Supreme Court at the apex, followed by High Courts and subordinate courts), justiciable Fundamental Rights (Part III), non-justiciable Directive Principles of State Policy (Part IV), and a secular state concept where all religions are given equal protection and respect by the state."
)


pn.br()
pn.bookmark("Q1.6 -- What article of the constitution defines equality before law?")
pn.qbox("Q1.6: What article of the constitution defines equality before law?")
pn.body(
    "<b>Article 14</b> in <b>Part III</b> of the Constitution of India defines the fundamental right to equality. It states: 'The State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India.' This right is a cornerstone of Indian democracy and applies to all persons -- citizens and foreigners alike, as well as legal corporations."
)
pn.section("The Dual Concept of Article 14")
pn.body("Article 14 incorporates two distinct but complementary concepts of equality:")
pn.info_table(
    ["Concept", "Equality Before Law", "Equal Protection of the Laws"],
    [
        [
            "Origin",
            "Borrowed from the British constitution / common law.",
            "Borrowed from Section 1 of the 14th Amendment of the US Constitution.",
        ],
        [
            "Nature",
            "Negative concept (implies absence of privilege).",
            "Positive concept (implies equal treatment under equal circumstances).",
        ],
        [
            "Core Meaning",
            "No person is above the law. All individuals, rich or poor, official or private citizen, are subject to the ordinary law of the land administered by ordinary courts.",
            "Like should be treated alike, not unlike. The law must apply equally to persons in similar circumstances, allowing the state to make special laws for different groups.",
        ],
        [
            "Application",
            "Ensures legal subjection of all citizens to the common rule of law.",
            "Enables protective discrimination (affirmative action, reservations, tax slabs).",
        ],
    ],
)
pn.section("Doctrine of Reasonable Classification")
pn.body(
    "While Article 14 forbids class legislation, it permits reasonable classification of persons, objects, and transactions by the legislature. To be constitutional, any classification must pass the <b>Twin Test</b> established by the Supreme Court:"
)
pn.bullet(
    [
        "<b>Intelligible Differentia:</b> There must be a clear and understandable difference distinguishing those grouped together from those left out.",
        "<b>Rational Nexus:</b> The differentia must have a direct, logical relation to the object sought to be achieved by the legislation.",
    ]
)
pn.section("New Dimension: Non-Arbitrariness")
pn.body(
    "In cases like <b>E.P. Royappa v. State of Tamil Nadu (1974)</b> and <b>Maneka Gandhi v. Union of India (1978)</b>, the Supreme Court expanded Article 14, holding that equality is a dynamic concept. Any state action that is arbitrary, unfair, or discriminatory is a direct violation of Article 14, regardless of classification tests."
)


pn.br()
pn.bookmark("Q1.7 -- What year was the 73rd and 74th constitutional amendment passed?")
pn.qbox("Q1.7: What year was the 73rd and 74th constitutional amendment passed?")
pn.body(
    "The <b>73rd and 74th Constitutional Amendment Acts</b> were passed by the Parliament in the year <b>1992</b>. These landmark amendments gave constitutional status to local self-governments in India, fulfilling the Gandhian dream of decentralized power. The 73rd Amendment came into force on <b>24 April 1993</b> (celebrated as National Panchayati Raj Day), and the 74th Amendment came into force on <b>1 June 1993</b>."
)
pn.section("Key Features of 73rd Amendment (Panchayati Raj)")
pn.body(
    "The 73rd Amendment added <b>Part IX</b> to the Constitution, titled 'The Panchayats', and the <b>11th Schedule</b> containing 29 functional subjects. It mandated a standardized three-tier structure:"
)
# Diagram: LayeredStack for Panchayati Raj
stack_pr = pd.LayeredStack(
    width=pn.CW * 0.75,
    height=185,
    theme=diag_theme,
    caption="Fig 1.1: Three-Tier Structure of Panchayati Raj System",
)
stack_pr.layer(
    "Zila Parishad (District Level)",
    sublabel="Apex body overseeing developmental activities across the district",
)
stack_pr.layer(
    "Panchayat Samiti (Block Level)",
    sublabel="Intermediate coordinating body executing plans at the taluka/block level",
)
stack_pr.layer(
    "Gram Panchayat (Village Level)",
    sublabel="Grassroots administrative body directly elected by the Gram Sabha",
)
pn.story.extend(stack_pr.as_flowable())
pn.sp(4)
pn.section("Key Features of 74th Amendment (Municipalities)")
pn.body(
    "The 74th Amendment added <b>Part IX-A</b>, titled 'The Municipalities', and the <b>12th Schedule</b> containing 18 functional subjects. It created three types of urban local bodies:"
)
pn.bullet(
    [
        "<b>Nagar Panchayats:</b> For transitional areas transitioning from rural to urban.",
        "<b>Municipal Councils:</b> For smaller urban areas.",
        "<b>Municipal Corporations:</b> For larger urban areas (metropolitan cities).",
    ]
)
pn.section("Common Mandatory Institutional Provisions")
pn.bullet(
    [
        "<b>Regular Elections:</b> Mandatory elections every 5 years; if dissolved earlier, elections must be held within 6 months.",
        "<b>Reservations:</b> Mandatory reservation of seats for SCs and STs in proportion to their population, and not less than 1/3rd of total seats reserved for women (including chairperson posts).",
        "<b>State Commissions:</b> Established the State Election Commission to conduct local polls, and the State Finance Commission every 5 years to recommend financial devolution.",
    ]
)


pn.br()
pn.bookmark(
    "Q1.8 -- What part of the constitution contains the directive principles of state policy?"
)
pn.qbox(
    "Q1.8: What part of the constitution contains the directive principles of state policy?"
)
pn.body(
    "The Directive Principles of State Policy (DPSP) are contained in <b>Part IV</b> (Articles 36 to 51) of the Constitution of India. Borrowed from the Irish Constitution (which had borrowed them from Spain), these principles represent the socio-economic goals of the Indian state. Article 37 declares that these principles are non-justiciable (not enforceable by any court), but are 'fundamental in the governance of the country' and it is the duty of the State to apply them in making laws."
)
pn.section("Classification of Directive Principles")
pn.body(
    "Although the Constitution does not formally classify DPSPs, they are categorized into three broad philosophical groups based on their content and objectives:"
)
pn.info_table(
    ["Classification", "Core Objective", "Key Articles & Provisions"],
    [
        [
            "Socialistic Principles",
            "Aims to establish a modern welfare state, remove inequalities, and ensure social justice.",
            "Art. 38 (minimize income inequality), Art. 39 (equal pay for equal work), Art. 39A (free legal aid), Art. 41 (right to work).",
        ],
        [
            "Gandhian Principles",
            "Represents the program of reconstruction enunciated by Mahatma Gandhi during the national movement.",
            "Art. 40 (organize village panchayats), Art. 43 (promote cottage industries), Art. 47 (prohibit intoxicating drinks/drugs).",
        ],
        [
            "Liberal-Intellectual Principles",
            "Focuses on liberal democracy, modern administration, and international relations.",
            "Art. 44 (Uniform Civil Code), Art. 45 (early childhood care/education), Art. 50 (separate judiciary from executive), Art. 51 (promote peace).",
        ],
    ],
)
pn.section("Relationship and Conflict with Fundamental Rights")
pn.body(
    "The relationship between Fundamental Rights (Part III) and DPSPs (Part IV) has evolved through key judicial rulings:"
)
pn.bullet(
    [
        "<b>Champakam Dorairajan (1951):</b> The Supreme Court ruled that Fundamental Rights prevail over Directive Principles in case of conflict. DPSPs must run as subsidiary to Part III.",
        "<b>25th Amendment (1971):</b> Introduced Article 31C, stating that laws passed to implement socialistic DPSPs (Art 39b & c) cannot be declared void for violating equality (Art 14) or freedoms (Art 19).",
        "<b>Minerva Mills Case (1980):</b> The Supreme Court held that the Constitution is founded on the bedrock of the balance between Part III and Part IV. They are like two wheels of a chariot, and one cannot be given absolute primacy over the other.",
    ]
)


pn.br()
pn.bookmark(
    "Q1.9 -- What is the full name of the document that became the foundation of the Indian Constitution?"
)
pn.qbox(
    "Q1.9: What is the full name of the document that became the foundation of the Indian Constitution?"
)
pn.body(
    "The single most important document that became the administrative foundation of the Indian Constitution is the <b>Government of India Act, 1935</b>. Passed by the British Parliament, it was the longest and most detailed act enacted at the time. Nearly 250 provisions -- almost 60% of the text of the Constitution of India adopted in 1949 -- were borrowed directly or adapted from this Act, earning it the label of the 'blueprint' or 'structural skeleton' of the Constitution."
)
pn.section("Key Administrative Features Borrowed from the 1935 Act")
pn.bullet(
    [
        "<b>Federal Scheme:</b> The Act proposed an All-India Federation consisting of British provinces and princely states. While the federation never materialized due to princely states refusing to join, the structural division of powers was adopted in the Constitution.",
        "<b>Three Legislative Lists:</b> The division of legislative subjects into Federal, Provincial, and Concurrent lists under the 1935 Act became the direct basis for the Union, State, and Concurrent lists of the Seventh Schedule.",
        "<b>Office of the Governor:</b> The position of the Governor as the executive head of the provinces, acting on the aid and advice of ministers, was retained as the model for the State Governor in independent India.",
        "<b>Emergency Provisions:</b> Section 102 (permitting central legislation in case of emergency) and Section 93 (allowing Governor to take over provincial administration in case of failure of constitutional machinery) became the direct precursors to Articles 352 and 356.",
        "<b>Public Service Commissions:</b> Established a Federal Public Service Commission and Provincial Public Service Commissions, which became the Union Public Service Commission (UPSC) and State Public Service Commissions (SPSC) under Article 315.",
    ]
)
pn.section("Other Historical Foundations")
pn.body(
    "In addition to the 1935 Act, the constitutional assembly (headed by Dr. Rajendra Prasad and drafted by the committee chaired by Dr. B.R. Ambedkar) adopted the formally titled <b>'Constitution of India'</b> on 26 November 1949. The philosophical foundation was provided by the <b>'Objective Resolution'</b> moved by Jawaharlal Nehru on 13 December 1946, which later became the basis of the Preamble."
)


pn.br()
pn.bookmark(
    "Q1.10 -- What article of the constitution defines the right to life and personal liberty?"
)
pn.qbox(
    "Q1.10: What article of the constitution defines the right to life and personal liberty?"
)
pn.body(
    "<b>Article 21</b> in <b>Part III</b> of the Constitution of India defines the right to life and personal liberty. It states: 'No person shall be deprived of his life or personal liberty except according to procedure established by law.' This right is considered the most fundamental of all rights, available to both citizens and non-citizens. Crucially, under Article 359 (amended by 44th Amendment), Article 21 cannot be suspended even during a National Emergency."
)
pn.section("The Judicial Evolution of Article 21")
pn.body(
    "The interpretation of Article 21 has undergone a major transition through two landmark cases:"
)
pn.info_table(
    ["Case Name", "Judicial Interpretation", "Procedure Standard", "Core Ruling"],
    [
        [
            "A.K. Gopalan v. State of Madras (1950)",
            "Narrow, literal interpretation. Right is protected only against arbitrary executive action, not against arbitrary legislative action.",
            "Procedure Established by Law (lex): As long as a law exists and the prescribed procedure is followed, the courts cannot check the fairness of the law itself.",
            "Prevention detention of the petitioner was upheld as valid since it followed statutory procedure.",
        ],
        [
            "Maneka Gandhi v. Union of India (1978)",
            "Broad, purposive interpretation. Right is protected against both arbitrary executive action and arbitrary legislative action.",
            "Due Process of Law (jus): The procedure depriving a person of life or liberty must be 'fair, just, and reasonable' and not arbitrary, fanciful, or oppressive.",
            "The passport confiscation was struck down as it violated the principles of natural justice and fairness.",
        ],
    ],
)
pn.section("Unenumerated Rights under Article 21")
pn.body(
    "By interpreting 'Life' not as mere animal existence but as living with human dignity, the Supreme Court has read several implied rights into Article 21:"
)
pn.bullet(
    [
        "<b>Right to Privacy:</b> Declared a fundamental right under Art. 21 in <i>K.S. Puttaswamy v. Union of India (2017)</i>.",
        "<b>Right to Clean Environment:</b> Protection against pollution and hazardous industries (<i>M.C. Mehta v. Union of India</i>).",
        "<b>Right to Education:</b> Free and compulsory education for children aged 6-14 (read in Art. 21 and subsequently enacted as Art. 21A by 86th Amendment).",
        "<b>Right to Livelihood:</b> Protection against arbitrary deprivation of work (<i>Olga Tellis v. Bombay Municipal Corporation</i>).",
        "<b>Other Rights:</b> Right to shelter, right to speedy trial, right to free legal aid, right to medical care, and right to travel abroad.",
    ]
)

pn.br()
pn.part_box("ASSIGNMENT 2 -- CO2: STRUCTURE, RIGHTS & PROCESSES")

pn.bookmark(
    "Q2.1 -- Explain the difference between constitutional law and constitutionalism."
)
pn.qbox(
    "Q2.1: Explain the difference between constitutional law and constitutionalism."
)
pn.body(
    "While the terms 'Constitution', 'Constitutional Law', and 'Constitutionalism' are closely related, they represent distinct concepts in political science and jurisprudence. A country may possess a constitution and a body of constitutional law, yet completely lack the spirit of constitutionalism if the rulers do not respect the limits placed upon their power."
)
pn.section("Detailed Definitions")
pn.bullet(
    [
        "<b>Constitutional Law:</b> The body of legal rules, doctrines, and judicial precedents that defines the structure, powers, and functions of the legislative, executive, and judicial organs of a state, and regulates the relationship between the government and its citizens. It is the formal legal manifestation of the Constitution.",
        "<b>Constitutionalism:</b> A political philosophy and doctrine which asserts that government authority must be derived from and limited by a body of fundamental law. It is the concept of 'limited government' and the 'rule of law' as opposed to arbitrary rule. It dictates that government must operate within strict legal boundaries.",
    ]
)
pn.section("Comparison Matrix")
pn.info_table(
    ["Dimension", "Constitutional Law", "Constitutionalism"],
    [
        [
            "Nature & Form",
            "Written text, amendments, statutory laws, and judicial precedents (objective rules).",
            "Political philosophy, value system, and institutional culture (subjective spirit).",
        ],
        [
            "Primary Goal",
            "Establishes government machinery, divides power, and enumerates rights.",
            "Restricts government power, prevents despotism, and protects individual liberty.",
        ],
        [
            "Key Question",
            "What are the rules and laws governing the state?",
            "Are those rules actually respected and do they limit political authority?",
        ],
        [
            "Status in Despotisms",
            "A dictatorship can have constitutional law on paper (e.g., Soviet Constitution).",
            "Despotisms cannot have constitutionalism since there are no effective limits on power.",
        ],
    ],
)
pn.section("Core Elements of Constitutionalism")
pn.body(
    "Constitutionalism in a modern democracy like India is sustained through several institutional mechanisms:"
)
pn.bullet(
    [
        "<b>Written Constitution:</b> Provides a clear, supreme legal framework that binds all state organs.",
        "<b>Separation of Powers:</b> Prevents concentration of power by distributing it among the Legislature, Executive, and Judiciary, coupled with a system of checks and balances.",
        "<b>Rule of Law:</b> Ensures that the law is supreme, all citizens are equal before it, and executive action is not arbitrary.",
        "<b>Judicial Review:</b> Empowers independent courts to declare legislative and executive actions unconstitutional if they exceed power limits.",
        "<b>Fundamental Rights:</b> Guarantees justiciable rights to citizens, creating an area of liberty free from state intrusion.",
    ]
)


pn.br()
pn.bookmark(
    "Q2.2 -- Summarize the historical influences that shaped the Indian Constitution."
)
pn.qbox(
    "Q2.2: Summarize the historical influences that shaped the Indian Constitution."
)
pn.body(
    "The Constitution of India was not drafted in a vacuum. It was the product of a long historical process, reflecting both the administrative legacy of British colonial rule and the democratic ideals championed during the Indian national movement. The framers, led by the Drafting Committee chaired by Dr. B.R. Ambedkar, carefully analyzed and borrowed structural, philosophical, and administrative features from various global models, adapting them to the Indian context."
)
pn.section("Comparative Borrowings from Global Constitutions")
pn.info_table(
    ["Country Source", "Borrowed Features in the Indian Constitution"],
    [
        [
            "Government of India Act, 1935",
            "Federal scheme, office of Governor, judiciary structure, Public Service Commissions, administrative details, emergency provisions.",
        ],
        [
            "United Kingdom",
            "Parliamentary form of government, rule of law, legislative procedure, single citizenship, cabinet system, bicameralism, prerogative writs.",
        ],
        [
            "United States of America",
            "Justiciable Fundamental Rights, independence of the judiciary, judicial review, impeachment of the President, removal of SC/HC judges, office of Vice-President.",
        ],
        [
            "Ireland",
            "Directive Principles of State Policy (DPSP), nomination of members to Rajya Sabha, method of election of the President.",
        ],
        [
            "Canada",
            "Federation with a strong Centre, vesting of residuary powers in the Centre, appointment of state Governors by the Centre, advisory jurisdiction of the Supreme Court.",
        ],
        [
            "Weimar Republic (Germany)",
            "Suspension of Fundamental Rights during emergency.",
        ],
        [
            "Soviet Union (USSR)",
            "Fundamental Duties, ideals of justice (social, economic, and political) in the Preamble.",
        ],
        [
            "Australia",
            "Concurrent List, freedom of trade, commerce and intercourse, joint sitting of the two Houses of Parliament.",
        ],
        [
            "South Africa & Japan",
            "Procedure for amendment of the Constitution (Art. 368), election of members of Rajya Sabha (SA); 'procedure established by law' (Japan).",
        ],
    ],
)
pn.section("Impact of the Nationalist Freedom Struggle")
pn.body(
    "The values of the freedom struggle directly shaped the Preamble, Fundamental Rights, and DPSPs. The <b>Motilal Nehru Report (1928)</b> had demanded a bill of rights, while the <b>Karachi Resolution (1931)</b> of the Indian National Congress outlined a socio-economic program advocating civil liberties, equality, and protection of labor, which became the blueprint for Parts III and IV."
)


pn.br()
pn.bookmark(
    "Q2.3 -- Describe the relationship between Fundamental Rights and Directive Principles."
)
pn.qbox(
    "Q2.3: Describe the relationship between Fundamental Rights and Directive Principles."
)
pn.body(
    "The relationship between Fundamental Rights (Part III) and Directive Principles of State Policy (Part IV) forms the moral and legal core of the Indian Constitution. Together, they are described by Granville Austin as the 'conscience of the Constitution'. While Part III guarantees civil liberties and political democracy, Part IV directs the state to establish socio-economic democracy. Their relationship has evolved from conflict to harmony through decades of judicial interpretation."
)
pn.section("Comparison of Key Differences")
pn.info_table(
    ["Dimension", "Fundamental Rights (Part III)", "Directive Principles (Part IV)"],
    [
        [
            "Justiciability",
            "Justiciable -- directly enforceable in court under Article 32 or 226 if violated.",
            "Non-justiciable -- not enforceable by courts; no legal action lies for their non-implementation.",
        ],
        [
            "Nature of Mandate",
            "Negative mandates (restrain the State from taking arbitrary actions against citizens).",
            "Positive mandates (direct the State to take active measures for welfare).",
        ],
        [
            "Objective",
            "Establish political democracy by protecting individual liberty.",
            "Establish social and economic democracy to build a welfare state.",
        ],
        [
            "Scope",
            "Focuses on individual rights and freedom.",
            "Focuses on societal welfare and collective interest.",
        ],
    ],
)
pn.section("Judicial Evolution of the Relationship")
pn.bullet(
    [
        "<b>Phase 1: Primacy of FRs (State of Madras v. Champakam Dorairajan, 1951):</b> The Supreme Court ruled that DPSPs are subsidiary to Fundamental Rights. If a law implementing DPSP violates a Fundamental Right, the law is void.",
        "<b>Phase 2: Legislative Backlash & 25th Amendment (1971):</b> Parliament inserted Article 31C to protect laws implementing socialistic DPSPs (Art 39b & c) from challenge under Articles 14 and 19.",
        "<b>Phase 3: The Doctrine of Harmony (Minerva Mills v. Union of India, 1980):</b> The Supreme Court held that the Constitution is built on the harmony and balance between Part III and Part IV. They are complementary. Giving primacy to one over the other would destroy the basic structure.",
        "<b>Phase 4: Modern Synthesis:</b> Courts now interpret Fundamental Rights in the light of Directive Principles. For example, the right to education (Art 21A) was read into Article 21 by referencing the directive under Article 45.",
    ]
)


pn.br()
pn.bookmark(
    "Q2.4 -- Explain the concept of federal structure with a unitary bias in the Indian context."
)
pn.qbox(
    "Q2.4: Explain the concept of federal structure with a unitary bias in the Indian context."
)
pn.body(
    "Article 1 of the Constitution describes India as a 'Union of States'. The Constitution establishes a federal system of government but endows it with a strong centralizing character. This unique design led constitutional expert K.C. Wheare to classify the Indian Constitution as <b>'quasi-federal'</b>. It is federal in structure but unitary in spirit, designed to maintain national integrity and security amidst extreme regional diversity."
)
pn.section("Federal Features of the Indian Constitution")
pn.bullet(
    [
        "<b>Dual Polity:</b> Clear division of government into the Union at the Centre and the States at the periphery, each exercising authority in their respective spheres.",
        "<b>Written Constitution:</b> A supreme, written document that serves as the source of power for both the Centre and the States.",
        "<b>Supremacy of the Constitution:</b> Any law passed by the Centre or States must conform to the Constitution; otherwise, it is declared void by the judiciary.",
        "<b>Rigidity:</b> Amendment of federal provisions requires ratification by half of the State Legislatures.",
        "<b>Independent Judiciary:</b> An independent judicial branch (Supreme Court) acts as the arbiter of disputes between the Centre and States.",
    ]
)
pn.section("Unitary Features (Unitary Bias)")
pn.bullet(
    [
        "<b>Strong Centre:</b> The Union List has more subjects, more important subjects, and residuary powers (Article 248) are vested in the Centre.",
        "<b>Single Constitution & Citizenship:</b> Unlike the US, where states have separate constitutions and dual citizenship, Indian citizens have only one citizenship and follow a single integrated constitution.",
        "<b>Appointment of Governor (Article 155):</b> The Governor of a State is appointed by the President and acts as an agent of the Centre, often leading to federal friction.",
        "<b>Emergency Provisions (Part XVIII):</b> During an emergency, the Centre gains control over state administrations without formal amendment.",
        "<b>All-India Services (Article 312):</b> IAS and IPS officers are recruited by the Centre but posted in States, ensuring central administrative control.",
        "<b>Integrated Judiciary:</b> A single hierarchy of courts (SC at the apex) enforces both central and state laws, unlike separate federal and state courts in the US.",
    ]
)


pn.br()
pn.bookmark("Q2.5 -- How does the parliamentary form of government function in India?")
pn.qbox("Q2.5: How does the parliamentary form of government function in India?")
pn.body(
    "The Constitution of India adopts the parliamentary form of government, also known as the Cabinet government or the Westminster model, at both the Centre and in the States. Based on the principle of cooperation and coordination between the executive and legislative branches, it differs fundamentally from the presidential system which is based on strict separation of powers."
)
pn.section("Key Functional Characteristics")
pn.bullet(
    [
        "<b>1. Nominal and Real Executives:</b> The President of India is the nominal executive (de jure head / head of state), while the Prime Minister is the real executive (de facto head / head of government). Executive decisions are taken in the President's name but on the aid and advice of the Council of Ministers (Article 74).",
        "<b>2. Majority Party Rule:</b> The political party that secures a majority of seats in the Lok Sabha (lower house of Parliament) forms the government. The leader of this party is appointed as the Prime Minister by the President.",
        "<b>3. Collective Responsibility (Article 75):</b> This is the cardinal principle of parliamentary democracy. The Council of Ministers is collectively responsible to the Lok Sabha. They stand or fall together -- if a No-Confidence Motion is passed in the Lok Sabha, the entire cabinet must resign.",
        "<b>4. Membership in Legislature:</b> Ministers must be members of Parliament. If a non-member is appointed as a minister, they must secure a seat in either House of Parliament within 6 consecutive months, or they cease to be a minister.",
        "<b>5. Prime Ministerial Leadership:</b> The Prime Minister plays a pivotal role in the cabinet system. As the head of the Council of Ministers, leader of the House, and chief advisor to the President, the Prime Minister exercises supreme executive authority.",
    ]
)
# Diagram: LayeredStack for Organs of Government
stack_organs = pd.LayeredStack(
    width=pn.CW * 0.75,
    height=185,
    theme=diag_theme,
    caption="Fig 2.1: Relationship and Functions of government organs",
)
stack_organs.layer(
    "Legislature",
    sublabel="Parliament (Lok Sabha & Rajya Sabha) -- Enacts and Frames Laws",
)
stack_organs.layer(
    "Executive",
    sublabel="President, PM & Council of Ministers -- Enforces and Implements Laws",
)
stack_organs.layer(
    "Judiciary",
    sublabel="Supreme Court, High Courts & Subordinate Courts -- Interprets Laws & Resolves Disputes",
)
pn.story.extend(stack_organs.as_flowable())
pn.sp(4)


pn.br()
pn.bookmark("Q2.6 -- Explain the process of amending the Indian Constitution.")
pn.qbox("Q2.6: Explain the process of amending the Indian Constitution.")
pn.body(
    "The amendment process under the Indian Constitution, governed by <b>Article 368</b> (Part XX), is a unique blend of rigidity and flexibility. It is designed to allow constitutional growth while protecting the foundational values of the republic from temporary majoritarian impulses."
)
pn.section("Detailed Step-by-Step Procedure")
pn.bullet(
    [
        "<b>1. Introduction:</b> An amendment bill can be initiated only by the introduction of a bill in either House of Parliament (Lok Sabha or Rajya Sabha). It cannot be introduced in state legislatures.",
        "<b>2. Who Can Introduce:</b> The bill can be introduced either by a minister (Government Bill) or by a private member (Private Member Bill), and does not require the prior permission of the President.",
        "<b>3. Voting in each House:</b> The bill must be passed in each House of Parliament by a <b>Special Majority</b> -- a majority of the total membership of that House and a majority of not less than two-thirds of the members of that House present and voting.",
        "<b>4. No Joint Sitting:</b> If there is a disagreement between the two Houses, there is no provision for holding a joint sitting. The bill must be passed by both Houses separately; otherwise, it defeats.",
        "<b>5. State Ratification:</b> If the bill seeks to amend the federal provisions of the Constitution (e.g., election of President, division of powers, Supreme Court), it must also be ratified by the legislatures of at least half of the States by a simple majority.",
        "<b>6. Presidential Assent:</b> After being passed by both Houses (and ratified by states if needed), the bill is presented to the President who <i>must</i> give assent. The President cannot withhold assent or return the bill for reconsideration.",
    ]
)
pn.section("Categories of Amendments")
pn.body(
    "Article 368 specifies two types of amendments (Special Majority, and Special Majority + State Ratification). However, some other provisions of the Constitution can be amended by a simple majority of Parliament (outside the scope of Article 368), such as the creation of new states, abolition of legislative councils, and rules of procedure in Parliament."
)


pn.br()
pn.bookmark("Q2.7 -- What are the grounds for imposing a National Emergency?")
pn.qbox("Q2.7: What are the grounds for imposing a National Emergency?")
pn.body(
    "A National Emergency is proclaimed under <b>Article 352</b> of the Constitution of India when the security of India or any part of its territory is threatened. Under Article 352, the President can declare a National Emergency on three specific grounds:"
)
pn.bullet(
    [
        "<b>1. War:</b> When there is an active, formal state of war between India and another country.",
        "<b>2. External Aggression:</b> When there is unilateral aggression/hostility by a foreign power against India, short of a formal declaration of war.",
        "<b>3. Armed Rebellion:</b> When there is an internal armed insurrection threatening the state. Originally, the Constitution used the term 'internal disturbance'. However, because of its vagueness and potential for abuse, the <b>44th Amendment Act of 1978</b> replaced it with 'armed rebellion'.",
    ]
)
pn.section("Key Classifications & Procedural Safeguards")
pn.bullet(
    [
        "<b>External vs Internal Emergency:</b> An emergency declared on the grounds of 'war' or 'external aggression' is called an 'External Emergency'. An emergency declared on the grounds of 'armed rebellion' is called an 'Internal Emergency'.",
        "<b>Cabinet Consent:</b> The President can proclaim a National Emergency only after receiving a written recommendation from the Cabinet (Prime Minister and other cabinet-rank ministers), ensuring collective decision-making.",
        "<b>Parliamentary Approval:</b> The proclamation must be approved by both Houses of Parliament within <b>1 month</b> (originally 2 months) by a special majority (majority of total membership and 2/3rd of members present and voting).",
        "<b>Judicial Review:</b> In the <i>Minerva Mills case (1980)</i>, the Supreme Court ruled that a proclamation of National Emergency can be challenged in court if it is based on malafide or irrelevant grounds.",
    ]
)


pn.br()
pn.bookmark("Q2.8 -- Explain the significance of Local Self Government in India.")
pn.qbox("Q2.8: Explain the significance of Local Self Government in India.")
pn.body(
    "Local Self-Government, constitutionalized through the 73rd and 74th Amendment Acts of 1992, represents the third tier of governance in the Indian federal structure (Panchayats in rural areas and Municipalities in urban areas). Its significance lies in translating the concept of democratic decentralization into grassroots reality."
)
pn.section("Key Aspects of Significance")
pn.bullet(
    [
        "<b>1. Democratic Decentralization:</b> It shifts power from centralized state capitals and New Delhi directly to the local community, promoting participatory democracy where citizens are directly involved in planning and executing local schemes.",
        "<b>2. Administrative Efficiency:</b> Local problems (sanitation, primary education, local water supply, rural roads) are best understood and solved by local representatives, rather than distant bureaucrats who lack local contextual knowledge.",
        "<b>3. Empowerment of Weaker Sections:</b> Mandatory reservation of seats for Scheduled Castes (SCs), Scheduled Tribes (STs), and women (not less than 1/3rd) has transformed rural leadership. It has empowered millions of women and backward-class citizens, giving them formal political agency.",
        "<b>4. Training Ground for Leadership:</b> Local bodies act as a political training ground for grassroots leaders, helping them build leadership skills before entering state assemblies or Parliament.",
        "<b>5. Local Resource Mobilization:</b> Local bodies can levy taxes, duties, and fees, encouraging local self-reliance and community-based resource management.",
    ]
)
pn.section("Core Challenges Faced")
pn.body(
    "Despite its significance, local self-government faces structural challenges known as the <b>'Three Fs'</b> deficit: inadequate <b>Funds</b> (heavy dependence on state grants), incomplete devolution of <b>Functions</b> by state governments, and lack of trained administrative <b>Functionaries</b> to execute policies."
)


pn.br()
pn.bookmark(
    "Q2.9 -- Describe the scope of the right to freedom of speech and expression."
)
pn.qbox("Q2.9: Describe the scope of the right to freedom of speech and expression.")
pn.body(
    "<b>Article 19(1)(a)</b> in Part III of the Constitution of India guarantees to all citizens the right to freedom of speech and expression. It is considered one of the most vital civil liberties, enabling the free exchange of ideas and opinions which is the lifeblood of a democratic society. Its scope has been significantly expanded through judicial interpretation, but it is subject to reasonable restrictions under Article 19(2)."
)
pn.section("Expanded Scope of Article 19(1)(a)")
pn.body(
    "While the text is concise, the Supreme Court has read several 'unenumerated' rights into its scope:"
)
pn.bullet(
    [
        "<b>Freedom of Press:</b> The right to print, publish, and circulate news without arbitrary state interference (<i>Romesh Thapar case</i>).",
        "<b>Right to Information (RTI):</b> The right to know about government actions and obtain public records (implied in the freedom to receive information).",
        "<b>Freedom of Silence:</b> The right not to speak or be forced to express an opinion, as protected in the national anthem case (<i>Bijoe Emmanuel v. State of Kerala</i>).",
        "<b>Commercial Speech:</b> Right of advertising and business expression, subject to reasonable regulation.",
        "<b>Right to Expression via Internet:</b> Access to the internet and expression on digital platforms is protected (<i>Shreya Singhal case, 2015</i>).",
    ]
)
pn.section("Reasonable Restrictions (Article 19(2))")
pn.body(
    "The right to free speech is not absolute. Under Article 19(2), the state can impose reasonable restrictions on only <b>eight specific grounds</b>:"
)
pn.info_table(
    ["Ground for Restriction", "Core Purpose", "Example Scenario"],
    [
        [
            "Sovereignty & Integrity of India",
            "To prevent secessionist speech or acts threatening national unity.",
            "Speech advocating partition or armed rebellion against the state.",
        ],
        [
            "Security of the State",
            "To protect against espionage, war, or rebellion.",
            "Disclosing military secrets or advocating violent overthrow of government.",
        ],
        [
            "Public Order",
            "To prevent riots, communal violence, or public disturbance.",
            "Hate speech inciting communal clashes in a sensitive area.",
        ],
        [
            "Decency or Morality",
            "To regulate obscenity and protect public morals.",
            "Banning highly obscene publications or public displays.",
        ],
        [
            "Defamation & Contempt of Court",
            "To protect individual reputation and maintain dignity of courts.",
            "Making false damaging claims about someone; disobeying court orders.",
        ],
        [
            "Friendly relations with foreign states",
            "To prevent diplomatic embarrassment.",
            "Inciting public hostility against a visiting head of state.",
        ],
    ],
)


pn.br()
pn.bookmark("Q2.10 -- Explain the importance of the right to constitutional remedies.")
pn.qbox("Q2.10: Explain the importance of the right to constitutional remedies.")
pn.body(
    "<b>Article 32</b> of the Constitution of India guarantees the right to move the Supreme Court for the enforcement of Fundamental Rights. Dr. B.R. Ambedkar famously declared Article 32 as <b>'the heart and soul of the Constitution'</b>, stating that without it, the Constitution would be a nullity. A declaration of rights on paper is meaningless without an effective mechanism for their enforcement against state excesses."
)
pn.section("Why Article 32 is Critically Important")
pn.bullet(
    [
        "<b>1. Justiciability of Rights:</b> Article 32 makes the Fundamental Rights justiciable. It transforms moral and legal declarations into enforceable commands.",
        "<b>2. Supreme Court as Guard and Guarantor:</b> It appoints the Supreme Court as the protector of citizens' rights, providing a direct channel of justice without going through lengthy lower court appeals.",
        "<b>3. Fundamental Right itself:</b> The right to petition the Supreme Court for enforcement of rights is <i>itself</i> a Fundamental Right. Parliament cannot take away this right by ordinary legislation, and it is part of the Basic Structure.",
        "<b>4. Power of Judicial Review:</b> It vests the Supreme Court with the power to strike down executive orders and legislative acts that violate Part III.",
    ]
)
pn.section("The Five Constitutional Writs")
pn.body(
    "Under Article 32 (and Article 226 for High Courts), the courts can issue writs, directions, or orders for rights enforcement:"
)
pn.info_table(
    ["Writ Type", "Literal Meaning", "Core Application", "Against Whom Issued"],
    [
        [
            "Habeas Corpus",
            "'To have the body of'",
            "Secures release of a person unlawfully detained by state or private individuals.",
            "Public authorities and private individuals.",
        ],
        [
            "Mandamus",
            "'We command'",
            "Directs a public official or body to perform a mandatory legal duty they have failed to do.",
            "Public bodies, corporations, tribunals, or officials.",
        ],
        [
            "Prohibition",
            "'To forbid'",
            "Issued by a higher court to a lower court to stop it from exceeding its jurisdiction.",
            "Judicial and quasi-judicial authorities only.",
        ],
        [
            "Certiorari",
            "'To be certified'",
            "Issued to quash the order of a lower court or tribunal that exceeded jurisdiction or made an error of law.",
            "Judicial, quasi-judicial, and administrative authorities.",
        ],
        [
            "Quo Warranto",
            "'By what authority?'",
            "Inquires into the legality of a person's claim to a public office, preventing usurpation.",
            "Public offices of a permanent character.",
        ],
    ],
    col_widths=["15%", "18%", "42%", "25%"],
)

pn.br()
pn.part_box("ASSIGNMENT 3 -- CO3: APPLIED CONSTITUTIONAL SCENARIOS")

pn.bookmark(
    "Q3.1 -- If a state government passes a law that violates a Fundamental Right, what legal recourse is available?"
)
pn.qbox(
    "Q3.1: If a state government passes a law that violates a Fundamental Right, what legal recourse is available?"
)
pn.body(
    "If a State Legislature passes a law that violates any Fundamental Right guaranteed under Part III of the Constitution, the law is void from its inception. The Constitution provides robust legal mechanisms under Articles 13, 32, and 226 for citizens to challenge such laws and for the judiciary to strike them down."
)
pn.section("Constitutional Basis of Judicial Review")
pn.bullet(
    [
        "<b>Article 13(2):</b> Explicitly prohibits the State from making any law that takes away or abridges the Fundamental Rights. Any law made in contravention of this clause is void to the extent of the contravention.",
        "<b>Article 13(3):</b> Defines 'law' broadly to include ordinances, orders, bye-laws, rules, regulations, notifications, customs, or usages having the force of law.",
    ]
)
pn.section("Available Legal Recourse for Citizens")
pn.info_table(
    [
        "Legal Pathway",
        "Constitutional Article",
        "Court Jurisdiction",
        "Nature of Remedy",
    ],
    [
        [
            "Writ Petition to Supreme Court",
            "Article 32",
            "Supreme Court of India (Apex level). Justiciable Fundamental Right.",
            "Can issue writs to strike down the state law and protect the individual's affected right directly.",
        ],
        [
            "Writ Petition to High Court",
            "Article 226",
            "High Court of the concerned State. Broader jurisdiction.",
            "Can strike down the law for violating Fundamental Rights or any other constitutional/legal rights.",
        ],
    ],
)
pn.section("Key Judicial Doctrines Applied by the Courts")
pn.body(
    "When a state law is challenged, the courts apply several established doctrines to determine its validity:"
)
pn.bullet(
    [
        "<b>Doctrine of Severability:</b> If only a portion of the state law violates a Fundamental Right, and that portion can be separated from the rest of the act, the court will strike down only the offending portion, leaving the remaining law intact.",
        "<b>Doctrine of Eclipse:</b> Holds that a pre-constitutional law that violates a Fundamental Right is not dead but remains dormant (e.g., eclipsed by the FR) and can become active again if the Constitution is amended to remove the conflict.",
        "<b>Doctrine of Colorable Legislation:</b> Applied when the legislature tries to do indirectly what it cannot do directly under the Constitution ('what cannot be done directly, cannot be done indirectly').",
    ]
)


pn.br()
pn.bookmark(
    "Q3.2 -- How can a citizen use the Fundamental Duties to promote social harmony?"
)
pn.qbox("Q3.2: How can a citizen use the Fundamental Duties to promote social harmony?")
pn.body(
    "Fundamental Duties, introduced in 1976 under Article 51A (Part IV-A), serve as a constant reminder to citizens of their responsibilities to the nation and to each other. While civil rights protect individuals from the state, duties help foster a sense of civic responsibility, national unity, and social harmony in a diverse society."
)
pn.section("Key Duties Fostering Social Harmony")
pn.bullet(
    [
        "<b>1. Promotion of Common Brotherhood (Art. 51A(e)):</b> Directly mandates citizens 'to promote harmony and the spirit of common brotherhood amongst all the people of India transcending religious, linguistic and regional or sectional diversities'. It encourages citizens to look past differences and cultivate mutual respect.",
        "<b>2. Renunciation of Derogatory Practices (Art. 51A(e)):</b> Mandates citizens 'to renounce practices derogatory to the dignity of women'. This is crucial for gender harmony, pushing communities to reform outdated patriarchal customs.",
        "<b>3. Respect for Composite Culture (Art. 51A(f)):</b> Mandates citizens 'to value and preserve the rich heritage of our composite culture'. India's culture is a blend of various traditions, and respecting this diversity is essential to prevent cultural friction.",
        "<b>4. Safeguarding Public Property (Art. 51A(i)):</b> Mandates citizens 'to safeguard public property and to abjure violence'. In times of public protests, this duty serves as a reminder to resolve disputes peacefully without damaging national assets.",
        "<b>5. Developing Scientific Temper (Art. 51A(h)):</b> Mandates citizens 'to develop the scientific temper, humanism and the spirit of inquiry and reform', which helps combat superstitions, communal bigotry, and blind dogma.",
    ]
)
pn.section("Statutory Enforcement and Civic Action")
pn.body(
    "Although the duties are non-justiciable on their own, citizens can use them as moral guidelines. Furthermore, the <b>Verma Committee (1999)</b> pointed out that several laws enforce these duties, such as the <i>Protection of Civil Rights Act (1955)</i> and the <i>IPC provisions</i> penalizing offenses inciting communal hatred, making compliance with these duties a legal necessity for social peace."
)


pn.br()
pn.bookmark(
    "Q3.3 -- How can the Directive Principles be applied to formulate social welfare policies?"
)
pn.qbox(
    "Q3.3: How can the Directive Principles be applied to formulate social welfare policies?"
)
pn.body(
    "The Directive Principles of State Policy (DPSP) under Part IV of the Constitution serve as the constitutional blueprint for economic democracy and social justice. Article 37 mandates that the State must apply these principles when enacting laws and policies. Governments have continuously drawn inspiration from Part IV to formulate landmark social welfare programs and laws."
)
pn.section("Application of DPSPs in Key National Policies")
pn.info_table(
    ["Policy Area / Law", "DPSP Article Applied", "Welfare Objective & Impact", "Key Implementation / Notes"],
    [
        [
            "Right to Education Act, 2009",
            "Article 45 & Article 39(f)",
            "Provides free and compulsory education to all children aged 6 to 14 years, securing early childhood development.",
            "Enacted Art. 21A as a fundamental right based on DPSP principles.",
        ],
        [
            "MGNREGA, 2005",
            "Article 39(a), Article 41 & Article 43",
            "Guarantees 100 days of manual wage employment in rural areas, securing the right to work and adequate livelihood.",
            "Promotes cottage and rural employment.",
        ],
        [
            "Maternity Benefit Act, 2017",
            "Article 42",
            "Mandates 26 weeks of paid maternity leave, crèche facilities, and job security for pregnant working women.",
            "Ensures just and humane conditions of work.",
        ],
        [
            "Legal Services Authorities Act, 1987",
            "Article 39A",
            "Establishes Lok Adalats and provides free legal aid to the poor and weaker sections of society.",
            "Ensures equal opportunity for justice.",
        ],
        [
            "Panchayati Raj Acts, 1992",
            "Article 40",
            "Gave constitutional status to Panchayats, decentralizing administrative power to the rural grassroots.",
            "Gandhi's model of village self-governance.",
        ],
    ],
    col_widths=["20%", "18%", "37%", "25%"],
)
pn.section("Ongoing Policy Challenges: Uniform Civil Code (Article 44)")
pn.body(
    "A key directive that remains a subject of policy debate is <b>Article 44</b>, which directs the State to secure a Uniform Civil Code (UCC) for all citizens throughout India. Applying this principle requires careful balancing of gender justice and minority rights, illustrating how DPSPs guide long-term social reform."
)


pn.br()
pn.bookmark(
    "Q3.4 -- In what situations might the President's rule be imposed in a state?"
)
pn.qbox("Q3.4: In what situations might the President's rule be imposed in a state?")
pn.body(
    "President's Rule, also known as State Emergency or Constitutional Emergency, is imposed in a State under <b>Article 356</b> of the Constitution. It is declared when the governance of a State cannot be carried out in accordance with the provisions of the Constitution. Upon proclamation, the elected State Government is dismissed, and executive authority is transferred to the Governor, who administers the state on behalf of the President."
)
pn.section("Constitutional Grounds for Imposition")
pn.bullet(
    [
        "<b>1. Failure of Constitutional Machinery (Article 356):</b> If the President, on receipt of a report from the Governor of a State or otherwise, is satisfied that a situation has arisen in which the government of the State cannot be carried on in accordance with the Constitution.",
        "<b>2. Non-Compliance with Central Directions (Article 365):</b> If a State fails to comply with or give effect to any direction issued by the Central government (e.g., on national security, railway protection), the President can hold that a situation has arisen where State governance has failed.",
    ]
)
pn.section("Typical Situations Warranting Article 356")
pn.info_table(
    ["Scenario Type", "Core Situation Description", "Example Scenario"],
    [
        [
            "Loss of Majority",
            "A ministry resigns or is defeated, and no other party can form a stable coalition government.",
            "Hung Assembly post-elections; large-scale party defections.",
        ],
        [
            "Breakdown of Law & Order",
            "The state government fails to curb severe lawlessness, communal riots, or armed insurgencies.",
            "Widespread state-wide violence where state police fails completely.",
        ],
        [
            "Political Instability",
            "Severe infighting in the ruling party leading to government paralysis.",
            "Constant changing of Chief Ministers; failure to pass the budget.",
        ],
    ],
)
pn.section("S.R. Bommai Guidelines (1994) & Safeguards")
pn.body(
    "Historically abused for political gains, the Supreme Court in the <b>S.R. Bommai case (1994)</b> established strict safeguards:"
)
pn.bullet(
    [
        "The proclamation of President's Rule is subject to judicial review.",
        "The State Legislative Assembly cannot be dissolved until both Houses of Parliament approve the proclamation (within 2 months). The assembly can only be suspended.",
        "The floor of the Assembly is the only place to test the majority of a government, not the subjective opinion of the Governor.",
    ]
)


pn.br()
pn.bookmark(
    "Q3.5 -- How does the distribution of financial powers impact the relationship between the Union and the States?"
)
pn.qbox(
    "Q3.5: How does the distribution of financial powers impact the relationship between the Union and the States?"
)
pn.body(
    "The distribution of financial powers between the Union and the States, governed by <b>Part XII</b> of the Constitution, is one of the most critical and friction-prone aspects of Indian federalism. The Constitution divides tax sources between the Centre and the States, but intentionally vests more productive tax avenues in the Centre, creating a structural fiscal imbalance that requires institutional resolution."
)
pn.section("Key Sources of Tax Allocation")
pn.bullet(
    [
        "<b>Union Taxes:</b> Income Tax (except agriculture), Customs, Corporation Tax, GST (Central and Integrated portion). These taxes are highly elastic and generate the bulk of public revenue.",
        "<b>State Taxes:</b> Land Revenue, Agricultural Income Tax, Stamp Duty, State Excise (on alcohol), GST (State portion). These taxes are less elastic and insufficient to meet the development needs of the states.",
    ]
)
pn.section("Resolving Fiscal Imbalances: The Finance Commission (Article 280)")
pn.body(
    "To bridge the gap between states' expenditure needs and tax resources (vertical imbalance) and inequalities among states (horizontal imbalance), the Constitution establishes the <b>Finance Commission</b> every 5 years under Article 280. Its core recommendations dictate:"
)
pn.bullet(
    [
        "<b>Devolution of Taxes:</b> The percentage of central taxes to be shared with the states (e.g., devolute 41% of net central tax pool to states).",
        "<b>Grants-in-Aid:</b> Principles governing grants-in-aid of the revenues of the states out of the Consolidated Fund of India (Article 275).",
    ]
)
pn.section("Impact of GST and Centrally Sponsored Schemes")
pn.body(
    "The introduction of the Goods and Services Tax (GST) through the 101st Amendment Act of 2016 created a unified market but limited the fiscal autonomy of the states. States can no longer unilaterally set tax rates on goods. Furthermore, states often complain about the conditions attached to <b>Centrally Sponsored Schemes (CSS)</b> and delays in GST compensation, making fiscal federalism a continuous site of union-state negotiation."
)


pn.br()
pn.bookmark(
    "Q3.6 -- If the parliament passes a law that contradicts the basic structure of the constitution, what can the supreme court do?"
)
pn.qbox(
    "Q3.6: If the parliament passes a law that contradicts the basic structure of the constitution, what can the supreme court do?"
)
pn.body(
    "If the Parliament passes a constitutional amendment or a law that violates or contradicts the 'Basic Structure' of the Constitution, the Supreme Court of India has the power of judicial review to declare that amendment or law unconstitutional and void. This power ensures the supremacy of the Constitution and protects the core identity of the republic."
)
pn.section("Origin and Meaning of the Basic Structure Doctrine")
pn.body(
    "The doctrine was established in the landmark case of <b>Kesavananda Bharati v. State of Kerala (1973)</b>. The Supreme Court ruled that while Article 368 gives Parliament the power to amend any part of the Constitution, it cannot alter or destroy its essential elements or 'Basic Structure'. Features like judicial review, democracy, secularism, and rule of law are immune to amendment."
)
pn.section("Available Judicial Remedial Actions")
pn.bullet(
    [
        "<b>Declare Unconstitutional:</b> The Supreme Court can strike down the entire amendment or the offending provisions under its writ jurisdiction (Articles 32 and 136).",
        "<b>Strike Down ordinary laws:</b> If the law is an ordinary statute, it can be declared void under Article 13 if it violates any Fundamental Right or exceeds legislative competence.",
        "<b>Apply Judicial Review:</b> The court can review any law placed in the <b>Ninth Schedule</b>. In the <i>I.R. Coelho case (2007)</i>, the Supreme Court held that laws added to the Ninth Schedule after 24 April 1973 are subject to judicial review if they violate the Basic Structure.",
    ]
)
pn.section("Real-World Example: 99th Amendment & NJAC (2015)")
pn.body(
    "A prominent example occurred in 2015 when Parliament passed the 99th Constitutional Amendment Act to establish the National Judicial Appointments Commission (NJAC). The Supreme Court struck down the amendment in its entirety, holding that it compromised the independence of the judiciary (a basic feature) by giving the executive a role in judicial appointments."
)


pn.br()
pn.bookmark(
    "Q3.7 -- How does the Right to Equality apply to affirmative action policies?"
)
pn.qbox("Q3.7: How does the Right to Equality apply to affirmative action policies?")
pn.body(
    "The Right to Equality in India (Articles 14 to 18) does not mean a mathematical, formal equality that ignores existing historical and social inequalities. Instead, the Constitution adopts the concept of <b>substantive equality</b>, which permits the State to take affirmative action and make special provisions for the advancement of socially and educationally backward classes."
)
pn.section("Constitutional Framework of Affirmative Action")
pn.bullet(
    [
        "<b>Article 15(4):</b> Enables the State to make special provisions for the advancement of any socially and educationally backward classes of citizens or for the Scheduled Castes (SCs) and Scheduled Tribes (STs) (e.g., educational reservations).",
        "<b>Article 16(4):</b> Enables the State to make provisions for the reservation of appointments or posts in favor of any backward class of citizens which, in the opinion of the State, is not adequately represented in the services under the State.",
    ]
)
pn.section("Key Judicial Principles & Boundaries")
pn.body(
    "To ensure that affirmative action does not destroy the right to equality of other citizens, the Supreme Court has laid down several key legal boundaries:"
)
pn.info_table(
    ["Judicial Case", "Established Rule / Doctrine", "Core Impact on Reservations"],
    [
        [
            "Indra Sawhney v. Union of India (1992) (Mandal Case)",
            "50% Limit & Creamy Layer",
            "Reservations cannot exceed 50% of seats in a year. The 'creamy layer' (wealthier backward class members) must be excluded from OBC reservations. No reservation in promotions.",
        ],
        [
            "M. Nagaraj v. Union of India (2006)",
            "Quantifiable Data Requirement",
            "State must show backwardness, inadequacy of representation, and overall administrative efficiency (Art 335) before introducing reservations in promotions for SC/ST.",
        ],
        [
            "Jarnail Singh v. Lachhmi Narain Gupta (2018)",
            "Creamy Layer in SC/ST",
            "Applied the 'creamy layer' exclusion principle to SC/ST promotions as well, ensuring benefits reach the most needy.",
        ],
    ],
)
pn.section("Recent Development: EWS Reservation (103rd Amendment)")
pn.body(
    "The 103rd Amendment Act of 2019 inserted Articles 15(6) and 16(6), permitting up to 10% reservation in educational institutions and public employment for the economically weaker sections (EWS) of citizens, shifting the affirmative action paradigm to include economic status alongside social backwardness."
)


pn.br()
pn.bookmark("Q3.8 -- How can Article 19 be used to protect journalistic freedom?")
pn.qbox("Q3.8: How can Article 19 be used to protect journalistic freedom?")
pn.body(
    "Although the Constitution of India does not explicitly mention 'freedom of the press', it is well-established that journalistic freedom is implied within <b>Article 19(1)(a)</b> -- the freedom of speech and expression. Journalists, editors, and publishers can invoke this article to protect their right to report, investigate, and disseminate information without arbitrary censorship."
)
pn.section("Key Protections Enabled for Journalists")
pn.bullet(
    [
        "<b>1. Right to Publish and Circulate:</b> In <i>Romesh Thappar v. State of Madras (1950)</i>, the Supreme Court held that freedom of speech includes the freedom of propagation of ideas, which is ensured only by freedom of circulation of publications. The state cannot arbitrarily ban the distribution of newspapers.",
        "<b>2. Protection against Pre-Censorship:</b> Pre-censorship (requiring government approval before publication) is generally held unconstitutional, except in rare emergency situations. The press cannot be silenced prior to publication.",
        "<b>3. Freedom from Fiscal Restrictions:</b> In <i>Sakal Papers v. Union of India (1962)</i>, the court struck down government regulations limiting newspaper pages and prices, holding that fiscal measures cannot be used to curb circulation.",
        "<b>4. Investigative Journalism & Sourcing:</b> Freedom of expression protects the right of journalists to conduct interviews and report on public matters, subject only to reasonable restrictions.",
    ]
)
pn.section("Reasonable Restrictions (Article 19(2))")
pn.body(
    "Journalistic freedom is not absolute and is subject to the eight reasonable restrictions under Article 19(2). Restrictions on journalists must be narrowly tailored and cannot be vague. For example, in <b>Shreya Singhal v. Union of India (2015)</b>, the Supreme Court struck down Section 66A of the IT Act, which had been used to arrest citizens and journalists for online posts, holding that it was vague and overbroad, violating Article 19(1)(a)."
)


pn.br()
pn.bookmark(
    "Q3.9 -- How does the supreme court help to expand the scope of article 21?"
)
pn.qbox("Q3.9: How does the supreme court help to expand the scope of article 21?")
pn.body(
    "Article 21 is a masterwork of judicial activism in India. Through a series of landmark judgments, the Supreme Court has expanded the literal words 'right to life and personal liberty' into a repository of numerous unenumerated rights, ensuring that 'life' does not mean mere animal existence but living with human dignity, self-respect, and health."
)
pn.section("The Transition: From Gopalan to Maneka Gandhi")
pn.body(
    "In the <i>A.K. Gopalan case (1950)</i>, the court interpreted Article 21 strictly, holding that 'personal liberty' only protected against arbitrary arrest, and the 'procedure established by law' meant any procedure enacted by the legislature. This was overruled in the <i>Maneka Gandhi case (1978)</i>, where the court held that any procedure depriving a person of life or liberty must be <b>'fair, just, and reasonable'</b> (Due Process). This opened the doors to expanding Article 21's scope."
)
pn.section("Key Unenumerated Rights Read into Article 21")
pn.info_table(
    ["Implied Right", "Landmark Supreme Court Case", "Core Constitutional Rationale"],
    [
        [
            "Right to Privacy",
            "K.S. Puttaswamy v. Union of India (2017)",
            "Privacy is an essential facet of human dignity and personal liberty under Article 21.",
        ],
        [
            "Right to Clean Environment",
            "M.C. Mehta v. Union of India (1987)",
            "Right to life includes the right to live in a pollution-free environment with clean air and water.",
        ],
        [
            "Right to Livelihool",
            "Olga Tellis v. Bombay Municipal Corporation (1985)",
            "Depriving a person of their livelihood amounts to depriving them of their life itself.",
        ],
        [
            "Right to Free Legal Aid",
            "Hussainara Khatoon v. State of Bihar (1979)",
            "A fair trial requires providing free legal representation to poor accused individuals.",
        ],
        [
            "Right to Shelter",
            "Chameli Singh v. State of U.P. (1996)",
            "Right to life includes the right to shelter, food, clothing, and decent living conditions.",
        ],
    ],
)
pn.section("Impact on the Right to Education (Article 21A)")
pn.body(
    "In <i>Mohini Jain (1992)</i> and <i>Unni Krishnan (1993)</i>, the Supreme Court held that the right to education is directly linked to human dignity. This forced Parliament to enact the <b>86th Constitutional Amendment Act of 2002</b>, formally inserting <b>Article 21A</b> to make free and compulsory primary education a justiciable fundamental right."
)


pn.br()
pn.bookmark(
    "Q3.10 -- If a citizen is arrested unlawfully, what fundamental right can they invoke?"
)
pn.qbox(
    "Q3.10: If a citizen is arrested unlawfully, what fundamental right can they invoke?"
)
pn.body(
    "If a citizen is arrested unlawfully by the police or any state authority, they can invoke their fundamental right to protection against arrest and detention under <b>Article 22</b>, read alongside the right to personal liberty under <b>Article 21</b>, and seek immediate release through the right to constitutional remedies under <b>Article 32</b>."
)
pn.section("Protections Guaranteed under Article 22(1) and 22(2)")
pn.bullet(
    [
        "<b>1. Right to be Informed of Grounds:</b> No person who is arrested shall be detained in custody without being informed, as soon as may be, of the grounds for such arrest.",
        "<b>2. Right to Legal Representation:</b> The arrested person has the right to consult and be defended by a legal practitioner of their choice.",
        "<b>3. 24-Hour Magistrate Rule:</b> Every person arrested must be produced before the nearest magistrate within a period of 24 hours of such arrest, excluding the time necessary for the journey; no person can be detained in custody beyond 24 hours without the authority of a magistrate.",
    ]
)
pn.section("Writ of Habeas Corpus: The Ultimate Remedy")
pn.body(
    "If these protections are violated (e.g., detention exceeds 24 hours without magistrate approval), the arrest is unlawful. The citizen (or their relatives/friends on their behalf) can file a writ petition for <b>Habeas Corpus</b> under Article 32 (Supreme Court) or Article 226 (High Court). The court will order the police to 'produce the body' of the detainee and release them immediately if the arrest lacks legal justification."
)
pn.section("Landmark D.K. Basu Guidelines (1997)")
pn.body(
    "In the case of <b>D.K. Basu v. State of West Bengal</b>, the Supreme Court laid down mandatory guidelines to prevent custodial violence and unlawful arrests, requiring police officers to wear clear identification tags, prepare an arrest memo witnessed by a family member, and allow the arrestee to undergo a medical examination."
)

pn.br()
pn.part_box("ASSIGNMENT 4 -- CO4: ANALYTICAL EVALUATION")

pn.bookmark(
    "Q4.1 -- Analyze the strengths and weaknesses of the Indian federal structure."
)
pn.qbox("Q4.1: Analyze the strengths and weaknesses of the Indian federal structure.")
pn.body(
    "The federal structure of India, described as 'quasi-federal' with a strong centralizing bias, was designed to accommodate the country's vast cultural, linguistic, and regional diversity while preserving national unity. This system has unique strengths that have sustained the republic, but it also suffers from structural weaknesses that cause frequent union-state friction."
)
pn.section("Strengths of Indian Federalism")
pn.bullet(
    [
        "<b>1. Preservation of National Unity:</b> By vesting strong powers (defense, foreign affairs, emergency) in the Centre, the Constitution prevents the disintegration of the country and ensures a unified response to external threats.",
        "<b>2. Accommodation of Diversity:</b> The creation of states on a linguistic basis (e.g., Andhra Pradesh, Maharashtra) and special autonomy provisions for tribal/northeastern states (Fifth and Sixth Schedules, Article 371) have satisfied regional aspirations, preventing secessionist movements.",
        "<b>3. Democratic Decentralization:</b> The three-tier structure (Centre, States, and Panchayats/Municipalities) brings governance closer to the people, promoting local participation.",
        "<b>4. Fiscal Redistribution:</b> The Finance Commission (Article 280) acts as an independent body to allocate resources, ensuring that economically weaker states receive grants and tax shares from the national pool.",
    ]
)
pn.section("Weaknesses and Areas of Friction")
pn.bullet(
    [
        "<b>1. Over-Centralization of Fiscal Power:</b> The Centre controls the most elastic tax sources, leaving states financially dependent on central transfers, which compromises their autonomy.",
        "<b>2. Misuse of the Office of the Governor:</b> Governors are appointed by the Centre and often act in the interest of the ruling party in New Delhi, creating conflicts with elected state governments (e.g., delaying bills, recommending President's Rule).",
        "<b>3. Abuse of Article 356 (President's Rule):</b> Historically, the Centre has frequently dismissed state governments led by opposition parties, though the <i>Bommai</i> judgment has restricted this.",
        "<b>4. Encroachment on State Subjects:</b> Central initiatives through centrally sponsored schemes and GST have restricted states' policy and financial autonomy.",
    ]
)


pn.br()
pn.bookmark(
    "Q4.2 -- Compare and contrast the powers of the President of India with those of the Prime Minister."
)
pn.qbox(
    "Q4.2: Compare and contrast the powers of the President of India with those of the Prime Minister."
)
pn.body(
    "The Indian parliamentary system establishes a dual executive structure: the President of India is the nominal executive (de jure head / head of state), while the Prime Minister is the real executive (de facto head / head of government). While all executive actions are formally taken in the President's name, real decision-making authority lies with the Prime Minister and the Council of Ministers."
)
pn.section("Comparison of Executive Status and Roles")
pn.info_table(
    ["Dimension", "The President of India", "The Prime Minister of India"],
    [
        [
            "Executive Status",
            "Nominal / Constitutional executive head (de jure).",
            "Real / Political executive head (de facto).",
        ],
        [
            "Cabinet Position",
            "Stands outside the cabinet; acts on its binding advice (Art. 74).",
            "Head of the Cabinet; presides over its meetings and shapes policies.",
        ],
        [
            "Legislative Role",
            "Summons, prorogues Parliament; gives assent to bills (Art. 111).",
            "Leader of the majority party in Lok Sabha; directs legislative agenda.",
        ],
        [
            "Emergency Status",
            "Formally proclaims emergencies (Arts. 352, 356, 360).",
            "Decides when to declare emergency; advises President in writing.",
        ],
    ],
)
pn.section("Pardoning and Appointment Powers")
pn.bullet(
    [
        "<b>Pardoning Power (Article 72):</b> The President has the exclusive power to grant pardons, reprieves, or commutations of sentences, including death sentences. The PM has no judicial powers.",
        "<b>Appointments:</b> The President appoints the PM, other ministers (on PM's advice), CJI, CAG, and Governors. The PM, however, makes all final decisions on who gets appointed.",
    ]
)
pn.section("Constitutional Discretion of the President")
pn.body(
    "Under Article 74 (amended by 44th Amendment), the President must act on ministerial advice, but can return advice once for reconsideration. The President also has situational discretion:"
)
pn.bullet(
    [
        "<b>1. Appointment of PM:</b> When no party has a clear majority in the Lok Sabha, the President must decide who to invite to form the government.",
        "<b>2. Dismissal of Ministry:</b> If the ministry loses the confidence of the Lok Sabha but refuses to resign.",
        "<b>3. Dissolution of Lok Sabha:</b> If the Prime Minister has lost majority and advises dissolution.",
    ]
)


pn.br()
pn.bookmark(
    "Q4.3 -- Evaluate the effectiveness of the Fundamental Duties in promoting civic responsibility."
)
pn.qbox(
    "Q4.3: Evaluate the effectiveness of the Fundamental Duties in promoting civic responsibility."
)
pn.body(
    "Fundamental Duties under Article 51A (Part IV-A) were introduced during the Emergency in 1976 to restore the balance between rights and duties. While they have acted as a moral guide for citizens and a constitutional interpretive tool for the judiciary, their effectiveness in promoting active civic responsibility has been a subject of criticism due to their non-justiciable nature."
)
pn.section("Areas of Effectiveness")
pn.bullet(
    [
        "<b>1. Judicial Interpretation:</b> The Supreme Court has ruled that in determining the constitutionality of any law, if the law seeks to give effect to a Fundamental Duty, it can be held as 'reasonable' under Article 14 or 19. Duties thus help defend welfare laws.",
        "<b>2. Statutory Support:</b> Many duties are backed by specific statutes that penalize violations. For example, the duty to respect the National Flag is backed by the <i>Prevention of Insults to National Honour Act</i>, and the duty to protect wildlife is enforced by the <i>Wildlife Protection Act</i>.",
        "<b>3. Educational Value:</b> They serve as a pedagogical tool in schools and colleges, raising awareness about environmental protection, cultural heritage, and national respect.",
    ]
)
pn.section("Key Criticisms and Limitations")
pn.bullet(
    [
        "<b>1. Non-Justiciability:</b> Unlike Fundamental Rights, there is no direct legal remedy for their violation. A citizen cannot be sued or arrested merely for failing to follow a duty, unless there is a specific enabling law.",
        "<b>2. Vague Language:</b> Terms like 'scientific temper', 'noble ideals', and 'composite culture' are abstract and open to multiple subjective interpretations.",
        "<b>3. Incomplete List:</b> The list omits several crucial civic duties recommended by the Swaran Singh Committee, such as the duty to pay taxes, the duty to vote in elections, and family planning.",
    ]
)


pn.br()
pn.bookmark(
    "Q4.4 -- Analyze the impact of major constitutional amendments on Indian polity."
)
pn.qbox("Q4.4: Analyze the impact of major constitutional amendments on Indian polity.")
pn.body(
    "Constitutional amendments under Article 368 have significantly reshaped the Indian polity, correcting administrative lacunae, responding to judicial challenges, and expanding democratic representation. Below is an analysis of four major amendments that have had a transformative impact on the governance structure of India:"
)
pn.info_table(
    ["Amendment & Year", "Key Changes Introduced", "Polity & Governance Impact"],
    [
        [
            "42nd Amendment Act, 1976 ('Mini-Constitution')",
            "Added 'Secular, Socialist, Integrity' to Preamble. Added Part IV-A (Fundamental Duties). Curbed power of judicial review. Made President bound by Cabinet advice.",
            "Represented the peak of centralizing power during the Emergency. Attempted to establish parliamentary supremacy over the judiciary.",
        ],
        [
            "44th Amendment Act, 1978",
            "Reversed many 42nd Amendment changes. Replaced 'internal disturbance' with 'armed rebellion' in Art 352. Provided that Art 20 & 21 cannot be suspended during emergency.",
            "Restored democratic checks and balances and established safeguards against the executive abuse of emergency powers.",
        ],
        [
            "86th Amendment Act, 2002",
            "Inserted Article 21A, making free and compulsory education for children aged 6 to 14 a Fundamental Right. Modified Article 45 and added Article 51A(k).",
            "Transformed education policy in India, leading to the Right to Education (RTE) Act of 2009 and promoting grassroots literacy.",
        ],
        [
            "101st Amendment Act, 2016",
            "Introduced the Goods and Services Tax (GST) and established the GST Council (Article 279A).",
            "Redefined fiscal federalism by replacing multiple indirect taxes with a unified national tax structure, requiring consensus between Centre and States.",
        ],
    ],
)
pn.section("Conclusion on Amendment Power")
pn.body(
    "These amendments show that the Indian Constitution is a dynamic, living document. While amendments allow the state to respond to modern needs, the <b>Basic Structure Doctrine</b> ensures that amendments cannot alter the democratic and secular character of the republic."
)


pn.br()
pn.bookmark(
    "Q4.5 -- How does the balance between individual rights and state power manifest in the Indian Constitution?"
)
pn.qbox(
    "Q4.5: How does the balance between individual rights and state power manifest in the Indian Constitution?"
)
pn.body(
    "The balance between individual rights and state power is one of the most delicate constitutional designs in India. The Constitution guarantees justiciable civil liberties to individuals under Part III, but simultaneously arms the State with powers to restrict these rights to protect national security, public order, and social welfare, ensuring that individual liberty does not degenerates into license."
)
pn.section("Constitutional Manifestation of the Balance")
pn.bullet(
    [
        "<b>1. Reasonable Restrictions (Articles 19(2) to 19(6)):</b> The rights under Article 19 are not absolute. The State can impose 'reasonable restrictions' on specific grounds like sovereignty, security, public order, and morality. The courts decide whether a restriction is indeed 'reasonable'.",
        "<b>2. Preventive Detention (Article 22):</b> Unlike western democracies, the Indian Constitution permits preventive detention (detaining a person without trial to prevent them from committing a crime) even in peacetime. However, Article 22 provides safeguards, such as review by an Advisory Board.",
        "<b>3. Suspension of Rights during Emergency (Articles 358 & 359):</b> During a National Emergency, Article 19 is automatically suspended, and the President can suspend the right to move courts for enforcement of other rights (except Articles 20 and 21).",
    ]
)
pn.section("Judicial Test: The Doctrine of Proportionality")
pn.body(
    "To prevent state encroachment on individual rights, the Supreme Court applies the <b>Doctrine of Proportionality</b> (reaffirmed in the <i>Puttaswamy case</i>). For a state restriction on a right to be constitutional, it must satisfy four conditions:"
)
pn.bullet(
    [
        "The restriction must be backed by a clear law (Legality).",
        "The restriction must serve a legitimate state goal (Legitimacy).",
        "The measure must be suitable for achieving that goal (Suitability).",
        "The restriction must be the least intrusive means, and the benefit must outweigh the harm (Proportionality).",
    ]
)


pn.br()
pn.bookmark("Q4.6 -- Analyze the impact of emergency provisions on fundamental rights.")
pn.qbox("Q4.6: Analyze the impact of emergency provisions on fundamental rights.")
pn.body(
    "The proclamation of a National Emergency under Article 352 has a severe impact on the Fundamental Rights of citizens. The Constitution contains two articles -- <b>Article 358</b> and <b>Article 359</b> -- which govern the suspension of Fundamental Rights, turning the state's focus from individual liberty to national security."
)
pn.section("Suspension of Article 19 (Article 358)")
pn.body(
    "When a National Emergency is declared on the grounds of war or external aggression, the six freedoms guaranteed under Article 19 are automatically suspended. The State is freed from the restrictions of Article 19 and can make any law or take executive action violating these freedoms. These laws and actions cannot be challenged in court. However, Article 19 is <i>not</i> suspended if the emergency is declared on the grounds of 'armed rebellion' (Internal Emergency)."
)
pn.section("Suspension of Enforcement of Other Rights (Article 359)")
pn.body(
    "Article 359 does not suspend the Fundamental Rights themselves but empowers the President to suspend the right to move any court for the enforcement of specified rights. Key features include:"
)
pn.bullet(
    [
        "The suspension must be through a specific Presidential Order specifying the rights and the period.",
        "<b>Non-suspension of Art 20 & 21:</b> Crucially, the 44th Amendment Act of 1978 provided that the President <i>cannot</i> suspend the right to move court for the enforcement of <b>Article 20</b> (protection in respect of conviction for offenses) and <b>Article 21</b> (right to life and personal liberty).",
    ]
)
pn.section("Historical Abuse and Restorations")
pn.body(
    "During the 1975 emergency, in the infamous case of <b>ADM Jabalpur v. Shivkant Shukla (1976)</b>, the Supreme Court ruled that even the right to life under Article 21 could be suspended during emergency, denying Habeas Corpus. This widely condemned ruling led to the <b>44th Amendment</b>, which permanently exempted Articles 20 and 21 from suspension, ensuring basic human rights are protected even in times of national crisis."
)


pn.br()
pn.bookmark(
    "Q4.7 -- Analyze the role of the judiciary in protecting fundamental rights"
)
pn.qbox("Q4.7: Analyze the role of the judiciary in protecting fundamental rights")
pn.body(
    "The judiciary is appointed by the Constitution as the protector and guarantor of the Fundamental Rights of citizens. Under Articles 32 and 226, the Supreme Court and High Courts have been armed with extraordinary powers to defend individual liberties against legislative excesses and executive arbitrariness."
)
pn.section("Constitutional Pillars of Judicial Protection")
pn.bullet(
    [
        "<b>Article 32 (Supreme Court):</b> Allows citizens to directly petition the Supreme Court if their rights are violated. The court can issue writs (Habeas Corpus, Mandamus, etc.) for enforcement.",
        "<b>Article 226 (High Courts):</b> Empowers High Courts to issue writs for the enforcement of Fundamental Rights and other legal rights within their territorial jurisdiction.",
    ]
)
pn.section("Innovative Judicial Mechanisms")
pn.info_table(
    ["Judicial Tool", "Key Mechanism & Innovation", "Governance & Rights Impact"],
    [
        [
            "Public Interest Litigation (PIL)",
            "Relaxes the rule of <i>locus standi</i>. Any public-spirited citizen can file a petition on behalf of poor, marginalized, or illiterate victims.",
            "Democratized access to justice. Enabled judicial intervention in prisons, labor exploitation, and pollution.",
        ],
        [
            "Epistolary Jurisdiction",
            "Courts treat letters, telegrams, or newspaper reports addressed to judges as formal writ petitions.",
            "Made it possible for inmates or social workers to trigger judicial protection directly from jail.",
        ],
        [
            "Judicial Activism",
            "Purposive interpretation of the constitutional text (especially Article 21) to discover new implied rights.",
            "Led to the expansion of right to privacy, clean environment, education, and shelter as justiciable rights.",
        ],
    ],
)
pn.section("Limitations and Criticisms")
pn.body(
    "While the judiciary has played a stellar role in protecting rights, it faces criticisms regarding <b>judicial overreach</b> (encroaching on executive policy-making, e.g., banning liquor sale on highways) and massive <b>judicial pendency</b>, which delays the delivery of justice to needy citizens."
)


pn.br()
pn.bookmark("Q4.8 -- Analyze the effectiveness of local self-government in India.")
pn.qbox("Q4.8: Analyze the effectiveness of local self-government in India.")
pn.body(
    "The formalization of local self-governments (Panchayati Raj and Municipalities) in 1992 aimed to deepen democracy by decentralizing administrative and financial powers. Over three decades of implementation, this system has achieved significant success in empowering local communities, but its effectiveness remains severely constrained by systemic challenges."
)
pn.section("Key Successes and Achievements")
pn.bullet(
    [
        "<b>1. Deepening Democracy:</b> India now has over 3 million elected local representatives (the largest in the world), creating political awareness and democratic representation at the village and town levels.",
        "<b>2. Gender and Social Empowerment:</b> The reservation of not less than 1/3rd of seats for women has brought over 1 million women into leadership roles. Reservations for SCs and STs have challenged traditional feudal power structures in rural areas.",
        "<b>3. Local Development Delivery:</b> Local bodies have successfully executed local developmental projects like village roads, primary schools, water harvesting, and implementation of MGNREGA.",
    ]
)
pn.section("Key Weaknesses and Failures")
pn.bullet(
    [
        "<b>1. The 'Three Fs' Deficit:</b> States have failed to devolve adequate <b>Funds</b> (local bodies have minimal tax base and rely heavily on state grants), <b>Functions</b> (overlapping jurisdictions between state departments and local bodies), and <b>Functionaries</b> (lack of independent administrative staff).",
        "<b>2. Proxy Politics ('Sarpanch Pati'):</b> In many rural areas, elected women representatives are dominated by their husbands or male relatives who exercise actual administrative power.",
        "<b>3. Bureaucratic Interference:</b> Local bodies remain heavily dependent on and controlled by district-level state bureaucrats (collectors, block development officers), diluting their autonomy.",
    ]
)


pn.br()
pn.bookmark("Q4.9 -- How has the interpretation of Article 21 changed over time?")
pn.qbox("Q4.9: How has the interpretation of Article 21 changed over time?")
pn.body(
    "The judicial interpretation of Article 21 ('right to life and personal liberty') is one of the most remarkable stories of constitutional evolution in the democratic world. It has transformed from a narrow, literal procedural guarantee in 1950 into a broad, substantive repository of human rights and dignity today."
)
pn.section("Chronological Phase Analysis")
pn.info_table(
    [
        "Phase / Era",
        "Key Landmark Case",
        "Judicial Doctrine & Interpretation",
        "Constitutional Impact",
    ],
    [
        [
            "Phase I: Narrow Literalism (1950s-1970s)",
            "A.K. Gopalan v. State of Madras (1950)",
            "Adopted a literal interpretation of 'procedure established by law'. The court held that if Parliament enacts a law to deprive liberty, the court cannot check the fairness of that law. Only executive action must follow procedure.",
            "Left citizens vulnerable to arbitrary legislative actions (e.g., preventive detention laws).",
        ],
        [
            "Phase II: Substantive Due Process (1978 onwards)",
            "Maneka Gandhi v. Union of India (1978)",
            "Overruled <i>Gopalan</i>. Held that the procedure depriving life or liberty must be 'fair, just, and reasonable' -- introducing 'Due Process' of law in India. 'Life' means living with dignity.",
            "Protected citizens against arbitrary legislative and executive acts, laying the foundation for judicial activism.",
        ],
        [
            "Phase III: Expansion of Implied Rights (1980s-2000s)",
            "Olga Tellis, Mohini Jain, M.C. Mehta cases",
            "Read several 'unenumerated' socio-economic rights into Article 21 (livelihood, environment, free legal aid, education).",
            "Forced the state to implement welfare laws (e.g., Right to Education Act, MGNREGA).",
        ],
        [
            "Phase IV: Autonomy & Privacy (2010s-Present)",
            "K.S. Puttaswamy v. Union of India (2017)",
            "Declared the right to privacy as an intrinsic part of life and liberty under Article 21, establishing a strict proportionality test.",
            "Struck down section 377 (homosexuality), protected digital data privacy, and limited Aadhaar usage.",
        ],
    ],
)


pn.br()
pn.bookmark(
    "Q4.10 -- What are the limitations of the right to freedom under article 19?"
)
pn.qbox("Q4.10: What are the limitations of the right to freedom under article 19?")
pn.body(
    "<b>Article 19</b> in Part III of the Constitution guarantees six democratic freedoms to all citizens: speech, assembly, association, movement, residence, and profession. However, these rights are not absolute. To prevent individual liberty from encroaching upon the rights of others or national security, the Constitution permits the State to impose 'reasonable restrictions' under Articles 19(2) to 19(6)."
)
pn.section("The Six Freedoms and Their Respective Limitation Grounds")
pn.info_table(
    [
        "Freedom Clause",
        "Right Guaranteed",
        "Permissible Grounds for Restriction (Art. 19(2) - 19(6))",
    ],
    [
        [
            "19(1)(a)",
            "Speech & Expression",
            "Sovereignty and integrity of India, security of the State, friendly relations with foreign States, public order, decency or morality, contempt of court, defamation, or incitement to an offense (Article 19(2)).",
        ],
        [
            "19(1)(b)",
            "Peaceful Assembly (without arms)",
            "Sovereignty and integrity of India, and public order (Article 19(3)).",
        ],
        [
            "19(1)(c)",
            "Form Associations / Unions",
            "Sovereignty and integrity of India, public order, and morality (Article 19(4)).",
        ],
        [
            "19(1)(d) & (e)",
            "Movement & Residence",
            "Interests of the general public, and protection of the interests of any Scheduled Tribe (Article 19(5)) (e.g., Inner Line Permit, tribal areas access).",
        ],
        [
            "19(1)(g)",
            "Practice Profession / Trade",
            "Interests of the general public, prescribing technical qualifications, or state monopoly of trade/industry (Article 19(6)).",
        ],
    ],
)
pn.section("The Requirement of 'Reasonableness'")
pn.body(
    "For any state restriction on these freedoms to be valid, it must satisfy two conditions:"
)
pn.bullet(
    [
        "<b>Legality:</b> The restriction must be imposed through a valid law passed by the legislature, not merely an executive order.",
        "<b>Reasonableness:</b> The restriction must not be arbitrary or disproportionate. The Supreme Court has the final authority to test the reasonableness of the restriction by looking at the public interest and the severity of the restriction.",
    ]
)

pn.br()
pn.part_box("ASSIGNMENT 5 -- CO5: CRITICAL & EVALUATIVE ANALYSIS")

pn.bookmark(
    "Q5.1 -- To what extent does the Indian Constitution ensure social and economic justice?"
)
pn.qbox(
    "Q5.1: To what extent does the Indian Constitution ensure social and economic justice?"
)
pn.body(
    "The Preamble of the Constitution declares the resolve of the people to secure to all its citizens <b>'Justice -- social, economic, and political'</b>. Social and economic justice form the core of the welfare state model adopted by the Constitution, which uses a combination of justiciable Fundamental Rights and non-justiciable Directive Principles to achieve these objectives."
)
pn.section("Constitutional Tools for Justice")
pn.bullet(
    [
        "<b>Social Justice:</b> The Preamble's promise and Article 38 direct the state to secure a social order for the promotion of welfare. Article 17 abolishes 'untouchability', and Article 15 prohibits discrimination on grounds of religion, race, caste, sex, or place of birth, promoting social equality. Articles 15(4) and 16(4) enable reservation policies to uplift Scheduled Castes, Scheduled Tribes, and OBCs.",
        "<b>Economic Justice:</b> Article 39(b) directs the state to distribute material resources of the community to serve the common good. Article 39(c) directs the state to prevent the concentration of wealth. Article 39(d) mandates equal pay for equal work for both men and women. Article 41 directs the state to secure the right to work, education, and public assistance in cases of unemployment or old age.",
    ]
)
pn.section("Critical Evaluation of Success and Gaps")
pn.bullet(
    [
        "<b>Successes:</b> Landmark legislations like the <i>Abolition of Zamindari System</i>, <i>Right to Education Act</i>, <i>MGNREGA</i>, and food security acts have significantly reduced absolute poverty and provided legal rights to the marginalized.",
        "<b>Gaps:</b> Economic inequality remains severe, with a major concentration of national wealth in the hands of a small percentage of the population. Social discrimination and caste-based violence continue in rural areas, showing that formal constitutional provisions require stronger executive implementation.",
    ]
)


pn.br()
pn.bookmark(
    "Q5.2 -- Evaluate the role of the judiciary in safeguarding constitutionalism in India."
)
pn.qbox(
    "Q5.2: Evaluate the role of the judiciary in safeguarding constitutionalism in India."
)
pn.body(
    "The judiciary has played a defining role in safeguarding constitutionalism (the principle of limited government and rule of law) in India. By acting as an independent check on legislative and executive authority, the Supreme Court has protected individual liberties and prevented majoritarian regimes from altering the democratic structure of the country."
)
pn.section("Key Judicial Tools and Doctrines")
pn.bullet(
    [
        "<b>1. Basic Structure Doctrine:</b> Established in the <i>Kesavananda Bharati case (1973)</i>, this doctrine acts as the ultimate check on Parliament's amending power. It prevents the ruling party from using a legislative majority to destroy democratic elections, judicial review, or federalism.",
        "<b>2. Judicial Review:</b> Under Articles 13, 32, and 226, the courts routinely strike down executive orders and statutes that violate Fundamental Rights or exceed constitutional power limits.",
        "<b>3. Public Interest Litigation (PIL):</b> By relaxing standing rules, the court allowed civil society to petition on behalf of marginalized groups, checking administrative corruption and protecting rights.",
        "<b>4. Expanding Article 21:</b> Read 'Due Process' and implied rights into the right to life, protecting citizens against arbitrary executive actions.",
    ]
)
pn.section("Areas of Criticism & Overreach")
pn.body(
    "While the judiciary has defended constitutionalism, it faces criticisms regarding <b>judicial overreach</b> (interfering in executive policy-making, like determining national highway liquor bans or directing river cleanup) and a severe backlog of cases (over 5 crore pending cases across courts), which compromises the right to speedy justice."
)


pn.br()
pn.bookmark(
    "Q5.3 -- Assess the success of the Indian Constitution in achieving its stated objectives."
)
pn.qbox(
    "Q5.3: Assess the success of the Indian Constitution in achieving its stated objectives."
)
pn.body(
    "The core objectives of the Indian Constitution are enshrined in its Preamble: to secure <b>Justice</b> (social, economic, and political), <b>Liberty</b> (of thought, expression, belief, faith, and worship), <b>Equality</b> (of status and opportunity), and to promote <b>Fraternity</b> assuring the dignity of the individual and the unity and integrity of the nation. Over 75 years of independence, India's success in achieving these goals represents a mix of institutional endurance and systemic challenges."
)
pn.section("Assessment of Objectives")
pn.info_table(
    ["Preamble Objective", "Key Achievements & Successes", "Key Failures & Gaps"],
    [
        [
            "Political Justice & Liberty",
            "Regular, free, and fair elections managed by an independent Election Commission. Freedom of speech, press, and religion widely protected by courts.",
            "Voter intimidation in regional pockets; misuse of sedition and national security laws to curb dissenting speech.",
        ],
        [
            "Social Justice & Equality",
            "Abolition of untouchability. Successful reservation policies empowering SCs, STs, and OBCs in education and public employment.",
            "Caste-based discrimination and gender violence continue, especially in rural areas; unequal status of women in personal laws.",
        ],
        [
            "Economic Justice",
            "Poverty levels reduced. Introduction of food security, right to work, and rural employment guarantee schemes.",
            "Growing economic inequality; high youth unemployment; lack of social security for informal sector workers.",
        ],
        [
            "Fraternity & Unity",
            "Preserved the territorial integrity of a highly diverse sub-continent; integration of northeastern states.",
            "Frequent communal friction, regionalism, and linguistic conflicts threaten national fraternity.",
        ],
    ],
)


pn.br()
pn.bookmark(
    "Q5.4 -- How effectively does the Indian Constitution balance the rights of individuals with the needs of the state?"
)
pn.qbox(
    "Q5.4: How effectively does the Indian Constitution balance the rights of individuals with the needs of the state?"
)
pn.body(
    "The balance between individual rights and the needs of the state (national security, public order, and socio-economic development) is one of the most complex aspects of Indian constitutional law. Unlike the US Constitution, which enumerates rights in absolute terms (leaving restrictions to judicial interpretation), the Indian Constitution incorporates both the rights and their specific limitations directly within the constitutional text."
)
pn.section("Institutional Balancing Mechanisms")
pn.bullet(
    [
        "<b>Reasonable Restrictions:</b> Under Article 19(2) to 19(6), the state can restrict individual freedoms only on eight specific grounds. The judiciary acts as the arbiter, applying the <b>test of reasonableness</b> and <b>proportionality</b> to strike down excessive state actions.",
        "<b>Preventive Detention (Article 22):</b> Allows the state to detain individuals without trial in the interest of public order or national security (e.g., under laws like UAPA, NSA). The Constitution attempts to balance this state power by mandating review by an independent Advisory Board.",
        "<b>Welfare legislation:</b> Articles 31A, 31B, and 31C protect state agrarian reforms and social welfare legislation from being challenged for violating individual property or equality rights, ensuring state capability for socio-economic development.",
    ]
)
pn.section("Critical Assessment")
pn.body(
    "While the framework is theoretically balanced, in practice, the executive often leverages state security laws (like sedition or UAPA) to curb individual dissent, leading to criticisms that the balance is tilted in favor of state power. However, the active use of writ petitions (Article 32/226) and judicial review acts as a continuous check to restore individual liberty."
)


pn.br()
pn.bookmark(
    "Q5.5 -- Is the amendment procedure of the Indian constitution too rigid, or too flexible?"
)
pn.qbox(
    "Q5.5: Is the amendment procedure of the Indian constitution too rigid, or too flexible?"
)
pn.body(
    "Constitutional experts generally agree that the amendment procedure of the Indian Constitution, governed by <b>Article 368</b>, represents a successful synthesis of rigidity and flexibility. It is rigid enough to protect the foundational democratic values from temporary majoritarian whims, yet flexible enough to allow the document to evolve with changing national needs."
)
pn.section("Comparative Analysis of Rigidity and Flexibility")
pn.info_table(
    ["Constitution", "Amendment Nature", "Procedure Complexity", "Outcome / Frequency"],
    [
        [
            "United States of America",
            "Highly Rigid",
            "Requires 2/3rd majority in both Houses of Congress and ratification by 3/4th of the States. Extremely difficult.",
            "Only 27 amendments passed in over 230 years.",
        ],
        [
            "United Kingdom",
            "Highly Flexible",
            "Can be amended by ordinary laws passed by a simple majority in Parliament. No special procedure.",
            "Constitutional conventions change constantly with simple legislation.",
        ],
        [
            "India (Article 368)",
            "Balanced Synthesis",
            "Three pathways: Simple majority for ordinary changes; Special majority (2/3rd) for major amendments; Special majority + 50% State ratification for federal changes.",
            "Over 105 amendments passed in 75 years, showing adaptability while maintaining core stability.",
        ],
    ],
)
pn.section("Evaluation of the Indian Synthesis")
pn.bullet(
    [
        "<b>Flexibility:</b> Allowed India to reorganize states on a linguistic basis, introduce Panchayati Raj (73rd/74th amendments), and bring major tax reforms (GST) without causing constitutional crises.",
        "<b>Rigidity (Basic Structure Safeguard):</b> The Supreme Court's introduction of the <i>Basic Structure Doctrine</i> in 1973 ensures that the flexible amendment procedure cannot be used to destroy the core identity of the Constitution (secularism, democracy, rule of law). It makes the foundational values completely rigid.",
    ]
)


pn.br()
pn.bookmark(
    "Q5.6 -- Evaluate the impact of the directive principals of state policy in India."
)
pn.qbox(
    "Q5.6: Evaluate the impact of the directive principals of state policy in India."
)
pn.body(
    "The Directive Principles of State Policy (DPSP) under Part IV of the Constitution were designed to guide the legislative and executive organs towards building a welfare state. Although non-justiciable, they have had a profound impact on the legal, social, and economic landscape of India, serving as the basis for major national policies and laws."
)
pn.section("Major Policy Impacts and Successes")
pn.bullet(
    [
        "<b>1. Grassroots Democracy (Article 40):</b> Provided the constitutional mandate that led to the 73rd and 74th Amendment Acts, establishing local self-governance across rural and urban India.",
        "<b>2. Educational Reform (Article 45):</b> Led to the Right to Education (RTE) Act of 2009 and the insertion of Article 21A, making free primary education a fundamental right.",
        "<b>3. Economic Security (Article 39, 41, 43):</b> Guided the creation of the <i>MGNREGA</i> (rural employment guarantee), <i>Land Reform Acts</i> (abolishing zamindari), and nationalization of key industries.",
        "<b>4. Legal Justice (Article 39A):</b> Guided the enactment of the <i>Legal Services Authorities Act (1987)</i>, providing free legal representation and establishing Lok Adalats.",
    ]
)
pn.section("Unfulfilled Directives and Criticisms")
pn.bullet(
    [
        "<b>Uniform Civil Code (Article 44):</b> A unified personal law for all citizens remains unimplemented due to political sensitivities and religious diversity.",
        "<b>Nutrition and Public Health (Article 47):</b> While schemes like the Mid-day Meal exist, malnutrition and high out-of-pocket healthcare costs remain major issues.",
        "<b>Concentration of Wealth (Article 39(c)):</b> Economic inequality has risen, showing that the state has struggled to fully implement the socialistic principles of Part IV.",
    ]
)


pn.br()
pn.bookmark("Q5.7 -- How well does the Indian constitution protect minority rights?")
pn.qbox("Q5.7: How well does the Indian constitution protect minority rights?")
pn.body(
    "The Constitution of India provides comprehensive safeguards to protect the religious, linguistic, and cultural rights of minorities. These rights are justiciable under Part III, protecting minority communities from assimilation by the majority and ensuring their active participation in the nation's democratic fabric."
)
pn.section("Core Constitutional Provisions")
pn.bullet(
    [
        "<b>Article 29 (Protection of Interests of Minorities):</b> Guarantees any section of citizens residing in India having a distinct language, script, or culture the right to conserve the same. It also prohibits discrimination in admission to state-funded educational institutions.",
        "<b>Article 30 (Right to Establish Educational Institutions):</b> Confers on all minorities, whether based on religion or language, the right to establish and administer educational institutions of their choice. The State cannot discriminate against minority-run institutions in granting aid.",
        "<b>Article 25 to 28 (Freedom of Religion):</b> Guarantees freedom of conscience, right to profess, practice, and propagate religion, and manage religious affairs, forming the basis of Indian secularism.",
    ]
)
pn.section("Judicial Interpretations and Boundaries")
pn.body(
    "The Supreme Court has clarified the scope of Article 30 to ensure it is not used to evade national education standards:"
)
pn.bullet(
    [
        "<b>T.M.A. Pai Foundation Case (2002):</b> The court ruled that the right under Article 30 is not absolute. The state can regulate minority institutions to ensure academic standards, safety, and proper administration.",
        "<b>In Re Kerala Education Bill (1958):</b> Held that the state can regulate curriculum and teacher qualifications in minority-aided schools, provided it does not destroy their right to administer.",
    ]
)


pn.br()
pn.bookmark("Q5.8 -- Evaluate the effectiveness of the emergency provisions in India.")
pn.qbox("Q5.8: Evaluate the effectiveness of the emergency provisions in India.")
pn.body(
    "The emergency provisions under Part XVIII (Articles 352 to 360) were incorporated to safeguard the sovereignty, unity, and security of the country during crises. While they have successfully preserved national unity during external wars, their historical application shows a mixed record of effectiveness, frequently marred by political abuse and suppression of civil liberties."
)
pn.section("Evaluation of Successes and Safeguarding Integrity")
pn.bullet(
    [
        "<b>External Emergencies:</b> Proclaimed during the 1962 Sino-Indian War, the 1965 and 1971 Indo-Pak Wars. During these external threats, the emergency provisions effectively centralized executive power, enabling the state to coordinate defense and mobilize national resources.",
        "<b>Integration of States:</b> Centralization of power helped manage regional border insurgencies and restore constitutional order during severe internal disturbances.",
    ]
)
pn.section("Abuse of Power and the 1975 Emergency")
pn.body(
    "The biggest criticism of these provisions is the 1975 Internal Emergency declared by Indira Gandhi on the grounds of 'internal disturbance'. It led to the mass arrest of opposition leaders, pre-censorship of the press, and suspension of basic human rights, illustrating how the executive can abuse emergency powers for political survival."
)
pn.section("Impact of the 44th Amendment Restorations")
pn.body(
    "To prevent future abuse, the 44th Amendment Act of 1978 introduced crucial safeguards:"
)
pn.bullet(
    [
        "Replaced 'internal disturbance' with 'armed rebellion' in Article 352.",
        "Mandated a written recommendation from the Cabinet to the President.",
        "Required parliamentary approval within 1 month by a special majority.",
        "Declared that <b>Articles 20 and 21</b> cannot be suspended under any circumstances.",
    ]
)


pn.br()
pn.bookmark("Q5.9 -- Is the indian constitution truly secular?")
pn.qbox("Q5.9: Is the indian constitution truly secular?")
pn.body(
    "Yes, the Indian Constitution is truly secular, but it adopts a unique, positive model of secularism that differs fundamentally from the Western concept of secularism. While Western secularism is based on a strict 'wall of separation' between the State and the Church, Indian secularism is based on the principle of equal respect for all religions."
)
pn.section("Comparison of Western vs Indian Secularism")
pn.info_table(
    [
        "Dimension",
        "Western Secularism (Strict Separation)",
        "Indian Secularism (Positive Tolerance)",
    ],
    [
        [
            "State & Religion Relationship",
            "Strict wall of separation. State cannot interfere in religious affairs; religion cannot influence state policy.",
            "Principled distance. The State maintains a distance from all religions but can interfere for social reform (e.g., abolishing untouchability).",
        ],
        [
            "State Funding",
            "State cannot fund or support any religious institution or activity.",
            "The State can provide financial aid and support to educational institutions run by all religious groups equally.",
        ],
        [
            "Minority Protections",
            "No special rights for religious minorities; strict uniformity.",
            "Guarantees special rights to religious and linguistic minorities to establish educational institutions (Art. 30).",
        ],
        [
            "Concept Name",
            "Secularism of separation.",
            "<i>Sarva Dharma Sama Bhava</i> (Equal respect for all religions).",
        ],
    ],
)
pn.section("Constitutional Evidence of Secularism")
pn.bullet(
    [
        "<b>Preamble:</b> The word 'Secular' was formally added to the Preamble by the 42nd Amendment in 1976.",
        "<b>Freedom of Religion:</b> Articles 25 to 28 guarantee freedom of conscience, right to practice and propagate religion, and manage religious affairs. Article 15 prohibits discrimination based on religion.",
        "<b>Basic Structure:</b> In the <i>S.R. Bommai case (1994)</i>, the Supreme Court declared that secularism is a basic feature of the Indian Constitution, meaning it cannot be abolished or diluted by any amendment.",
    ]
)


pn.br()
pn.bookmark(
    "Q5.10 -- To what extent does the Indian constitution promote democratic values?"
)
pn.qbox("Q5.10: To what extent does the Indian constitution promote democratic values?")
pn.body(
    "The Constitution of India promotes democratic values to a very high degree, establishing India as the world's largest representative democracy. It goes beyond merely setting up electoral machinery by incorporating deep substantive democratic values -- equality, liberty, rule of law, and minority protections -- into its core structure."
)
pn.section("Core Pillars Promoting Democratic Values")
pn.bullet(
    [
        "<b>1. Universal Adult Franchise (Article 326):</b> Guarantees every citizen who is not less than 18 years of age the right to vote in elections, without discrimination based on caste, class, creed, or gender. This was a revolutionary step in 1950, empowering the masses.",
        "<b>2. Independent Election Commission (Article 324):</b> Establishes an autonomous, constitutional body to supervise, direct, and control all elections to Parliament, State Legislatures, and the offices of President and Vice-President, ensuring free and fair polls.",
        "<b>3. Representative Parliamentary System:</b> Ensures executive accountability to the elected representatives of the people in Parliament and State Assemblies (collective responsibility under Art. 75/164).",
        "<b>4. Separation of Powers and Rule of Law:</b> Distributes power among the three organs, with an independent judiciary acting as a check on executive overreach, preserving democratic debate.",
        "<b>5. Constitutional Autonomy of Watchdogs:</b> Protects key oversight institutions like the Comptroller and Auditor General (CAG) and the Union Public Service Commission (UPSC) to maintain integrity and prevent nepotism.",
    ]
)
pn.section("Conclusion on Indian Democracy")
pn.body(
    "While Indian democracy faces operational challenges (e.g., money power in elections, criminalization of politics), the Constitution has successfully sustained a democratic polity for over seven decades, showing that its democratic values are deeply institutionalized."
)

# List of students to generate assignments for
students = [
    {"name": "Aayush Sahu", "enroll": "0101IT241001"},
    {"name": "Abhinav Sharma", "enroll": "0101IT241002"},
    {"name": "Adarsh Dwivedi", "enroll": "0101IT241003"},
    {"name": "Aditya Tandekar", "enroll": "0101IT241004"},
    {"name": "Amey Agnihotri", "enroll": "0101IT241005"},
    {"name": "Ankush Tiwari", "enroll": "0101IT241006"},
    {"name": "Aryan Singh", "enroll": "0101IT241007"},
    {"name": "Aryan Verma", "enroll": "0101IT241008"},
    {"name": "Ashay Motghare", "enroll": "0101IT241009"},
    {"name": "Ayaan Siddiqui", "enroll": "0101IT241010"},
    {"name": "Ayush Meshram", "enroll": "0101IT241011"},
    {"name": "Badal Goswami", "enroll": "0101IT241012"},
    {"name": "Bharat Dangi", "enroll": "0101IT241013"},
    {"name": "Chirag Verma", "enroll": "0101IT241014"},
    {"name": "Dev Bhargav", "enroll": "0101IT241015"},
    {"name": "Garvishka Lakwal", "enroll": "0101IT241016"},
    {"name": "Harsh Kumar Jatav", "enroll": "0101IT241017"},
    {"name": "Janhavi Satramwar", "enroll": "0101IT241018"},
    {"name": "Jatin Chouhan", "enroll": "0101IT241019"},
    {"name": "Jaydeep Bakode", "enroll": "0101IT241020"},
    {"name": "Jitendra Kumar", "enroll": "0101IT241021"},
    {"name": "Jitesh Dhanware", "enroll": "0101IT241022"},
    {"name": "Kavya Thakre", "enroll": "0101IT241023"},
    {"name": "Keshav Agar", "enroll": "0101IT241024"},
    {"name": "Khushi Nigam", "enroll": "0101IT241025"},
    {"name": "Khushi Yadav", "enroll": "0101IT241026"},
    {"name": "Krishna Yadav", "enroll": "0101IT241027"},
    {"name": "Kushal Patidar", "enroll": "0101IT241028"},
    {"name": "Manav Soni", "enroll": "0101IT241029"},
    {"name": "Manendra Jhade", "enroll": "0101IT241030"},
    {"name": "Mayank Bhumarkar", "enroll": "0101IT241031"},
    {"name": "Meetansh Dubey", "enroll": "0101IT241032"},
    {"name": "Mitanshi Bhawsar", "enroll": "0101IT241033"},
    {"name": "Mohit Singh", "enroll": "0101IT241034"},
    {"name": "Monu Prajapati", "enroll": "0101IT241035"},
    {"name": "Nancy Jha", "enroll": "0101IT241036"},
    {"name": "Nikhil Bhadwal", "enroll": "0101IT241037"},
    {"name": "Nikhil Ghanghoriya", "enroll": "0101IT241038"},
    {"name": "Nishant Ahirwar", "enroll": "0101IT241039"},
    {"name": "Palak Khare", "enroll": "0101IT241040"},
    {"name": "Parth Sonwane", "enroll": "0101IT241041"},
    {"name": "Piyush Kumar Chaurasiya", "enroll": "0101IT241042"},
    {"name": "Prabhat Kumar Singh", "enroll": "0101IT241043"},
    {"name": "Rahul Ahirwar", "enroll": "0101IT241044"},
    {"name": "Rishabh Dhoke", "enroll": "0101IT241045"},
    {"name": "Rishabh Pandey", "enroll": "0101IT241046"},
    {"name": "Roshan Kumar Sunaniya", "enroll": "0101IT241047"},
    {"name": "Sadhvi Ladhave", "enroll": "0101IT241048"},
    {"name": "Sagar Patel", "enroll": "0101IT241049"},
    {"name": "Saksham Dangi", "enroll": "0101IT241050"},
    {"name": "Sakshi Sinha", "enroll": "0101IT241051"},
    {"name": "Samit Raikhere", "enroll": "0101IT241052"},
    {"name": "Sanjana Mehra", "enroll": "0101IT241053"},
    {"name": "Sarika Dubey", "enroll": "0101IT241054"},
    {"name": "Shashank Singh", "enroll": "0101IT241055"},
    {"name": "Shivam Kumar Dahima", "enroll": "0101IT241056"},
    {"name": "Shivam Shivankar", "enroll": "0101IT241057"},
    {"name": "Shivani Chouhan", "enroll": "0101IT241058"},
    {"name": "Shreeyansh Asati", "enroll": "0101IT241059"},
    {"name": "Shreya Thakur", "enroll": "0101IT241060"},
    {"name": "Shriram Rajpoot", "enroll": "0101IT241061"},
    {"name": "Shubhank Prajapati", "enroll": "0101IT241062"},
    {"name": "Siddhant Choudhary", "enroll": "0101IT241063"},
    {"name": "Soumya", "enroll": "0101IT241064"},
    {"name": "Srijan Soni", "enroll": "0101IT241065"},
    {"name": "Srujan Singh", "enroll": "0101IT241066"},
    {"name": "Sujal Sanodiya", "enroll": "0101IT241067"},
    {"name": "Sujal Sharma", "enroll": "0101IT241068"},
    {"name": "Sumit Sharma", "enroll": "0101IT241069"},
    {"name": "Swastik Choudhary", "enroll": "0101IT241070"},
    {"name": "Swati Bhaskar", "enroll": "0101IT241071"},
    {"name": "Swati Singh", "enroll": "0101IT241072"},
    {"name": "Tekram Kushre", "enroll": "0101IT241073"},
    {"name": "Tushar Goplani", "enroll": "0101IT241074"},
    {"name": "Upendra Tripathi", "enroll": "0101IT241075"},
    {"name": "Vandana Patidar", "enroll": "0101IT241076"},
    {"name": "Vidit Singh Chadar", "enroll": "0101IT241077"},
    {"name": "Yogesh Patel", "enroll": "0101IT241078"},
    # Additional:
    {"name": "Jayshri Khatarkar", "enroll": "0101EC241064"},
    {"name": "Mansi Rathod", "enroll": "0101EC241077"},
    {"name": "Alok Yadav", "enroll": "0101IT231008"},
    {"name": "Yogesh Khas", "enroll": "0101IT231079"},
    {"name": "Raj Mewade", "enroll": "0101EX241051"},
    # Lateral Entry:
    {"name": "Anuj Rai", "enroll": "0101IT253D01"},
    {"name": "Rani Kolte", "enroll": "0101IT253D02"},
    {"name": "Rishabh Kumre", "enroll": "0101IT253D03"},
    {"name": "Rohit Rao Ghorpade", "enroll": "0101IT253D04"},
    {"name": "Vanshika Garg", "enroll": "0101IT253D05"},
    {"name": "Varsha Patel", "enroll": "0101IT253D06"},
    # Mechanical:
    {"name": "Dolly Choudhary", "enroll": "0101ME241017"},
    {"name": "Harsh Agrawal", "enroll": "0101ME241020"},
]

# Find where the metadata table is in the story
meta_table_idx = pn.story.index(meta_table)

import os
import zipfile
import shutil

zip_filename = "IC_Assignments_IT410.zip"
temp_dir = "temp_pdfs"
os.makedirs(temp_dir, exist_ok=True)

# Generate PDFs and pack them into the ZIP file
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for s in students:
        name = s["name"]
        enroll = s["enroll"]
        
        # 1. Reconstruct a new metadata table for this student and replace it in-place in the story
        new_metadata = [
            [Paragraph("Name:", st_key), Paragraph(name, st_val)],
            [Paragraph("Enrollment No.:", st_key), Paragraph(enroll, st_val)],
            [Paragraph("Subject:", st_key), Paragraph("Indian Constitution", st_val)],
            [Paragraph("Subject Code:", st_key), Paragraph("IT-410", st_val)],
            [Paragraph("Instructor:", st_key), Paragraph("Dr Arpit Namdev", st_val)],
            [Paragraph("Batch:", st_key), Paragraph("2024-2028", st_val)],
            [Paragraph("Semester:", st_key), Paragraph("IVth Semester", st_val)],
            [Paragraph("Year:", st_key), Paragraph("IInd year", st_val)],
        ]
        new_meta_table = Table(new_metadata, colWidths=[150, 200], hAlign="CENTER")
        new_meta_table.setStyle(meta_table_style)
        pn.story[meta_table_idx] = new_meta_table
        
        # 2. Update the global footer configuration
        pn.set_global_footer(
            left=f"Name: {name}",
            center=f"Enrollment no: {enroll}",
            show_page_num=True,
        )
        
        # 3. Build the PDF inside the temp directory
        pdf_filename = f"IC_Assignment_IT410_{enroll}.pdf"
        pdf_path = os.path.join(temp_dir, pdf_filename)
        pn.build_doc(pdf_path)
        print(f"[{students.index(s) + 1}/{len(students)}] Generated: {pdf_filename} for {name}")
        
        # 4. Add to ZIP file
        zipf.write(pdf_path, pdf_filename)
        
        # Keep the default name in the root workspace directory for Bharat Dangi
        if enroll == "0101IT241013":
            shutil.copyfile(pdf_path, "IC_Assignment_IT410.pdf")
            print("Generated: IC_Assignment_IT410.pdf (default copy)")

# Clean up the temporary directory containing individual PDFs
shutil.rmtree(temp_dir)
print(f"All student PDFs successfully generated and packaged into {zip_filename}")
