"""
Indian Constitution (IT410) -- Previous Year Question Answers
UIT-RGPV (Autonomous) Bhopal | Semester IV
Covers: June 2022, May-June 2023, May-June 2024, Nov-Dec 2024, June-July 2025
Run:    python ic_pyq.py
Output: IC_PYQ_Answers.pdf
"""

from __future__ import annotations

import paperforge_notes as pn
import paperforge_diagrams as pd

# =============================================================================
#  THEME & GLOBAL FOOTER & HEADER
# =============================================================================
pn.set_story([])

# Create print-optimized light theme using Times New Roman
print_theme = pn.LIGHT.copy_with(
    name="Print Light",
    body_font="Times-Roman",
    heading_font="Times-Bold",
    size_body=10.0,
    size_question=12.0,
    double_page_border=True,
    page_border_margin=15.0,
    page_border_gap=3.0,
    show_headers=True,
)
pn.set_theme(print_theme)

pn.set_global_header(
    left="Indian Constitution",
    center="Semester –IV",
    right="Session-July-Dec 2025",
)

pn.set_global_footer(
    left="Name: _________________________",
    center="Enrollment no: _________________________",
    show_page_num=True,
)

diag_theme = pd.DiagramTheme.from_notes_theme(pn.get_theme())

# =============================================================================
#  COVER PAGE
# =============================================================================
pn.bookmark("Cover Page")
pn.suppress_header(page_only=True)
pn.suppress_footer(page_only=True)
pn.sp(22)

pn.cover_card(
    "INDIAN CONSTITUTION (IT410)",
    "Previous Year Questions & Model Answers",
)
pn.cover_subtitle(
    [
        "UIT-RGPV (Autonomous) Bhopal  |  Semester IV  |  Subject Code: IT410",
        "Exam Papers Covered: June 2022  |  May-June 2023  |  May-June 2024  |  Nov-Dec 2024  |  June-July 2025",
        "All 5 Questions with Comprehensive Model Answers, Diagrams, and Tables",
    ]
)
pn.sp(8)
pn.rule(pn.get_theme().rl(pn.get_theme().accent), 1.5)
pn.sp(6)

pn.info_table(
    ["Question", "Topic Area", "Key Sub-Parts Covered"],
    [
        [
            "Q1",
            "Constitution & Salient Features",
            "Definition of Constitution and Constitutionalism, Salient Features, Company Rule (1773-1785), "
            "First Cabinet of Free India (1947), Supreme Court Original Jurisdiction, High Court constitution & qualifications",
        ],
        [
            "Q2",
            "Fundamental Rights, Duties & DPSP",
            "Universal Adult Franchise, Judicial Review, Preamble (elements/status), Writs under Article 32, "
            "Directive Principles of State Policy (importance/welfare state), Fundamental Duties (Swaran Singh & Verma Committees)",
        ],
        [
            "Q3",
            "Government Organs, Lok Sabha & Rajya Sabha",
            "Organs of Government, President/VP election & removal, President's judicial powers, Inter-State Council, "
            "Attorney General of India, Cabinet Secretariat, Rajya Sabha vs Lok Sabha, Centre-State legislative/financial relations",
        ],
        [
            "Q4",
            "Amendments, Emergency & Legislative Process",
            "Zero Hour, President's Rule vs Governor's Rule, National/Financial Emergency, Parliamentary Committees, "
            "Amendment procedure (Art. 368 & Basic Structure), Ordinary vs Money Bills, Delegated Legislation, Collective Responsibility",
        ],
        [
            "Q5",
            "Local Self Government, Citizenship & Environment",
            "Panchayati Raj (73rd/74th Amendments, Balwant Rai Mehta Committee, State Finance Commission), Decentralization, "
            "Art. 19 freedoms & restrictions, Art. 21 scope (life & liberty), Art. 14, Citizenship termination, NGOs in environment",
        ],
    ],
    col_widths=["10%", "28%", "62%"],
)

pn.sp(6)
pn.note(
    "Mark scheme: Part (a) = 3 marks | Part (b) = 4 marks | Part (c) = 4 marks | "
    "Part (d) = 10 marks | Part (e) = 10 marks (internal choice). "
    "Questions appearing across multiple exam years are consolidated into ONE comprehensive answer."
)
pn.br()

pn.suppress_header(page_only=True)
pn.suppress_footer(page_only=True)
pn.toc(style="index")
pn.br()

# #############################################################################
#  QUESTION 1 -- CONSTITUTION & SALIENT FEATURES
# #############################################################################
pn.part_box("QUESTION 1 -- CONSTITUTION & SALIENT FEATURES")

pn.chap_box(
    "Q1(a) [3 Marks] -- Definition of Constitution & Constitutionalism\n"
    "(May-June 2024 | May-June 2023 | June 2022 | June-July 2025)"
)

pn.section("Meaning of Constitution & Constitutional Law")
pn.definition(
    "<b>Constitution:</b> A constitution is the fundamental and supreme law of a country. "
    "It is a set of basic principles and established precedents according to which a state is governed. "
    "It defines the framework for the structure of government, distribution of powers among different organs "
    "(Legislature, Executive, Judiciary), and guarantees certain rights to citizens. Every other law in "
    "the country must conform to the constitution."
)
pn.definition(
    "<b>Constitutional Law:</b> Constitutional law is the body of law that defines the relationship "
    "between different entities within a state — the executive, legislature, and judiciary. "
    "It also defines the rights of citizens. Constitutional law includes the text of the constitution "
    "itself as well as all judicial interpretations and conventions that have developed around it."
)

pn.section("Meaning of Constitutionalism")
pn.definition(
    "<b>Constitutionalism:</b> Constitutionalism is the political philosophy that government authority "
    "is derived from and limited by a body of fundamental law (the constitution). It means that government "
    "must operate within the limits set by the constitution — no authority is absolute or unlimited. "
    "It embodies the principles of limited government, rule of law, separation of powers, "
    "protection of fundamental rights, and judicial review."
)

pn.section("Comparison: Constitution vs Constitutionalism")
pn.info_table(
    ["Basis", "Constitution", "Constitutionalism"],
    [
        [
            "Meaning",
            "The written or unwritten document/framework of governance.",
            "The political principle that government power is limited by law.",
        ],
        ["Nature", "A legal document.", "A political doctrine / ideology."],
        [
            "Focus",
            "Structure of government and rights.",
            "Limitation of government power.",
        ],
        [
            "Example",
            "The Constitution of India.",
            "Judicial review, fundamental rights enforcement.",
        ],
        [
            "Requirement",
            "A state may have a constitution.",
            "Constitutionalism requires the constitution to be respected and enforced.",
        ],
    ],
)


pn.br()
pn.chap_box("Q1(b) [4 Marks] -- Company Rule in India (1773-1785)\n" "(June 2022)")

pn.section("Historical Context of Company Rule")
pn.body(
    "Before direct British Crown rule (post-1858), the East India Company ruled India. "
    "The constitutional history of this period (1773–1785) is marked by the British Parliament's "
    "attempts to regulate the Company's affairs, which laid the foundation of centralized administration in India."
)

pn.section("Regulating Act of 1773")
pn.bullet(
    [
        "<b>Governor-General of Bengal:</b> Designated the Governor of Bengal as the 'Governor-General of Bengal' (Warren Hastings) and created an Executive Council of four members.",
        "<b>Subordination of Presidencies:</b> Made the Governors of Bombay and Madras Presidencies subordinate to the Governor-General of Bengal.",
        "<b>Supreme Court:</b> Provided for the establishment of a Supreme Court at Calcutta (1774) comprising one Chief Justice and three other judges.",
        "<b>Anti-Corruption:</b> Prohibited Company servants from engaging in private trade or accepting bribes/presents from natives.",
    ]
)

pn.section("Pitt's India Act of 1784")
pn.bullet(
    [
        "<b>Dual System of Control:</b> Distinguished between the commercial and political functions of the Company.",
        "<b>Board of Control:</b> Created a Board of Control to manage political affairs, while the Court of Directors managed commercial affairs.",
        "<b>Crown Supremacy:</b> Company territories in India were called the 'British possessions in India' for the first time, placing political affairs directly under British government supervision.",
        "<b>Reduction of Council Size:</b> Reduced the Governor-General's Executive Council size from four to three members to make administration more efficient.",
    ]
)

