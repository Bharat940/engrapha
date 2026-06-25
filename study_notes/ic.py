"""
Indian Constitution (IT410) — Complete Exam Notes + PYQ Answers
UIT-RGPV (Autonomous) Bhopal | Semester IV
Covers all 15 syllabus topics, CO1–CO5, PYQs from 2022–2025
Run:    python indian_constitution_it410.py
Output: IndianConstitution_IT410_Notes.pdf
"""

from __future__ import annotations

import paperforge_notes as pn
import paperforge_diagrams as pd

# =============================================================================
#  THEME & GLOBAL FOOTER
# =============================================================================
pn.set_story([])
pn.set_theme(pn.OCEAN_DARK)

pn.set_global_footer(
    left="Indian Constitution (IT410) — UIT-RGPV Bhopal",
    right="Semester IV",
    show_page_num=True,
)

diag_theme = pd.DiagramTheme.from_notes_theme(pn.get_theme())

# =============================================================================
#  COVER PAGE
# =============================================================================
pn.bookmark("Cover Page")
pn.suppress_footer(page_only=True)
pn.sp(22)

pn.cover_card(
    "INDIAN CONSTITUTION",
    "Complete Exam Notes & PYQ Answers",
)
# pn.cover_subtitle(
#     [
#         "Subject Code: IT410  |  UIT-RGPV (Autonomous) Bhopal  |  Semester IV",
#         "PYQs Covered: June 2022  |  May-June 2023  |  May-June 2024  |  Nov-Dec 2024  |  June-July 2025",
#         "All 15 Syllabus Topics  |  CO1–CO5  |  3-mark, 4-mark & 10-mark Model Answers",
#     ]
# )
pn.sp(8)
pn.rule(pn.get_theme().rl(pn.get_theme().accent), 1.5)
pn.sp(6)

pn.info_table(
    ["Unit / CO", "Topics Covered"],
    [
        [
            "CO1 — Constitution & History",
            "Meaning of Constitution Law, Constitutionalism, Historical Perspective, "
            "Company Rule (1773–1947), Salient Features & Characteristics of Indian Constitution",
        ],
        [
            "CO2 — Fundamental Duties & DPSP",
            "Scheme of Fundamental Duties, Legal Status, Verma & Swaran Singh Committees, "
            "Directive Principles of State Policy — Importance & Implementation",
        ],
        [
            "CO3 — Federal Structure & President",
            "Federal Structure, Distribution of Legislative & Financial Powers (Union–State), "
            "Parliamentary Form of Government, Powers & Status of the President of India",
        ],
        [
            "CO4 — Amendments & Emergency",
            "Constitutional Amendment Powers & Procedure, Historical Perspective of Amendments, "
            "National Emergency (Art. 352), President's Rule (Art. 356), Financial Emergency (Art. 360), "
            "Local Self Government — 73rd & 74th Amendments, Panchayati Raj",
        ],
        [
            "CO5 — Fundamental Rights",
            "Scheme of Fundamental Right to Equality (Art. 14–18), "
            "Right to Certain Freedoms under Article 19, "
            "Scope of Right to Life & Personal Liberty under Article 21",
        ],
    ],
    col_widths=["28%", "72%"],
)

pn.sp(6)
pn.note(
    "Mark scheme: Part (a) = 3 marks | Part (b) = 4 marks | Part (c) = 4 marks | "
    "Part (d) = 10 marks | Part (e) = 10 marks (internal choice). "
    "All PYQ questions are answered with model answers calibrated to the mark weightage."
)

# =============================================================================
#  TABLE OF CONTENTS
# =============================================================================
pn.br()
pn.suppress_footer(page_only=True)
pn.toc()

# #############################################################################
#  PART A — CO1: CONSTITUTION, HISTORY & CHARACTERISTICS
# #############################################################################
pn.part_box("UNIT I — CO1: CONSTITUTION, HISTORY & CHARACTERISTICS")

# =============================================================================
#  1.1  MEANING OF CONSTITUTION, CONSTITUTION LAW & CONSTITUTIONALISM
# =============================================================================
pn.chap_box("1.1  Meaning of Constitution, Constitutional Law & Constitutionalism")

pn.section("What is a Constitution?")
pn.definition(
    "<b>Constitution:</b> A constitution is the fundamental and supreme law of a country. "
    "It is a set of basic principles and established precedents according to which a state is "
    "governed. It defines the framework for the structure of government, distribution of powers "
    "among different organs (Legislature, Executive, Judiciary), and guarantees certain rights "
    "to citizens. Every other law in the country must conform to the constitution."
)
pn.body(
    "A constitution may be <b>written</b> (like India and USA) or <b>unwritten</b> (like the UK, "
    "based on conventions and statutes). India has one of the longest written constitutions in the world."
)

pn.section("Constitutional Law")
pn.definition(
    "<b>Constitutional Law:</b> Constitutional law is the body of law that defines the relationship "
    "between different entities within a state — the executive, legislature, and judiciary. "
    "It also defines the rights of citizens. Constitutional law includes the text of the constitution "
    "itself as well as all judicial interpretations and conventions that have developed around it."
)

pn.section("Constitutionalism")
pn.definition(
    "<b>Constitutionalism:</b> Constitutionalism is the idea that government authority is derived "
    "from and limited by a body of fundamental law (the constitution). It means that government "
    "must operate within the limits set by the constitution — no authority is absolute or unlimited. "
    "It embodies the principles of limited government, rule of law, separation of powers, "
    "protection of fundamental rights, and judicial review."
)

pn.info_table(
    ["Basis", "Constitution", "Constitutionalism"],
    [
        [
            "Meaning",
            "The written or unwritten document/framework of governance",
            "The political principle that government power is limited by law",
        ],
        ["Nature", "A legal document", "A political doctrine / ideology"],
        [
            "Focus",
            "Structure of government and rights",
            "Limitation of government power",
        ],
        [
            "Example",
            "The Constitution of India",
            "Judicial review, fundamental rights enforcement",
        ],
        [
            "Requirement",
            "A state may have a constitution",
            "Constitutionalism requires the constitution to be respected and enforced",
        ],
    ],
)

pn.exam(
    "PYQ Tip: 'Compare Constitution and Constitutionalism' (June 2022, 3 marks) and 'What do you mean by constitutionalism?' "
    "(June-July 2025, 3 marks). Always give the definition of both and a comparison table."
)

# =============================================================================
#  1.2  HISTORICAL PERSPECTIVE OF INDIAN CONSTITUTION
# =============================================================================
pn.chap_box("1.2  Historical Perspective of the Indian Constitution")

pn.section("Company Rule and Pre-Independence Constitutional History")
pn.body(
    "Before the Constitution of India came into force on 26 January 1950, India's governance "
    "was shaped by a series of Charter Acts, Regulating Acts, and Government of India Acts "
    "introduced during British rule."
)

pn.info_table(
    ["Act / Year", "Key Provisions"],
    [
        [
            "Regulating Act, 1773",
            "First attempt by the British Parliament to regulate the affairs of the East India Company. "
            "Created the post of Governor-General of Bengal (Warren Hastings). "
            "Established a Supreme Court at Calcutta (1774). Reduced power of Bombay and Madras Presidencies.",
        ],
        [
            "Pitt's India Act, 1784",
            "Distinguished between commercial and political functions. "
            "Created a Board of Control in London. Company's political affairs came under British government supervision.",
        ],
        [
            "Charter Act, 1813",
            "Ended the East India Company's trade monopoly (except tea and China trade). "
            "Christian missionaries allowed in India. Provision for Indian education.",
        ],
        [
            "Charter Act, 1833",
            "Governor-General of Bengal became Governor-General of India (first being Lord William Bentinck). "
            "East India Company became purely an administrative body. Law Commission established.",
        ],
        [
            "Charter Act, 1853",
            "Last charter act. Introduced open competition for civil services. "
            "Legislative and executive functions of Governor-General's Council separated.",
        ],
        [
            "Government of India Act, 1858",
            "Transferred control from East India Company to the British Crown. "
            "Secretary of State for India (with Council) became the supreme authority. "
            "Governor-General designated as Viceroy of India (Lord Canning was first).",
        ],
        [
            "Indian Councils Act, 1861",
            "Introduced legislative councils. Indians associated with law-making. "
            "Portfolio system introduced. Legislative decentralization started.",
        ],
        [
            "Indian Councils Act, 1892",
            "Increased size of legislative councils. Indirect elections introduced. "
            "Councils could discuss budget and ask questions.",
        ],
        [
            "Indian Councils Act, 1909\n(Morley-Minto Reforms)",
            "Introduced direct elections to legislative councils. "
            "Separate electorates for Muslims (communal representation). "
            "Indians appointed to executive councils of Viceroy and Governors.",
        ],
        [
            "Government of India Act, 1919\n(Montagu-Chelmsford Reforms)",
            "Introduced dyarchy in provinces — central and provincial subjects divided. "
            "Bicameralism at center (Council of State + Legislative Assembly). "
            "Public Service Commission introduced. Franchise extended.",
        ],
        [
            "Government of India Act, 1935",
            "Most detailed act — major source of the Indian Constitution. "
            "Proposed All-India Federation (center + provinces + princely states). "
            "Provincial autonomy introduced. Dyarchy at center, full responsible government in provinces. "
            "Federal Court and Reserve Bank of India established. Three lists of powers.",
        ],
        [
            "Indian Independence Act, 1947",
            "Ended British rule. Created two dominions — India and Pakistan. "
            "Constituent Assembly of each dominion became fully sovereign. "
            "Governor-General appointed by each dominion.",
        ],
    ],
)

pn.section("Constituent Assembly")
pn.definition(
    "<b>Constituent Assembly of India:</b> The body that drafted and adopted the Constitution of India. "
    "It was constituted in December 1946 under the Cabinet Mission Plan (1946). "
    "Dr. Rajendra Prasad was elected as its President. "
    "Dr. B.R. Ambedkar was the Chairman of the Drafting Committee."
)
pn.bullet(
    [
        "<b>Total members:</b> 389 (reduced to 299 after partition; Muslim League members joined Pakistan's assembly).",
        "<b>Drafting Committee Chairman:</b> Dr. B.R. Ambedkar — known as the Father of the Indian Constitution.",
        "<b>First meeting:</b> 9 December 1946. <b>Adopted:</b> 26 November 1949 (Constitution Day). <b>Enforced:</b> 26 January 1950.",
        "<b>Time taken:</b> 2 years, 11 months, 18 days. <b>Sessions:</b> 11 sessions. <b>Sittings:</b> 165 days.",
        "<b>First Cabinet (1947):</b> Jawaharlal Nehru (PM), Sardar Vallabhbhai Patel (Home), B.R. Ambedkar (Law), Maulana Azad (Education).",
    ]
)

pn.exam(
    "PYQ: 'Discuss the composition of Constituent Assembly' (Nov-Dec 2024, 4 marks). "
    "Also: 'Outline Company rule 1773-1785' (June 2022) and 'Name leaders of First Cabinet of free India' (June 2022)."
)

# =============================================================================
#  1.3  SALIENT FEATURES & CHARACTERISTICS
# =============================================================================
pn.chap_box("1.3  Salient Features & Characteristics of the Indian Constitution")

pn.section("Salient Features")
pn.body(
    "The Constitution of India is unique in many respects. Its key characteristics are:"
)
pn.info_table(
    ["Feature", "Explanation"],
    [
        [
            "1. Lengthiest Written Constitution",
            "Originally 395 Articles, 8 Schedules, 22 Parts. Now 448 Articles, 12 Schedules, 25 Parts. "
            "Most elaborate written constitution in the world.",
        ],
        [
            "2. Partly Rigid, Partly Flexible",
            "Some provisions can be amended by a simple majority (e.g., new states). "
            "Others require a special majority (2/3 of Parliament + 50% state ratification, e.g., fundamental rights).",
        ],
        [
            "3. Federal System with Unitary Bias",
            "India is a 'Union of States' (not a federation). "
            "Strong centre: residuary powers with Parliament, single citizenship, single judiciary, "
            "central control over states in emergencies — making it quasi-federal.",
        ],
        [
            "4. Parliamentary Form of Government",
            "President is the constitutional head; real executive power lies with the Prime Minister and Council of Ministers. "
            "The executive is collectively responsible to the Lok Sabha.",
        ],
        [
            "5. Unique Blend of Rigidity and Flexibility",
            "Constitution can be amended by Parliament following a defined procedure (Art. 368). "
            "Neither fully rigid (like USA) nor fully flexible (like UK).",
        ],
        [
            "6. Fundamental Rights (Part III)",
            "Six categories of fundamental rights guaranteed to all citizens (and some to all persons). "
            "Enforceable by courts. Part III, Articles 12–35.",
        ],
        [
            "7. Directive Principles of State Policy (Part IV)",
            "Non-justiciable guidelines for the State to follow for social and economic justice. "
            "Important for welfare state objectives. Articles 36–51.",
        ],
        [
            "8. Fundamental Duties (Part IV-A, Art. 51A)",
            "Added by 42nd Amendment (1976) following Swaran Singh Committee recommendations. "
            "Currently 11 duties. Non-justiciable but morally binding.",
        ],
        [
            "9. Secular State",
            "No official state religion. Equal treatment and protection to all religions. "
            "'Secular' added to Preamble by 42nd Amendment (1976).",
        ],
        [
            "10. Universal Adult Franchise",
            "Every citizen aged 18 and above has the right to vote, irrespective of caste, religion, sex, or literacy. "
            "Originally 21 years; lowered to 18 by 61st Amendment (1988).",
        ],
        [
            "11. Independent Judiciary",
            "Supreme Court at the apex, followed by High Courts and subordinate courts. "
            "Judges appointed by President on advice of collegium. Judicial review power.",
        ],
        [
            "12. Single Citizenship",
            "Unlike USA (dual citizenship), India provides only single citizenship — "
            "Indian citizenship regardless of state of residence.",
        ],
        [
            "13. Emergency Provisions",
            "Three types of emergency: National (Art. 352), State/President's Rule (Art. 356), "
            "Financial (Art. 360). These alter the balance of power in favour of the Centre.",
        ],
        [
            "14. Integrated and Independent Judiciary",
            "Single integrated court system for both central and state laws. "
            "Supreme Court is the guardian of the Constitution.",
        ],
    ],
)
pn.br()

