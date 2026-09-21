# Agentic AI System Universe — Native AI Systems, Agents, Runtimes & Libraries — 2026-09

## Purpose

This file is the **broad system-level discovery layer** for reusable AI-native / agentic systems.

It is intentionally broader than a normal "AI agent framework" list. It covers:

**finished agent systems → agent runtimes → multi-agent systems → coding agents → research agents → browser/computer agents → voice agents → multimodal agents → RAG/knowledge agents → memory systems → workflow agents → tool/MCP systems → local AI → AI workspaces/AI operating systems → domain/business agents → evaluation/security/governance infrastructure.**

The goal is:

**DISCOVER → INSPECT → VERIFY → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING**

This is a discovery catalog, **not a ranking**.

> Status note: the agent ecosystem changes extremely quickly. This file is a living registry. A project appearing here means "inspect it"; it does **not** mean it is production-ready, secure, compatible with Nivy, or licensed for copying.

---

## 1. Core agent frameworks / runtimes

| System | Type | Source |
|---|---|---|
| LangGraph | Stateful graph agent runtime | https://github.com/langchain-ai/langgraph |
| LangChain | LLM/agent framework | https://github.com/langchain-ai/langchain |
| LlamaIndex | Agent + data/RAG framework | https://github.com/run-llama/llama_index |
| CrewAI | Role/task multi-agent framework | https://github.com/crewAIInc/crewAI |
| Microsoft Agent Framework | Microsoft agent/workflow framework | https://github.com/microsoft/agent-framework |
| AutoGen / AG2 lineage | Multi-agent conversation/orchestration | https://github.com/microsoft/autogen |
| Semantic Kernel | Enterprise agent SDK | https://github.com/microsoft/semantic-kernel |
| OpenAI Agents SDK | Agent SDK, tools, handoffs, guardrails | https://github.com/openai/openai-agents-python |
| Google ADK | Google agent development kit | https://github.com/google/adk-python |
| PydanticAI | Typed Python agent framework | https://github.com/pydantic/pydantic-ai |
| smolagents | Lightweight code-agent framework | https://github.com/huggingface/smolagents |
| Mastra | TypeScript agent/workflow framework | https://github.com/mastra-ai/mastra |
| Agno | Agent framework/runtime | https://github.com/agno-agi/agno |
| Haystack | Agent/RAG pipeline framework | https://github.com/deepset-ai/haystack |
| DSPy | Programmatic LM/agent optimization | https://github.com/stanfordnlp/dspy |
| Atomic Agents | Modular agent framework | https://github.com/BrainBlend-AI/atomic-agents |
| AgentScope | Multi-agent framework | https://github.com/agentscope-ai/agentscope |
| Swarms | Multi-agent orchestration | https://github.com/kyegomez/swarms |
| MetaGPT | Role-based software-company agents | https://github.com/FoundationAgents/MetaGPT |
| AutoGPT | Autonomous agent platform | https://github.com/Significant-Gravitas/AutoGPT |

## 2. General-purpose autonomous / native AI systems

These are closer to **ready-made AI workers** than bare libraries.

| System | Capability | Source |
|---|---|---|
| AutoGPT | Goal-driven agents/workflows | https://github.com/Significant-Gravitas/AutoGPT |
| Agent Zero | General-purpose organic agent using computer/OS/tools/memory | https://github.com/agent0ai/agent-zero |
| Hermes Agent | Self-improving agent with skills + persistent learning | https://github.com/NousResearch/hermes-agent |
| Goose | Native local AI agent for code, workflows, research and automation | https://github.com/block/goose |
| OpenHands | Autonomous software/developer agent | https://github.com/All-Hands-AI/OpenHands |
| OpenClaw | Personal/local agent ecosystem | https://github.com/openclaw/openclaw |
| SOMI | Local-first AI workstation/agent framework | https://github.com/Somi-Project/Somi |
| Aria | Browser AI OS / multi-agent workspace | https://github.com/skmdroid/aria |
| useAgent | AI coworker with browser/computer/workspace | https://github.com/useagenthq/useagent |
| Agent Cockpit | Local multi-vendor AI-agent cockpit | https://github.com/daronyondem/agent-cockpit |
| BabyAGI | Autonomous task-loop research lineage | https://github.com/yoheinakajima/babyagi |
| MetaGPT | Software-company simulation / agent team | https://github.com/FoundationAgents/MetaGPT |

## 3. Multi-agent / agent-team systems

| System | Pattern | Source |
|---|---|---|
| CrewAI | Role-based teams | https://github.com/crewAIInc/crewAI |
| LangGraph | Graph/supervisor/hierarchical teams | https://github.com/langchain-ai/langgraph |
| Microsoft Agent Framework | Enterprise agent orchestration | https://github.com/microsoft/agent-framework |
| AG2 | Multi-agent conversations | https://github.com/ag2ai/ag2 |
| AgentScope | Multi-agent applications | https://github.com/agentscope-ai/agentscope |
| Swarms | Agent swarm orchestration | https://github.com/kyegomez/swarms |
| MetaGPT | Role-playing company | https://github.com/FoundationAgents/MetaGPT |
| AutoGen | Multi-agent framework lineage | https://github.com/microsoft/autogen |
| Agent Squad | Multi-agent routing/orchestration | https://github.com/awslabs/multi-agent-orchestrator |
| AgentVerse | Multi-agent environments | https://github.com/OpenBMB/AgentVerse |
| Hive | Specialized agent collaboration projects | https://github.com/aden-hive/hive |
| EvoAgentX | Evolving/optimizing agent workflows | https://github.com/EvoAgentX/EvoAgentX |

