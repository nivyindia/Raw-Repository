# Agent Memory, RAG, Context Engineering & Knowledge Systems Catalog
Research date: 2026-09-19

## Why this file exists

The earlier company catalog covered agents, workflows and channels, but it did **not** sufficiently separate the information/memory layer. That is a major omission.

For Nivy Company OS, "memory" is not one feature. We need to discover reusable systems for:

**RAG → Agentic RAG → GraphRAG → Multimodal RAG → Long-term memory → Short-term/session memory → episodic memory → semantic memory → procedural memory → working memory → user/profile memory → organizational/company memory → temporal memory → reasoning memory → shared multi-agent memory → cross-agent memory → memory consolidation → reflection/dreaming → forgetting/decay → contradiction resolution → provenance → knowledge graphs → context engineering → retrieval/evaluation → memory governance.**

This catalog is a discovery library, not an adoption recommendation.

---

## 1. Major agent-memory platforms / frameworks

| ID | System | Primary type | Key coverage | Link |
|---|---|---|---|---|
| MEM01 | Mem0 | Long-term agent memory | Fact extraction, persistent memory, retrieval, personalization, framework integrations; OSS + managed platform | https://github.com/mem0ai/mem0 |
| MEM02 | Zep | Managed context/memory platform | Agent memory, context engineering, temporal/context graphs, retrieval and context assembly | https://github.com/getzep/zep |
| MEM03 | Graphiti | Temporal context graph | Incremental graph memory, temporal facts, provenance, hybrid semantic/keyword/graph retrieval, MCP | https://github.com/getzep/graphiti |
| MEM04 | Letta (MemGPT lineage) | Stateful agent runtime | Hierarchical memory, core memory, archival/external memory, self-editing memory, multi-agent shared memory | https://github.com/letta-ai/letta |
| MEM05 | Cognee | Open-source AI memory | Knowledge graph + vector retrieval + session cache; persistent memory; self-host/cloud | https://github.com/topoteretes/cognee |
| MEM06 | LangMem | Agent memory toolkit | Extract/store/search memories, prompt optimization, long-term memory, LangGraph storage integration | https://github.com/langchain-ai/langmem |
| MEM07 | Supermemory | Memory + context engine | User profiles, hybrid RAG+memory, connectors, multimodal ingestion, automatic updates/forgetting, MCP/plugins | https://github.com/supermemoryai/supermemory |
| MEM08 | Memobase | User-profile memory | Long-term user profiles, chat memory, profile-oriented personalization | https://github.com/memodb-io/memobase |
| MEM09 | Neo4j Agent Memory | Graph-native agent memory | Short-term, long-term and reasoning memory; entity resolution; graph + vector/text retrieval; MCP | https://github.com/neo4j-labs/agent-memory |
| MEM10 | Redis Agent Memory | Session + long-term memory | TTL session state, extracted facts, vector retrieval, background promotion from session to long-term memory | https://github.com/redis/agent-memory-server |
| MEM11 | OpenJiuwen / JiuwenMemory | AutoGenetic memory | Extraction, storage, retrieval, migration; cross-platform/self-evolving memory architecture | https://github.com/openJiuwen-ai/agent-memory |
| MEM12 | agent-memory (Postgres/pgvector) | Persistent memory server | Thoughts + documents, semantic recall, freshness/quality ranking, MCP | https://github.com/rzem-ai/agent-memory |
| MEM13 | agent-memory (SQLite/HNSW) | Embedded memory | Working → conversation → long-term; vector search; fact extraction; local-first | https://github.com/ivanzwb/agent-memory |
| MEM14 | agent-memory (filesystem) | File-native memory | Markdown source of truth, BM25/vector fusion, links/graph, sleep-time consolidation, no API key | https://github.com/tigerless-labs/agent-memory |
| MEM15 | agent-memory (plugin model) | Automatic memory extraction | Background extraction/classification into identity, knowledge, preferences, lessons and recent memory | https://github.com/Jannhsu/agent-memory |
| MEM16 | Agent Memory Kit | Structured memory pattern | Working + episodic + semantic + procedural + feedback memory | https://github.com/reflectt/agent-memory-kit |
| MEM17 | Mnemosyne | Advanced memory engine | Temporal relevance, multi-signal retrieval, proactive recall, procedural memory, graph memory | https://github.com/28naem-del/mnemosyne |
| MEM18 | Awesome Agent Memory | Discovery index | Memory APIs, OSS engines, MCP servers, benchmarks and research | https://github.com/mnemoverse/awesome-agent-memory |
| MEM19 | Awesome AI Memory | 2026 research/project index | Agent-memory projects, benchmarks, papers and taxonomy | https://github.com/fomos-openai/awesome-ai-memory |
| MEM20 | Agent Memory Research | Research corpus | 1,000+ papers covering architecture, consolidation, forgetting, security, benchmarks and efficiency | https://github.com/tobias-weiss-ai-xr/agent-memory-research |