pn.br()
pn.chap_box(
    "Q1(c) [4 Marks] -- First Cabinet (1947) & Development Factors\n"
    "(June 2022 | June-July 2025)"
)

pn.section("First Cabinet of Free India (1947)")
pn.body(
    "Following independence on 15 August 1947, the first Cabinet of free India was formed. "
    "It comprised prominent leaders who headed key departments:"
)
pn.info_table(
    ["Leader", "Department / Portfolio"],
    [
        [
            "Jawaharlal Nehru",
            "Prime Minister, External Affairs & Commonwealth Relations, Scientific Research",
        ],
        ["Sardar Vallabhbhai Patel", "Home, Information & Broadcasting, States"],
        ["Dr. B.R. Ambedkar", "Law (Drafting Committee Chairman)"],
        ["Maulana Abul Kalam Azad", "Education"],
        ["Dr. John Matthai", "Railways & Transport"],
        ["Sardar Baldev Singh", "Defence"],
        ["Jagjivan Ram", "Labour"],
        ["Rafi Ahmed Kidwai", "Communications"],
        ["Rajkumari Amrit Kaur", "Health"],
        ["R.K. Shanmukham Chetty", "Finance"],
        ["Dr. Shyama Prasad Mukherjee", "Industries & Supplies"],
    ],
)

pn.section("Factors Influencing the Development of the Indian Constitution")
pn.body(
    "The development and features of the Indian Constitution were shaped by several critical factors:"
)
pn.bullet(
    [
        "<b>British Colonial Legacy & GOI Act 1935:</b> The administrative structure of the Constitution is heavily borrowed from the Government of India Act, 1935 (around 60% of the text). Provisions like the federal system, emergency powers, office of the Governor, judiciary, and public service commissions trace their origins here.",
        "<b>The Nationalist Freedom Struggle:</b> Decades of the independence movement crystallized key values. The Nehru Report (1928) championed fundamental rights, and the Karachi Resolution of the Indian National Congress (1931) laid down concrete economic and social policies, which later became the DPSPs and Fundamental Rights.",
        "<b>Global Constitutional Borrowings:</b> The framers, led by Dr. B.R. Ambedkar, 'ransacked' all known constitutions to adapt best practices. They borrowed the Parliamentary form of government and Rule of Law from the UK, Fundamental Rights and Judicial Review from the USA, DPSPs from Ireland, Emergency provisions from Germany (Weimar Constitution), and Amendment procedure from South Africa.",
        "<b>Socio-Economic & Cultural Diversity:</b> India's vast religious diversity, castewise inequalities, and geographical spread required specific constitutional safeguards. This influenced the inclusion of Article 17 (abolition of untouchability), religious freedom (Articles 25-28), and special provisions for SC/STs and backward classes in Part XVI."
    ]
)

pn.br()
pn.chap_box(
    "Q1(d) [10 Marks] -- Salient Features of the Indian Constitution\n"
    "(June 2022 | May-June 2024 | May-June 2023 | June-July 2025)"
)

pn.section("Salient Features of the Constitution")
pn.body(
    "The Constitution of India is unique in both its spirit and contents. Its salient features include:"
)
pn.info_table(
    ["Feature", "Explanation"],
    [
        [
            "1. Lengthiest Written Constitution",
            "Originally had 395 Articles (22 Parts, 8 Schedules). Now expanded to 448+ Articles. "
            "Due to geographical diversity, historical factors (1935 Act), and single constitution for both Centre and States.",
        ],
        [
            "2. Drawn from Various Sources",
            "Structural part from GoI Act 1935, philosophical part (FR & DPSP) from USA and Ireland, "
            "and political part (Parliamentary system) from the British Constitution.",
        ],
        [
            "3. Blend of Rigidity & Flexibility",
            "Partly rigid (requires 2/3 majority in Parliament + state ratification for federal features) "
            "and partly flexible (amended by a simple majority like ordinary laws).",
        ],
        [
            "4. Federal System with Unitary Bias",
            "Contains federal features (two governments, division of powers, written constitution, independent judiciary) "
            "but also strong unitary features (strong centre, single citizenship, single judiciary, emergency powers).",
        ],
        [
            "5. Parliamentary Form of Government",
            "Based on the Westminster model. Features nominal & real executives, majority party rule, "
            "collective responsibility of the executive to the legislature, and dissolution of the lower house.",
        ],
        [
            "6. Fundamental Rights (Part III)",
            "Six categories of justiciable rights guaranteed to citizens, acting as limitations on the tyranny of the executive "
            "and arbitrary laws of the legislature.",
        ],
        [
            "7. Directive Principles (Part IV)",
            "Non-justiciable guidelines to the State for establishing social and economic democracy, aiming to make India a welfare state.",
        ],
        [
            "8. Fundamental Duties (Part IV-A)",
            "Added by the 42nd Amendment (1976). Moral obligations on citizens to help maintain social order and patriotism.",
        ],
        [
            "9. Secular State",
            "No official religion. Equal respect and protection to all religions (positive concept of secularism).",
        ],
        [
            "10. Universal Adult Franchise",
            "Every citizen aged 18 or above has the right to vote in elections without discrimination. "
            "Voting age was reduced from 21 to 18 by the 61st Amendment (1988).",
        ],
        [
            "11. Integrated & Independent Judiciary",
            "Single integrated system of courts with the Supreme Court at the apex, guarding the Constitution "
            "and Fundamental Rights.",
        ],
        [
            "12. Single Citizenship",
            "Provides only Indian citizenship, fostering national integration unlike dual citizenship systems (e.g., USA).",
        ],
    ],
)

pn.br()
pn.chap_box(
    "Q1(e) [10 Marks] -- High Court Qualifications & Supreme Court Jurisdiction\n"
    "(May-June 2023 | June-July 2025)"
)

pn.section("Original Jurisdiction of the Supreme Court (Article 131)")
pn.definition(
    "<b>Original Jurisdiction:</b> The power of the Supreme Court to hear and decide disputes "
    "at the first instance, without going through lower courts. "
    "Under Article 131, the Supreme Court has exclusive original jurisdiction in federal disputes."
)
pn.body("This exclusive jurisdiction covers disputes between:")
pn.bullet(
    [
        "The Government of India (Centre) and one or more States.",
        "The Centre and any State(s) on one side, and one or more other States on the other side.",
        "Two or more States.",
    ]
)
pn.body(
    "<b>Note:</b> This jurisdiction does not extend to disputes arising out of pre-constitution treaties, "
    "covenants, agreements, or water disputes between states (which are referred to separate tribunals)."
)

pn.section("Other Jurisdictions of the Supreme Court")
pn.info_table(
    ["Jurisdiction", "Constitutional Provision & Scope"],
    [
        [
            "Writ Jurisdiction (Art. 32)",
            "Power to issue writs for the enforcement of Fundamental Rights. Enforceable against any authority.",
        ],
        [
            "Appellate Jurisdiction (Art. 132-134)",
            "Hears appeals against High Court judgments in constitutional, civil, and criminal matters.",
        ],
        [
            "Advisory Jurisdiction (Art. 143)",
            "The President can seek the opinion of the Supreme Court on questions of law or fact of public importance. Non-binding.",
        ],
        [
            "Court of Record (Art. 129)",
            "Its judgments are recorded for perpetual memory and testimony, and it has power to punish for contempt of itself.",
        ],
    ],
)

pn.section("Constitution of the High Court")
pn.definition(
    "<b>High Court:</b> Under Article 214, there shall be a High Court for each State. "
    "Article 216 states that every High Court shall consist of a Chief Justice and such other Judges "
    "as the President may from time to time deem it necessary to appoint."
)

pn.section("Qualifications of a High Court Judge (Article 217(2))")
pn.body(
    "To be appointed as a Judge of a High Court, a person must fulfill the following qualifications:"
)
pn.bullet(
    [
        "He must be a <b>citizen of India</b>.",
        "He must have held a <b>judicial office</b> in the territory of India for at least <b>10 years</b>, OR",
        "He must have been an <b>advocate</b> of a High Court (or of two or more such courts in succession) for at least <b>10 years</b>.",
    ]
)
pn.body(
    "<b>Note:</b> Unlike the Supreme Court, there is no provision in Article 217 for the appointment of a 'distinguished jurist' "
    "as a High Court Judge."
)
pn.br();