## 4. Coding / software-engineering agents

| System | Capability | Source |
|---|---|---|
| OpenHands | Autonomous coding/development | https://github.com/All-Hands-AI/OpenHands |
| SWE-agent | Automated software-engineering tasks | https://github.com/SWE-agent/SWE-agent |
| Aider | AI pair-programming in terminal/git | https://github.com/Aider-AI/aider |
| Cline | Coding agent in editor/terminal | https://github.com/cline/cline |
| Roo Code | Coding-agent fork/ecosystem | https://github.com/RooCodeInc/Roo-Code |
| Continue | Open coding assistant | https://github.com/continuedev/continue |
| Goose | Local general/coding agent | https://github.com/block/goose |
| OpenCode | Open-source coding agent | https://github.com/anomalyco/opencode |
| OpenHands | Repo/terminal/browser/code execution agent | https://github.com/All-Hands-AI/OpenHands |
| MetaGPT | Software-company agents | https://github.com/FoundationAgents/MetaGPT |
| SWE-bench | Software-agent evaluation | https://github.com/SWE-bench/SWE-bench |
| aider-chat | Git-aware coding agent | https://github.com/Aider-AI/aider |

## 5. Research / deep-research / knowledge-worker agents

| System | Type | Source |
|---|---|---|
| OpenDeepResearch | Open deep-research implementations | https://github.com/huggingface/smolagents |
| STORM | Long-form research/report generation | https://github.com/stanford-oval/storm |
| GPT Researcher | Autonomous web research | https://github.com/assafelovic/gpt-researcher |
| OpenAI Deep Research ecosystem examples | Deep research patterns | https://github.com/openai |
| LlamaIndex research agents | Data/research agents | https://github.com/run-llama/llama_index |
| LangGraph research agents | Stateful research workflows | https://github.com/langchain-ai/langgraph |
| AutoGPT research workflows | Autonomous research | https://github.com/Significant-Gravitas/AutoGPT |
| AgentScope research workflows | Multi-agent research | https://github.com/agentscope-ai/agentscope |
| STORM | Multi-perspective research synthesis | https://github.com/stanford-oval/storm |
| PaperQA | Scientific literature QA | https://github.com/Future-House/paper-qa |

## 6. Browser / web / computer-use agents

| System | Capability | Source |
|---|---|---|
| Browser Use | LLM browser control | https://github.com/browser-use/browser-use |
| Playwright | Deterministic browser execution layer | https://github.com/microsoft/playwright |
| Stagehand | AI browser automation | https://github.com/browserbase/stagehand |
| Skyvern | Vision/browser workflow automation | https://github.com/Skyvern-AI/skyvern |
| BrowserGym | Browser-agent research environment | https://github.com/ServiceNow/BrowserGym |
| WebArena | Web-agent benchmark/environment | https://github.com/web-arena-x/webarena |
| AgentBrowser | REST/browser/vision agent interface | https://github.com/smouj/agent-browser |
| Tencent BrowserSkill | Logged-in browser control for agents | https://github.com/Tencent/BrowserSkill |
| agent-browser | CLI browser automation for AI agents | https://github.com/vercel-labs/agent-browser |
| OpenHands browser capabilities | Browser + coding agent | https://github.com/All-Hands-AI/OpenHands |
| BrowserGym WorkArena | Enterprise browser-agent benchmark | https://github.com/ServiceNow/WorkArena |
| WebVoyager | Web browsing agent research | https://github.com/MinorJerry/WebVoyager |

**Rule:** browser agents must respect site terms, authentication boundaries, CAPTCHAs, robots/access restrictions and platform policies.

## 7. Voice / speech / realtime agents

| System | Type | Source |
|---|---|---|
| LiveKit Agents | Realtime voice/video agents | https://github.com/livekit/agents |
| Pipecat | Realtime voice/multimodal pipelines | https://github.com/pipecat-ai/pipecat |
| Vapi | Voice-agent platform | https://github.com/VapiAI/server-sdk |
| Retell | Voice-agent platform | https://github.com/RetellAI |
| Pipecat | Voice + multimodal agent framework | https://github.com/pipecat-ai/pipecat |
| OpenAI Realtime examples | Realtime agent patterns | https://github.com/openai/openai-agents-python |
| LiveKit | WebRTC agent infrastructure | https://github.com/livekit/agents |
| Parlant | Governed conversational agents | https://github.com/emcie-co/parlant |
| OpenVoice | Voice cloning/synthesis research | https://github.com/myshell-ai/OpenVoice |
| Whisper | Speech recognition | https://github.com/openai/whisper |