# #############################################################################
#  PART B — CO2: FUNDAMENTAL DUTIES & DIRECTIVE PRINCIPLES
# #############################################################################
pn.part_box("UNIT II — CO2: FUNDAMENTAL DUTIES & DIRECTIVE PRINCIPLES OF STATE POLICY")

# =============================================================================
#  2.1  FUNDAMENTAL DUTIES
# =============================================================================
pn.chap_box("2.1  Scheme of Fundamental Duties & Legal Status")

pn.section("Introduction")
pn.definition(
    "<b>Fundamental Duties (Part IV-A, Article 51A):</b> Originally the Indian Constitution had no "
    "chapter on fundamental duties. They were added by the <b>42nd Constitutional Amendment Act, 1976</b> "
    "on the recommendation of the <b>Swaran Singh Committee</b>. A 11th duty was added by the "
    "<b>86th Amendment, 2002</b>. They are modelled on the constitutions of USSR, Japan, and China."
)

pn.section("All 11 Fundamental Duties (Article 51A)")
pn.info_table(
    ["No.", "Fundamental Duty"],
    [
        [
            "(a)",
            "Abide by the Constitution and respect its ideals and institutions, the National Flag and the National Anthem.",
        ],
        [
            "(b)",
            "Cherish and follow the noble ideals which inspired the national struggle for freedom.",
        ],
        ["(c)", "Uphold and protect the sovereignty, unity and integrity of India."],
        [
            "(d)",
            "Defend the country and render national service when called upon to do so.",
        ],
        [
            "(e)",
            "Promote harmony and the spirit of common brotherhood amongst all the people of India, transcending religious, linguistic and regional diversities; renounce practices derogatory to the dignity of women.",
        ],
        ["(f)", "Value and preserve the rich heritage of our composite culture."],
        [
            "(g)",
            "Protect and improve the natural environment including forests, lakes, rivers, and wildlife; have compassion for living creatures.",
        ],
        [
            "(h)",
            "Develop the scientific temper, humanism, and the spirit of inquiry and reform.",
        ],
        ["(i)", "Safeguard public property and abjure violence."],
        [
            "(j)",
            "Strive towards excellence in all spheres of individual and collective activity so that the nation rises to higher levels of endeavour and achievement.",
        ],
        [
            "(k)",
            "Provide opportunities for education to his child or ward between the age of 6 and 14 years. (Added by 86th Amendment, 2002)",
        ],
    ],
)

pn.section("Legal Status of Fundamental Duties")
pn.body(
    "Fundamental duties are <b>non-justiciable</b> — they cannot be enforced by courts through writs. "
    "However, they are not without legal significance:"
)
pn.bullet(
    [
        "They serve as a warning to citizens against anti-national activities.",
        "Courts can use them to uphold the constitutional validity of laws made to enforce them.",
        "They help in determining whether a law is reasonable (Art. 19 restrictions).",
        "They remind citizens that enjoyment of rights comes with corresponding duties.",
        "The Supreme Court has held that Fundamental Duties are equally important as Fundamental Rights.",
    ]
)

pn.section("Swaran Singh Committee Recommendations (1976)")
pn.definition(
    "<b>Swaran Singh Committee:</b> Appointed in 1976 to recommend a chapter on Fundamental Duties. "
    "The committee recommended: (1) Eight fundamental duties be included. "
    "(2) Parliament should have power to legislate to enforce them. "
    "(3) Some duties should be applicable to certain categories of citizens (e.g., military). "
    "<b>Result:</b> 10 duties were added (not all recommendations were accepted exactly). "
    "The committee also recommended penalties for violation, but this was not accepted by government."
)

pn.section("Verma Committee Report (1999)")
pn.definition(
    "<b>Justice J.S. Verma Committee (1999):</b> Constituted to operationalize the Fundamental Duties "
    "and identify laws in force for their implementation. Key findings: "
    "(1) Several existing laws already correspond to fundamental duties (e.g., Prevention of Insults to National Honour Act, "
    "Wildlife Protection Act, Environment Protection Act). "
    "(2) Recommended that teachers and students be educated about Fundamental Duties. "
    "(3) Suggested that provisions in existing laws should be amended to make references to Art. 51A."
)

pn.exam(
    "PYQ (June 2022): 'Explain Verma Committee Observation' (4 marks) and 'Define Swaran Singh Committee Recommendation' (4 marks). "
    "PYQ (Nov-Dec 2024): 'Fundamental duties are not enforceable by writ... but fundamental to well-being' (10 marks)."
)

# =============================================================================
#  2.2  DIRECTIVE PRINCIPLES OF STATE POLICY
# =============================================================================
pn.chap_box(
    "2.2  Directive Principles of State Policy (DPSP) — Part IV, Articles 36–51"
)

pn.section("Introduction & Constitutional Position")
pn.definition(
    "<b>Directive Principles of State Policy (DPSP):</b> Part IV of the Constitution (Articles 36–51) "
    "contains the Directive Principles. They are guidelines or directives given to the central and "
    "state governments to be kept in mind while framing laws and policies. They represent the "
    "positive obligations of the State (what the State should do), as opposed to Fundamental Rights "
    "(which represent negative obligations — what the State should NOT do)."
)
pn.body(
    "The DPSP are <b>non-justiciable</b> — they cannot be enforced by courts. "
    "However, Article 37 states that 'it shall be the duty of the State to apply these principles "
    "in making laws.' They borrowed from the Irish Constitution (which took it from the Spanish Constitution)."
)

pn.section("Classification of Directive Principles")
pn.info_table(
    ["Category", "Key Articles", "Content"],
    [
        [
            "Socialistic Principles\n(Social Justice)",
            "Art. 38, 39, 39A, 41, 42, 43, 43A, 47",
            "Adequate means of livelihood, equal pay for equal work, prevent concentration of wealth, "
            "free legal aid, right to work, maternity relief, living wage, workers' participation in management.",
        ],
        [
            "Gandhian Principles\n(Gram Swaraj)",
            "Art. 40, 43, 43B, 46, 47, 48",
            "Organisation of village panchayats, cottage industries, promotion of SC/ST interests, "
            "prohibition of intoxicants, protection of cows.",
        ],
        [
            "Liberal-Intellectual Principles\n(Liberal Policies)",
            "Art. 44, 45, 48A, 49, 50, 51",
            "Uniform Civil Code, early childhood care, protection of environment, "
            "monuments of historical importance, separation of judiciary from executive, "
            "promotion of international peace.",
        ],
    ],
)

pn.section("Importance and Implementation of DPSPs")
pn.bullet(
    [
        "<b>Welfare State:</b> DPSPs transform India into a welfare state by directing the government to ensure social and economic justice for all citizens.",
        "<b>Political Manifesto:</b> They serve as a yardstick to measure the performance of political parties in power.",
        "<b>Guide to Legislation:</b> Parliament has used DPSPs to justify laws even when they restrict fundamental rights (e.g., land reform laws).",
        "<b>Implemented Laws:</b> Equal Pay Act, Maternity Benefit Act, Minimum Wages Act, Land Acquisition Acts, Legal Aid Services, Panchayati Raj (73rd Amendment), Right to Education (86th Amendment, Art. 21A) — all implement DPSPs.",
        "<b>Judicial Interpretation:</b> In Minerva Mills (1980), the Supreme Court held that Fundamental Rights and DPSPs together form the 'conscience of the Constitution.' Neither is superior in absolute terms.",
    ]
)

pn.section("Fundamental Rights vs Directive Principles — Comparison")
pn.info_table(
    ["Basis", "Fundamental Rights", "Directive Principles"],
    [
        ["Part", "Part III (Articles 12–35)", "Part IV (Articles 36–51)"],
        [
            "Nature",
            "Justiciable (enforceable by courts)",
            "Non-justiciable (not enforceable)",
        ],
        [
            "Obligation",
            "Negative — prohibit State from acting",
            "Positive — direct State to act",
        ],
        ["Source", "Constitution of USA, Ireland", "Irish Constitution (from Spain)"],
        ["Character", "Legal rights", "Moral obligations on State"],
        [
            "Conflict with FR",
            "Both should be harmonised; courts promote harmonious construction",
            "Parliament can amend FR to implement DPSP (42nd Amendment)",
        ],
        ["Purpose", "Individual liberty", "Collective welfare of society"],
    ],
)

pn.exam(
    "PYQ (May-June 2023, 2024): 'Discuss importance and implementation of DPSP' (10 marks). "
    "'DPSP constitute a comprehensive political, social and economic program for a modern democratic welfare state' (10 marks). "
    "Also: 'Explain interrelationship between FRs and DPSP' (Nov-Dec 2024). "
    "'Compare FRs and DPSP' (June 2022, 10 marks)."
)
pn.br()

# #############################################################################
#  PART C — CO3: FEDERAL STRUCTURE, PARLIAMENT & PRESIDENT
# #############################################################################
pn.part_box("UNIT III — CO3: FEDERAL STRUCTURE & PARLIAMENTARY GOVERNMENT")

# =============================================================================
#  3.1  FEDERAL STRUCTURE
# =============================================================================
pn.chap_box("3.1  Federal Structure & Distribution of Legislative and Financial Powers")

pn.section("Federal vs Unitary Constitutions")
pn.info_table(
    ["Basis", "Federal Constitution", "Unitary Constitution"],
    [
        [
            "Division of Powers",
            "Powers divided between Centre and States",
            "All powers vested in the Centre",
        ],
        ["Supremacy", "Constitution is supreme", "Parliament is supreme"],
        ["Citizenship", "Dual (federal + state)", "Single"],
        ["Rigid/Flexible", "Mostly rigid", "Mostly flexible"],
        ["Examples", "USA, Australia, Canada", "UK, France, Japan"],
        ["India", "Quasi-federal — union with strong centre", "—"],
    ],
)

pn.section("Federal Features of the Indian Constitution")
pn.bullet(
    [
        "<b>Written Constitution:</b> Codified and supreme law of the land.",
        "<b>Dual Polity:</b> Two sets of government — Central (Union) and State.",
        "<b>Division of Powers:</b> Seventh Schedule — Union List, State List, Concurrent List.",
        "<b>Supremacy of Constitution:</b> All organs (Legislature, Executive, Judiciary) are subordinate to the Constitution.",
        "<b>Rigid Constitution:</b> Requires special procedure for amendment of federal provisions.",
        "<b>Independent Judiciary:</b> Supreme Court resolves disputes between Centre and States.",
        "<b>Bicameralism:</b> Parliament has two houses — Lok Sabha (lower) and Rajya Sabha (upper/representing states).",
    ]
)

pn.section("Unitary / Non-Federal Features of the Indian Constitution")
pn.bullet(
    [
        "<b>'Union of States' not Federation:</b> Art. 1 — India is a Union; states cannot secede.",
        "<b>Strong Centre:</b> Residuary powers with Parliament (unlike USA where residual powers are with states).",
        "<b>Single Citizenship:</b> Unlike USA, India has single citizenship only.",
        "<b>Integrated Judiciary:</b> Single court system for both central and state laws.",
        "<b>Governor appointed by President:</b> States lack full autonomy; Governor is a central agent.",
        "<b>Emergency Provisions:</b> Federal balance can be altered in favour of Centre during emergencies.",
        "<b>All-India Services:</b> IAS, IPS officers (appointed by Centre) serve both Centre and States.",
        "<b>Rajya Sabha Inequality:</b> States are not represented equally in Rajya Sabha (based on population).",
    ]
)

pn.section("Distribution of Legislative Powers — Seventh Schedule")
pn.definition(
    "<b>Seventh Schedule:</b> Contains three lists of subjects on which laws can be made:"
)
pn.info_table(
    ["List", "Subjects (Count)", "Who Legislates", "Examples"],
    [
        [
            "Union List (List I)",
            "~100 subjects",
            "Parliament only",
            "Defence, Foreign Affairs, Atomic Energy, Railways, Banking, Currency, Post & Telegraph, Census",
        ],
        [
            "State List (List II)",
            "~61 subjects",
            "State Legislature only",
            "Police, Public Order, Agriculture, Land, Local Government, Public Health, Trade within State",
        ],
        [
            "Concurrent List (List III)",
            "~52 subjects",
            "Both Parliament and State Legislatures",
            "Education, Forests, Trade Unions, Marriage, Succession, Criminal Law, Bankruptcy",
        ],
        [
            "Residuary Powers",
            "All other subjects",
            "Parliament",
            "Cyber crimes, space, genetic engineering — not mentioned in any list",
        ],
    ],
)
pn.note(
    "In case of conflict between Parliamentary and State law on a Concurrent List subject, "
    "Parliamentary law prevails (Art. 254). But if state law received Presidential assent, it prevails in that state."
)

pn.section("Distribution of Financial Powers")
pn.info_table(
    ["Revenue Source", "Levy By", "Collected By", "Appropriated By"],
    [
        [
            "Income Tax (excl. agri. income)",
            "Centre",
            "Centre",
            "Centre + States (shared)",
        ],
        ["Customs Duty", "Centre", "Centre", "Centre only"],
        [
            "GST (Goods & Services Tax)",
            "Centre + States jointly (101st Amend.)",
            "Centre + State",
            "Centre + States",
        ],
        ["Stamp Duty on Bills of Exchange", "Centre", "State", "State"],
        ["Agricultural Income Tax", "State", "State", "State"],
        ["Land Revenue", "State", "State", "State"],
        ["State GST (SGST)", "State", "State", "State"],
        [
            "Finance Commission",
            "Art. 280 — body that recommends distribution of taxes between Centre and States",
            "",
            "",
        ],
    ],
)

