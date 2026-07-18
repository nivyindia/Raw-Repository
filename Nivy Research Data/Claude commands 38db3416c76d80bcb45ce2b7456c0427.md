# Claude commands

Bilkul. Main recommend karunga ki **ek hi mega prompt use na karein**. Uske badle **specialized commands** banayein. Ye zyada accurate, reusable aur Claude ke context window ke hisaab se practical hoga.

# 🏛 MASTER COMMAND 0 – SYSTEM ROLE (Har Chat ki Shuruaat)

Is command ko har naye Claude project/chat ki shuruaat me use karein.

```
You are my Chief Knowledge Architect, Chief Operating Officer, Enterprise Information Architect, Business Process Consultant, AI Systems Architect, and Notion Operating System Designer.

Your role is not to summarize documents.

Your role is to continuously build and improve the Nivy Empires Company Operating System.

Treat every document as a company asset.

Never lose information.
Never invent information.
Never delete information unless it is an exact duplicate.
Always preserve the original meaning.

Whenever possible:

• Split large documents into reusable components.
• Extract SOPs.
• Extract Tasks.
• Extract Workflows.
• Extract Templates.
• Extract Policies.
• Extract Checklists.
• Extract Knowledge.
• Extract Best Practices.
• Extract Prompts.
• Extract Metrics.
• Extract Resources.

Everything should fit into the Company OS architecture.

Always optimize for:

Scalability
Searchability
Automation
AI Readiness
Crowdsourcing
Global Operations
Long-term Maintainability

Whenever uncertain, ask for clarification instead of guessing.
```

---

# 📂 COMMAND 1 – CLASSIFY DOCUMENT

Use for every raw document.

```
Analyze this document.

Do NOT summarize.

Instead classify it into the Nivy Empires Company OS.

Return:

Primary Category

Secondary Category

Department

Business

Service

Workflow

Process

Project

Task

SOP

Knowledge

Resource

Asset

Country

Priority

Status

Owner

Recommended Folder

Recommended Database

Suggested Parent Page

Suggested Child Pages

Related Documents

Reasoning for classification
```

---

# 🏷 COMMAND 2 – GENERATE METADATA

```
Generate enterprise metadata.

Create:

Unique ID

Title

Short Description

Version

Keywords

Tags

Aliases

Difficulty

Automation %

Crowdsourcing %

Estimated Time

Estimated Cost

Department

Workflow

Project

Owner

Reviewer

Quality Score

Related SOPs

Related Tasks

Related Assets

Related Templates

Search Keywords

Internal Search Terms

Do not change the original content.
```

---

# ✂ COMMAND 3 – SPLIT LARGE DOCUMENT

```
Analyze this document.

If it contains multiple topics,

split it into multiple logical pages.

Keep every piece of information.

Never lose anything.

Return:

Page 1

Page 2

Page 3

...

with suggested titles.

Also recommend where each page belongs inside Company OS.
```

---

# 🔄 COMMAND 4 – REMOVE DUPLICATES

```
Compare these documents.

Find duplicate information.

Keep the best version.

Merge only exact duplicates.

Keep all unique information.

Generate:

Master Version

Reference Links

Duplicate List

Missing Information

Recommended Archive
```

---

# 📋 COMMAND 5 – EXTRACT TASKS

```
Read the document.

Extract every actionable task.

For every task generate:

Task Name

Department

Workflow

Priority

Owner Type

(AI / Student / Freelancer / Partner / Core Team)

Estimated Time

Estimated Cost

Quality Checklist

Related SOP

Automation Potential

Crowdsourcing Potential

Dependencies

KPI
```

---

# 📑 COMMAND 6 – EXTRACT SOPs

```
Extract every SOP.

Create:

Purpose

Prerequisites

Steps

Inputs

Outputs

Quality Checklist

Common Mistakes

Automation Ideas

Training Needed

Related Tasks

Related Resources
```

---

# 🧠 COMMAND 7 – EXTRACT KNOWLEDGE

```
Extract all reusable knowledge.

Including:

Best Practices

Lessons Learned

Mistakes

Warnings

Tips

Frameworks

Decision Logic

FAQs

Research

Store everything in Company Brain.
```

---

# 🤖 COMMAND 8 – AI & AUTOMATION REVIEW

```
Review the document.

Identify:

What AI can do

What can be automated

What requires humans

What can be crowdsourced

Automation Priority

Recommended AI Tools

Suggested AI Agents

Potential Cost Savings
```

---

# 👥 COMMAND 9 – RESOURCE ALLOCATION

```
Analyze every task.

Recommend the best resource.

Choose from:

AI

Automation

Student

Intern

VA

Freelancer

Agency

Partner

Consultant

Core Team

Explain why.
```

---

# 🔗 COMMAND 10 – BUILD RELATIONS

```
Connect this document with Company OS.

Generate:

Related Tasks

Related SOPs

Related Workflows

Related Projects

Related Clients

Related Assets

Related Templates

Related Knowledge

Related Automation

Related Departments

Related KPIs
```

---

# 📊 COMMAND 11 – QUALITY REVIEW

```
Audit this document.

Check:

Missing Information

Duplicate Information

Broken Logic

Poor Formatting

Missing SOPs

Missing Tasks

Missing Metadata

Missing Relations

Missing Keywords

Suggest improvements.
```

---

# 📦 COMMAND 12 – FINAL IMPORT FORMAT

```
Prepare this document for Notion.

Return:

Folder

Database

Page Title

Metadata

Properties

Relations

Tags

Keywords

Suggested Icon

Suggested Cover

Backlinks

Child Pages

Everything should be ready for direct import.
```

---

# 🚀 Recommended Workflow

Is order me commands chalaiye:

```
0. System Role (once per chat)
        ↓
1. Classify Document
        ↓
2. Generate Metadata
        ↓
3. Split Document (if needed)
        ↓
4. Remove Duplicates (batch)
        ↓
5. Extract Tasks
        ↓
6. Extract SOPs
        ↓
7. Extract Knowledge
        ↓
8. AI & Automation Review
        ↓
9. Resource Allocation
        ↓
10. Build Relations
        ↓
11. Quality Review
        ↓
12. Final Notion Import
```

## Ek practical suggestion

Aapke paas **1000+ documents** hain, isliye manually ye 12 commands har document par chalana bahut time lega. Main is workflow ko aur optimize karunga:

- **Batch Command A:** Commands **1–4** (classification, metadata, splitting, deduplication)
- **Batch Command B:** Commands **5–10** (tasks, SOPs, knowledge, automation, resources, relations)
- **Batch Command C:** Commands **11–12** (quality review + Notion-ready output)

Is tarah har document sirf **3 processing stages** se guzrega, consistency bhi bani rahegi aur migration ka kaam kaafi tezi se hoga.