## 8. Multimodal / vision / image / video agent systems

| System | Capability | Source |
|---|---|---|
| LLaVA | Vision-language models | https://github.com/haotian-liu/LLaVA |
| Qwen-VL | Vision-language models | https://github.com/QwenLM/Qwen3-VL |
| Transformers | Multimodal model runtime/library | https://github.com/huggingface/transformers |
| smolagents | Text/vision/video/audio agents | https://github.com/huggingface/smolagents |
| LlamaIndex multimodal | Multimodal RAG/agents | https://github.com/run-llama/llama_index |
| Open WebUI | Multimodal local AI interface | https://github.com/open-webui/open-webui |
| ComfyUI | Generative image/video workflow engine | https://github.com/comfyanonymous/ComfyUI |
| InvokeAI | Generative image platform | https://github.com/invoke-ai/InvokeAI |
| AUTOMATIC1111 | Stable Diffusion web UI | https://github.com/AUTOMATIC1111/stable-diffusion-webui |
| Whisper | Speech modality | https://github.com/openai/whisper |

## 9. RAG / retrieval / knowledge agents

| System | Layer | Source |
|---|---|---|
| LlamaIndex | RAG + agents + workflows | https://github.com/run-llama/llama_index |
| Haystack | RAG pipelines + agents | https://github.com/deepset-ai/haystack |
| LangChain | Retrieval + agents | https://github.com/langchain-ai/langchain |
| Microsoft GraphRAG | Knowledge-graph RAG | https://github.com/microsoft/graphrag |
| GraphRAG Core | Governed knowledge graphs | https://github.com/raphaelsty/graphiti |
| Graphiti | Temporal context graph | https://github.com/getzep/graphiti |
| Neo4j GraphRAG | Graph + vector retrieval | https://github.com/neo4j/neo4j-graphrag-python |
| RAGFlow | Document/RAG platform | https://github.com/infiniflow/ragflow |
| Danswer / Onyx | Enterprise search/RAG | https://github.com/onyx-dot-app/onyx |
| AnythingLLM | Local/enterprise RAG workspace | https://github.com/Mintplex-Labs/anything-llm |
| Open WebUI | Local knowledge/RAG UI | https://github.com/open-webui/open-webui |
| txtai | Embeddings/search/RAG | https://github.com/neuml/txtai |
| Haystack | Retrieval pipelines | https://github.com/deepset-ai/haystack |
| ColBERT | Neural retrieval | https://github.com/stanford-futuredata/ColBERT |

## 10. Memory / long-term agent memory

| System | Memory model | Source |
|---|---|---|
| Mem0 | Agent/user long-term memory | https://github.com/mem0ai/mem0 |
| Zep | Temporal/agent memory | https://github.com/getzep/zep |
| Graphiti | Temporal knowledge/context graph | https://github.com/getzep/graphiti |
| Letta | Stateful agents + memory | https://github.com/letta-ai/letta |
| Cognee | Knowledge graph + memory | https://github.com/topoteretes/cognee |
| LangMem | Long-term memory tools | https://github.com/langchain-ai/langmem |
| Supermemory | Memory/context engine | https://github.com/supermemoryai/supermemory |
| Memobase | User-profile memory | https://github.com/memodb-io/memobase |
| Neo4j Agent Memory | Graph/vector/text memory | https://github.com/neo4j-labs/agent-memory |
| Redis Agent Memory Server | Session + long-term memory | https://github.com/redis/agent-memory-server |
| Agent Memory Kit | Working/long-term/feedback memory | https://github.com/reflectt/agent-memory-kit |
| Mnemosyne | Advanced agent memory | https://github.com/28naem-del/mnemosyne |
| MemGraphRAG | Memory + GraphRAG | https://github.com/hubert0527/MemGraphRAG |
| Letta MemFS | Git-backed agent memory | https://github.com/letta-ai/letta |
| Mem0 MCP | Memory through MCP | https://github.com/mem0ai/mem0 |

## 11. Context engineering / prompt-memory systems

| System | Function | Source |
|---|---|---|
| Letta | Stateful context/memory management | https://github.com/letta-ai/letta |
| LangMem | Memory extraction/update | https://github.com/langchain-ai/langmem |
| Mem0 | Memory extraction/retrieval | https://github.com/mem0ai/mem0 |
| Zep | Temporal context retrieval | https://github.com/getzep/zep |
| Supermemory | Context engine | https://github.com/supermemoryai/supermemory |
| LlamaIndex | Context augmentation | https://github.com/run-llama/llama_index |
| DSPy | Programmatic prompt/LM optimization | https://github.com/stanfordnlp/dspy |
| Guidance | Structured generation/control | https://github.com/guidance-ai/guidance |
| Outlines | Structured generation | https://github.com/dottxt-ai/outlines |
| Instructor | Structured LLM outputs | https://github.com/567-labs/instructor |

## 12. Workflow / automation-native AI