Current research indexes show the field now spans managed memory, OSS frameworks, MCP memory servers, benchmarks and papers rather than one single "memory" architecture. citeturn0search10turn0search11turn0search6

---

## 2. Memory types Nivy must support

| Type | Meaning | Company OS use |
|---|---|---|
| Working memory | Current task state | What an agent is doing now |
| Context memory | Current assembled context | Prompt/context window management |
| Session memory | Current conversation/task session | Continue a live task |
| Short-term memory | Recent interactions | Recent customer/employee events |
| Long-term memory | Durable facts across sessions | Company/user/project history |
| Episodic memory | What happened | Calls, meetings, incidents, actions |
| Semantic memory | What is known | Policies, facts, products, customers |
| Procedural memory | How to do something | SOPs, skills, workflows |
| Preference memory | What a person/company prefers | Communication, pricing, workflow preferences |
| Identity memory | Who/what an entity is | Person, customer, employee, vendor, agent |
| Profile memory | Consolidated entity profile | Customer/employee/company profile |
| Organizational memory | Institutional knowledge | Nivy-wide knowledge |
| Project memory | Project-specific state/history | Client/project context |
| Customer memory | Customer history | Interactions, needs, commitments |
| Decision memory | Why a decision was made | Strategy and governance |
| Reasoning memory | Prior reasoning/tool-use outcomes | Reuse successful approaches |
| Experience memory | Lessons from outcomes | Improve agent behavior |
| Feedback memory | Human/automated feedback | Learning from corrections |
| Temporal memory | Facts with validity periods | "What was true on date X?" |
| Relational/graph memory | Entities + relationships | Company/people/product networks |
| Multimodal memory | Text + image + audio + video | Calls, documents, media |
| Shared memory | Multiple agents access same memory | Department/team memory |
| Federated memory | Multiple memory stores | Company + client + personal scopes |
| External/archival memory | Deep store outside active context | Large historical records |
| Cache memory | Fast temporary retrieval | Reduce latency/cost |
| Scratchpad | Ephemeral reasoning state | Current execution |
| Skill/procedural memory | Reusable process knowledge | Agent skills |
| Failure memory | What failed and why | Prevent repeated mistakes |
| Negative memory | What should NOT be done | Guardrails and exclusions |
| Memory of tools | Tool behavior and outcomes | Tool selection and reliability |
| Memory of sources | Provenance/citations | Auditability |
| Memory of contradictions | Conflicting facts | Reconciliation |
| Expiring memory | Facts with TTL | Temporary tasks/events |
| Consent/governed memory | Permission-scoped information | Privacy/RBAC |

Letta's current architecture explicitly separates always-in-context core memory from external memory, with shared memory repositories possible between agents. citeturn3search3turn3search11

---

## 3. RAG family