pn.exam(
    "PYQ: 'Discuss distribution of legislative and financial powers between Union and States' (May-June 2023, 5 marks). "
    "'Distribution of powers is tilted towards the Centre — Clarify' (May-June 2024, 10 marks). "
    "'Examine administrative and financial relations between Union and State' (June-July 2025, 10 marks)."
)

# =============================================================================
#  3.2  PARLIAMENTARY FORM OF GOVERNMENT
# =============================================================================
pn.chap_box("3.2  Parliamentary Form of Government in India")

pn.section("Features of Parliamentary Government")
pn.definition(
    "<b>Parliamentary Government (Westminster Model):</b> A system where the executive is "
    "responsible to the legislature for its policies and actions. India follows the British "
    "Westminster model — the President is the nominal head, and real power lies with the "
    "Prime Minister and the Council of Ministers."
)
pn.info_table(
    ["Feature", "Explanation"],
    [
        [
            "Nominal & Real Executive",
            "President is the nominal/constitutional head. Prime Minister and Cabinet are the real executive.",
        ],
        [
            "Majority Party Rule",
            "The party with majority in Lok Sabha forms the government. PM must command majority.",
        ],
        [
            "Collective Responsibility",
            "Council of Ministers collectively responsible to the Lok Sabha (Art. 75(3)). "
            "If a no-confidence motion passes, the entire Cabinet must resign.",
        ],
        [
            "Individual Responsibility",
            "Each Minister is individually responsible to the President for the Ministry.",
        ],
        [
            "Political Homogeneity",
            "In normal times, all ministers belong to the same party or coalition; they follow a common program.",
        ],
        [
            "Double Membership",
            "Ministers must be members of Parliament (either House) or become members within 6 months.",
        ],
        [
            "Leadership of PM",
            "Prime Minister is the head of Cabinet, leader of the majority party, and chief link between President and Cabinet.",
        ],
        [
            "Dissolution of Lok Sabha",
            "The President can dissolve the Lok Sabha on the advice of the Prime Minister.",
        ],
    ],
)

pn.section("Parliamentary vs Presidential Government")
pn.info_table(
    ["Basis", "Parliamentary (India)", "Presidential (USA)"],
    [
        [
            "Executive-Legislature Relation",
            "Executive is part of and responsible to Legislature",
            "Executive is separate from and independent of Legislature",
        ],
        [
            "Head of Government",
            "PM is head of government; President is head of state",
            "President is both head of state and government",
        ],
        [
            "Tenure of Executive",
            "No fixed tenure; depends on Lok Sabha majority",
            "Fixed 4-year term regardless of Congress majority",
        ],
        [
            "Accountability",
            "Collective and individual responsibility to legislature",
            "Not directly accountable to Congress",
        ],
        [
            "Separation of Powers",
            "Fusion of executive and legislative powers",
            "Strict separation of powers",
        ],
        [
            "Party System",
            "Multi-party coalition common",
            "Essentially two-party system",
        ],
        [
            "Dissolution",
            "PM can advise dissolution of lower house",
            "No dissolution of Congress",
        ],
    ],
)

# =============================================================================
#  3.3  POWERS & STATUS OF THE PRESIDENT
# =============================================================================
pn.chap_box("3.3  Constitutional Powers & Status of the President of India")

pn.section("Election and Removal of the President")
pn.definition(
    "<b>Election:</b> The President is elected by an Electoral College consisting of: "
    "(a) elected members of both Houses of Parliament, and (b) elected members of the Legislative Assemblies of States and Union Territories with legislatures. "
    "The election is by a system of single transferable vote (proportional representation). "
    "Term: 5 years. Re-election permitted."
)
pn.definition(
    "<b>Removal:</b> The President can be removed from office by the process of <b>impeachment</b> "
    "(Article 61) for violation of the Constitution. A charge signed by not less than 1/4 of the total membership "
    "of the House must be preferred. The resolution must be passed by a majority of not less than 2/3 of the "
    "total membership of each House. As of 2025, no President of India has been impeached."
)

pn.section("Powers of the President of India")
pn.info_table(
    ["Category of Powers", "Key Powers"],
    [
        [
            "Executive Powers",
            "Supreme executive power of the Union vested in the President (Art. 53). "
            "All executive actions of the GoI taken in President's name. "
            "Appoints PM, Council of Ministers, Governors, AG, CAG, CJI, SC Judges, "
            "UPSC members, Election Commissioners, Finance Commission, etc.",
        ],
        [
            "Legislative Powers",
            "Summons, prorogues, and dissolves Parliament. "
            "Addresses both Houses at the commencement of the first session after each general election. "
            "Nominates 12 members to Rajya Sabha (art, literature, science, social service). "
            "Nominates 2 Anglo-Indian members to Lok Sabha (deleted by 104th Amendment, 2020). "
            "Prior recommendation for Money Bills. "
            "Power to promulgate Ordinances when Parliament is not in session (Art. 123).",
        ],
        [
            "Judicial Powers",
            "Can grant pardon, reprieve, respite, and remit punishment (Art. 72). "
            "Consults with the Supreme Court on legal matters (Art. 143 — Advisory Jurisdiction). "
            "Appoints the Chief Justice and Judges of the Supreme Court and High Courts.",
        ],
        [
            "Emergency Powers",
            "Proclaims National Emergency (Art. 352) on advice of Cabinet. "
            "Proclaims President's Rule (Art. 356) on failure of constitutional machinery in states. "
            "Proclaims Financial Emergency (Art. 360).",
        ],
        [
            "Financial Powers",
            "Annual Financial Statement (Union Budget) placed before Parliament on President's behalf. "
            "No Money Bill can be introduced without President's prior recommendation. "
            "Contingency Fund of India placed at President's disposal.",
        ],
        [
            "Diplomatic & Military",
            "Diplomatic — all treaties and international agreements negotiated in President's name. "
            "Supreme Commander of Indian Defence Forces. Declares war or peace.",
        ],
        [
            "Veto Powers",
            "Art. 111: Three types of veto over Bills passed by Parliament: "
            "(1) Absolute Veto — withhold assent permanently. "
            "(2) Suspensive Veto — return bill for reconsideration (except Money Bills). "
            "(3) Pocket Veto — keep the bill without taking any action (no time limit).",
        ],
    ],
)

pn.section("Constitutional Position of the President")
pn.body(
    "The President of India is the constitutional/nominal/titular executive head. "
    "Under the 42nd and 44th Amendments and the Supreme Court decision in <b>Shamsher Singh vs State of Punjab (1974)</b>, "
    "the President acts on the advice of the Council of Ministers headed by the PM. "
    "The President cannot act independently in most matters. "
    "However, the President retains <b>situational discretion</b> in certain matters, such as "
    "appointing a PM when no party has a clear majority."
)

pn.exam(
    "PYQ: 'Discuss Judicial powers of the President' (May-June 2024, 4 marks). "
    "'Explain procedure of election and removal of President' (May-June 2023, 4 marks). "
    "'Functions and powers of President' (June-July 2025, 4 marks). "
    "'Constitutional position and powers of Governor' (June-July 2025, appears twice — check carefully!)."
)

pn.section("Powers and Functions of the Governor")
pn.definition(
    "<b>Governor:</b> The constitutional head of a State, appointed by the President for a 5-year term. "
    "Like the President at the centre, the Governor is a nominal head at the state level. "
    "Real executive power lies with the Chief Minister and the State Council of Ministers."
)
pn.bullet(
    [
        "<b>Executive Powers:</b> All executive actions of the State Government taken in Governor's name. Appoints CM, Council of Ministers, Advocate General, State PSC members.",
        "<b>Legislative Powers:</b> Summons, prorogues, and dissolves State Legislature. Addresses the assembly. Nominates 1/6 of members to Legislative Council. Assents to Bills or returns them for reconsideration.",
        "<b>Financial Powers:</b> Annual Financial Statement placed before Legislature on Governor's behalf. No Money Bill without prior recommendation.",
        "<b>Judicial Powers:</b> Can pardon sentences (Art. 161). Consulted on appointment of High Court Judges.",
        "<b>Discretionary Powers:</b> Governor has genuine discretion in: (a) Appointing CM when no clear majority, (b) Dismissing ministry if it loses majority confidence, (c) Dissolving assembly on CM advice, (d) Seeking information from CM.",
        "<b>Veto Power:</b> Can withhold assent and refer bill to President's consideration (Art. 200).",
    ]
)
pn.br()

# #############################################################################
#  PART D — CO4: AMENDMENTS, EMERGENCY & LOCAL SELF GOVERNMENT
# #############################################################################
pn.part_box("UNIT IV — CO4: AMENDMENTS, EMERGENCY & LOCAL SELF GOVERNMENT")

# =============================================================================
#  4.1  AMENDMENT PROCEDURE
# =============================================================================
pn.chap_box("4.1  Amendment of Constitutional Powers and Procedure (Article 368)")

pn.section("Article 368 — Power of Parliament to Amend")
pn.definition(
    "<b>Article 368:</b> Provides for amendment of the Constitution. Parliament can amend the "
    "Constitution by way of addition, variation, or repeal of any provision of the Constitution. "
    "The constitution is the supreme law and its amendment procedure is different from ordinary legislation."
)

pn.section("Three Methods of Amendment")
pn.info_table(
    ["Method", "Procedure", "Examples of Provisions"],
    [
        [
            "1. Simple Majority\n(Ordinary Parliamentary Majority)",
            "Passed by a simple majority in both Houses, like any ordinary law. "
            "Not under Article 368.",
            "Admission/formation of new states (Art. 2, 3), Second Schedule, "
            "quorum in Parliament, Salaries of MPs, rules of procedure.",
        ],
        [
            "2. Special Majority\n(Article 368)",
            "Bill must be passed in each House by a majority of the TOTAL membership of that House AND "
            "a majority of NOT LESS THAN 2/3 of members PRESENT AND VOTING. "
            "No joint sitting possible for constitutional amendment.",
            "Fundamental Rights, DPSPs, DPSP vs FR conflict, Citizenship, Supreme Court powers, "
            "High Courts, Union-State relations.",
        ],
        [
            "3. Special Majority + State Ratification",
            "Same as above PLUS ratification by legislatures of NOT LESS THAN HALF of the States "
            "by simple majority before the bill is presented to the President.",
            "Federal provisions: Election of President, Executive powers of Union and States, "
            "Distribution of legislative powers (7th Schedule), Representation of States in Parliament, "
            "Article 368 itself.",
        ],
    ],
)

pn.section("Basic Structure Doctrine")
pn.definition(
    "<b>Basic Structure Doctrine (Kesavananda Bharati Case, 1973):</b> The Supreme Court held "
    "that while Parliament has wide powers to amend the Constitution (including Fundamental Rights), "
    "it cannot alter the <b>'basic structure'</b> or <b>'basic features'</b> of the Constitution. "
    "The amendment power under Article 368 is not unlimited. "
    "The basic structure includes: Supremacy of Constitution, Republican and democratic form of government, "
    "Secular character, Separation of powers, Federal character, Judicial review, "
    "Sovereignty, unity and integrity, Parliamentary democracy."
)

pn.section("Historical Perspective of Constitutional Amendments")
pn.info_table(
    ["Amendment", "Year", "Key Changes"],
    [
        [
            "1st Amendment",
            "1951",
            "Added 9th Schedule (land reform laws cannot be challenged), added Art. 31A & 31B, inserted 'Reasonable restrictions' in Art. 19.",
        ],
        [
            "7th Amendment",
            "1956",
            "Reorganisation of states on linguistic basis; abolition of Part A, B, C, D states classification.",
        ],
        [
            "24th Amendment",
            "1971",
            "Affirmed Parliament's power to amend any part of the Constitution including Fundamental Rights.",
        ],
        [
            "25th Amendment",
            "1971",
            "Restricted right to property; Art. 31C added — laws implementing DPSP Art. 39(b)(c) cannot be challenged on FR grounds.",
        ],
        [
            "42nd Amendment",
            "1976",
            "Most comprehensive: Added Fundamental Duties (51A), Preamble words 'socialist, secular, integrity'; DPSPs given priority over some FRs; tenure of Lok Sabha extended to 6 years (later reversed).",
        ],
        [
            "44th Amendment",
            "1978",
            "Reversed several 42nd Amendment changes; Right to Property made legal right (Art. 300A); restored 5-year Lok Sabha term; restored Art. 20 and 21 during emergency.",
        ],
        ["52nd Amendment", "1985", "Added Tenth Schedule (Anti-defection law)."],
        ["61st Amendment", "1988", "Lowered voting age from 21 to 18 years."],
        [
            "73rd Amendment",
            "1992",
            "Added Part IX — Panchayati Raj (Art. 243 series); 11th Schedule.",
        ],
        [
            "74th Amendment",
            "1992",
            "Added Part IX-A — Municipalities (Art. 243P series); 12th Schedule.",
        ],
        [
            "86th Amendment",
            "2002",
            "Right to Education (Art. 21A), 11th Fundamental Duty.",
        ],
        ["101st Amendment", "2016", "GST — Goods and Services Tax."],
        [
            "103rd Amendment",
            "2019",
            "10% reservation for Economically Weaker Sections (EWS).",
        ],
    ],
)

pn.exam(
    "PYQ: 'Explain amendment procedure' (multiple years, 10 marks). "
    "'Powers of Parliament to amend the Constitution is wide but not unlimited' (May-June 2023, 10 marks). "
    "'Classify Historical perspective of constitutional amendments' (May-June 2023). "
    "Always mention the Basic Structure Doctrine from Kesavananda Bharati case."
)

# =============================================================================
#  4.2  EMERGENCY PROVISIONS
# =============================================================================
pn.chap_box("4.2  Emergency Provisions — National, President's Rule & Financial")

pn.section("Overview of Three Emergency Provisions")
pn.body(
    "Part XVIII of the Constitution (Articles 352–360) contains emergency provisions. "
    "The three types are:"
)