| System | Function | Source |
|---|---|---|
| n8n | Workflow automation + AI agents | https://github.com/n8n-io/n8n |
| Dify | Agent/workflow application platform | https://github.com/langgenius/dify |
| Flowise | Visual LLM/agent workflows | https://github.com/FlowiseAI/Flowise |
| Activepieces | Open automation platform | https://github.com/activepieces/activepieces |
| Windmill | Developer workflow automation | https://github.com/windmill-labs/windmill |
| Kestra | Event/workflow orchestration | https://github.com/kestra-io/kestra |
| Temporal | Durable workflow runtime | https://github.com/temporalio/temporal |
| Prefect | Workflow orchestration | https://github.com/PrefectHQ/prefect |
| Dagster | Data/asset orchestration | https://github.com/dagster-io/dagster |
| AutoGPT | Agentic workflow builder | https://github.com/Significant-Gravitas/AutoGPT |
| LlamaIndex Workflows | Agentic event-driven workflows | https://github.com/run-llama/llama_index |

## 13. Visual / low-code AI agent builders

| System | Source |
|---|---|
| Dify | https://github.com/langgenius/dify |
| Flowise | https://github.com/FlowiseAI/Flowise |
| Langflow | https://github.com/langflow-ai/langflow |
| n8n | https://github.com/n8n-io/n8n |
| AutoGPT | https://github.com/Significant-Gravitas/AutoGPT |
| Sim | https://github.com/simstudioai/sim |
| Botpress | https://github.com/botpress/botpress |
| AnythingLLM | https://github.com/Mintplex-Labs/anything-llm |
| Open WebUI | https://github.com/open-webui/open-webui |
| RAGFlow | https://github.com/infiniflow/ragflow |
| Langflow | https://github.com/langflow-ai/langflow |

## 14. MCP / tool ecosystems

| System | Function | Source |
|---|---|---|
| Model Context Protocol | Standard agent/tool interface | https://github.com/modelcontextprotocol |
| MCP Servers | Official/community server ecosystem | https://github.com/modelcontextprotocol/servers |
| Composio | Agent tool integrations | https://github.com/ComposioHQ/composio |
| Smithery | MCP/server ecosystem | https://github.com/smithery-ai |
| mcp-use | MCP agent integration library | https://github.com/mcp-use/mcp-use |
| FastMCP | MCP server framework | https://github.com/jlowin/fastmcp |
| Browser Use MCP | Browser as agent tool | https://github.com/browser-use/browser-use |
| Goose extensions | MCP-powered agent extensions | https://github.com/block/goose |
| Agent Zero tools/plugins | Extensible agent tools | https://github.com/agent0ai/agent-zero |
| OpenHands tools | Agent tool/runtime layer | https://github.com/All-Hands-AI/OpenHands |

## 15. Agent-to-agent / interoperability

| System | Function | Source |
|---|---|---|
| A2A Protocol | Agent-to-agent interoperability | https://github.com/a2aproject/A2A |
| MCP | Agent-to-tool/context interoperability | https://github.com/modelcontextprotocol |
| Agent Communication Protocol (ACP) | Agent interoperability research/ecosystem | https://github.com/i-am-bee/acp |
| AG-UI | Agent ↔ frontend event protocol | https://github.com/ag-ui-protocol/ag-ui |
| Open Agent Specification | Agent definitions/interoperability projects | https://github.com/agentic-ai-foundation |
| Agent2Agent examples | Multi-agent interoperability | https://github.com/a2aproject/A2A |

## 16. Local / private / self-hosted AI engines

| System | Function | Source |
|---|---|---|
| Ollama | Local LLM runtime | https://github.com/ollama/ollama |
| llama.cpp | Local inference runtime | https://github.com/ggml-org/llama.cpp |
| vLLM | High-throughput inference server | https://github.com/vllm-project/vllm |
| LocalAI | OpenAI-compatible local inference | https://github.com/mudler/LocalAI |
| LM Studio | Local model desktop runtime | https://github.com/lmstudio-ai |
| Jan | Local AI desktop application | https://github.com/menloresearch/jan |
| GPT4All | Local/private LLM application | https://github.com/nomic-ai/gpt4all |
| Open WebUI | Local AI workspace | https://github.com/open-webui/open-webui |
| AnythingLLM | Private/local AI workspace | https://github.com/Mintplex-Labs/anything-llm |
| KoboldCpp | Local inference UI/runtime | https://github.com/LostRuins/koboldcpp |
| text-generation-webui | Local model UI/runtime | https://github.com/oobabooga/text-generation-webui |

## 17. Model serving / agent infrastructure

| System | Function | Source |
|---|---|---|
| vLLM | LLM serving | https://github.com/vllm-project/vllm |
| SGLang | High-performance serving | https://github.com/sgl-project/sglang |
| TensorRT-LLM | NVIDIA inference | https://github.com/NVIDIA/TensorRT-LLM |
| TGI | Hugging Face inference server | https://github.com/huggingface/text-generation-inference |
| BentoML | AI model/app serving | https://github.com/bentoml/BentoML |
| Ray | Distributed AI workloads | https://github.com/ray-project/ray |
| KServe | Kubernetes model serving | https://github.com/kserve/kserve |
| Modal | Serverless AI compute | https://github.com/modal-labs/modal-examples |