| ID | System/pattern | Coverage | Link |
|---|---|---|---|
| RAG01 | Basic Vector RAG | Embeddings + vector retrieval | https://github.com/pgvector/pgvector |
| RAG02 | Hybrid RAG | Vector + keyword/BM25 | https://github.com/qdrant/qdrant |
| RAG03 | Agentic RAG | Agent plans retrieval, uses tools, evaluates results | https://github.com/aws-samples/samples-for-rag-solutions |
| RAG04 | Self-corrective RAG | Retrieval/answer critique and iterative correction | https://github.com/aws-samples/samples-for-rag-solutions |
| RAG05 | Corrective RAG / CRAG | Evaluate retrieval quality and correct search | https://github.com/HKUDS/Corrective-RAG |
| RAG06 | Adaptive RAG | Dynamically choose retrieval strategy | https://github.com/langchain-ai/langgraph |
| RAG07 | GraphRAG | Knowledge graph + retrieval | https://github.com/microsoft/graphrag |
| RAG08 | GraphRAG core | Governed KG extraction, provenance and agent-callable tools | https://github.com/cdel1/graphrag-core |
| RAG09 | MemGraphRAG | Memory-enhanced multi-agent GraphRAG | https://github.com/XMUDeepLIT/MemGraphRAG |
| RAG10 | Multimodal RAG | Text, images, tables, audio/video and OCR | https://github.com/Kasshern/multimodal-rag-agent |
| RAG11 | Multimodal RAG system | Agentic retrieval + entity graph + hybrid vector | https://github.com/KnowledgeHub-git/multimodal-rag-system |
| RAG12 | Microsoft GraphRAG | Hierarchical graph communities + summaries + retrieval | https://github.com/microsoft/graphrag |
| RAG13 | Neo4j GraphRAG provider | Vector + fulltext + graph traversal for agents | https://github.com/MicrosoftDocs/semantic-kernel-docs/blob/main/agent-framework/integrations/neo4j-graphrag.md |
| RAG14 | Domain-agnostic GraphRAG | LLM extraction + provenance-native graph + tools | https://github.com/cdel1/graphrag-core |
| RAG15 | GraphRAG Agent | Entity/relation extraction + k-hop retrieval + citations | https://github.com/axon011/graphrag-agent |

Microsoft's GraphRAG pipeline extracts graphs and claims, detects communities, generates reports and embeds chunks/entities/reports; Neo4j's Agent Framework integration adds vector, full-text and graph traversal retrieval. citeturn1search16turn1search6

The MemGraphRAG project specifically combines unstructured passages, extracted facts and abstract schemas into a multi-layer memory for multi-agent RAG. citeturn0search12

---

## 4. Retrieval techniques that must be tracked separately

Do not treat "RAG" as one technique. The retrieval registry should include:

- Dense/vector retrieval
- Sparse/BM25 retrieval
- Hybrid retrieval
- Metadata filtering
- Semantic filtering
- Query rewriting
- Query expansion
- Multi-query retrieval
- HyDE
- Step-back retrieval
- Decomposition retrieval
- Recursive retrieval
- Parent-child retrieval
- Hierarchical retrieval
- Sentence-window retrieval
- Contextual retrieval
- Graph traversal
- Multi-hop retrieval
- Temporal retrieval
- Entity retrieval
- Relationship retrieval
- SQL retrieval
- API/tool retrieval
- Web retrieval
- Federated retrieval
- Cross-encoder reranking
- LLM reranking
- Diversity reranking
- MMR
- Reciprocal Rank Fusion
- Citation-aware retrieval
- Provenance-aware retrieval
- Permission-aware retrieval
- Personalized retrieval
- Intent-aware retrieval
- Agentic search
- Deep research retrieval
- Cache-aware retrieval

---

## 5. Context engineering

This is separate from RAG.