pn.section("1. National Emergency — Article 352")
pn.definition(
    "<b>National Emergency (Art. 352):</b> Proclaimed by the President when the security of India "
    "or any part of it is threatened by war, external aggression, or <b>armed rebellion</b> "
    "(the term 'internal disturbance' was replaced by 'armed rebellion' by the 44th Amendment, 1978). "
    "Cabinet's written recommendation is mandatory (44th Amendment added this safeguard)."
)
pn.info_table(
    ["Aspect", "Provision"],
    [
        [
            "Proclamation",
            "President's written communication to Cabinet before proclamation; based on Cabinet's written advice.",
        ],
        [
            "Approval",
            "Must be approved by both Houses of Parliament by special majority (2/3 present + voting AND majority of total) within 1 month.",
        ],
        [
            "Duration",
            "Continues for 6 months; can be extended by 6 months at a time by Parliamentary resolution.",
        ],
        [
            "Revocation",
            "Lok Sabha can pass a resolution by simple majority to revoke it.",
        ],
        [
            "Effect on Centre-State",
            "Parliament can legislate on State List subjects; executive directions to states; state revenue can be used for defence; Fundamental Rights under Art. 19 suspended automatically.",
        ],
        [
            "Effect on FR",
            "Art. 19 (six freedoms) suspended during war/external aggression emergencies. Art. 20 and 21 CANNOT be suspended at any time.",
        ],
        [
            "Instances",
            "1962 (India-China war), 1971 (India-Pakistan war), 1975 (Internal emergency — declared on ground of internal disturbance, controversial).",
        ],
    ],
)

pn.section("2. President's Rule / Governor's Rule — Article 356")
pn.definition(
    "<b>President's Rule / State Emergency (Art. 356):</b> Proclaimed when the President (on Governor's report "
    "or otherwise) is satisfied that the government of a state cannot be carried on in accordance "
    "with the provisions of the Constitution. Also called 'Constitutional Emergency' or 'State Emergency'."
)
pn.info_table(
    ["Aspect", "Provision"],
    [
        [
            "Basis",
            "Failure of constitutional machinery in the state — Art. 356. Parliament can also make state laws under Art. 357.",
        ],
        [
            "Approval",
            "Must be approved by both Houses within 2 months. Can continue for 6 months; extendable to maximum 3 years (with fresh approvals every 6 months).",
        ],
        [
            "Effect",
            "President assumes all functions of State government. State Legislature is dissolved or suspended. Parliament legislates for the state.",
        ],
        [
            "Landmark Case",
            "S.R. Bommai v. Union of India (1994) — SC held that imposition of President's Rule is subject to judicial review. Floor test must be held.",
        ],
        ["Instances", "Over 100 times. Most recent notable: Arunachal Pradesh 2016."],
    ],
)

pn.section("3. Financial Emergency — Article 360")
pn.definition(
    "<b>Financial Emergency (Art. 360):</b> Proclaimed when the President is satisfied that "
    "the financial stability or credit of India or any part of it is threatened."
)
pn.info_table(
    ["Aspect", "Provision"],
    [
        [
            "Approval",
            "Both Houses of Parliament must approve within 2 months by simple majority.",
        ],
        ["Duration", "Continues until revoked; no maximum period specified."],
        [
            "Effect",
            "Directions may be given to all states regarding financial propriety. "
            "Salaries of all government servants (including judges of Supreme Court and High Courts) may be reduced. "
            "All Money Bills and Financial Bills of states to be reserved for President's consideration.",
        ],
        ["Instance", "Never been proclaimed in India so far."],
    ],
)

pn.section("Comparison of Three Emergencies")
pn.info_table(
    [
        "Basis",
        "National Emergency (Art. 352)",
        "President's Rule (Art. 356)",
        "Financial Emergency (Art. 360)",
    ],
    [
        [
            "Ground",
            "War, External Aggression, Armed Rebellion",
            "Failure of Constitutional Machinery",
            "Threat to Financial Stability",
        ],
        ["Approval Period", "1 month", "2 months", "2 months"],
        [
            "Approval Majority",
            "Special majority (both Houses)",
            "Simple majority (both Houses)",
            "Simple majority (both Houses)",
        ],
        [
            "Maximum Duration",
            "No maximum (6-month extensions)",
            "3 years (6-month extensions)",
            "No maximum (indefinite)",
        ],
        [
            "Effect on FR",
            "Art. 19 suspended (war/aggression); Art. 20 & 21 never suspended",
            "No direct effect on FRs",
            "No direct suspension",
        ],
        [
            "Effect on State Autonomy",
            "Centre legislates on State List; executive directions",
            "State executive + legislature under Centre's control",
            "Financial directions to states; salary cuts",
        ],
        ["Instances", "3 times", "100+ times", "Never"],
    ],
)
pn.br()

# =============================================================================
#  4.3  LOCAL SELF GOVERNMENT
# =============================================================================
pn.chap_box("4.3  Local Self Government — 73rd & 74th Constitutional Amendments")

pn.section("What is Panchayati Raj?")
pn.definition(
    "<b>Panchayati Raj:</b> Panchayati Raj refers to the system of local self-government in rural areas "
    "of India. The word 'panchayat' means an assembly of five persons. "
    "It is a system of governance in which gram panchayats are the basic unit of administration. "
    "Constitutional status was given to Panchayati Raj by the <b>73rd Constitutional Amendment Act, 1992</b> "
    "(came into force on 24 April 1993). Added Part IX (Art. 243 to 243O) and 11th Schedule."
)

pn.section("Historical Background")
pn.info_table(
    ["Year / Report", "Key Contribution"],
    [
        [
            "Balwant Rai Mehta Committee (1957)",
            "First major recommendation for democratic decentralization. "
            "Recommended 3-tier Panchayati Raj system: Village Panchayat (Gram Panchayat), "
            "Block level (Panchayat Samiti), District level (Zila Parishad). "
            "Democratic elections at all levels. Transfer of finances, personnel, and functions to local bodies.",
        ],
        [
            "Ashok Mehta Committee (1977)",
            "Recommended 2-tier structure (District Panchayat + Mandal Panchayat). "
            "Voluntary disclosure of caste in panchayat elections. Official participation of political parties.",
        ],
        [
            "G.V.K. Rao Committee (1985)",
            "Recommended making District Collector the pivot of rural development. "
            "Strengthening Zila Parishad. Regular elections.",
        ],
        [
            "L.M. Singhvi Committee (1986)",
            "Recommended constitutional recognition to Panchayati Raj institutions. "
            "Concept of Gram Sabha emphasized. Independent finance commissions for PRIs.",
        ],
        [
            "73rd Amendment, 1992",
            "Gave constitutional status to Panchayats. Part IX of Constitution.",
        ],
    ],
)

pn.section("Balwant Rai Mehta Committee (1957) — Important Recommendations")
pn.bullet(
    [
        "Establishment of a 3-tier Panchayati Raj structure: Village (Gram Panchayat), Block (Panchayat Samiti), District (Zila Parishad).",
        "District level should be the keystone of the Panchayat Raj structure.",
        "Democratic decentralization of power — elected bodies at all levels.",
        "Transfer of financial resources, personnel, and governmental functions to local bodies.",
        "Block Development Officer (BDO) to be executive officer of Panchayat Samiti.",
        "National Extension Service to be reorganised on this pattern.",
    ]
)

pn.section("73rd Amendment — Panchayati Raj Key Provisions")
pn.info_table(
    ["Provision", "Article", "Content"],
    [
        [
            "Gram Sabha",
            "Art. 243A",
            "Body of persons registered as voters in a Panchayat area. Foundation of Panchayati Raj.",
        ],
        [
            "3-Tier Structure",
            "Art. 243B",
            "Village, Intermediate, and District level Panchayats (State with population < 20 lakhs can have 2-tier).",
        ],
        [
            "Composition",
            "Art. 243C",
            "Members directly elected by voters. Chairpersons elected by members.",
        ],
        [
            "Reservation",
            "Art. 243D",
            "Seats reserved for SC/ST (proportional to population). Not less than 1/3 seats reserved for women.",
        ],
        [
            "Duration",
            "Art. 243E",
            "5-year term. If dissolved, elections within 6 months.",
        ],
        [
            "State Finance Commission",
            "Art. 243I",
            "Governor constitutes State Finance Commission every 5 years to review financial position of Panchayats.",
        ],
        [
            "State Election Commission",
            "Art. 243K",
            "Superintendence, direction, control of preparation of electoral rolls and conduct of elections to Panchayats.",
        ],
        [
            "Powers and Functions",
            "Art. 243G + 11th Schedule",
            "29 subjects in 11th Schedule: agriculture, land improvement, minor irrigation, animal husbandry, fisheries, social forestry, elementary education, markets, etc.",
        ],
    ],
)

pn.section("74th Amendment — Urban Local Bodies (Municipalities)")
pn.definition(
    "<b>74th Constitutional Amendment Act, 1992</b> gave constitutional status to urban local bodies. "
    "Added Part IX-A (Art. 243P to 243ZG) and 12th Schedule (18 subjects). "
    "Three types of municipalities: Nagar Panchayat, Municipal Council, Municipal Corporation (based on population)."
)
pn.bullet(
    [
        "Reservation of seats for SC/ST, women (minimum 1/3).",
        "12th Schedule contains 18 subjects including urban planning, regulation of land use, public health, water supply, fire services, urban poverty alleviation.",
        "State Finance Commission to review financial position of municipalities.",
        "State Election Commission to conduct elections.",
    ]
)

pn.section("State Finance Commission (SFC)")
pn.definition(
    "<b>State Finance Commission (Art. 243I, 243Y):</b> Constituted by the Governor every 5 years. "
    "It reviews the financial position of Panchayats and Municipalities and makes recommendations "
    "regarding: distribution of net proceeds of state taxes/duties between the state and PRIs; "
    "grants-in-aid from the Consolidated Fund of the State; measures to improve the financial "
    "position of Panchayats and Municipalities."
)

pn.section("Decentralization of Power — Benefits")
pn.bullet(
    [
        "<b>Democracy at Grassroots:</b> Brings government closer to the people; increases political participation.",
        "<b>Efficient Local Governance:</b> Local problems understood and solved better by local bodies.",
        "<b>Social Justice:</b> Reservation for SC/ST and women ensures inclusion of marginalised sections.",
        "<b>Development Planning:</b> Local development plans prepared and implemented more effectively.",
        "<b>Reduced Corruption:</b> Local accountability reduces misuse of public funds.",
        "<b>National Integration:</b> People develop sense of belonging and responsibility to larger democratic process.",
    ]
)

pn.exam(
    "PYQ (multiple years): 'What do you mean by Panchayati Raj?' (3 marks). "
    "'Recommendations of Balwant Rai Mehta Committee' (4 marks). "
    "'State Finance Commission functions' (4 marks). "
    "'Benefits of Decentralization of Power' (10 marks). "
    "'Critically analyse working of rural local self government' (10 marks)."
)
pn.br()

# #############################################################################
#  PART E — CO5: FUNDAMENTAL RIGHTS
# #############################################################################
pn.part_box("UNIT V — CO5: FUNDAMENTAL RIGHTS — EQUALITY, ARTICLE 19 & ARTICLE 21")

# =============================================================================
#  5.1  SCHEME OF FUNDAMENTAL RIGHTS
# =============================================================================
pn.chap_box("5.1  Scheme of Fundamental Rights (Part III, Articles 12–35)")

pn.section("Introduction")
pn.definition(
    "<b>Fundamental Rights:</b> Part III (Articles 12–35) of the Constitution guarantees certain "
    "basic rights to every person, which form the foundation of individual liberty and human dignity. "
    "These rights are called 'fundamental' because they are essential for the all-round development "
    "of individuals and are justiciable (enforceable through courts). "
    "They are derived primarily from the constitutions of the USA, Ireland, and UK."
)
pn.body(
    "Originally 7 categories of Fundamental Rights. After the 44th Amendment (1978), "
    "<b>Right to Property</b> (Art. 19(f) and Art. 31) was removed from the list of FRs "
    "and made a legal/constitutional right under Art. 300A. Now there are <b>6 categories</b>."
)

pn.section("Six Fundamental Rights — Overview")
pn.info_table(
    ["Fundamental Right", "Articles", "Key Provisions"],
    [
        [
            "1. Right to Equality",
            "Art. 14–18",
            "Equality before law (Art. 14), Prohibition of discrimination on grounds of religion, race, caste, sex, birth place (Art. 15), "
            "Equality of opportunity in public employment (Art. 16), Abolition of untouchability (Art. 17), "
            "Abolition of titles (Art. 18).",
        ],
        [
            "2. Right to Freedom",
            "Art. 19–22",
            "6 Freedoms under Art. 19: speech & expression, assembly, association, movement, residence, profession. "
            "Protection against conviction for ex-post-facto laws (Art. 20). "
            "Right to Life and Personal Liberty (Art. 21). Education (Art. 21A). "
            "Protection against arbitrary arrest and detention (Art. 22).",
        ],
        [
            "3. Right against Exploitation",
            "Art. 23–24",
            "Prohibition of traffic in human beings and forced labour (Art. 23). "
            "Prohibition of child labour in factories, hazardous employment for children below 14 years (Art. 24).",
        ],
        [
            "4. Right to Freedom of Religion",
            "Art. 25–28",
            "Freedom of conscience and free profession, practice, propagation of religion (Art. 25). "
            "Freedom to manage religious affairs (Art. 26). "
            "No tax for promotion of religion (Art. 27). "
            "No religious instruction in state-funded educational institutions (Art. 28).",
        ],
        [
            "5. Cultural and Educational Rights",
            "Art. 29–30",
            "Protection of interests of minorities — right to conserve language, script, culture (Art. 29). "
            "Right of minorities to establish and administer educational institutions (Art. 30).",
        ],
        [
            "6. Right to Constitutional Remedies",
            "Art. 32",
            "Dr. Ambedkar called Art. 32 'the heart and soul of the Constitution.' "
            "Right to move the Supreme Court for enforcement of fundamental rights. "
            "Supreme Court can issue writs: Habeas Corpus, Mandamus, Prohibition, Certiorari, Quo Warranto.",
        ],
    ],
)