# #############################################################################
#  QUESTION 2 -- FUNDAMENTAL RIGHTS, DUTIES & DPSP
# #############################################################################
pn.part_box("QUESTION 2 -- FUNDAMENTAL RIGHTS, DUTIES & DPSP")

pn.chap_box(
    "Q2(a) [3 Marks] -- Universal Adult Franchise & Duties Scheme\n"
    "(May-June 2024 | June 2022 | Nov-Dec 2024 | June-July 2025)"
)

pn.section("Universal Adult Franchise (Article 326)")
pn.definition(
    "<b>Universal Adult Franchise:</b> It means the right of every adult citizen of India to vote "
    "in elections, irrespective of caste, religion, sex, literacy, wealth, or place of birth. "
    "In India, every citizen who is 18 years of age or above has the right to vote (Art. 326). "
    "The voting age was reduced from 21 to 18 by the 61st Constitutional Amendment Act, 1988."
)

pn.section("Fundamental Duties Scheme (Article 51A)")
pn.definition(
    "<b>Fundamental Duties:</b> Part IV-A (Article 51A) contains the Fundamental Duties. "
    "They were added by the 42nd Amendment (1976) on the recommendation of the Swaran Singh Committee. "
    "They are non-justiciable but serve as moral guidelines for citizens."
)
pn.info_table(
    ["Article 51A", "Summary of Fundamental Duty"],
    [
        [
            "(a) Respect Constitution",
            "Respect the Constitution, National Flag, and National Anthem.",
        ],
        ["(b) Cherish Ideals", "Follow the noble ideals of the freedom struggle."],
        [
            "(c) Protect Sovereignty",
            "Uphold and protect the sovereignty, unity, and integrity of India.",
        ],
        [
            "(d) Defend Country",
            "Defend the country and render national service when called upon.",
        ],
        [
            "(e) Promote Harmony",
            "Promote brotherhood and renounce practices derogatory to women.",
        ],
        [
            "(f) Value Heritage",
            "Value and preserve the rich heritage of our composite culture.",
        ],
        [
            "(g) Environment",
            "Protect forests, lakes, rivers, wildlife; have compassion for creatures.",
        ],
        [
            "(h) Scientific Temper",
            "Develop scientific temper, humanism, spirit of inquiry and reform.",
        ],
        ["(i) Public Property", "Safeguard public property and abjure violence."],
        [
            "(j) Excellence",
            "Strive toward excellence in all individual and collective spheres.",
        ],
        [
            "(k) Education (6-14)",
            "Provide education to child/ward aged 6-14 (86th Amendment, 2002).",
        ],
    ],
)

pn.br()
pn.chap_box(
    "Q2(b) [4 Marks] -- Judicial Review & Committee Reports on Duties\n"
    "(May-June 2024 | June 2022)"
)

pn.section("Judicial Review")
pn.definition(
    "<b>Judicial Review:</b> The power of the judiciary (Supreme Court and High Courts) to examine "
    "the constitutionality of legislative enactments and executive orders, and declare them void "
    "if they violate the Constitution. It is a part of the basic structure of the Constitution (Article 13, 32, 226)."
)
pn.bullet(
    [
        "<b>Constitutional Basis:</b> Article 13 declares that laws inconsistent with Fundamental Rights are void. Articles 32 and 226 empower courts to issue writs to enforce these rights.",
        "<b>Scope:</b> Applies to constitutional amendments, central/state legislation, and administrative actions.",
        "<b>Landmark Cases:</b> Marbury v. Madison (USA, 1803 - origin); Kesavananda Bharati (1973) and Minerva Mills (1980) confirmed review as basic structure."
    ]
)

pn.section("Swaran Singh Committee (1976) & Verma Committee (1999)")
pn.body(
    "<b>Swaran Singh Committee:</b> Appointed to recommend constitutional amendments on duties. "
    "Suggested incorporating 8 duties, and proposed that Parliament could impose penalties or "
    "punishment for refusal to observe them. Government accepted inclusion of duties (10 duties added) "
    "but rejected the penalty recommendation.<br/><br/>"
    "<b>Verma Committee (1999):</b> Appointed to operationalize and plan the implementation of "
    "Fundamental Duties. It observed that many duties are already legally enforceable through "
    "existing statutes, meaning that while the duties themselves are non-justiciable under Art. 51A, "
    "separate laws enact penalties for their violation."
)
pn.bullet(
    [
        "<b>Prevention of Insults to National Honour Act, 1971:</b> Prevents desecration of the National Flag and National Anthem.",
        "<b>Protection of Civil Rights Act, 1955:</b> Penalizes practices of untouchability and discrimination.",
        "<b>Wildlife Protection Act, 1972 & Forest Conservation Act, 1980:</b> Protect and conserve forests and wildlife.",
        "<b>Representation of the People Act, 1951:</b> Disqualifies members of Parliament/MLAs for corrupt electoral practices."
    ]
)

pn.section("Enforceability and Significance of Fundamental Duties (10 Marks)")
pn.definition(
    "<b>Enforceability:</b> Fundamental Duties are <i>non-justiciable</i>. Unlike Fundamental Rights, "
    "citizens cannot approach the courts directly for writs to enforce them. However, they are vital "
    "to the democratic fabric and well-being of the nation."
)
pn.bullet(
    [
        "<b>Constant Reminder:</b> They remind citizens that while enjoying rights, they must also be conscious of their duties to the nation and fellow citizens.",
        "<b>Deterrent against Anti-Social Activities:</b> They serve as a warning against anti-national and anti-social activities like burning the national flag, destroying public property, or disrupting peace.",
        "<b>Promoting Active Citizenship:</b> They foster a sense of discipline, commitment, and active participation among citizens, moving them from passive spectators to active participants in nation-building.",
        "<b>Source of Inspiration:</b> They promote a feeling of patriotism and respect for composite culture, national unity, and environmental preservation.",
        "<b>Constitutional Interpretation:</b> In determining the constitutionality of any law, courts refer to Fundamental Duties. If a law seeks to give effect to a duty, it is considered reasonable under Article 14 or 19."
    ]
)

pn.br()
pn.chap_box(
    "Q2(c) [4 Marks] -- Preamble Elements & Constitutional Status\n"
    "(May-June 2024 | May-June 2023)"
)

pn.section("Text of the Preamble")
pn.highlight(
    "<b>WE, THE PEOPLE OF INDIA,</b> having solemnly resolved to constitute India into a "
    "<b>SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC, REPUBLIC</b> and to secure to all its citizens: "
    "JUSTICE, LIBERTY, EQUALITY, FRATERNITY..."
)

pn.section("Five Key Elements of the Preamble")
pn.info_table(
    ["Element", "Meaning & Significance"],
    [
        [
            "1. Sovereign",
            "India is an independent state, free from any external control or dominion, and possesses supreme authority within its borders.",
        ],
        [
            "2. Socialist",
            "Added by 42nd Amendment (1976). Aims to achieve socialistic goals through democratic means (mixed economy, welfare state).",
        ],
        [
            "3. Secular",
            "Added by 42nd Amendment (1976). The State treats all religions equally and has no official state religion.",
        ],
        [
            "4. Democratic",
            "Power is vested in the people, exercised through adult franchise and elected representatives accountable to the electorate.",
        ],
        [
            "5. Republic",
            "The head of the state (President) is elected for a fixed term, and not a hereditary monarch.",
        ],
    ],
)

pn.section("Is the Preamble Part of the Constitution?")
pn.body("The legal status of the Preamble evolved through landmark cases:")
pn.bullet(
    [
        "<b>Berubari Union Case (1960):</b> The Supreme Court held that the Preamble is a key to open the minds of the framers, but it is <b>NOT</b> a part of the Constitution.",
        "<b>Kesavananda Bharati Case (1973):</b> The Supreme Court rejected its earlier view and held that the Preamble <b>IS</b> a part of the Constitution. It can be amended under Article 368, provided the basic structure is not altered.",
    ]
)

pn.br()
pn.chap_box(
    "Q2(d) [10 Marks] -- Constitutional Remedies & Writs (Article 32)\n"
    "(May-June 2024 | Nov-Dec 2024)"
)