| Capability | What it solves |
|---|---|
| Context selection | What information enters the prompt |
| Context compression | Reduce tokens while retaining useful information |
| Context ranking | Put the most useful evidence first |
| Context assembly | Combine memory + RAG + tools + task state |
| Context isolation | Prevent unrelated client/department data leakage |
| Context budgeting | Control token/cost limits |
| Context caching | Reuse stable context |
| Context routing | Select the correct knowledge source |
| Context versioning | Know which knowledge/policy version was used |
| Context provenance | Trace every fact to source |
| Context freshness | Prefer current information |
| Context expiration | Remove stale information |
| Context conflict resolution | Resolve contradictory sources |
| Context personalization | Per-user/per-agent context |
| Context hierarchy | Global → company → department → project → customer → task |
| Context permissions | RBAC/ABAC/tenant-aware retrieval |

Supermemory explicitly combines memory, RAG, user profiles, connectors and multimodal extraction into a single context layer. citeturn3search8

---

## 6. Knowledge graph / context graph layer

Nivy should distinguish:

**Knowledge Graph**
- entities
- relationships
- ontology
- taxonomy
- provenance
- graph traversal

**Context Graph**
- temporal facts
- episodes
- validity windows
- changing relationships
- personalized context

Graphiti is specifically designed around temporal context graphs with provenance, incremental updates and hybrid semantic/keyword/graph retrieval. citeturn2search3

Relevant systems:
- Graphiti — https://github.com/getzep/graphiti
- Zep — https://github.com/getzep/zep
- Neo4j Agent Memory — https://github.com/neo4j-labs/agent-memory
- Cognee — https://github.com/topoteretes/cognee
- Microsoft GraphRAG — https://github.com/microsoft/graphrag
- graphrag-core — https://github.com/cdel1/graphrag-core
- MemGraphRAG — https://github.com/XMUDeepLIT/MemGraphRAG

Neo4j Agent Memory includes short-term, long-term and reasoning memory, entity resolution, graph/vector/text retrieval, MCP tools and integrations with several agent frameworks. citeturn0search7

---

## 7. Multi-agent / shared memory

This must be a first-class capability.

### Required patterns

1. Agent-private memory
2. Department shared memory
3. Company-wide memory
4. Customer-scoped memory
5. Project-scoped memory
6. Team memory
7. Cross-agent memory
8. Cross-session memory
9. Cross-model memory
10. Cross-runtime memory
11. Human + AI shared memory
12. Federated memory
13. Memory access through MCP
14. Memory access through APIs
15. Memory access through filesystem/git
16. Memory synchronization
17. Memory conflict resolution
18. Memory ownership
19. Memory permissions
20. Memory audit trail.

Letta's MemFS supports shared memory repositories that multiple agents can attach to, while Cognee's integrations expose permanent knowledge-graph memory plus a session cache that can be promoted into durable memory. citeturn3search3turn3search10

---

## 8. Memory lifecycle / "AI that learns"

The memory engine should have an explicit lifecycle:

**Observe → Extract → Classify → Store → Link → Retrieve → Apply → Evaluate → Consolidate → Update → Supersede → Forget/Expire → Audit**

Systems to study for these patterns:
- Letta dreaming / memory doctor
- LangMem
- Mem0
- Cognee
- Supermemory
- Graphiti
- Neo4j Agent Memory
- JiuwenMemory
- filesystem agent-memory systems.

Letta currently documents background "dreaming" that reviews recent conversations, consolidates useful lessons and updates memory without interrupting active work. citeturn3search13

---

## 9. Memory consolidation / reflection / self-improvement

Separate reusable patterns:

- Reflection memory
- Sleep-time processing
- Conversation summarization
- Fact extraction
- Memory deduplication
- Entity resolution
- Contradiction detection
- Fact supersession
- Importance scoring
- Recency scoring
- Freshness scoring
- Relevance scoring
- Decay
- Forgetting
- Memory pruning
- Memory compression
- Experience replay
- Failure learning
- Skill generation
- Prompt optimization
- Policy improvement.

LangMem explicitly supports extracting information from interactions, optimizing agent behavior through prompt refinement and maintaining long-term memory. citeturn2search11

---

## 10. File / Git-based memory