pn.section("Are Fundamental Rights Absolute?")
pn.body(
    "Fundamental Rights are NOT absolute. Most FRs can be restricted (but not abrogated) "
    "by the State on reasonable grounds. For example:"
)
pn.bullet(
    [
        "Art. 19 freedoms are subject to 'reasonable restrictions' in the interests of sovereignty, security, public order, decency, morality, etc.",
        "Art. 25 right to religion is subject to public order, morality, and health.",
        "Art. 14 (equality) allows reasonable classification (not arbitrary classification).",
        "During a National Emergency, Art. 19 rights can be suspended.",
        "ONLY Art. 20 (protection against self-incrimination) and Art. 21 (right to life) CANNOT be suspended even during emergency.",
    ]
)

# =============================================================================
#  5.2  RIGHT TO EQUALITY (ARTICLES 14–18)
# =============================================================================
pn.chap_box("5.2  Fundamental Right to Equality — Articles 14–18")

pn.section("Article 14 — Equality Before Law and Equal Protection of Laws")
pn.definition(
    "<b>Art. 14:</b> 'The State shall not deny to any person equality before the law or equal protection "
    "of the laws within the territory of India.' "
    "It contains two concepts: (1) Equality before Law (negative concept — borrowed from English common law) — "
    "equal subjection of all to the same law. No person is above the law. "
    "(2) Equal Protection of Laws (positive concept — borrowed from the US Constitution) — "
    "like should be treated alike; right to equal treatment in similar circumstances."
)
pn.note(
    "The doctrine of 'Reasonable Classification' (not arbitrary classification) is permitted under Art. 14. "
    "A law may classify persons or things differently if: (a) there is an intelligible differentia "
    "(a real difference between the groups), and (b) the differentia has a rational nexus to the object of the law."
)

pn.section("Article 15 — Prohibition of Discrimination")
pn.definition(
    "<b>Art. 15:</b> Prohibits discrimination by the State against any citizen on grounds of "
    "religion, race, caste, sex, or place of birth only. "
    "Guarantees equal access to public places (restaurants, hotels, public wells, roads, etc.). "
    "Exception: State can make special provisions for women, children, SC, ST, OBC (socially and educationally backward classes)."
)

pn.section("Article 16 — Equality of Opportunity in Public Employment")
pn.definition(
    "<b>Art. 16:</b> All citizens have equal opportunity in matters relating to employment or appointment "
    "to any office under the State. "
    "Exception: Reservation can be provided for backward classes, SC/ST not adequately represented. "
    "Residence requirement can be prescribed for certain state government posts."
)

pn.section("Article 17 — Abolition of Untouchability")
pn.definition(
    "<b>Art. 17:</b> Abolishes untouchability and makes its practice in any form an offence. "
    "The Protection of Civil Rights Act, 1955 gives effect to Art. 17. "
    "This is one of the few absolute rights — no exceptions."
)

pn.section("Article 18 — Abolition of Titles")
pn.definition(
    "<b>Art. 18:</b> Prohibits the State from conferring any title on any person (other than military or academic distinctions). "
    "Citizens of India cannot accept titles from foreign states without the President's consent. "
    "Bharat Ratna, Padma awards are NOT titles under Art. 18 (Supreme Court held in Balaji Raghavan case, 1996)."
)

# =============================================================================
#  5.3  ARTICLE 19 — SIX FREEDOMS
# =============================================================================
pn.chap_box("5.3  Right to Certain Freedoms — Article 19")

pn.section("Article 19 — Six Freedoms and Their Restrictions")
pn.definition(
    "<b>Art. 19:</b> Guarantees to all CITIZENS (not all persons) six freedoms. "
    "Originally 7 freedoms; Art. 19(1)(f) — right to acquire, hold, and dispose of property — "
    "was deleted by the 44th Amendment, 1978."
)

pn.info_table(
    ["Freedom (Art. 19(1))", "Content", "Permissible Restrictions (Art. 19(2)–(6))"],
    [
        [
            "(a) Speech & Expression",
            "Right to express one's views, opinions, beliefs freely through any medium (spoken word, writing, pictures, electronic media, internet).",
            "Reasonable restrictions in interests of: sovereignty & integrity of India, security of state, friendly relations with foreign states, public order, decency/morality, contempt of court, defamation, incitement to offence.",
        ],
        [
            "(b) Peaceful Assembly",
            "Right to assemble peaceably and without arms.",
            "Restrictions in interest of sovereignty & integrity of India or public order.",
        ],
        [
            "(c) Association & Unions",
            "Right to form associations, unions, or cooperative societies.",
            "Restrictions in interest of sovereignty & integrity of India, public order, or morality.",
        ],
        [
            "(d) Free Movement",
            "Right to move freely throughout the territory of India.",
            "Restrictions in interest of general public or protection of interests of any Schedule Tribe.",
        ],
        [
            "(e) Residence & Settlement",
            "Right to reside and settle in any part of India.",
            "Same as (d).",
        ],
        [
            "(g) Profession / Occupation",
            "Right to practise any profession, carry on any occupation, trade, or business.",
            "The State can prescribe professional or technical qualifications, and carry on any trade or business to the exclusion of citizens (State monopoly).",
        ],
    ],
)

pn.section("Freedom of Speech & Expression — Landmark Cases")
pn.info_table(
    ["Case", "Holding"],
    [
        [
            "Romesh Thapar v. State of Madras (1950)",
            "Held freedom of speech and expression includes freedom to propagate ideas through publication and circulation.",
        ],
        [
            "Maneka Gandhi v. Union of India (1978)",
            "Broadened scope of Art. 21 by linking it with Art. 14 and 19; personal liberty interpreted widely.",
        ],
        [
            "Shreya Singhal v. Union of India (2015)",
            "Struck down Sec. 66A of IT Act as unconstitutional — speech that is merely offensive (not incitement to crime) cannot be restricted.",
        ],
        [
            "PUCL v. Union of India (2003)",
            "Held that the right to vote and stand in elections is part of freedom of expression.",
        ],
    ],
)

pn.exam(
    "PYQ: 'Explain Article 19' (June 2022, 10 marks). "
    "'Explain freedom of speech and expression under Art. 19 with decided cases' (June-July 2025, 10 marks). "
    "'Classify the six freedoms under Article 19' (multiple years). "
    "Always list all 6 freedoms with their corresponding restrictions."
)

# =============================================================================
#  5.4  ARTICLE 21 — RIGHT TO LIFE AND PERSONAL LIBERTY
# =============================================================================
pn.chap_box("5.4  Scope of Right to Life and Personal Liberty — Article 21")

pn.section("Article 21 — Text and Interpretation")
pn.definition(
    "<b>Art. 21:</b> 'No person shall be deprived of his life or personal liberty except according to "
    "procedure established by law.' "
    "Originally interpreted narrowly (procedure established by law = any procedure laid down by statute). "
    "After <b>Maneka Gandhi v. Union of India (1978)</b>, the Supreme Court gave an expanded interpretation: "
    "the procedure must be <b>right, just, fair, and reasonable</b> — not arbitrary, fanciful, or oppressive. "
    "This brought Art. 21 close to the US concept of 'due process of law.'"
)

pn.section("Expanded Scope of Article 21 — Rights Implied")
pn.body(
    "The Supreme Court has progressively expanded Art. 21 to include a wide variety of rights "
    "through judicial interpretation. These are sometimes called the 'unenumerated rights' or "
    "'rights implicit in Art. 21':"
)
pn.info_table(
    ["Right Implied under Art. 21", "Case / Authority"],
    [
        ["Right to Livelihood", "Olga Tellis v. Bombay Municipal Corporation (1985)"],
        [
            "Right to Privacy",
            "K.S. Puttaswamy v. Union of India (2017) — 9-judge bench; Right to Privacy is a fundamental right.",
        ],
        [
            "Right to Education (for children 6–14)",
            "Unni Krishnan case (1993); later constitutionalised by Art. 21A (86th Amendment, 2002)",
        ],
        [
            "Right to Health and Medical Care",
            "Paschim Banga Khet Mazdoor Samity (1996)",
        ],
        ["Right to Speedy Trial", "Hussainara Khatoon v. State of Bihar (1979)"],
        [
            "Right against Handcuffing",
            "Prem Shankar Shukla v. Delhi Administration (1980)",
        ],
        ["Right to Legal Aid", "M.H. Hoskot v. State of Maharashtra (1978)"],
        ["Right to a Clean Environment", "Subhash Kumar v. State of Bihar (1991)"],
        ["Right to Sleep / Rest", "Re-Ramlila Maidan Incident (2012)"],
        [
            "Right to Die with Dignity",
            "Common Cause v. Union of India (2018) — Passive euthanasia permitted",
        ],
        [
            "Right against Sexual Harassment at Workplace",
            "Vishaka v. State of Rajasthan (1997)",
        ],
        ["Right to Food", "PUCL v. Union of India (2001)"],
        ["Right to Shelter", "Chameli Singh v. State of U.P. (1996)"],
    ],
)

pn.section("Article 21A — Right to Education")
pn.definition(
    "<b>Art. 21A (86th Amendment, 2002):</b> 'The State shall provide free and compulsory education "
    "to all children of the age of 6 to 14 years in such manner as the State may, by law, determine.' "
    "This was a DPSP (Art. 45) that was converted into a Fundamental Right. "
    "The Right to Education Act, 2009 gives effect to Art. 21A."
)

pn.section("Preventive Detention — Article 22")
pn.definition(
    "<b>Preventive Detention (Art. 22):</b> Detention of a person without trial to prevent a possible "
    "future breach of law. "
    "Art. 22(1) and (2) — Safeguards for persons arrested: right to be informed of grounds of arrest, "
    "right to consult a lawyer, produced before a magistrate within 24 hours. "
    "Art. 22(3) to (7) — Safeguards for preventive detention: person to be informed of grounds, "
    "right of representation to an Advisory Board, maximum detention initially 3 months "
    "(extended only on Advisory Board's opinion)."
)

pn.exam(
    "PYQ: 'Explain scope of Right to Life and Personal Liberty under Art. 21' (multiple years, 4-10 marks). "
    "'Define Article 21' (June 2022, 10 marks). "
    "'What do you mean by Preventive detention?' (Nov-Dec 2024, 3 marks). "
    "'Classify personal liberty in Indian Constitution' (June 2022, 4 marks). "
    "Key cases to mention: Maneka Gandhi (1978), K.S. Puttaswamy (2017), Olga Tellis (1985)."
)
pn.br()

# #############################################################################
#  PART F — ADDITIONAL TOPICS FROM PYQs
# #############################################################################
pn.part_box("ADDITIONAL PYQ TOPICS — WRITS, PARLIAMENT, PREAMBLE & MORE")

# =============================================================================
#  6.1  CONSTITUTIONAL REMEDIES & WRITS
# =============================================================================
pn.chap_box("6.1  Article 32 — Constitutional Remedies & Five Writs")

pn.section("Article 32 — Right to Constitutional Remedies")
pn.definition(
    "<b>Art. 32:</b> Called the 'Heart and Soul of the Constitution' by Dr. B.R. Ambedkar. "
    "Guarantees the right to move the Supreme Court for enforcement of Fundamental Rights. "
    "The Supreme Court can issue writs for this purpose. "
    "Art. 226 gives similar (wider) powers to High Courts for enforcement of both FRs and other legal rights."
)

pn.section("Five Writs — Detailed")
pn.info_table(
    ["Writ", "Literal Meaning", "Against Whom", "Purpose", "Example"],
    [
        [
            "Habeas Corpus",
            "'To have the body'",
            "Any person detaining another (government or private)",
            "Direct the person who has detained another to produce the detained person before the court and justify the detention.",
            "Illegal arrest, preventive detention without valid grounds",
        ],
        [
            "Mandamus",
            "'We command'",
            "Public authorities, government bodies, inferior courts",
            "Command a public official or body to perform a public or statutory duty that it has failed or refused to perform.",
            "Government officer refusing to issue a licence as required by law",
        ],
        [
            "Prohibition",
            "'To forbid'",
            "Inferior courts and quasi-judicial tribunals",
            "Issued to prevent a lower court from acting beyond its jurisdiction or from proceeding with a case that is outside its authority.",
            "Preventing a district court from hearing a case beyond its pecuniary jurisdiction",
        ],
        [
            "Certiorari",
            "'To be certified'",
            "Inferior courts and quasi-judicial tribunals",
            "Issued to quash the order of a lower court already made, if the lower court acted without jurisdiction or in excess of it, or in violation of natural justice.",
            "Quashing an illegal tribunal decision",
        ],
        [
            "Quo Warranto",
            "'By what authority'",
            "Person holding a public office",
            "Inquire into the legality of the claim of a person to hold a public office. "
            "Prevents illegal assumption of public office.",
            "Challenging appointment of a person not qualified for a constitutional post",
        ],
    ],
)

pn.exam(
    "PYQ: 'Under Art. 32, how many types of writs can be issued by Supreme Court? Discuss in detail' "
    "(May-June 2024, 10 marks). Always name all 5 writs with meanings, purpose, and examples."
)

# =============================================================================
#  6.2  PREAMBLE
# =============================================================================
pn.chap_box("6.2  Preamble of the Indian Constitution")

pn.section("Text of the Preamble")
pn.highlight(
    "<b>WE, THE PEOPLE OF INDIA,</b> having solemnly resolved to constitute India into a "
    "<b>SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC, REPUBLIC</b> and to secure to all its citizens:<br/><br/>"
    "<b>JUSTICE</b>, social, economic and political;<br/>"
    "<b>LIBERTY</b> of thought, expression, belief, faith and worship;<br/>"
    "<b>EQUALITY</b> of status and of opportunity;<br/>"
    "and to promote among them all<br/>"
    "<b>FRATERNITY</b> assuring the dignity of the individual and the unity and integrity of the Nation;<br/><br/>"
    "IN OUR CONSTITUENT ASSEMBLY this <b>twenty-sixth day of November, 1949</b>, do HEREBY ADOPT, ENACT AND GIVE TO OURSELVES THIS CONSTITUTION."
)