## 18. Vector databases / retrieval substrates

| System | Source |
|---|---|
| Qdrant | https://github.com/qdrant/qdrant |
| Weaviate | https://github.com/weaviate/weaviate |
| Milvus | https://github.com/milvus-io/milvus |
| Chroma | https://github.com/chroma-core/chroma |
| pgvector | https://github.com/pgvector/pgvector |
| LanceDB | https://github.com/lancedb/lancedb |
| Vespa | https://github.com/vespa-engine/vespa |
| OpenSearch | https://github.com/opensearch-project/OpenSearch |
| Elasticsearch | https://github.com/elastic/elasticsearch |
| Redis | https://github.com/redis/redis |
| FAISS | https://github.com/facebookresearch/faiss |

## 19. Knowledge graphs / graph intelligence

| System | Source |
|---|---|
| Neo4j | https://github.com/neo4j/neo4j |
| Graphiti | https://github.com/getzep/graphiti |
| Microsoft GraphRAG | https://github.com/microsoft/graphrag |
| Kuzu | https://github.com/kuzudb/kuzu |
| Memgraph | https://github.com/memgraph/memgraph |
| FalkorDB | https://github.com/FalkorDB/FalkorDB |
| Apache AGE | https://github.com/apache/age |
| RDFLib | https://github.com/RDFLib/rdflib |
| NetworkX | https://github.com/networkx/networkx |
| Cognee | https://github.com/topoteretes/cognee |

## 20. Document / OCR / document-agent systems

| System | Function | Source |
|---|---|---|
| LlamaParse | Agentic document parsing | https://github.com/run-llama/llama_parse |
| Unstructured | Document ingestion/extraction | https://github.com/Unstructured-IO/unstructured |
| Docling | Document conversion/understanding | https://github.com/docling-project/docling |
| Marker | PDF → Markdown/structured text | https://github.com/datalab-to/marker |
| MinerU | PDF/document extraction | https://github.com/opendatalab/MinerU |
| PaddleOCR | OCR | https://github.com/PaddlePaddle/PaddleOCR |
| Tesseract | OCR | https://github.com/tesseract-ocr/tesseract |
| Surya | OCR/layout analysis | https://github.com/datalab-to/surya |
| OCRmyPDF | Searchable PDF OCR | https://github.com/ocrmypdf/OCRmyPDF |
| RAGFlow | Document/RAG platform | https://github.com/infiniflow/ragflow |

## 21. AI search / web-data agents

| System | Function | Source |
|---|---|---|
| Firecrawl | Web crawling for AI agents | https://github.com/firecrawl/firecrawl |
| Crawl4AI | Open-source AI web crawler | https://github.com/unclecode/crawl4ai |
| Scrapy | Web crawling framework | https://github.com/scrapy/scrapy |
| Tavily | Search API for agents | https://github.com/tavily-ai/tavily-python |
| Jina Reader | Web-to-LLM content | https://github.com/jina-ai/reader |
| Exa | Neural search/retrieval | https://github.com/exa-labs/exa-py |
| Browser Use | Browser research | https://github.com/browser-use/browser-use |
| GPT Researcher | Autonomous research | https://github.com/assafelovic/gpt-researcher |
| STORM | Research synthesis | https://github.com/stanford-oval/storm |
| Crawl4AI | Agent-ready crawling | https://github.com/unclecode/crawl4ai |

## 22. AI sales / marketing / business agents

| System / library | Use | Source |
|---|---|---|
| SaaS Marketing Agents | Marketing-agent collection | https://github.com/ai-boost/saas-marketing-agents |
| Sales-Outreach | Sales/outreach automation | https://github.com/ehsansaleh1/Sales-Outreach |
| UnifAI Agents | Business/agent workflows | https://github.com/unifai-network/unifai-sdk |
| n8n AI workflows | Sales/marketing automations | https://github.com/n8n-io/n8n |
| Composio | CRM/sales tool integrations | https://github.com/ComposioHQ/composio |
| AutoGPT | Sales/marketing workflows | https://github.com/Significant-Gravitas/AutoGPT |
| Dify | Business workflow agents | https://github.com/langgenius/dify |
| CrewAI | Sales/marketing agent teams | https://github.com/crewAIInc/crewAI |
| OpenAI Agents SDK | Custom sales/marketing agents | https://github.com/openai/openai-agents-python |
| LangGraph | Stateful GTM workflows | https://github.com/langchain-ai/langgraph |

## 23. Customer support / service agents

| System | Source |
|---|---|
| Dify | https://github.com/langgenius/dify |
| Botpress | https://github.com/botpress/botpress |
| Rasa | https://github.com/RasaHQ/rasa |
| OpenDialog | https://github.com/opendialogai/OpenDialog |
| Haystack | https://github.com/deepset-ai/haystack |
| LangGraph | https://github.com/langchain-ai/langgraph |
| Parlant | https://github.com/emcie-co/parlant |
| LiveKit Agents | https://github.com/livekit/agents |
| Open WebUI | https://github.com/open-webui/open-webui |
| AnythingLLM | https://github.com/Mintplex-Labs/anything-llm |