This is especially relevant to Nivy because company knowledge already lives heavily in GitHub/Markdown.

Systems:
- Letta MemFS — https://github.com/letta-ai/letta
- tigerless agent-memory — https://github.com/tigerless-labs/agent-memory
- Jannhsu agent-memory — https://github.com/Jannhsu/agent-memory
- Agent Memory Kit — https://github.com/reflectt/agent-memory-kit

Filesystem memory is not a primitive fallback only. It can provide:
- human-readable memory
- Git versioning
- reviewable changes
- portable data
- branch-based experimentation
- audit trail
- easy backup
- no vendor lock-in.

The tigerless system combines a filesystem source of truth with ranked retrieval, graph links and sleep-time consolidation. citeturn0search2

---

## 11. Database/vector/graph substrates

The library must separately track storage technologies:

### Vector/search
- pgvector
- Qdrant
- Weaviate
- Milvus
- Pinecone
- Chroma
- Elasticsearch/OpenSearch
- Redis Vector

### Graph
- Neo4j
- FalkorDB
- Kuzu
- Memgraph
- Amazon Neptune

### Relational/document
- PostgreSQL
- SQLite
- MongoDB
- Redis

### File/object
- Markdown/Git
- S3-compatible object storage
- local filesystem

The same memory architecture can often be implemented on different substrates, so **memory architecture ≠ database choice**.

---

## 12. Multimodal memory

Nivy must not limit memory to text.

Required ingestion:
- PDF
- DOCX
- XLSX
- PPTX
- Markdown
- HTML
- web pages
- screenshots
- scanned documents
- images
- diagrams
- tables
- charts
- audio
- meetings
- phone calls
- video
- code repositories
- Git history
- emails
- CRM records
- calendar events
- tickets
- social posts
- customer messages.

Multimodal agentic RAG implementations already combine PDF/images/OCR/tables/Markdown/HTML/code, hybrid retrieval, reranking, planning, self-reflection and evaluation. citeturn1search1

---

## 13. Memory evaluation / benchmarks

Do not deploy a memory system based only on a README.

Track:
- LongMemEval
- LoCoMo
- MemoryBench
- MemoryAgentBench
- MemGym
- GroupMemBench
- EvoMemBench
- ConvoMem
- retrieval precision/recall
- temporal correctness
- contradiction handling
- forgetting accuracy
- personalization accuracy
- cross-session recall
- cost per memory operation
- latency
- context reduction
- privacy leakage
- tenant isolation
- provenance accuracy.

The 2026 memory research indexes now track more than 1,000 papers and include dedicated benchmarks for long-horizon memory, consolidation, security and efficiency. citeturn0search6turn1search15

---

## 14. Memory governance / security

This is critical for a company-wide AI OS.

Every memory record should eventually have:

| Field | Purpose |
|---|---|
| tenant_id | Company/client isolation |
| owner | Who owns the memory |
| scope | Personal/team/department/company/customer |
| sensitivity | Public/internal/confidential/restricted |
| source | Where it came from |
| source_timestamp | When it was observed |
| valid_from | When fact became true |
| valid_until | When fact stopped being true |
| confidence | Confidence level |
| provenance | Evidence chain |
| permissions | Who can retrieve it |
| retention | How long to retain |
| expiry | Automatic expiration |
| version | Memory version |
| supersedes | Previous fact |
| contradicts | Conflicting fact |
| audit_id | Audit trace |
| consent | Required consent status |
| deletion_status | Deletion/forget request state |

Never put every company record into one unrestricted vector database.

---

## 15. Nivy Company OS target memory architecture

Recommended logical layers to investigate before implementation:

**Layer 0 — Live context**
- current conversation
- current task
- active tools
- scratchpad

**Layer 1 — Session**
- current session events
- temporary decisions
- current task state

**Layer 2 — Agent memory**
- agent identity
- preferences
- learned procedures
- failures
- experience

**Layer 3 — Entity memory**
- person
- customer
- employee
- vendor
- company
- product