pn.section("Key Terms in the Preamble")
pn.info_table(
    ["Term", "Meaning"],
    [
        [
            "Sovereign",
            "India is free from external control; supreme authority within its territory.",
        ],
        [
            "Socialist",
            "Added by 42nd Amendment (1976). Means democratic socialism — mixed economy; not Soviet-style state socialism.",
        ],
        [
            "Secular",
            "Added by 42nd Amendment (1976). No state religion; equal respect and protection to all religions.",
        ],
        [
            "Democratic",
            "People are the ultimate source of authority. Universal adult franchise. Responsible government.",
        ],
        [
            "Republic",
            "Head of State (President) is elected; not hereditary. Sovereignty vests in the people.",
        ],
        [
            "Justice (Social, Economic, Political)",
            "Social — no discrimination; Economic — equitable distribution; Political — equal political rights.",
        ],
        ["Liberty", "Freedom of thought, expression, belief, faith, worship."],
        ["Equality", "No privilege; equal status and opportunity for all."],
        [
            "Fraternity",
            "Sense of brotherhood; dignity of the individual; unity and integrity of the nation.",
        ],
    ],
)

pn.section("Is Preamble a Part of the Constitution?")
pn.body(
    "The Supreme Court settled this question in <b>Kesavananda Bharati v. State of Kerala (1973)</b>. "
    "It is now firmly established that the Preamble IS a part of the Constitution and can be "
    "amended under Art. 368. However, its basic features cannot be destroyed."
)

pn.exam(
    "PYQ: 'What is Preamble? Is it part of Constitution? Can it be used for interpretation?' (May-June 2023, 4 marks). "
    "'Write five elements of the Preamble' (May-June 2024, 4 marks)."
)

# =============================================================================
#  6.3  LOK SABHA vs RAJYA SABHA
# =============================================================================
pn.chap_box("6.3  Parliament — Lok Sabha vs Rajya Sabha")

pn.section("Parliament of India")
pn.definition(
    "<b>Parliament (Art. 79):</b> The Union Legislature consists of the President and two Houses: "
    "the <b>Council of States (Rajya Sabha)</b> and the <b>House of the People (Lok Sabha)</b>."
)

pn.info_table(
    ["Basis", "Lok Sabha (Lower House)", "Rajya Sabha (Upper House)"],
    [
        ["Also Called", "House of the People", "Council of States"],
        [
            "Members",
            "Maximum 552 (543 elected + up to 2 nominated by President for Anglo-Indians — removed by 104th Amdt, 2020)",
            "Maximum 250 (238 elected by states + 12 nominated by President)",
        ],
        [
            "Election",
            "Directly elected by people through Universal Adult Franchise",
            "Indirectly elected by elected MLAs of states and UTs (using Proportional Representation — Single Transferable Vote)",
        ],
        [
            "Duration",
            "5-year term; can be dissolved by President",
            "Permanent body — never dissolved; 1/3 members retire every 2 years. Each member serves 6-year term.",
        ],
        [
            "Speaker/Chairman",
            "Speaker (elected by Lok Sabha members)",
            "Vice President of India is ex-officio Chairman",
        ],
        [
            "Money Bills",
            "Introduced only in Lok Sabha; Rajya Sabha has no veto — can delay for 14 days only",
            "Cannot introduce Money Bills",
        ],
        [
            "No Confidence Motion",
            "Government can be ousted by no-confidence motion in Lok Sabha",
            "No confidence motion cannot be introduced in Rajya Sabha",
        ],
        [
            "Constitutional Amendment",
            "Equal powers with Rajya Sabha; no joint sitting for amendments",
            "Equal powers; both must pass by special majority",
        ],
        [
            "Special Powers",
            "Budget and Money Bills, No-confidence motion against government",
            "Can authorise Parliament to legislate on State List (Art. 249); create new All India Services (Art. 312)",
        ],
    ],
)

pn.section("Why is Rajya Sabha called a Permanent Chamber?")
pn.body(
    "Rajya Sabha is a permanent body because it is never dissolved. Its members are elected for "
    "6-year terms and one-third of its members retire every two years. This ensures continuity "
    "of legislative work even when the Lok Sabha is dissolved. The Rajya Sabha thus provides "
    "stability and acts as a revising chamber that cannot be suddenly swept away by popular sentiment."
)

pn.section("Zero Hour of Indian Parliament")
pn.definition(
    "<b>Zero Hour:</b> The time immediately following Question Hour (at 12 noon) in Parliament. "
    "It is not mentioned in the Constitution or Parliamentary Rules; it is an informal parliamentary "
    "innovation. Members raise matters of urgent public importance during Zero Hour without giving "
    "prior notice. It allows MPs to raise current and urgent issues immediately."
)

pn.section("Parliamentary Committees")
pn.info_table(
    ["Committee", "Composition & Function"],
    [
        [
            "Public Accounts Committee",
            "15 Lok Sabha + 7 Rajya Sabha members. Chaired by the Leader of Opposition. "
            "Examines the annual audit reports of the Comptroller and Auditor General (CAG). "
            "Ensures money granted by Parliament is spent for authorised purposes only.",
        ],
        [
            "Estimates Committee",
            "30 members from Lok Sabha only. Examines budget estimates — whether money is well-laid-out and economically spent. "
            "Suggests alternative policies and economies. Does not examine expenditure already incurred (that is PAC's role).",
        ],
        [
            "Committee on Public Undertakings",
            "15 Lok Sabha + 7 Rajya Sabha members. Examines reports and accounts of Government-owned companies.",
        ],
    ],
)

pn.exam(
    "PYQ: 'Difference between Rajya Sabha and Lok Sabha' (Nov-Dec 2024, 3 marks). "
    "'Compare powers of Lok Sabha and Rajya Sabha' (May-June 2024, 10 marks). "
    "'Why is Rajya Sabha called permanent chamber?' (June-July 2025, 10 marks). "
    "'What is Zero Hour?' (May-June 2024, 3 marks). "
    "'Note on Parliamentary Accounts Committee and Estimates Committee' (May-June 2024, 10 marks)."
)
pn.br()

# =============================================================================
#  6.4  INTER-STATE COUNCIL, NITI AAYOG, ATTORNEY GENERAL
# =============================================================================
pn.chap_box("6.4  Inter-State Council | NITI Aayog | Attorney General of India")

pn.section("Inter-State Council (Article 263)")
pn.definition(
    "<b>Inter-State Council (Art. 263):</b> A body established to promote coordination between "
    "the States and between States and the Centre. "
    "Established in 1990 on the recommendation of Sarkaria Commission. "
    "Presided over by the Prime Minister. Includes all Chief Ministers of States, "
    "Chief Ministers of Union Territories with legislatures, and Administrators of UTs without legislatures, "
    "plus 6 Cabinet Ministers of the Union as nominated by PM. "
    "Discusses and recommends policies on matters of common interest — though its recommendations are non-binding."
)

pn.section("NITI Aayog")
pn.definition(
    "<b>NITI Aayog (National Institution for Transforming India):</b> Established on 1 January 2015 "
    "to replace the Planning Commission. It is a government think tank and policy advisory body. "
    "Chaired by the Prime Minister. CEO is appointed by the Prime Minister. "
    "<b>NITI Aayog does NOT allocate funds</b> (unlike the old Planning Commission). "
    "It focuses on bottom-up planning, cooperative federalism, long-term strategic national programs, "
    "and monitoring the implementation of government initiatives. "
    "Key bodies: Governing Council (all CMs and LGs of UTs), Regional Councils, Full-time members."
)

pn.section("Attorney General of India (Article 76)")
pn.definition(
    "<b>Attorney General of India (Art. 76):</b> The first law officer of the Government of India. "
    "Appointed by the President. Must be qualified to be a judge of the Supreme Court. "
    "<b>Functions:</b> Give advice to the Government of India on legal matters; "
    "appear on behalf of the Union in the Supreme Court in cases involving the Union; "
    "perform other duties assigned by the President. "
    "The AG has the right of audience in all courts throughout India. "
    "The AG is not a full-time government servant — he can also appear in private cases (provided no conflict of interest)."
)

pn.exam(
    "PYQ: 'Write a short note on Inter-state Council' (May-June 2024, 4 marks). "
    "'What do you understand by NITI Aayog?' (Nov-Dec 2024, 3 marks). "
    "'Attorney General is the chief legal adviser of GoI — Discuss' (Nov-Dec 2024, 10 marks)."
)

# =============================================================================
#  6.5  CITIZENSHIP
# =============================================================================
pn.chap_box("6.5  Citizenship — Methods of Acquisition and Termination")

pn.section("Citizenship in India")
pn.body(
    "Part II (Articles 5–11) of the Constitution deals with citizenship at the commencement "
    "of the Constitution. The Citizenship Act, 1955 governs citizenship thereafter."
)

pn.section("Acquisition of Citizenship")
pn.info_table(
    ["Mode", "Provision"],
    [
        [
            "By Birth",
            "Born in India on or after 26 Jan 1950 but before 1 Jul 1987 — automatic citizen. "
            "After 1 Jul 1987 — at least one parent must be Indian citizen.",
        ],
        [
            "By Descent",
            "Person born outside India whose father (or either parent after 2004) was a citizen.",
        ],
        [
            "By Registration",
            "Persons of Indian origin who have been resident for prescribed period. Persons married to Indian citizens.",
        ],
        [
            "By Naturalisation",
            "Foreigners who have resided in India for 12 years (5 years OCI) can apply.",
        ],
        [
            "By Incorporation of Territory",
            "If a new territory becomes part of India, its people become Indian citizens.",
        ],
    ],
)

pn.section("Termination / Loss of Citizenship")
pn.info_table(
    ["Mode", "How it Occurs"],
    [
        [
            "Renunciation (Sec. 8)",
            "Citizen makes a declaration of renunciation (when of majority age and acquiring foreign nationality). Minors' citizenship also terminates with parent.",
        ],
        [
            "Termination (Sec. 9)",
            "If a citizen voluntarily acquires the citizenship of another country, Indian citizenship automatically terminates.",
        ],
        [
            "Deprivation (Sec. 10)",
            "Compulsory termination by Government if citizenship was obtained by fraud, false representation, or concealment; citizen shown disloyalty; illegally traded with an enemy; imprisonment within 5 years of registration.",
        ],
    ],
)

pn.exam(
    "PYQ (June-July 2025): 'Write notes on methods of termination of Indian citizenship' (4 marks)."
)
pn.br()

# =============================================================================
#  6.6  SUPREME COURT & HIGH COURT
# =============================================================================
pn.chap_box("6.6  Supreme Court and High Court — Jurisdictions & Qualifications")

pn.section("Jurisdictions of the Supreme Court of India")
pn.definition(
    "<b>Supreme Court (Articles 124–147):</b> The apex court of the Indian judicial system. "
    "It has vast powers and holds different types of jurisdictions:"
)
pn.info_table(
    ["Jurisdiction Type", "Article", "Scope and Key Provisions"],
    [
        [
            "Original Jurisdiction",
            "Art. 131",
            "Disputes between: (1) Government of India and one or more States; "
            "(2) GoI and any State(s) on one side and other State(s) on the other; "
            "(3) Two or more States. Exclusive jurisdiction of the SC.",
        ],
        [
            "Writ Jurisdiction",
            "Art. 32",
            "Power to issue writs (Habeas Corpus, Mandamus, Prohibition, Certiorari, "
            "Quo Warranto) for the enforcement of Fundamental Rights.",
        ],
        [
            "Appellate Jurisdiction",
            "Art. 132–134",
            "Hears appeals against High Court judgments in: (1) Constitutional matters, "
            "(2) Civil cases, (3) Criminal cases.",
        ],
        [
            "Advisory Jurisdiction",
            "Art. 143",
            "The President can seek the opinion of the SC on any question of law or fact "
            "of public importance. The SC's opinion is advisory and not binding on the President.",
        ],
    ],
)

pn.section("High Court Constitution and Judges Qualifications")
pn.definition(
    "<b>High Court (Articles 214–231):</b> The highest judicial organ in a State. "
    "Consists of a Chief Justice and such other Judges as the President may appoint."
)
pn.bullet(
    [
        "<b>Essential Qualifications (Art. 217(2)):</b> A person is qualified for appointment as a High Court Judge if: "
        "(1) He is a citizen of India; and "
        "(2) He has held a judicial office in the territory of India for at least 10 years, OR "
        "(3) He has been an advocate of a High Court (or of two or more such courts in succession) for at least 10 years.",
        "<b>Appointment:</b> Appointed by the President after consultation with the Chief Justice of India, the Governor of the State, and the Chief Justice of the High Court.",
    ]
)

pn.section("Veto Power of the Governor")
pn.definition(
    "<b>Governor's Veto Power (Article 200):</b> When a Bill passed by the State Legislature is presented to the Governor, he can: "
    "(1) Give assent to the Bill; (2) Withhold assent; (3) Return the Bill (if not a Money Bill) for reconsideration; "
    "(4) Reserve the Bill for the consideration of the President (compulsory if it endangers the High Court's position)."
)
pn.exam(
    "PYQ (June-July 2025): 'Explain the scope of original jurisdiction of the Supreme Court' (4 marks), "
    "'Explain the constitution of High Court and qualifications of HC Judge' (10 marks), "
    "and 'Explain the Veto power of the Governor' (10 marks)."
)
pn.br()

# =============================================================================
#  6.7  ORDINARY BILL vs MONEY BILL & LEGISLATIVE PROCESS
# =============================================================================
pn.chap_box("6.7  Legislative Bills — Ordinary Bill vs Money Bill & Passing Procedure")