pn.section("Article 32: Right to Constitutional Remedies")
pn.definition(
    "<b>Article 32:</b> Guarantees the right to move the Supreme Court by appropriate proceedings "
    "for the enforcement of Fundamental Rights. Dr. B.R. Ambedkar called Article 32 the "
    "'heart and soul' of the Constitution because it makes Fundamental Rights justiciable."
)

pn.section("The Five Writs")
pn.info_table(
    ["Writ", "Literal Meaning", "Scope & Against Whom", "Example / Application"],
    [
        [
            "1. Habeas Corpus",
            "'To have the body'",
            "Issued against both public authorities and private entities. Directs a person detaining another to produce them in court.",
            "To challenge illegal arrest or unlawful detention.",
        ],
        [
            "2. Mandamus",
            "'We command'",
            "Issued to public officials, public bodies, inferior courts, or tribunals. Commands them to perform a statutory duty.",
            "To compel an officer to issue a license they are legally bound to issue.",
        ],
        [
            "3. Prohibition",
            "'To forbid'",
            "Issued by a higher court to a lower court or quasi-judicial body to prevent it from exceeding its jurisdiction.",
            "To stop a district court from trying a case outside its jurisdiction.",
        ],
        [
            "4. Certiorari",
            "'To be certified'",
            "Issued by a higher court to a lower court or tribunal to quash an order already passed in excess of jurisdiction.",
            "To quash an illegal administrative tribunal order.",
        ],
        [
            "5. Quo Warranto",
            "'By what authority'",
            "Issued to inquire into the legality of the claim of a person to a public office. Prevents illegal usurpation.",
            "To challenge the appointment of an unqualified university vice-chancellor.",
        ],
    ],
)

pn.section("Article 32 vs Article 226 Writ Jurisdiction")
pn.info_table(
    ["Feature", "Article 32 (Supreme Court)", "Article 226 (High Court)"],
    [
        [
            "Purpose",
            "Enforcement of Fundamental Rights only.",
            "Enforcement of Fundamental Rights AND other legal rights (wider scope).",
        ],
        [
            "Territory",
            "Territorial jurisdiction extends to the entire country.",
            "Limited to the territory of the respective State.",
        ],
        [
            "Nature of Power",
            "It is a Fundamental Right itself; the SC cannot refuse to entertain a petition.",
            "It is discretionary; the HC can refuse if alternate remedies exist.",
        ],
    ],
)

pn.br()
pn.chap_box(
    "Q2(e) [10 Marks] -- DPSPs, Welfare State & Fundamental Rights\n"
    "(May-June 2024 | May-June 2023 | June 2022 | Nov-Dec 2024 | June-July 2025)"
)

pn.section("DPSPs: Welfare State Objectives")
pn.definition(
    "<b>Directive Principles of State Policy (DPSP):</b> Contained in Part IV (Articles 36–51). "
    "They are non-justiciable directives to the State to secure a social order characterized by justice, "
    "equality, and liberty, aiming to transform India into a welfare state."
)

pn.section("Classification of DPSPs")
pn.info_table(
    ["Category", "Articles", "Key Directives"],
    [
        [
            "1. Socialistic Principles",
            "Art. 38, 39, 39A, 41, 42, 43, 47",
            "Promote public welfare, minimize inequalities, secure equal pay for equal work, "
            "provide free legal aid, right to work, and maternity relief.",
        ],
        [
            "2. Gandhian Principles",
            "Art. 40, 43, 43B, 46, 47, 48",
            "Organize village panchayats, promote cottage industries, promote educational interests "
            "of SC/ST, prohibit consumption of intoxicating drinks, and ban cow slaughter.",
        ],
        [
            "3. Liberal-Intellectual",
            "Art. 44, 45, 48, 48A, 49, 50, 51",
            "Secure a Uniform Civil Code (Art. 44), provide early childhood education, protect environment, "
            "separate judiciary from executive (Art. 50), and promote international peace.",
        ],
    ],
)

pn.section("Scheme & Classification of Fundamental Rights")
pn.body(
    "Fundamental Rights in Part III (Articles 12-35) are justiciable. They are classified into six groups:"
)
pn.bullet(
    [
        "<b>Right to Equality (Articles 14-18):</b> Equality before law, abolition of untouchability, equal opportunity.",
        "<b>Right to Freedom (Articles 19-22):</b> Six freedoms (Art. 19), protection of life & personal liberty (Art. 21).",
        "<b>Right against Exploitation (Articles 23-24):</b> Ban on forced labour and child labour.",
        "<b>Right to Freedom of Religion (Articles 25-28):</b> Freedom of conscience, manage religious affairs.",
        "<b>Cultural and Educational Rights (Articles 29-30):</b> Protect minority languages and establish institutions.",
        "<b>Right to Constitutional Remedies (Article 32):</b> Power to move the Supreme Court for writ enforcement.",
    ]
)

pn.section("FR vs DPSP Interrelationship")
pn.body(
    "While Fundamental Rights protect political democracy (individual liberty), DPSPs promote social and "
    "economic democracy (collective welfare). In <b>Minerva Mills Case (1980)</b>, the Supreme Court held "
    "that the Indian Constitution is founded on the bedrock of the balance between Part III and Part IV. "
    "They are complementary and together form the 'conscience of the Constitution.'"
)
pn.br();

# #############################################################################
#  QUESTION 3 -- GOVERNMENT ORGANS, LOK SABHA & RAJYA SABHA
# #############################################################################
pn.part_box("QUESTION 3 -- GOVERNMENT ORGANS, LOK SABHA & RAJYA SABHA")

pn.chap_box(
    "Q3(a) [3 Marks] -- Organs of Government & Inter-State Council\n"
    "(May-June 2024 | Nov-Dec 2024)"
)

pn.section("Three Organs of the Indian Government")
pn.body(
    "The government functions through three distinct organs, ensuring a system of checks and balances:"
)