**Layer 4 — Project memory**
- project facts
- decisions
- documents
- milestones
- conversations

**Layer 5 — Department memory**
- SOPs
- KPIs
- policies
- domain knowledge

**Layer 6 — Company memory**
- strategy
- organization
- governance
- institutional knowledge
- company decisions

**Layer 7 — Knowledge/RAG**
- documents
- web research
- external knowledge
- structured databases

**Layer 8 — Graph/context**
- relationships
- temporal facts
- provenance
- dependencies

**Layer 9 — Archive**
- historical records
- superseded knowledge
- audit evidence

**Layer 10 — Governance**
- permissions
- retention
- deletion
- consent
- audit
- compliance.

---

## 16. Critical distinction

Nivy should NOT select "Mem0 vs RAG vs GraphRAG" as if they are mutually exclusive.

They solve different layers:

**RAG**
→ retrieve external knowledge.

**Memory**
→ retain learned/user/agent/company context across time.

**GraphRAG**
→ retrieve relationships and multi-hop knowledge.

**Context engineering**
→ decide what context reaches the model.

**Knowledge graph/context graph**
→ represent relationships, provenance and temporal state.

**Agent runtime**
→ reason, plan and act.

**Workflow engine**
→ execute deterministic processes.

**ERP/CRM**
→ remain system-of-record for business transactions.

The eventual Nivy architecture can combine all of these.

---

## 17. Highest-priority systems for deeper technical inspection

Not a ranking; this is a **coverage shortlist** for architecture study:

1. Mem0 — https://github.com/mem0ai/mem0
2. Zep — https://github.com/getzep/zep
3. Graphiti — https://github.com/getzep/graphiti
4. Letta — https://github.com/letta-ai/letta
5. Cognee — https://github.com/topoteretes/cognee
6. LangMem — https://github.com/langchain-ai/langmem
7. Supermemory — https://github.com/supermemoryai/supermemory
8. Neo4j Agent Memory — https://github.com/neo4j-labs/agent-memory
9. Redis Agent Memory — https://github.com/redis/agent-memory-server
10. JiuwenMemory — https://github.com/openJiuwen-ai/agent-memory
11. Microsoft GraphRAG — https://github.com/microsoft/graphrag
12. MemGraphRAG — https://github.com/XMUDeepLIT/MemGraphRAG
13. Multimodal RAG Agent — https://github.com/Kasshern/multimodal-rag-agent
14. Agent Memory Kit — https://github.com/reflectt/agent-memory-kit
15. Agent Memory Research — https://github.com/tobias-weiss-ai-xr/agent-memory-research

These are **research targets**, not "best system" claims.

---

## 18. Reuse rule

Before building Nivy memory from scratch:

1. inspect existing Nivy memory/knowledge implementation;
2. inspect Mem0/Zep/Graphiti/Letta/Cognee/LangMem/Supermemory;
3. inspect GraphRAG and multimodal RAG;
4. inspect MCP memory servers;
5. inspect filesystem/Git memory;
6. inspect benchmarks;
7. compare architecture, license, deployment, privacy, APIs and maintenance;
8. reuse/adapt the smallest suitable components;
9. build only the missing integration/orchestration layer.

## 19. Discovery status

**NOT COMPLETE.**

The next pass should continue into:
- memory MCP servers
- memory-specific A2A agents
- enterprise memory platforms
- CRM/customer-memory systems
- email/calendar memory ingestion
- meeting/voice memory
- browser/web memory
- code-agent memory
- multi-agent shared memory
- federated memory
- memory security/poisoning defenses
- privacy/deletion/right-to-be-forgotten systems
- memory compression
- learned retrieval
- neural/parametric memory
- external memory architectures
- long-context vs memory hybrids
- memory benchmarks and evaluation harnesses
- production case studies.

The goal is to create a **Memory & Context Reuse Layer** for the Nivy Company OS rather than merely adding one vector database.