pn.section("Differences between Ordinary Bill and Money Bill")
pn.info_table(
    ["Basis", "Ordinary Bill", "Money Bill (Article 110)"],
    [
        [
            "Introduction",
            "Can be introduced in either House of Parliament (Lok Sabha or Rajya Sabha).",
            "Can be introduced ONLY in Lok Sabha.",
        ],
        [
            "Recommendation",
            "Introduced without the recommendation of the President.",
            "Can be introduced only on the recommendation of the President.",
        ],
        [
            "Rajya Sabha Powers",
            "Rajya Sabha can amend or reject the Bill.",
            "Rajya Sabha cannot amend or reject it. Can only make recommendations and delay for max 14 days.",
        ],
        [
            "Joint Sitting",
            "In case of deadlock, the President can summon a Joint Sitting (Art. 108) to resolve it.",
            "No provision for a Joint Sitting. Lok Sabha has the final say.",
        ],
        [
            "President's Veto",
            "President can give assent, withhold assent, or return the Bill for reconsideration.",
            "President can give assent or withhold assent, but CANNOT return it for reconsideration.",
        ],
    ],
)

pn.section("Procedure for Passing an Ordinary Bill")
pn.body(
    "The passage of an Ordinary Bill involves five distinct stages in each House of Parliament:"
)
pn.bullet(
    [
        "<b>1. First Reading:</b> Introduction of the Bill and publication in the Gazette. No discussion takes place.",
        "<b>2. Second Reading:</b> Detailed clause-by-clause consideration. The Bill is discussed generally, then referred to a Select Committee or discussed in detail, and amendments are proposed and voted on.",
        "<b>3. Third Reading:</b> Final debate on whether the Bill as a whole should be passed. Only acceptance or rejection is voted on.",
        "<b>4. Passage in the Other House:</b> Sent to the second House where it goes through the same three readings. If the second House rejects or holds it for 6 months, a deadlock occurs.",
        "<b>5. Presidential Assent (Art. 111):</b> Once passed by both Houses, it goes to the President. Upon receiving assent, the Bill becomes an Act.",
    ]
)

pn.section("Parliamentary Legislation in the State Field")
pn.body(
    "Under normal circumstances, Parliament cannot make laws on State List subjects. However, under five extraordinary situations, Parliament acquires this power:"
)
pn.bullet(
    [
        "<b>1. National Interest (Art. 249):</b> If Rajya Sabha passes a resolution supported by 2/3 of members present and voting.",
        "<b>2. National Emergency (Art. 250):</b> While a proclamation of National Emergency is in operation.",
        "<b>3. State Agreement (Art. 252):</b> If two or more States pass resolutions requesting Parliament to make laws.",
        "<b>4. International Agreements (Art. 253):</b> To implement treaties, agreements, or conventions with foreign nations.",
        "<b>5. President's Rule (Art. 357):</b> When President's Rule (Art. 356) is imposed in a State.",
    ]
)
pn.exam(
    "PYQ (May/June 2023): 'Distinguish between Ordinary Bill and Money Bill. Discuss the procedure for passing an Ordinary Bill' (10 marks) "
    "and 'Explain parliamentary legislation in the state field' (10 marks)."
)
pn.br()

# =============================================================================
#  6.8  ADMINISTRATIVE STRUCTURE & GOVERNANCE ORGANS
# =============================================================================
pn.chap_box("6.8  Administrative Governance — Cabinet Secretariat & Cabinet vs CoM")

pn.section("Cabinet Secretariat — Role and Functions")
pn.definition(
    "<b>Cabinet Secretariat:</b> An administrative organ of the Government of India operating "
    "directly under the Prime Minister. Its administrative head is the <b>Cabinet Secretary</b>, "
    "who is the senior-most civil servant in India."
)
pn.bullet(
    [
        "<b>Secretariat Assistance:</b> Prepares agenda for Cabinet and Cabinet Committees, records and circulates minutes of meetings, and tracks implementation of decisions.",
        "<b>Inter-Ministerial Coordination:</b> Resolves differences between ministries and coordinates major inter-departmental policies.",
        "<b>Rule Allocation:</b> Administers the Government of India (Allocation of Business) Rules, 1961.",
        "<b>Crisis Management:</b> Acts as the central coordinating node during national crises.",
    ]
)

pn.section("Differences between Cabinet and Council of Ministers (CoM)")
pn.info_table(
    ["Basis", "Council of Ministers (Articles 74, 75)", "Cabinet"],
    [
        [
            "Size",
            "A larger body consisting of 60 to 80 ministers of all ranks.",
            "A smaller body consisting of 15 to 20 senior ministers of Cabinet rank.",
        ],
        [
            "Categories",
            "Includes Cabinet Ministers, Ministers of State, and Deputy Ministers.",
            "Consists of Cabinet Ministers only.",
        ],
        [
            "Policy Making",
            "Does not meet as a body to decide policy; its functions are determined by the Cabinet.",
            "Meets regularly to formulate national policies, take decisions, and guide the CoM.",
        ],
        [
            "Constitutional Mention",
            "Described in detail in the original Constitution (Articles 74 and 75).",
            "Was not mentioned in the original Constitution; inserted in Art. 352 by the 44th Amendment (1978).",
        ],
    ],
)

pn.section("Delegated Legislation")
pn.definition(
    "<b>Delegated Legislation (Subordinate Legislation):</b> The law-making power delegated "
    "by the Legislature to the Executive (administrative authorities). The Legislature drafts the "
    "broad policy framework, and the Executive drafts the detailed rules, regulations, and bye-laws."
)
pn.bullet(
    [
        "<b>Importance for Administrative Efficiency:</b> (1) Saves parliamentary time; (2) Deals with highly technical matters (e.g., taxation, environment rules); (3) Provides flexibility to adapt rules quickly without amending acts; (4) Essential for handling emergencies.",
        "<b>Safeguards:</b> Subject to: (1) Judicial control (can be declared void if ultra vires), and (2) Parliamentary control (must be laid before Parliament for review).",
    ]
)

pn.section("Governor's Rule vs President's Rule")
pn.body(
    "In normal states, failure of constitutional machinery immediately results in President's Rule under Article 356. "
    "However, under the former Constitution of Jammu & Kashmir (Section 92), if the state machinery failed, "
    "<b>Governor's Rule</b> was first imposed for a maximum of 6 months. "
    "If the machinery was not restored within 6 months, President's Rule (Art. 356) was then proclaimed. "
    "Post the abrogation of Article 370 in 2019, J&K is a Union Territory and comes directly under the standard central provisions."
)
pn.exam(
    "PYQ (Nov-Dec 2024): 'Discuss the role and functions of Cabinet Secretariat' (4 marks), "
    "'Discuss the difference between Cabinet and Council of Ministers' (4 marks), "
    "'Define delegated legislation and discuss its importance' (10 marks), "
    "and 'What do you understand by Governor Rule?' (4 marks)."
)
pn.br()

# =============================================================================
#  6.9  LSG CHALLENGES, NGOs & ENVIRONMENTAL ISSUES
# =============================================================================
pn.chap_box("6.9  Governance Challenges — LSG Constraints, NGOs & Environment")

pn.section("Major Challenges Confronting Local Self-Government (LSGs)")
pn.body(
    "Despite the 73rd and 74th Amendments, Panchayati Raj Institutions (PRIs) face several challenges:"
)
pn.bullet(
    [
        "<b>1. Financial Constraints (3 Fs):</b> Lack of independent financial resources. LSGs depend heavily on state/union grants; state governments are often reluctant to devolve taxing powers (Funds, Functions, Functionaries).",
        "<b>2. Bureaucratic Interference:</b> Local officials and district administration often dominate over elected local representatives.",
        "<b>3. Infrastructure Deficit:</b> Many village panchayats lack office buildings, internet connectivity, and trained secretarial staff.",
        "<b>4. Domination by Local Elites:</b> In many areas, social hierarchies prevent marginalized groups (SC/ST/women) from exercising real decision-making power, leading to 'proxy' governance (e.g., Sarpanch Pati).",
    ]
)

pn.section("Role of NGOs in Environmental Protection")
pn.definition(
    "<b>NGOs (Non-Governmental Organisations):</b> Voluntary, non-profit citizen groups "
    "that play a crucial role in environmental advocacy, research, and resource management."
)
pn.info_table(
    ["Role / Contribution", "Key Constraints & Barriers"],
    [
        [
            "Public Awareness & Campaigns (e.g., Narmada Bachao Andolan)",
            "<b>FCRA & Regulatory Hurdles:</b> Stringent foreign contribution regulations limit funding.",
        ],
        [
            "Advocacy & Judicial Activism (e.g., filing PILs for forest protection)",
            "<b>Financial Constraints:</b> Dependence on temporary donations and grants.",
        ],
        [
            "Grassroots conservation, community afforestation, waste recycling",
            "<b>Local Conflict:</b> Facing opposition from local political/corporate interests.",
        ],
        [
            "Environmental research and policy lobbying",
            "<b>Lack of Capacity:</b> Shortage of technical expertise and legal assistance.",
        ],
    ],
)
pn.exam(
    "PYQ (Nov-Dec 2024 / June-July 2025): 'What are the major challenges confronting Local Self-Government?' (4 marks), "
    "'In the absence of organized local level government, Panchayats have remained mainly political institutions... Critically discuss' (10 marks), "
    "and 'Discuss the role of NGOs to protect the environment and their constraints' (10 marks)."
)
pn.br()

# #############################################################################
#  RAPID REVISION & FLASHCARDS
# #############################################################################
pn.br()
pn.part_box("RAPID REVISION — KEY ARTICLES, CASES & PYQ ANSWERS")

pn.chap_box("Master Reference: All Important Articles")

pn.section("Quick Article Reference Card")
pn.info_table(
    ["Article(s)", "Topic"],
    [
        ["Art. 1", "India — that is Bharat — shall be a Union of States."],
        ["Art. 12–35", "Part III — Fundamental Rights"],
        ["Art. 14", "Equality before law and equal protection of laws"],
        ["Art. 17", "Abolition of untouchability"],
        [
            "Art. 19",
            "Six freedoms (speech, assembly, association, movement, residence, profession)",
        ],
        [
            "Art. 20",
            "Protection against arbitrary conviction (cannot be suspended even during emergency)",
        ],
        ["Art. 21", "Right to Life and Personal Liberty"],
        [
            "Art. 21A",
            "Right to free and compulsory education for children 6–14 years (86th Amendment, 2002)",
        ],
        [
            "Art. 22",
            "Protection against arbitrary arrest; Preventive Detention safeguards",
        ],
        ["Art. 32", "'Heart and Soul' — Right to Constitutional Remedies; Five Writs"],
        ["Art. 36–51", "Part IV — Directive Principles of State Policy"],
        ["Art. 51A", "Part IV-A — Fundamental Duties (11 duties)"],
        [
            "Art. 52–78",
            "Part V — The Union Executive (President, VP, PM, Council of Ministers, AG)",
        ],
        ["Art. 63–71", "Vice President of India"],
        ["Art. 72", "President's power to grant pardons, reprieves, etc."],
        ["Art. 74", "Council of Ministers to aid and advise President"],
        ["Art. 76", "Attorney General of India"],
        ["Art. 79–122", "Parliament — Lok Sabha and Rajya Sabha"],
        ["Art. 108", "Joint sitting of both Houses of Parliament"],
        ["Art. 111", "President's assent to bills; veto powers"],
        ["Art. 123", "President's power to promulgate Ordinances"],
        ["Art. 124–147", "Supreme Court of India"],
        ["Art. 141", "Law declared by Supreme Court is binding on all courts"],
        ["Art. 143", "Advisory Jurisdiction of Supreme Court"],
        ["Art. 148", "Comptroller and Auditor General of India"],
        ["Art. 152–237", "Part VI — The States"],
        [
            "Art. 153–167",
            "State Executive — Governor, Council of Ministers, Chief Minister",
        ],
        ["Art. 168–212", "State Legislature"],
        ["Art. 213", "Governor's Ordinance making power"],
        ["Art. 214–231", "High Courts in States"],
        ["Art. 233–237", "Subordinate Courts"],
        ["Art. 238", "Deleted by 7th Amendment (1956) — reorganisation of states"],
        ["Art. 239–242", "Union Territories"],
        ["Art. 243–243O", "Part IX — Panchayati Raj (73rd Amendment, 1992)"],
        ["Art. 243P–243ZG", "Part IX-A — Municipalities (74th Amendment, 1992)"],
        ["Art. 245–263", "Part XI — Relations between Union and States"],
        [
            "Art. 249",
            "Parliament legislates on State List in national interest (Rajya Sabha resolution)",
        ],
        ["Art. 254", "Conflict between Union and State laws on Concurrent List"],
        ["Art. 263", "Inter-State Council"],
        ["Art. 265–291", "Part XII — Finance, Property, Contracts, Suits"],
        ["Art. 280", "Finance Commission"],
        [
            "Art. 300A",
            "Right to property — legal right (not fundamental right) after 44th Amendment",
        ],
        ["Art. 312", "All-India Services — Rajya Sabha can authorise creation"],
        ["Art. 324–329", "Part XV — Elections; Election Commission"],
        ["Art. 352", "National Emergency — War, External Aggression, Armed Rebellion"],
        [
            "Art. 356",
            "President's Rule — Failure of Constitutional Machinery in States",
        ],
        ["Art. 360", "Financial Emergency — Threat to Financial Stability"],
        ["Art. 368", "Power and Procedure for Amendment of Constitution"],
        ["Art. 393", "Short title of Constitution — 'The Constitution of India'"],
    ],
)