## 24. Data / analytics / SQL agents

| System | Function | Source |
|---|---|---|
| LlamaIndex | Text-to-SQL/data agents | https://github.com/run-llama/llama_index |
| LangChain SQL agents | SQL/tool agents | https://github.com/langchain-ai/langchain |
| Vanna | AI SQL generation | https://github.com/vanna-ai/vanna |
| DB-GPT | Database/analytics agent platform | https://github.com/eosphoros-ai/DB-GPT |
| MindsDB | AI + database integration | https://github.com/mindsdb/mindsdb |
| PandasAI | Conversational data analysis | https://github.com/sinaptik-ai/pandas-ai |
| Jupyter AI | AI for data science | https://github.com/jupyterlab/jupyter-ai |
| Evidence | Data/BI workflows | https://github.com/evidence-dev/evidence |

## 25. Computer-use / desktop AI

| System | Source |
|---|---|
| Agent Zero | https://github.com/agent0ai/agent-zero |
| OpenHands | https://github.com/All-Hands-AI/OpenHands |
| Goose | https://github.com/block/goose |
| Browser Use | https://github.com/browser-use/browser-use |
| Tencent BrowserSkill | https://github.com/Tencent/BrowserSkill |
| OpenClaw | https://github.com/openclaw/openclaw |
| SOMI | https://github.com/Somi-Project/Somi |
| Aria | https://github.com/skmdroid/aria |
| Open Interpreter | https://github.com/OpenInterpreter/open-interpreter |
| OSWorld | https://github.com/xlang-ai/OSWorld |

## 26. AI operating systems / agent workspaces / company-like systems

| System | Concept | Source |
|---|---|---|
| AutoGPT Platform | Agent platform + marketplace + builder | https://github.com/Significant-Gravitas/AutoGPT |
| Open WebUI | Local AI workspace | https://github.com/open-webui/open-webui |
| AnythingLLM | AI workspace/RAG | https://github.com/Mintplex-Labs/anything-llm |
| Dify | AI application/agent platform | https://github.com/langgenius/dify |
| Sim | AI workflow/agent workspace | https://github.com/simstudioai/sim |
| Aria | AI operating system UI | https://github.com/skmdroid/aria |
| SOMI | AI workstation/OS-like agent framework | https://github.com/Somi-Project/Somi |
| Agent Cockpit | Vendor-neutral agent cockpit | https://github.com/daronyondem/agent-cockpit |
| useAgent | AI coworker/workspace | https://github.com/useagenthq/useagent |
| Agent Zero | Computer-native organic agent | https://github.com/agent0ai/agent-zero |

## 27. Agent evaluation / benchmarks

| System | Purpose | Source |
|---|---|---|
| SWE-bench | Software engineering agents | https://github.com/SWE-bench/SWE-bench |
| GAIA | General AI assistant benchmark | https://huggingface.co/gaia-benchmark |
| AgentBench | Agent capability benchmark | https://github.com/THUDM/AgentBench |
| BrowserGym | Browser agents | https://github.com/ServiceNow/BrowserGym |
| WebArena | Web agents | https://github.com/web-arena-x/webarena |
| OSWorld | Computer-use agents | https://github.com/xlang-ai/OSWorld |
| τ-bench | Tool-agent benchmark | https://github.com/sierra-research/tau-bench |
| BFCL | Function/tool calling | https://github.com/ShishirPatil/gorilla |
| LongMemEval | Long-term memory | https://github.com/xiaowu0162/LongMemEval |
| LoCoMo | Long-context/memory | https://github.com/snap-research/locomo |
| Mem0 benchmarks | Agent memory | https://github.com/mem0ai/mem0 |
| RAGAS | RAG evaluation | https://github.com/explodinggradients/ragas |
| DeepEval | LLM/agent evaluation | https://github.com/confident-ai/deepeval |
| Promptfoo | LLM/agent testing | https://github.com/promptfoo/promptfoo |

## 28. Agent observability / tracing

| System | Source |
|---|---|
| Langfuse | https://github.com/langfuse/langfuse |
| Arize Phoenix | https://github.com/Arize-ai/phoenix |
| Helicone | https://github.com/Helicone/helicone |
| OpenLLMetry | https://github.com/traceloop/openllmetry |
| OpenTelemetry | https://github.com/open-telemetry/opentelemetry-specification |
| LangSmith SDK ecosystem | https://github.com/langchain-ai/langsmith-sdk |
| Braintrust | https://github.com/braintrustdata/braintrust-sdk |
| AgentOps | https://github.com/AgentOps-AI/agentops |

## 29. Agent safety / guardrails / security