# Diagram: LayeredStack for Organs of Government
stack_organs = pd.LayeredStack(
    width=pn.CW * 0.75,
    height=185,
    theme=diag_theme,
    caption="Fig 3.1: Three Organs of the Indian Government",
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

pn.section("Inter-State Council (Article 263)")
pn.definition(
    "<b>Inter-State Council:</b> A constitutional body established under Article 263 to promote "
    "coordination between the States and the Centre. Established in 1990 on the recommendation "
    "of the Sarkaria Commission, it is presided over by the Prime Minister and includes all State Chief Ministers."
)

pn.br()
pn.chap_box(
    "Q3(b) [4 Marks] -- President's Judicial Powers & Cabinet Secretariat\n"
    "(May-June 2024 | Nov-Dec 2024)"
)

pn.section("Judicial Powers of the President of India (Article 72)")
pn.body(
    "Article 72 empowers the President to grant pardons, reprieves, respites, or remissions of "
    "punishment, or to suspend, remit, or commute the sentence of any person convicted of any offence:"
)
pn.bullet(
    [
        "<b>Pardon:</b> Completely absolves the offender from both the conviction and the sentence, making them a free citizen.",
        "<b>Commutation:</b> Substitutes one form of punishment for a lighter form (e.g., death sentence commuted to rigorous imprisonment).",
        "<b>Remission:</b> Reduces the period of sentence without changing its character (e.g., reducing imprisonment from 2 years to 1 year).",
        "<b>Respite:</b> Awards a lesser sentence in place of one originally awarded due to special facts (e.g., pregnancy of a female offender).",
        "<b>Reprieve:</b> Stays the execution of a sentence (especially death sentence) temporarily to allow the convict time to seek pardon.",
    ]
)

pn.section("Role & Functions of the Cabinet Secretariat")
pn.definition(
    "<b>Cabinet Secretariat:</b> An administrative organ operating directly under the Prime Minister. "
    "Its administrative head is the Cabinet Secretary, the senior-most civil servant in India. "
    "It provides secretarial assistance and facilitates smooth transaction of business in the Government of India."
)
pn.bullet(
    [
        "<b>Meeting Coordination:</b> Prepares agendas and records minutes of Cabinet and Cabinet Committee meetings.",
        "<b>Policy Tracking:</b> Monitors the implementation of decisions taken by the Cabinet.",
        "<b>Inter-Ministerial Coordination:</b> Resolves disputes and coordinates administrative action between different ministries.",
    ]
)

pn.br()
pn.chap_box(
    "Q3(c) [4 Marks] -- President & Vice President Election & Impeachment\n"
    "(May-June 2023 | June 2022)"
)

pn.section("President of India: Election and Impeachment")
pn.definition(
    "<b>Election:</b> Elected indirectly by an Electoral College consisting of: (1) Elected members of both "
    "Houses of Parliament (MPs), and (2) Elected members of State Legislative Assemblies (MLAs). "
    "System: Proportional representation with single transferable vote."
)
pn.definition(
    "<b>Impeachment (Article 61):</b> Can be removed only for 'violation of the Constitution'. "
    "Impeachment charges can be initiated by either House of Parliament (signed by 1/4 of members). "
    "Passed by a special majority of <b>not less than 2/3 of the total membership</b> of both Houses."
)

pn.section("Vice President of India: Election and Removal")
pn.definition(
    "<b>Election (Article 66):</b> Elected by an Electoral College consisting of members of both Houses of Parliament "
    "(both elected and nominated MPs). State legislatures do not participate."
)
pn.definition(
    "<b>Removal:</b> Can be removed by a resolution of the Rajya Sabha passed by an effective majority "
    "(majority of all the then members) and agreed to by the Lok Sabha by a simple majority. "
    "No formal impeachment procedure is required."
)

pn.br()
pn.chap_box(
    "Q3(d) [10 Marks] -- Attorney General & Centre-State Relations\n"
    "(Nov-Dec 2024 | June-July 2025)"
)

pn.section("Attorney General of India (Article 76)")
pn.definition(
    "<b>Attorney General (AG):</b> The chief legal adviser and lawyer of the Government of India, "
    "appointed by the President. Must be qualified to be appointed as a Supreme Court Judge."
)
pn.bullet(
    [
        "<b>Duties:</b> Give advice to the GoI on legal matters, perform legal duties assigned by the President, and represent the Union in courts.",
        "<b>Rights:</b> Right of audience in all courts in India. Right to speak and participate in proceedings of both Houses of Parliament (and committees) but <b>without the right to vote</b>.",
        "<b>Limitations:</b> Cannot advise against the GoI, and cannot represent accused in criminal cases without government permission.",
    ]
)

pn.section("Centre-State Legislative relations (Articles 245-255)")
pn.body("Legislative powers are divided into three lists under the Seventh Schedule:")
pn.bullet(
    [
        "<b>Union List (List I):</b> ~100 subjects (Defence, Foreign Affairs, Banking) where Parliament has exclusive power.",
        "<b>State List (List II):</b> ~61 subjects (Police, Agriculture, Local Government) where State Legislatures legislate.",
        "<b>Concurrent List (List III):</b> ~52 subjects (Education, Forests) where both can legislate. Central law prevails in case of conflict (Art. 254).",
    ]
)
pn.body("<b>Note:</b> Residuary powers of legislation are vested in Parliament (Article 248).")

pn.section("Centre-State Administrative & Financial Relations")
pn.body(
    "<b>Administrative Relations (Articles 256-263):</b> Executive power of States must be exercised "
    "to ensure compliance with Union laws. The Centre can issue directions to States. All-India Services "
    "(IAS, IPS) are controlled by the Centre but serve States.<br/><br/>"
    "<b>Financial Relations (Articles 268-293):</b> Taxes are levied, collected, and distributed "
    "between Union and States based on recommendations of the Finance Commission (Art. 280). "
    "The Centre also provides grants-in-aid to States out of the Consolidated Fund of India."
)

pn.br()
pn.chap_box(
    "Q3(e) [10 Marks] -- Parliamentary Houses & Federal/Unitary Structure\n"
    "(May-June 2024 | June 2022 | Nov-Dec 2024 | June-July 2025)"
)

pn.section("Comparison: Lok Sabha vs Rajya Sabha")
pn.info_table(
    ["Basis", "Lok Sabha (Lower House)", "Rajya Sabha (Upper House)"],
    [
        [
            "Composition",
            "Max 550 members (representing the people directly).",
            "Max 250 members (representing States/UTs indirectly).",
        ],
        [
            "Tenure",
            "5 years. Can be dissolved earlier by the President.",
            "Permanent chamber. 1/3 members retire every 2 years. 6-year term.",
        ],
        [
            "Presiding Officer",
            "Speaker (elected by the House).",
            "Vice President of India (Ex-officio Chairman).",
        ],
        [
            "Money Bills",
            "Can only be introduced here. LS has absolute power.",
            "Cannot be introduced here. Can only delay for 14 days.",
        ],
        [
            "No-Confidence",
            "Can oust the Government via no-confidence motion.",
            "No power to pass a no-confidence motion.",
        ],
        [
            "Special Powers",
            "Passes budget and ousts executive.",
            "Art. 249 (leg on State list), Art. 312 (All-India Services).",
        ],
    ],
)

pn.section("Why is Rajya Sabha called a Permanent Chamber?")
pn.body(
    "Under Article 83(1), the Rajya Sabha is not subject to dissolution. This ensures continuity "
    "in governance during times when the Lok Sabha is dissolved (e.g., during elections or cabinet collapse). "
    "It acts as a stabilizing force and a revising chamber to prevent hasty legislation."
)

pn.section("Federal vs Unitary Features of the Indian Constitution")
pn.body(
    "India is described as a 'Union of States' (Article 1). K.C. Wheare described it as 'quasi-federal' "
    "due to its blend of federal and unitary features:"
)
pn.info_table(
    ["Federal Features (Autonomy)", "Unitary Features (Central Control)"],
    [
        [
            "Dual Polity (Centre and State governments).",
            "Strong Centre (more subjects in Union List, residuary powers).",
        ],
        [
            "Written and Supreme Constitution.",
            "Single Constitution for both Centre and States.",
        ],
        [
            "Division of powers (Seventh Schedule lists).",
            "Single integrated judiciary with Supreme Court at apex.",
        ],
        [
            "Independent Judiciary to resolve federal disputes.",
            "Appointment of Governor by the President.",
        ],
        [
            "Bicameralism (Rajya Sabha representing states).",
            "Emergency provisions (converts federal structure to unitary).",
        ],
    ],
)
pn.br();

# #############################################################################
#  QUESTION 4 -- AMENDMENTS, EMERGENCY & LEGISLATIVE PROCESS
# #############################################################################
pn.part_box("QUESTION 4 -- AMENDMENTS, EMERGENCY & LEGISLATIVE PROCESS")

pn.chap_box(
    "Q4(a) [3 Marks] -- Zero Hour & Emergency Types\n" "(May-June 2024 | May-June 2023)"
)

pn.section("Zero Hour in Indian Parliament")
pn.definition(
    "<b>Zero Hour:</b> An informal parliamentary innovation in India (not mentioned in the rules). "
    "It starts immediately after the Question Hour (around 12:00 noon) and lasts until the regular agenda. "
    "During this time, members of Parliament can raise matters of urgent public importance "
    "without any prior notice."
)

pn.section("Types of Emergency in the Indian Constitution (10 Marks)")
pn.body(
    "Part XVIII of the Constitution (Articles 352–360) describes three types of emergency, "
    "which can be proclaimed by the President of India when the security, governance, or financial stability "
    "of the nation is under threat. These provisions temporarily convert the federal system into a unitary one."
)
pn.info_table(
    ["Emergency Type", "Article", "Grounds for Proclamation", "Parliamentary Approval & Max Duration"],
    [
        ["1. National Emergency", "Article 352", "War, external aggression, or armed rebellion (amended from 'internal disturbance' by 44th Amendment).", "Approved by special majority of both Houses within 1 month. Valid for 6 months; can be extended indefinitely."],
        ["2. President's Rule (State)", "Article 356", "Failure of constitutional machinery in a State (Art. 356) or non-compliance with Centre's directions (Art. 365).", "Approved by simple majority of both Houses within 2 months. Valid for 6 months; max 3 years."],
        ["3. Financial Emergency", "Article 360", "Threat to the financial stability or credit of India or any part of its territory.", "Approved by simple majority of both Houses within 2 months. Valid indefinitely until revoked."]
    ],
)
pn.bullet(
    [
        "<b>National Emergency (Art. 352):</b> Suspends the distribution of revenues between Centre and States. Parliament gets the power to make laws on State List subjects. Under Article 358, the six freedoms of Article 19 are automatically suspended, while Article 359 allows suspension of the right to move courts to enforce other Fundamental Rights (except Article 20 and 21).",
        "<b>President's Rule (Art. 356):</b> The Governor administers the State on behalf of the President, and the State Legislative Assembly is either suspended or dissolved. Parliament assumes the legislative powers of the State.",
        "<b>Financial Emergency (Art. 360):</b> The President can issue directions to States to observe canons of financial propriety, reserve all Money Bills passed by State legislatures for Presidential assent, and reduce the salaries of all public servants, including Supreme Court and High Court judges."
    ]
)

pn.br()
pn.chap_box(
    "Q4(b) [4 Marks] -- State Emergency & Bills Comparison\n"
    "(May-June 2024 | May-June 2023 | Nov-Dec 2024)"
)

pn.section("President's Rule (Art. 356) vs Governor's Rule")
pn.body(
    "Under the general scheme of the Constitution, a failure of constitutional machinery in a state "
    "leads directly to <b>President's Rule</b> under Article 356. The President assumes the executive functions "
    "of the state government. Historically, in the former state of Jammu & Kashmir (under Section 92 of the J&K Constitution), "
    "a failure of machinery first resulted in <b>Governor's Rule</b> for 6 months. If not resolved, President's Rule "
    "was then imposed. Post 2019, J&K is a Union Territory under standard central provisions."
)

pn.section("Comparison: National Emergency (Art. 352) vs President's Rule (Art. 356)")
pn.info_table(
    ["Basis of Comparison", "National Emergency (Article 352)", "President's Rule (Article 356)"],
    [
        [
            "Grounds",
            "Declared only when the security of India or a part of it is threatened by war, external aggression, or armed rebellion.",
            "Declared when the government of a State cannot be carried on in accordance with the provisions of the Constitution.",
        ],
        [
            "State Government",
            "The State executive and legislature continue to exist and function, but they are subject to the concurrent control of the Union.",
            "The State executive is dismissed and the State legislature is either suspended or dissolved. The Governor administers the State.",
        ],
        [
            "Legislative Power",
            "Parliament makes laws on State List subjects itself, and cannot delegate this legislative power to other authorities.",
            "Parliament can delegate the power to make laws for the State to the President or to any other authority specified by the President.",
        ],
        [
            "Parliament Approval",
            "Must be approved within 1 month by a special majority (2/3 of members present & voting + majority of total membership).",
            "Must be approved within 2 months by a simple majority.",
        ],
        [
            "Maximum Duration",
            "No maximum period. Can be extended indefinitely every 6 months with parliamentary approval.",
            "Maximum period is 3 years. Beyond that, a constitutional amendment is required to extend it.",
        ],
        [
            "Fundamental Rights",
            "Affects Fundamental Rights. Art. 19 is automatically suspended; other rights (except Art. 20 and 21) can be suspended by decree.",
            "Has absolutely no effect on the Fundamental Rights of the citizens in the State.",
        ],
    ],
)

pn.section("Comparison: Ordinary Bill vs Money Bill")
pn.info_table(
    ["Basis", "Ordinary Bill", "Money Bill (Article 110)"],
    [
        [
            "Introduction",
            "Can be introduced in either Lok Sabha or Rajya Sabha.",
            "Can be introduced ONLY in the Lok Sabha.",
        ],
        [
            "Prior Recommendation",
            "No prior recommendation of the President is required.",
            "Can be introduced only on the President's recommendation.",
        ],
        [
            "Rajya Sabha Powers",
            "Rajya Sabha can amend or reject the Bill.",
            "Rajya Sabha cannot amend or reject. Must return in 14 days.",
        ],
        [
            "Joint Sitting",
            "Joint sitting (Art. 108) is allowed to resolve deadlocks.",
            "No provision for a joint sitting.",
        ],
        [
            "Presidential Assent",
            "President can assent, reject, or return for reconsideration.",
            "President can assent or reject, but <b>cannot</b> return it.",
        ],
    ],
)

pn.br()
pn.chap_box(
    "Q4(c) [4 Marks] -- Financial Emergency & Ordinary Bill Procedure\n"
    "(June 2022 | May-June 2023)"
)

pn.section("Financial Emergency (Article 360) (10 Marks)")
pn.definition(
    "<b>Financial Emergency:</b> Under Article 360, the President can proclaim a Financial Emergency "
    "if they are satisfied that a situation has arisen whereby the financial stability or credit of India "
    "or any part of its territory is threatened."
)
pn.bullet(
    [
        "<b>Parliamentary Approval:</b> The proclamation must be approved by both Houses of Parliament within <b>two months</b> of its issuance by a simple majority. If the Lok Sabha is dissolved, it must be approved within 30 days of the first sitting of the new Lok Sabha, provided the Rajya Sabha has already approved it.",
        "<b>Duration:</b> Once approved, it continues <b>indefinitely</b> without requiring periodic approvals, until it is revoked by the President through a subsequent proclamation.",
        "<b>Impact on State Finances:</b> The Union executive can issue directions to any State to observe specified canons of financial propriety. This includes requiring all Money Bills or other Financial Bills passed by the State legislature to be reserved for the President's consideration.",
        "<b>Salary Reductions:</b> The Centre can direct States to reduce the salaries and allowances of any class of persons serving the State. Furthermore, the President can order salary and allowance reductions for all Union government servants, including the judges of the Supreme Court and the High Courts.",
        "<b>Historical Context:</b> To date, a Financial Emergency has <b>never</b> been declared in India, not even during the severe balance of payments crisis of 1991."
    ]
)

pn.section("Procedure for Passing an Ordinary Bill")
pn.body("The passage of an Ordinary Bill involves five key stages:")

# Diagram: LayeredStack for passage of a bill
stack_bill = pd.LayeredStack(
    width=pn.CW * 0.75,
    height=250,
    theme=diag_theme,
    caption="Fig 4.1: Key Stages in the Passage of an Ordinary Bill",
)
stack_bill.layer(
    "Stage 5: Presidential Assent (Art. 111)",
    sublabel="Assent, veto, or return for reconsideration (except Money Bills)",
)
stack_bill.layer(
    "Stage 4: Passage in the Second House",
    sublabel="Sent to the other chamber where it undergoes the same three readings",
)
stack_bill.layer(
    "Stage 3: Third Reading",
    sublabel="Final debate and voting on the passage of the Bill as a whole",
)
stack_bill.layer(
    "Stage 2: Second Reading",
    sublabel="Clause-by-clause scrutiny, committee review, and voting on amendments",
)
stack_bill.layer(
    "Stage 1: First Reading",
    sublabel="Introduction of the Bill in either House and publication in the Gazette",
)
pn.story.extend(stack_bill.as_flowable())
pn.sp(4)

pn.br()
pn.chap_box(
    "Q4(d) [10 Marks] -- Delegated Legislation & Executive Responsibility\n"
    "(Nov-Dec 2024 | May-June 2023)"
)

pn.section("Delegated Legislation (Subordinate Legislation)")
pn.definition(
    "<b>Delegated Legislation:</b> The process by which the legislature (Parliament) delegates law-making "
    "authority to the executive (ministries and administrative bodies) to frame detailed rules, "
    "regulations, and bye-laws within the limits of the parent Act."
)
pn.bullet(
    [
        "<b>Importance for Efficiency:</b> Parliament lacks the time to draft highly detailed, technical rules (e.g., tax procedures, environmental limits), so it defines the policy framework, and the executive fills in the details.",
        "<b>Technical Expertise:</b> Administrative bodies possess the technical experts required to draft rules for specialized sectors (e.g., cyber laws, telecom standards).",
        "<b>Flexibility:</b> Enables quick changes to rules to adapt to changing circumstances or emergencies without passing a new act in Parliament.",
        "<b>Safeguards:</b> Controlled via <i>judicial review</i> (declared void if ultra vires the parent Act or Constitution) and <i>parliamentary committees</i> on delegated legislation.",
    ]
)

pn.section("Collective Responsibility of the Council of Ministers (Article 75(3))")
pn.definition(
    "<b>Collective Responsibility:</b> Article 75(3) states that the Council of Ministers shall be "
    "collectively responsible to the Lok Sabha. This is the cornerstone of parliamentary democracy, "
    "meaning that all ministers stand or fall together."
)
pn.bullet(
    [
        "<b>Swim or Sink Together:</b> The cabinet decisions bind all ministers. If a minister disagrees with a cabinet decision, they must resign (e.g., Dr. B.R. Ambedkar resigned in 1951 over the Hindu Code Bill).",
        "<b>No-Confidence Motion:</b> If a no-confidence motion is passed in the Lok Sabha against the Prime Minister or any single minister on policy matters, the entire Council of Ministers must resign.",
        "<b>Defense of Policy:</b> Every minister is duty-bound to defend cabinet decisions both inside and outside Parliament, ensuring administrative unity.",
    ]
)

pn.br()
pn.chap_box(
    "Q4(e) [10 Marks] -- Amendment Procedure & Parliamentary Committees\n"
    "(May-June 2024 | May-June 2023 | June 2022 | Nov-Dec 2024)"
)

pn.section("Amendment Procedure under Article 368")
pn.body(
    "Article 368 outlines the power and procedure of Parliament to amend the Constitution by way of "
    "addition, variation, or repeal. Amendments are made through three methods:"
)
pn.info_table(
    ["Amendment Method", "Procedure Required", "Examples of Provisions"],
    [
        [
            "1. Simple Majority",
            "Passed by a simple majority of members present and voting in each House (outside Art. 368).",
            "Admission of new states, salaries of MPs, rules of procedure, official language.",
        ],
        [
            "2. Special Majority (Art. 368)",
            "Passed in each House by: (1) majority of total membership, AND (2) 2/3 of members present and voting.",
            "Fundamental Rights (Part III) and Directive Principles of State Policy (Part IV).",
        ],
        [
            "3. Special Majority + State Ratification",
            "Special majority in Parliament PLUS ratification by legislatures of at least 50% of the States.",
            "Federal provisions: Election of President, Union-State distribution of legislative powers (7th Schedule), Article 368 itself.",
        ],
    ],
)

pn.section("Basic Structure Doctrine")
pn.body(
    "In the landmark <b>Kesavananda Bharati Case (1973)</b>, the Supreme Court held that while Parliament "
    "has wide powers to amend the Constitution, it <b>cannot alter or destroy the basic structure</b> "
    "of the Constitution (e.g., supremacy of the Constitution, secularism, democracy, federalism, judicial review)."
)

pn.section("Parliamentary Committees: PAC and Estimates Committee")
pn.body(
    "Financial committees of Parliament ensure financial accountability of the executive:"
)
pn.info_table(
    ["Feature", "Public Accounts Committee (PAC)", "Estimates Committee"],
    [
        [
            "Composition",
            "22 members (15 Lok Sabha + 7 Rajya Sabha).",
            "30 members (all from Lok Sabha only).",
        ],
        [
            "Role & Function",
            "Examines the appropriation accounts and the audit reports of the CAG to ensure funds were spent as authorized.",
            "Examines budget estimates to suggest economies, organizational improvements, and efficiency in administration.",
        ],
        [
            "Focus",
            "Post-mortem analysis of expenditure already incurred.",
            "Pre-expenditure analysis of budget estimates.",
        ],
        [
            "Chairman",
            "By convention, appointed from the Opposition party.",
            "Appointed from the ruling party.",
        ],
    ],
)
pn.br();

# #############################################################################
#  QUESTION 5 -- LOCAL SELF GOVERNMENT, CITIZENSHIP & ENVIRONMENT
# #############################################################################
pn.part_box("QUESTION 5 -- LOCAL SELF GOVERNMENT, CITIZENSHIP & ENVIRONMENT")

pn.chap_box(
    "Q5(a) [3 Marks] -- Panchayati Raj & Citizenship Termination\n"
    "(May-June 2024 | Nov-Dec 2024 | June-July 2025)"
)

pn.section("What is Panchayati Raj?")
pn.definition(
    "<b>Panchayati Raj:</b> The system of rural local self-government in India. Constitutionalized "
    "by the <b>73rd Constitutional Amendment Act, 1992</b> (adding Part IX and the 11th Schedule with 29 subjects). "
    "It establishes a 3-tier structure (Gram Panchayat, Panchayat Samiti, Zila Parishad) to ensure grassroots democracy."
)

pn.section("Methods of Termination of Indian Citizenship")
pn.body(
    "The Citizenship Act, 1955 prescribes three methods of losing/terminating Indian citizenship:"
)
pn.info_table(
    ["Method", "How it Occurs"],
    [
        [
            "1. Renunciation",
            "A citizen of full age and capacity voluntarily declares they are giving up Indian citizenship (e.g., on acquiring foreign nationality).",
        ],
        [
            "2. Termination",
            "If an Indian citizen voluntarily acquires the citizenship of another country, their Indian citizenship automatically terminates.",
        ],
        [
            "3. Deprivation",
            "A compulsory termination by the Central Government on grounds of fraud, disloyalty to the Constitution, or illegal trade during war.",
        ],
    ],
)

pn.br()
pn.chap_box(
    "Q5(b) [4 Marks] -- Balwant Rai Mehta Committee & Finance Commission\n"
    "(May-June 2024 | Nov-Dec 2024)"
)

pn.section("Recommendations of Balwant Rai Mehta Committee (1957)")
pn.body(
    "Appointed to examine the working of the Community Development Programme, the committee recommended "
    "democratic decentralization through a 3-tier Panchayati Raj system:"
)
pn.bullet(
    [
        "<b>Three-Tier System:</b> Gram Panchayat at village level (direct election), Panchayat Samiti at block level (indirect election), and Zila Parishad at district level (advisory/supervisory).",
        "<b>Panchayat Samiti as Pivot:</b> The block level should be the primary executive body for developmental works.",
        "<b>Devolution of Power:</b> Genuine transfer of power, responsibility, and financial resources to these local bodies.",
        "<b>District Collector:</b> The Collector should be the Chairman of the Zila Parishad to ensure coordination.",
    ]
)

pn.section("State Finance Commission (Article 243I)")
pn.definition(
    "<b>State Finance Commission (SFC):</b> A constitutional body constituted by the Governor of "
    "a State every 5 years under Article 243I (and 243Y) to review the financial position of local bodies "
    "(Panchayats and Municipalities) and recommend tax devolution."
)
pn.bullet(
    [
        "<b>Tax Distribution:</b> Recommends the distribution of net proceeds of state taxes, duties, and tolls between the State and local bodies.",
        "<b>Grants-in-Aid:</b> Determines the grants-in-aid to be paid to local bodies from the Consolidated Fund of the State.",
        "<b>Financial Soundness:</b> Suggests measures to improve the financial health and revenue-raising capacity of Panchayats.",
    ]
)

pn.br()
pn.chap_box(
    "Q5(c) [4 Marks] -- Scope of Right to Life & Personal Liberty\n"
    "(May-June 2023 | June 2022)"
)

pn.section("Article 21: Right to Life and Personal Liberty (10 Marks)")
pn.definition(
    "<b>Article 21:</b> 'No person shall be deprived of his life or personal liberty except according "
    "to procedure established by law.' This right is available to both citizens and non-citizens. "
    "The scope of Article 21 has undergone a massive evolution through judicial interpretation."
)
pn.bullet(
    [
        "<b>A.K. Gopalan Case (1950) -- Narrow View:</b> The Supreme Court held a literal view of 'procedure established by law'. It ruled that if the legislature passed a law providing a procedure for depriving a person of life or liberty, the court could not examine the fairness or justice of that law. It offered protection only against arbitrary executive action, not legislative action.",
        "<b>Maneka Gandhi Case (1978) -- Wide View:</b> The Supreme Court overruled Gopalan and held that 'procedure' must be <b>fair, just, and reasonable</b>, and not arbitrary, oppressive, or fanciful. This introduced the American concept of <i>'Due Process of Law'</i>. The court ruled that Article 21 is not isolated but must be read with Articles 14 and 19 (the <b>'Golden Triangle'</b> of the Constitution).",
        "<b>Meaning of 'Life':</b> The court declared that 'life' does not mean mere animal existence. It includes the right to live with human dignity and all those aspects of life which go to make a man's life meaningful, complete, and worth living."
    ]
)

pn.section("Implied Rights under Article 21")
pn.body(
    "Through judicial activism, the Supreme Court has read several unenumerated rights into Article 21, "
    "expanding its scope to include the following rights:"
)
pn.info_table(
    ["Implied Right", "Scope & Constitutional Significance", "Landmark Supreme Court Case"],
    [
        [
            "1. Right to Privacy",
            "Declared a fundamental right. Protects informational privacy and bodily autonomy.",
            "K.S. Puttaswamy v. Union of India (2017)",
        ],
        [
            "2. Right to Livelihood",
            "No person can be deprived of their livelihood except through fair and just procedure, as it is essential for life.",
            "Olga Tellis v. Bombay Municipal Corporation (1985)",
        ],
        [
            "3. Right to a Clean Environment",
            "Includes the right to pollution-free water and air for full enjoyment of life. Led to green litigation.",
            "M.C. Mehta v. Union of India (1987) / Subhash Kumar (1991)",
        ],
        [
            "4. Right to Free Education (6-14)",
            "Every child has a right to free education. This led to the 86th Amendment adding Article 21A.",
            "Unni Krishnan v. State of A.P. (1993)",
        ],
        [
            "5. Right to Die with Dignity",
            "Permitted passive euthanasia under strict guidelines; recognizes the right of terminally ill patients to refuse life support.",
            "Common Cause v. Union of India (2018)",
        ],
    ],
)

pn.br()
pn.chap_box(
    "Q5(d) [10 Marks] -- Decentralization Benefits & LSG Challenges\n"
    "(May-June 2024 | Nov-Dec 2024 | June-July 2025)"
)

pn.section("Benefits of Decentralization of Power")
pn.body(
    "Decentralization refers to the transfer of authority and responsibility from the central government "
    "to local government units. Key benefits include:"
)
pn.bullet(
    [
        "<b>Grassroots Democracy:</b> Enhances direct citizen participation in governance, allowing people to solve local problems themselves.",
        "<b>Social Inclusion:</b> Mandatory reservation of seats for SC/ST and at least 1/3 for women has empowered marginalized groups.",
        "<b>Efficient Local Planning:</b> Local bodies are better suited to identify and implement development plans (e.g., sanitation, primary education, markets) than distant bureaucrats.",
        "<b>Accountability:</b> Gram Sabha meetings provide a forum for citizens to hold elected representatives directly accountable.",
    ]
)

# Diagram: LayeredStack for Panchayati Raj
stack_pr = pd.LayeredStack(
    width=pn.CW * 0.75,
    height=185,
    theme=diag_theme,
    caption="Fig 5.1: Three-Tier Structure of Panchayati Raj System",
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

pn.section("Critical Analysis & Major Challenges Confronting LSGs")
pn.body(
    "Despite the constitutional mandate of the 73rd and 74th Amendments, local self-governments "
    "often remain political institutions rather than effective instruments of governance due to several barriers:"
)
pn.bullet(
    [
        "<b>1. Financial Starvation (The 3 Fs Deficit):</b> States are reluctant to devolve revenue-raising powers (Funds, Functions, and Functionaries). Local bodies depend heavily on tied state/central grants.",
        "<b>2. Bureaucratic Dominance:</b> Local government officials (BDOs, Collectors) often exercise veto power over decisions made by elected representatives.",
        "<b>3. Proxy Governance (Sarpanch Pati):</b> In many rural areas, reserved seats for women are controlled by their husbands or male relatives, undermining genuine empowerment.",
        "<b>4. Lack of Infrastructure:</b> Many village panchayats operate without basic office space, computers, or trained administrative staff.",
    ]
)

pn.br()
pn.chap_box(
    "Q5(e) [10 Marks] -- Art. 19 Freedoms, Art. 14 Equality & NGOs\n"
    "(June 2022 | June-July 2025 | Nov-Dec 2024)"
)

pn.section("Article 19: Six Freedoms and Permissible Restrictions")
pn.body(
    "Article 19(1) guarantees six fundamental freedoms to citizens, subject to reasonable restrictions "
    "in the interest of sovereignty, public order, and morality:"
)
pn.info_table(
    ["Freedom (Article 19(1))", "Scope", "Permissible Restrictions (Art 19(2)-(6))"],
    [
        [
            "(a) Speech & Expression",
            "Right to express opinions through speech, writing, printing, or media.",
            "Sovereignty of India, security of State, public order, decency, defamation, contempt of court.",
        ],
        [
            "(b) Peaceful Assembly",
            "Right to assemble peaceably and without arms.",
            "Sovereignty and integrity of India, public order.",
        ],
        [
            "(c) Form Associations",
            "Right to form unions, associations, or cooperative societies.",
            "Sovereignty and integrity of India, public order, morality.",
        ],
        [
            "(d) Free Movement",
            "Right to move freely throughout the territory of India.",
            "Interests of the general public, protection of Scheduled Tribes.",
        ],
        [
            "(e) Residence",
            "Right to reside and settle in any part of the country.",
            "Interests of the general public, protection of Scheduled Tribes.",
        ],
        [
            "(g) Profession & Trade",
            "Right to practice any profession, trade, or business.",
            "Professional/technical qualifications; State monopoly in trade.",
        ],
    ],
)
pn.body(
    "<b>Landmark Case:</b> <i>Shreya Singhal v. Union of India (2015)</i> struck down Section 66A of the IT Act "
    "for violating Article 19(1)(a) as it was vague and disproportionate."
)

pn.section("Article 14: Fundamental Right to Equality (10 Marks)")
pn.definition(
    "<b>Article 14:</b> 'The State shall not deny to any person equality before the law or "
    "the equal protection of the laws within the territory of India.' This right is available to "
    "both citizens and foreigners, and applies to legal corporations as well."
)
pn.info_table(
    ["Concept Component", "Origin & Nature", "Core Meaning & Implications"],
    [
        [
            "1. Equality before Law",
            "British Origin (Rule of Law). Negative concept.",
            "Absence of special privileges for any individual. All persons are subject to the ordinary law of the land, and no person (rich, poor, official) is above the law.",
        ],
        [
            "2. Equal Protection of Laws",
            "American Origin. Positive concept.",
            "Equality of treatment under equal circumstances. Like should be treated alike, not unlike. Permits the State to make special laws for different classes if circumstances differ.",
        ],
    ],
)
pn.bullet(
    [
        "<b>Doctrine of Reasonable Classification:</b> Article 14 forbids class legislation (treating equals unequally) but permits the classification of persons, objects, and transactions for legislative purposes. This is to ensure that unequal people (e.g., children, disabled) can be given protective discrimination (e.g., reservation, tax slabs).",
        "<b>The Twin Test of Classification:</b> To be valid, any legislative classification must satisfy two conditions: (1) <i>Intelligible Differentia</i> -- there must be a clear, understandable difference distinguishing those grouped together from others left out. (2) <i>Rational Nexus</i> -- the differentia must have a direct, logical relation to the object sought to be achieved by the law.",
        "<b>New Doctrine of Equality (Non-Arbitrariness):</b> In <i>E.P. Royappa v. State of Tamil Nadu (1974)</i> and <i>Maneka Gandhi (1978)</i>, the Supreme Court established that equality is a dynamic concept. It is antithetical to arbitrariness. Any state action that is arbitrary, unfair, or discriminatory is a direct violation of Article 14."
    ]
)

pn.section("Role of NGOs in Environmental Protection & Constraints")
pn.body(
    "Non-Governmental Organizations (NGOs) have played a stellar role in environmental preservation in India "
    "(e.g., Chipko movement, Narmada Bachao Andolan, filing Public Interest Litigations (PILs))."
)
pn.info_table(
    ["Role of NGOs in Environmental Protection", "Major Constraints & Barriers Faced"],
    [
        [
            "Spreading public awareness and educating communities on conservation.",
            "<b>Regulatory Hurdles:</b> Stringent Foreign Contribution Regulation Act (FCRA) rules that restrict foreign funds.",
        ],
        [
            "Advocating policy changes and engaging in legal battles (PILs) against polluters.",
            "<b>Funding Deficits:</b> Heavy reliance on temporary public donations and grants.",
        ],
        [
            "Carrying out grassroots conservation projects (water harvesting, afforestation).",
            "<b>Political & Corporate Backlash:</b> Conflict with powerful economic and political lobbies.",
        ],
    ],
)

# =============================================================================
#  BUILD DOCUMENT
# =============================================================================
pn.build_doc("IC_PYQ_Answers.pdf")

print("Generated: IC_PYQ_Answers.pdf")