pn.section("Landmark Supreme Court Cases")
pn.info_table(
    ["Case (Year)", "Significance"],
    [
        [
            "A.K. Gopalan v. State of Madras (1950)",
            "Original narrow interpretation of Art. 21 (procedure = any legal procedure).",
        ],
        [
            "State of Madras v. Champakam Dorairajan (1951)",
            "DPSPs cannot override Fundamental Rights — led to 1st Constitutional Amendment.",
        ],
        [
            "Golak Nath v. State of Punjab (1967)",
            "Parliament cannot amend Fundamental Rights — later overruled.",
        ],
        [
            "Kesavananda Bharati v. State of Kerala (1973)",
            "Basic Structure Doctrine — Parliament cannot destroy basic structure; Fundamental Rights can be amended.",
        ],
        [
            "Indira Gandhi v. Raj Narain (1975)",
            "Free and fair election is part of basic structure.",
        ],
        [
            "ADM Jabalpur v. Shivakant Shukla (1976)",
            "During emergency, even Art. 21 can be suspended — this was overruled later.",
        ],
        [
            "Maneka Gandhi v. Union of India (1978)",
            "Art. 21 procedure must be fair, just and reasonable — expanded interpretation; linked Art. 14, 19, 21.",
        ],
        [
            "Minerva Mills v. Union of India (1980)",
            "Parliament cannot abridge basic structure; harmony between FRs and DPSPs.",
        ],
        [
            "S.R. Bommai v. Union of India (1994)",
            "President's Rule under Art. 356 is subject to judicial review; floor test must be held.",
        ],
        [
            "Vishaka v. State of Rajasthan (1997)",
            "Laid down guidelines against sexual harassment at workplace (derived from Art. 21).",
        ],
        [
            "K.S. Puttaswamy v. Union of India (2017)",
            "Right to Privacy is a fundamental right under Art. 21 (9-judge bench).",
        ],
        [
            "Navtej Singh Johar v. Union of India (2018)",
            "Section 377 IPC decriminalised; consensual same-sex relations not criminal.",
        ],
    ],
)

pn.chap_box("PYQ Model Answers — 3/4-Mark Questions")

pn.section("(3 Marks) What do you mean by Universal Adult Franchise?")
pn.highlight(
    "<b>Universal Adult Franchise:</b> It means the right of every adult citizen of India to vote "
    "in elections, irrespective of caste, religion, sex, literacy, economic status, or place of birth. "
    "In India, every citizen who is 18 years of age or above has the right to vote (Art. 326). "
    "The voting age was reduced from 21 to 18 by the 61st Constitutional Amendment Act, 1988. "
    "It ensures that every person has an equal say in electing representatives, making democracy truly representative."
)

pn.section("(3 Marks) What do you mean by Public Account of India?")
pn.highlight(
    "<b>Public Account of India (Art. 266(2)):</b> All other public moneys received by or on behalf "
    "of the Government of India, OTHER than those credited to the Consolidated Fund of India, "
    "are part of the Public Account. "
    "It includes Provident Funds, deposits, advances, savings bank deposits, departmental advances. "
    "Parliament's authorisation is NOT needed for payments from the Public Account (unlike Consolidated Fund). "
    "The Comptroller and Auditor General (CAG) audits the Public Account."
)

pn.section("(4 Marks) Judicial Review")
pn.highlight(
    "<b>Judicial Review:</b> The power of the Supreme Court (and High Courts) to examine the constitutionality "
    "of laws enacted by the Legislature and actions taken by the Executive, and to declare them void "
    "if they are found to be unconstitutional (ultra vires). "
    "It is an implied power derived from the provisions of the Constitution (especially Arts. 13, 32, 226). "
    "India follows a 'limited' form of judicial review (as opposed to the broad power of review in the USA). "
    "The Constitution is supreme — any law inconsistent with it is void (Art. 13). "
    "Landmark cases: Marbury v. Madison (USA, 1803 — origin), Kesavananda Bharati (India, 1973)."
)

pn.section("(4 Marks) President's Rule / Governor's Rule")
pn.highlight(
    "<b>President's Rule (Art. 356):</b> When the President, acting on the Governor's report "
    "or otherwise, is satisfied that the government of a state cannot be carried on in accordance "
    "with the provisions of the Constitution, the President can assume to himself the functions of "
    "the State Government (except the High Court). "
    "The State Legislature is dissolved or kept in suspended animation. "
    "Parliament makes laws for the state during this period. "
    "Must be approved by both Houses of Parliament within 2 months. "
    "Maximum duration: 3 years (approved in 6-month installments). "
    "S.R. Bommai Case (1994) — imposition is subject to judicial review."
)

pn.section("(4 Marks) Discuss Centre-State Legislative Relations")
pn.highlight(
    "<b>Centre-State Legislative Relations:</b> "
    "Arts. 245–255 deal with distribution of legislative powers. "
    "(1) Union List (List I) — 100 subjects — Parliament has exclusive power. "
    "(2) State List (List II) — 61 subjects — State Legislatures have exclusive power normally. "
    "(3) Concurrent List (List III) — 52 subjects — both can legislate; Parliamentary law prevails in conflict. "
    "(4) Residuary Powers — with Parliament (Art. 248). "
    "<b>Parliament can legislate on State List in 5 extraordinary situations:</b> "
    "(a) National interest — Rajya Sabha resolution by 2/3 majority (Art. 249). "
    "(b) During National Emergency (Art. 250). "
    "(c) Consent of two or more states (Art. 252). "
    "(d) International agreements (Art. 253). "
    "(e) Failure of constitutional machinery — President's Rule (Art. 356)."
)

pn.chap_box("Quick Revision — Key Points for Exam")

pn.revision_card(
    "CO1 — Constitution & History",
    [
        "3 methods of Constitutional Amendment: Simple majority, Special majority (Art. 368), Special majority + State ratification.",
        "Basic Structure Doctrine: Kesavananda Bharati (1973) — Parliament cannot destroy basic structure.",
        "Constitution enacted on 26 Nov 1949; enforced 26 Jan 1950 (Republic Day).",
        "Drafting Committee Chairman: Dr. B.R. Ambedkar. Constituent Assembly President: Dr. Rajendra Prasad.",
        "India is Quasi-federal: Union list, State list, Concurrent list + residuary with Centre.",
    ],
)

pn.revision_card(
    "CO2 — Fundamental Duties & DPSP",
    [
        "11 Fundamental Duties under Art. 51A. Added by 42nd Amendment (1976). 11th added by 86th Amendment (2002).",
        "DPSPs are non-justiciable (Part IV, Art. 36–51). Classified as: Socialistic, Gandhian, Liberal-Intellectual.",
        "Swaran Singh Committee (1976) — recommended Fundamental Duties.",
        "Verma Committee (1999) — recommended operationalization of Fundamental Duties.",
        "Harmony between FRs and DPSPs: Minerva Mills Case (1980).",
    ],
)

pn.revision_card(
    "CO3 — Federal Structure & President",
    [
        "Federal features: Written constitution, Dual polity, Division of powers, Supreme Constitution, Rigid constitution.",
        "Non-federal features: Strong Centre, Single citizenship, Governor appointed by President, Integrated judiciary.",
        "President's election: Electoral College = elected MPs + elected MLAs. Single Transferable Vote.",
        "President's veto: Absolute, Suspensive, Pocket veto.",
        "Parliamentary form: Nominal head (President) + Real executive (PM + Cabinet). Collective responsibility to Lok Sabha.",
    ],
)

pn.revision_card(
    "CO4 — Emergency & Local Self Government",
    [
        "National Emergency (Art. 352): War/External Aggression/Armed Rebellion. Art. 19 suspended. Never Art. 20 & 21.",
        "President's Rule (Art. 356): Failure of constitutional machinery. Max 3 years. S.R. Bommai case.",
        "Financial Emergency (Art. 360): Never proclaimed in India. Salaries of judges can be reduced.",
        "73rd Amendment (1992): Constitutional status to Panchayats. Part IX, Art. 243. 11th Schedule. 29 subjects.",
        "Balwant Rai Mehta Committee (1957): 3-tier Panchayati Raj — Village, Block, District.",
    ],
)

pn.revision_card(
    "CO5 — Fundamental Rights",
    [
        "6 Fundamental Rights (Part III, Art. 12–35). Right to Property removed by 44th Amendment — now legal right (Art. 300A).",
        "Art. 14: Equality before law + Equal protection. Reasonable classification allowed. Not arbitrary classification.",
        "Art. 19: 6 freedoms for CITIZENS only. Subject to reasonable restrictions.",
        "Art. 21: Right to Life & Personal Liberty. Expanded by Maneka Gandhi (1978). Includes right to privacy (Puttaswamy, 2017).",
        "Art. 32: 5 writs — Habeas Corpus, Mandamus, Prohibition, Certiorari, Quo Warranto. 'Heart and Soul' — Ambedkar.",
    ],
)

pn.section("Flashcards — Most Asked 3-Mark Answers")
pn.flashcard(
    "What is constitutionalism?",
    "The political principle that government authority is derived from and limited by a fundamental law (Constitution). "
    "Emphasises: limited government, rule of law, separation of powers, and protection of fundamental rights.",
)
pn.flashcard(
    "What are the 3 organs of Indian Government?",
    "1. Legislature (Parliament — Lok Sabha + Rajya Sabha): makes laws. "
    "2. Executive (President + Council of Ministers): implements laws. "
    "3. Judiciary (Supreme Court + High Courts): interprets laws and settles disputes.",
)
pn.flashcard(
    "What is Judicial Review?",
    "Power of SC/HC to examine constitutionality of laws and executive actions. "
    "Void if inconsistent with Constitution (Art. 13). Key cases: Marbury v. Madison (USA), Kesavananda Bharati (India, 1973).",
)
pn.flashcard(
    "3 types of Emergency in India",
    "1. National Emergency (Art. 352) — War/External Aggression/Armed Rebellion. "
    "2. President's Rule (Art. 356) — Failure of Constitutional Machinery in State. "
    "3. Financial Emergency (Art. 360) — Threat to Financial Stability. Only #3 has never been proclaimed.",
)
pn.flashcard(
    "What is Panchayati Raj?",
    "System of rural local self-government in India. Constitutional status given by 73rd Amendment (1992). "
    "3-tier: Village (Gram Panchayat), Block (Panchayat Samiti), District (Zila Parishad). "
    "Reservation for SC/ST and minimum 1/3 for women.",
)
pn.flashcard(
    "Article 21 — Key Cases",
    "Maneka Gandhi v. UoI (1978) — procedure must be fair, just, reasonable. "
    "K.S. Puttaswamy v. UoI (2017) — Right to Privacy is a fundamental right. "
    "Olga Tellis v. BMC (1985) — Right to Livelihood.",
)
pn.flashcard(
    "Difference: Hard Link vs Soft Link (Analogy in Constitution)",
    "Not applicable to Constitution. But for FRs vs DPSPs: "
    "FRs = justiciable (hard enforcement). DPSPs = non-justiciable (soft guidance). "
    "Both are essential — Minerva Mills (1980) held they are complementary.",
)

# =============================================================================
#  EXAM STRATEGY SECTION
# =============================================================================
pn.br()
pn.chap_box("Exam Strategy & Unit-wise High-Frequency Questions")

pn.section("Mark Distribution Analysis from PYQs (2022–2025)")
pn.info_table(
    ["Question Pattern", "Topic (appears every year)", "Marks"],
    [
        [
            "Q1(a/b/c) + Q1(d/e)",
            "Constitution meaning, Salient features, Fundamental Rights overview, Historical perspective, Preamble",
            "3+4+4+10",
        ],
        [
            "Q2(a/b/c) + Q2(d/e)",
            "Parliament structure, Government of India Acts, Constituent Assembly, Federal system, Rajya Sabha vs Lok Sabha",
            "3+4+4+10",
        ],
        [
            "Q3(a/b/c) + Q3(d/e)",
            "NITI Aayog, Cabinet Secretariat, Centre-State relations, Attorney General, FRs and DPSPs",
            "3+4+4+10",
        ],
        [
            "Q4(a/b/c) + Q4(d/e)",
            "Public Account, Governor's Rule, Cabinet vs CoM, Emergency provisions, Local Self Government",
            "3+4+4+10",
        ],
        [
            "Q5(a/b/c) + Q5(d/e)",
            "Panchayati Raj, State Finance Commission, Accountability in democracy, Financial Emergency, Fundamental Duties",
            "3+4+4+10",
        ],
    ],
)

pn.section("Top 10 Most Important Topics (attempt ALL of these)")
pn.bullet(
    [
        "<b>1.</b> Salient features of the Indian Constitution — write 10+ features for 10-mark question.",
        "<b>2.</b> Fundamental Rights — all 6 categories with Article numbers (Art. 14–32).",
        "<b>3.</b> Directive Principles of State Policy — classification + importance + comparison with FRs.",
        "<b>4.</b> Emergency Provisions — all 3 types, comparison table, instances in India.",
        "<b>5.</b> Article 19 — all 6 freedoms + permissible restrictions (with grounds for each).",
        "<b>6.</b> Article 21 — scope, landmark cases (Maneka Gandhi, Puttaswamy), expanded rights.",
        "<b>7.</b> Distribution of powers — Union List, State List, Concurrent List with examples.",
        "<b>8.</b> Panchayati Raj — 73rd Amendment, 3-tier structure, Balwant Rai Mehta Committee.",
        "<b>9.</b> Amendment procedure — 3 methods, Article 368, Basic Structure Doctrine.",
        "<b>10.</b> Five Writs under Article 32 — with meanings, purpose, and examples.",
    ]
)

pn.exam(
    "EXAM TIP: For 10-mark questions, always write: (1) Introduction/Definition, "
    "(2) Historical background or constitutional provision, (3) Detailed explanation with sub-points/table, "
    "(4) Landmark Supreme Court cases where applicable, (5) Brief critical analysis or conclusion. "
    "For 3-mark questions: Direct definition + 2 key points. For 4-mark: Definition + classification/comparison."
)

# =============================================================================
#  BUILD DOCUMENT
# =============================================================================
pn.build_doc("IndianConstitution_IT410_Notes.pdf")

print("Generated: IndianConstitution_IT410_Notes.pdf")