| System | Purpose | Source |
|---|---|---|
| NeMo Guardrails | Programmable guardrails | https://github.com/NVIDIA-NeMo/Guardrails |
| Guardrails AI | Validation/guardrails | https://github.com/guardrails-ai/guardrails |
| Llama Guard | Safety classifier models | https://github.com/meta-llama/PurpleLlama |
| Lakera Guard | AI security/guardrails | https://github.com/lakeraai/lakera |
| Rebuff | Prompt-injection defense research | https://github.com/protectai/rebuff |
| Presidio | PII detection/redaction | https://github.com/microsoft/presidio |
| PyRIT | AI red teaming | https://github.com/Azure/PyRIT |
| Garak | LLM vulnerability scanner | https://github.com/NVIDIA/garak |
| Promptfoo | Red teaming/evaluation | https://github.com/promptfoo/promptfoo |
| AgentDojo | Agent security benchmark | https://github.com/ethz-spylab/agentdojo |

## 30. Agent sandboxes / secure execution

| System | Source |
|---|---|
| E2B | https://github.com/e2b-dev/E2B |
| Daytona | https://github.com/daytonaio/daytona |
| Modal | https://github.com/modal-labs/modal-examples |
| Docker | https://github.com/docker/docker-ce |
| gVisor | https://github.com/google/gvisor |
| Firecracker | https://github.com/firecracker-microvm/firecracker |
| OpenHands runtime | https://github.com/All-Hands-AI/OpenHands |
| Blaxel | https://github.com/blaxel-ai |

## 31. Skills / reusable agent capability systems

| System | Source |
|---|---|
| Agent Skills specification/ecosystem | https://github.com/agentskills/agentskills |
| Claude Skills ecosystem | https://github.com/anthropics/skills |
| Skills CLI ecosystem | https://github.com/vercel-labs/skills |
| OpenAI skills/examples | https://github.com/openai |
| Agent Zero Skills | https://github.com/agent0ai/agent-zero |
| Hermes skills | https://github.com/NousResearch/hermes-agent |
| Goose recipes/extensions | https://github.com/block/goose |
| awesome-agent-skills | https://github.com/VoltAgent/awesome-agent-skills |
| awesome-claude-skills | https://github.com/BehiSecc/awesome-claude-skills |

## 32. AI model / provider abstraction

| System | Function | Source |
|---|---|---|
| LiteLLM | Unified LLM gateway | https://github.com/BerriAI/litellm |
| OpenRouter | Multi-model routing | https://github.com/OpenRouterTeam/openrouter |
| Portkey | AI gateway | https://github.com/Portkey-AI/gateway |
| OpenLLM | Model serving/abstraction | https://github.com/bentoml/OpenLLM |
| Ollama | Local model runtime | https://github.com/ollama/ollama |
| vLLM | Model serving | https://github.com/vllm-project/vllm |
| llama.cpp | Local inference | https://github.com/ggml-org/llama.cpp |
| Transformers | Model ecosystem/runtime | https://github.com/huggingface/transformers |

## 33. AI agent registries / discovery lists — important meta-sources

These should themselves be crawled periodically because they expose many additional systems.

| Registry | Coverage | Source |
|---|---|---|
| awesome-ai-agents / tysoncung | Agents/frameworks/tools | https://github.com/tysoncung/awesome-ai-agents |
| awesome-ai-agents / korchasa | Automatically compiled agent ecosystem | https://github.com/korchasa/awesome-ai-agents |
| awesome-ai-agents / NipunaRanasinghe | 100+ frameworks/tools/platforms | https://github.com/NipunaRanasinghe/awesome-ai-agents |
| awesome-ai-agents-2026 | Structured 2026 agent catalog | https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026 |
| awesome-agent-orchestration | Orchestration/MCP/A2A/swarm | https://github.com/vivy-yi/awesome-agent-orchestration |
| ai-agent-frameworks | 175+ SDKs/workflows/agents | https://github.com/aglio-lab/ai-agent-frameworks |
| Awesome Agent Memory | Memory systems | https://github.com/mnemoverse/awesome-agent-memory |
| Awesome AI Memory | AI memory ecosystem | https://github.com/fomos-ai/awesome-ai-memory |
| AgentVerse | Agent ecosystem knowledge graph | https://github.com/OpenBMB/AgentVerse |
| MCP Servers | Tool-server ecosystem | https://github.com/modelcontextprotocol/servers |

---

# 34. System-type taxonomy for Nivy

The discovery process must not stop at "agents".

Every candidate should be classified into one or more of these layers:

1. **Model** — LLM/VLM/SLM/audio/video/image model
2. **Inference** — local/cloud model serving
3. **Agent runtime** — reasoning/planning/action loop
4. **Agent application** — ready-made AI worker
5. **Multi-agent runtime** — teams/swarms/supervisors
6. **Workflow engine** — deterministic/event-driven execution
7. **Tool layer** — APIs/functions/browser/filesystem/SQL
8. **MCP layer** — model-context/tool interoperability
9. **A2A layer** — agent-to-agent interoperability
10. **Skills** — reusable capability packages
11. **Memory** — session/episodic/semantic/procedural/organizational
12. **RAG** — retrieval/context augmentation
13. **Knowledge graph** — entity/relationship/temporal knowledge
14. **Context engineering** — selection/compression/routing/assembly
15. **Browser/computer use** — GUI/DOM/OS interaction
16. **Voice/realtime** — STT/TTS/WebRTC/phone agents
17. **Multimodal** — image/video/audio/document understanding
18. **Document intelligence** — OCR/parsing/extraction
19. **Data/SQL agents** — analytics and database operations
20. **Coding agents** — repository/software engineering
21. **Research agents** — web/literature/deep research
22. **Business agents** — sales/marketing/support/finance/HR/legal/etc.
23. **Agent workspace/AI OS** — unified human/agent interface
24. **Sandbox** — isolated execution
25. **Observability** — traces/runs/costs
26. **Evaluation** — quality/agent benchmarks
27. **Security** — prompt injection, data leakage, permissions
28. **Governance** — approval, RBAC, audit, policy
29. **Deployment** — containers/serverless/Kubernetes
30. **Agent registry/marketplace** — discover/install/reuse agents

---

# 35. Important distinction

Do **not** collapse these into one category:

**LLM ≠ AI application ≠ Agent ≠ Multi-agent system ≠ Workflow ≠ RAG ≠ Memory ≠ Knowledge Graph ≠ Context Engineering ≠ Tool/MCP ≠ Browser agent ≠ Computer-use agent ≠ AI OS ≠ ERP/CRM.**

A complete Nivy architecture can combine all of them.

Example:

**Nivy UI → Company Digital Twin → Agent Router → Agent Team → Skills → Tools/MCP → Workflow → ERP/CRM → RAG/Knowledge Graph → Memory → Sandbox → Human Approval → Execution → Audit → Evaluation**

---

# 36. Discovery rule for future research

When a new agentic system is found, record:

| Field | Required |
|---|---|
| Name | Yes |
| System class | Yes |
| Subclass | Yes |
| Repository/source URL | Yes |
| Documentation | Prefer |
| License | Yes |
| Open-source / managed / hybrid | Yes |
| Self-hostable | Yes/No |
| Local-model support | Yes/No/Unknown |
| MCP | Yes/No/Unknown |
| A2A | Yes/No/Unknown |
| Memory | Type |
| RAG | Type |
| Browser/computer use | Yes/No |
| Voice | Yes/No |
| Multimodal | Yes/No |
| Multi-agent | Yes/No |
| Skills | Yes/No |
| Integrations | List |
| Sandbox | Yes/No |
| Observability | Yes/No |
| Evaluation | Yes/No |
| Security/governance | Yes/No |
| Reuse method | Reuse / Adapt / Integrate / Reference |
| Nivy mapping | Capability/department |
| Verification date | YYYY-MM-DD |

---

# 37. Reuse decision

For every discovered system:

**1. REUSE** — directly usable with configuration.

**2. ADAPT** — useful code/architecture/skills can be modified.

**3. INTEGRATE** — keep it external and connect through API/MCP/A2A/webhook.

**4. REFERENCE** — architecture/pattern is useful but code is not reusable.

**5. BUILD** — only after the above four do not cover the requirement.

Never copy a repository merely because it is open source. Verify the current license, dependencies, security posture, data handling, terms, and compatibility before incorporation.

---

# 38. Research coverage status

This catalog now covers the major **classes of agentic AI systems**, not merely RAG/memory.

Still-open discovery buckets:

- finance/CFO agents
- accounting/tax agents
- HR/recruiting agents
- legal/compliance agents
- procurement agents
- cybersecurity agents
- DevOps/SRE agents
- project-management agents
- product-management agents
- customer-success agents
- sales/SDR agents
- marketing/content/social agents
- ecommerce agents
- healthcare/medical agents
- education/tutoring agents
- scientific/lab agents
- investment/trading agents
- logistics/supply-chain agents
- real-estate agents
- government/public-sector agents
- travel/hospitality agents
- manufacturing/industrial agents
- robotics/embodied agents
- gaming agents
- simulation/world-model agents
- personal-life agents
- accessibility agents
- multilingual/localization agents
- legal-document/contract agents
- meeting/voice-memory agents
- email/calendar agents
- CRM/customer-memory agents
- federated/distributed agent systems
- self-improving/evolutionary agents
- agent security/red-team systems
- agent governance/RBAC/approval systems
- agent marketplaces/registries
- enterprise managed agent platforms

These should be added as dedicated domain catalogs rather than pretending this one file is complete.

---

## Source discovery references

The following living catalogs were used as discovery accelerators:

- https://github.com/aglio-lab/ai-agent-frameworks
- https://github.com/tysoncung/awesome-ai-agents
- https://github.com/korchasa/awesome-ai-agents
- https://github.com/NipunaRanasinghe/awesome-ai-agents
- https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026
- https://github.com/vivy-yi/awesome-agent-orchestration
- https://github.com/mnemoverse/awesome-agent-memory

**Important:** discovery registries are indexes, not proof of quality, maintenance, security, license compatibility, or production suitability. Each candidate must be verified at its canonical source before reuse.
