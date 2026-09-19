# AI Technology Universe — Gap Expansion Catalog (2026-09)

> Living discovery catalog for ready-made AI systems across technology families that are not limited to agent frameworks.
>
> Governing rule: **DISCOVER → VERIFY → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING.**

This file expands the technology universe beyond the existing agent, memory, workflow, and company-operation catalogs. It is a discovery index, not a ranking. A project appearing here does not mean it is production-ready for Nivy. Before adoption, verify current maintenance, license, dependencies, security, model/data terms, deployment requirements, and integration interfaces.

## 1. Technology coverage map

| Technology family | Ready-made systems / projects | Primary use | Link |
|---|---|---|---|
| Model hubs & open models | Hugging Face Hub, ModelScope, Ollama, llama.cpp | Discover/download/run models | https://huggingface.co/ |
| LLM serving | vLLM, SGLang, TensorRT-LLM, llama.cpp, ONNX Runtime, OpenVINO | High-throughput/local inference | https://github.com/vllm-project/vllm |
| API/model gateway | LiteLLM, OpenRouter, Portkey | One interface across model providers | https://github.com/BerriAI/litellm |
| Fine-tuning | LLaMA-Factory, Unsloth, Axolotl, TRL, ms-swift | SFT/LoRA/QLoRA/post-training | https://github.com/hiyouga/LLaMA-Factory |
| Training | PyTorch, JAX, DeepSpeed, Megatron-LM | Model training/distributed compute | https://github.com/pytorch/pytorch |
| Inference optimization | FlashAttention, FlashInfer, DeepSpeed, TensorRT-LLM | Memory/latency optimization | https://github.com/Dao-AILab/flash-attention |
| Quantization | AutoGPTQ, GPTQModel, AWQ, bitsandbytes, llama.cpp quantization | Smaller/faster model deployment | https://github.com/bitsandbytes-foundation/bitsandbytes |
| Vision-language AI | LLaVA, Qwen-VL ecosystem, Transformers | Image+text reasoning | https://github.com/LLaVA-VL/LLaVA |
| OCR/document AI | PaddleOCR, Docling, Tesseract, Surya | OCR, PDF/document extraction | https://github.com/PaddlePaddle/PaddleOCR |
| Document parsing | Docling, Marker, Unstructured, Apache Tika | Convert complex documents to structured data | https://github.com/docling-project/docling |
| Speech recognition | Whisper, faster-whisper, whisper.cpp | Speech-to-text | https://github.com/openai/whisper |
| Text-to-speech | Piper, Coqui TTS, OpenVoice | Voice synthesis | https://github.com/rhasspy/piper |
| Voice/real-time AI | LiveKit Agents, Pipecat, Vocode | Voice agents and realtime media | https://github.com/livekit/agents |
| Image generation | ComfyUI, Diffusers, InvokeAI, AUTOMATIC1111 | Generative images | https://github.com/comfyanonymous/ComfyUI |
| Video generation | Wan, CogVideo, Diffusers video pipelines, World-R1 | Generative video/world-aware video | https://github.com/Wan-Video/Wan2.1 |
| 3D generation | Shap-E, Hunyuan3D, NVIDIA Kaolin | Text/image-to-3D and 3D research | https://github.com/openai/shap-e |
| Digital humans / avatars | MuseTalk, Wav2Lip, SadTalker | Talking-head/avatar generation | https://github.com/TMElyralab/MuseTalk |
| Music/audio generation | AudioCraft, MusicGen, Stable Audio ecosystem | Music/sound generation | https://github.com/facebookresearch/audiocraft |
| Computer vision | OpenCV, Detectron2, Ultralytics, Segment Anything | Detection, segmentation, visual processing | https://github.com/opencv/opencv |
| Vision foundation models | DINOv2, SAM, Depth Anything, Transformers | Embeddings, segmentation, depth | https://github.com/facebookresearch/dinov2 |
| Synthetic data | SDV, Gretel, Mostly AI, SynthCity | Synthetic tabular/data generation | https://github.com/sdv-dev/SDV |
| Data labeling | Label Studio, CVAT | Human/AI-assisted annotation | https://github.com/HumanSignal/label-studio |
| Data integration | Airbyte, Meltano, Singer | Connectors and data movement | https://github.com/airbytehq/airbyte |
| Data orchestration | Airflow, Dagster, Prefect, Kestra | Scheduled/reliable data workflows | https://github.com/apache/airflow |
| Data quality | Great Expectations, Soda Core, dbt tests | Data validation/quality | https://github.com/great-expectations/great_expectations |
| Data catalog/governance | OpenMetadata, DataHub, Amundsen | Data discovery, lineage, governance | https://github.com/open-metadata/OpenMetadata |
| Lakehouse/table formats | Apache Iceberg, Delta Lake, Apache Hudi | Large-scale analytical storage | https://github.com/apache/iceberg |
| Vector/search | Qdrant, Weaviate, Milvus, pgvector, OpenSearch | Semantic/hybrid retrieval | https://github.com/qdrant/qdrant |
| Graph databases | Neo4j, Kuzu, Memgraph, FalkorDB, Apache AGE | Knowledge/context graphs | https://github.com/neo4j/neo4j |
| Search engines | OpenSearch, Elasticsearch, Vespa, Typesense | Full-text/hybrid search | https://github.com/opensearch-project/OpenSearch |
| Knowledge/RAG apps | RAGFlow, Onyx, AnythingLLM, Open WebUI | Ready-made private knowledge assistants | https://github.com/infiniflow/ragflow |
| ML experiment tracking | MLflow, Weights & Biases | Experiments/model lifecycle | https://github.com/mlflow/mlflow |
| ML serving platforms | KServe, BentoML, Ray Serve | Production model serving | https://github.com/kserve/kserve |
| Distributed compute | Ray, Spark, Dask | Scalable AI/data workloads | https://github.com/ray-project/ray |
| Reinforcement learning | Stable-Baselines3, Ray RLlib, CleanRL, TorchRL, VERL | Decision/post-training/RL | https://github.com/DLR-RM/stable-baselines3 |
| Optimization | OR-Tools, Optuna, BoTorch, Nevergrad | Scheduling/search/optimization | https://github.com/google/or-tools |
| Forecasting | NeuralForecast, StatsForecast, Darts, GluonTS | Demand/revenue/time-series forecasting | https://github.com/Nixtla/neuralforecast |
| Causal AI | DoWhy, EconML, CausalML, causal-learn | Causal inference/decision support | https://github.com/py-why/dowhy |
| Privacy-preserving AI | Flower, FedML, OpenFL, FATE, PySyft | Federated/privacy-preserving ML | https://github.com/adap/flower |
| Edge AI | ONNX Runtime, OpenVINO, ExecuTorch, LiteRT | On-device inference | https://github.com/microsoft/onnxruntime |
| Mobile AI | ExecuTorch, MediaPipe, ONNX Runtime Mobile | Android/iOS/edge inference | https://github.com/pytorch/executorch |
| Browser/computer use | Playwright, Browser Use, Skyvern, Stagehand, OSWorld | Web/GUI automation | https://github.com/browser-use/browser-use |
| Deep research | GPT Researcher, STORM, PaperQA, OpenDeepResearch | Multi-source research/synthesis | https://github.com/assafelovic/gpt-researcher |
| Web crawling/extraction | Crawl4AI, Firecrawl, Trafilatura, Scrapy | Web ingestion for AI | https://github.com/unclecode/crawl4ai |
| AI evaluation | DeepEval, RAGAS, Promptfoo, OpenAI Evals | Quality/evaluation testing | https://github.com/confident-ai/deepeval |
| LLM observability | Langfuse, Arize Phoenix, OpenLLMetry, AgentOps | Tracing/cost/evaluation | https://github.com/langfuse/langfuse |
| Guardrails | NeMo Guardrails, Guardrails AI, Presidio | Safety/policy/PII controls | https://github.com/NVIDIA-NeMo/Guardrails |
| AI security testing | Garak, PyRIT, AgentDojo | Adversarial/security testing | https://github.com/NVIDIA/garak |
| AI governance | Presidio, Open Policy Agent, InstructLab ecosystem | Policy, PII, governance | https://github.com/open-policy-agent/opa |
| Agent interoperability | MCP, A2A, AG-UI, OpenSharing | Tools/agent/data interoperability | https://github.com/modelcontextprotocol |
| Agent memory | Mem0, Zep, Letta, Graphiti, Cognee, LangMem | Persistent agent memory | https://github.com/mem0ai/mem0 |
| Agent runtimes | LangGraph, CrewAI, PydanticAI, Agno, Google ADK, Microsoft Agent Framework | Agent orchestration | https://github.com/langchain-ai/langgraph |
| AI workflow automation | n8n, Dify, Flowise, Activepieces, Windmill | Business automation | https://github.com/n8n-io/n8n |
| AI coding | OpenHands, Cline, Aider, Continue, Goose | Software engineering agents | https://github.com/All-Hands-AI/OpenHands |
| AI desktop/computer agents | Open Interpreter, OpenClaw-class systems, Agent Zero | General computer operation | https://github.com/OpenInterpreter/open-interpreter |
| Robotics middleware | ROS 2, Isaac Lab, LeRobot, MuJoCo | Physical/embodied AI | https://github.com/ros2/ros2 |
| Robotics policies | openpi, ACT ecosystem, Open X-Embodiment | Robot foundation policies | https://github.com/Physical-Intelligence/openpi |
| World models | NVIDIA Cosmos, DreamerV3, V-JEPA 2 ecosystem, DIAMOND | Simulated/environment prediction | https://github.com/nvidia-cosmos |
| Physical AI simulation | Isaac Sim, Isaac Lab, ManiSkill, MuJoCo | Robotics simulation/training | https://github.com/isaac-sim/IsaacLab |
| Digital twins | OpenUSD, NVIDIA Omniverse ecosystem, Project Chrono, OranSim | Executable/simulated systems | https://github.com/oran-ai/oransim |
| Neuro-symbolic AI | DeepProbLog, Logic Tensor Networks, PyReason | Symbolic + neural reasoning | https://github.com/ML-KULeuven/deepproblog |
| Quantum ML | PennyLane, Qiskit, TensorFlow Quantum | Quantum algorithms/ML research | https://github.com/PennyLaneAI/pennylane |
| Neuromorphic AI | Lava, Nengo, snnTorch | Spiking/neuromorphic computing | https://github.com/lava-nc/lava |
| Scientific AI | BioNeMo ecosystem, DeepChem, OpenFold, AlphaFold ecosystem | Biology/chemistry/science | https://github.com/deepchem/deepchem |
| Geospatial AI | TorchGeo, Raster Vision, GeoPandas, Segment Anything geospatial ecosystem | Earth/remote-sensing AI | https://github.com/microsoft/torchgeo |
| Healthcare AI | MONAI, OHIF, nnU-Net | Medical imaging/clinical research infrastructure | https://github.com/Project-MONAI/MONAI |
| Finance AI | FINOS projects, FinGPT, OpenBB | Financial data/research/AI | https://github.com/AI4Finance-Foundation/FinGPT |
| Accounting/finance operations | ERPNext, Odoo, Akaunting, Frappe ecosystem | Ledger/ERP/invoicing/operations backbone | https://github.com/frappe/erpnext |
| HR/recruiting AI | Open-source ATS/HR ecosystems + agent directories | Recruiting/HR automation | https://github.com/OpensourceHR/opensourcehr |
| Legal AI | Open-source legal NLP + contract-analysis ecosystems | Legal research/contracts | https://github.com/Law-AI |
| Cybersecurity AI | Wazuh, Zeek, Suricata, Security Onion ecosystem + AI layers | Detection/response/security telemetry | https://github.com/wazuh/wazuh |
| DevOps/SRE AI | OpenHands, SWE-agent, K8sGPT, Backstage | Engineering operations | https://github.com/k8sgpt-ai/k8sgpt |
| Product/research AI | GPT Researcher, STORM, LlamaIndex, DSPy | Product/market/user research | https://github.com/stanford-oval/storm |
| BI/analytics AI | Evidence, Metabase, Superset, Lightdash | Analytics/BI + AI interfaces | https://github.com/metabase/metabase |
| Customer support AI | Rasa, Dify, Botpress ecosystem, Onyx | Support/chat automation | https://github.com/RasaHQ/rasa |
| Commerce/e-commerce AI | Medusa, Saleor, Shopify ecosystem, Vendure | Commerce backend + AI extensions | https://github.com/medusajs/medusa |
| Recommendation AI | NVIDIA Merlin, RecBole, LightFM | Personalization/recommendations | https://github.com/NVIDIA-Merlin/Merlin |
| Graph ML | PyTorch Geometric, DGL | Graph representation/learning | https://github.com/pyg-team/pytorch_geometric |
| Explainable AI | SHAP, LIME, Captum | Model explanation/interpretability | https://github.com/shap/shap |
| Active learning | modAL, Small-Text, Label Studio workflows | Efficient labeling/model improvement | https://github.com/modAL-python/modAL |
| Model/data lineage | MLflow, OpenLineage, OpenMetadata | Provenance/lineage | https://github.com/OpenLineage/OpenLineage |
| AI asset exchange | OpenSharing ecosystem, model hubs, MCP registries | Exchange models/skills/data | https://github.com/OpenSharingProject |
| AI skill ecosystems | Agent Skills collections, Claude Skills, business skill libraries | Reusable procedural capability | https://github.com/anthropics/skills |
| AI app/workspace UI | Open WebUI, AnythingLLM, LibreChat, OpenHands | Unified user interfaces | https://github.com/open-webui/open-webui |
| Low-code AI app builders | Appsmith, Budibase, ToolJet, Dify | Internal apps/admin interfaces | https://github.com/appsmithorg/appsmith |
| API/backend building blocks | FastAPI, Pydantic, Supabase, Hasura | AI service/application backend | https://github.com/fastapi/fastapi |
| Workflow/temporal infrastructure | Temporal, Dagster, Prefect, Kestra | Durable business execution | https://github.com/temporalio/temporal |
| Identity/access | Keycloak, Authentik, Ory | SSO/RBAC/identity for AI systems | https://github.com/keycloak/keycloak |
| Policy/authorization | OpenFGA, OPA, Cerbos | Fine-grained authorization | https://github.com/openfga/openfga |
| Secrets/security | Vault, Infisical, SOPS | Secrets and credential management | https://github.com/hashicorp/vault |
| Container/orchestration | Docker, Kubernetes, K3s | Deployment substrate | https://github.com/kubernetes/kubernetes |

## 2. Industry-specific ready-made discovery lanes

The Nivy library must continue searching by **industry + workflow**, not just by technology:

| Industry / department | Search for ready-made systems |
|---|---|
| Marketing | SEO, content, social, ads, CRO, attribution, brand, creative, marketing intelligence |
| Sales | prospecting, enrichment, SDR, email, calling, qualification, proposal, forecasting, CRM |
| Customer Success | onboarding, health scoring, support, renewal, expansion, churn, advocacy |
| Finance | AP/AR, bookkeeping, FP&A, treasury, tax, audit evidence, reconciliation |
| HR | ATS, sourcing, screening, interview, onboarding, payroll, performance, LMS |
| Legal | contracts, clause extraction, legal research, compliance, privacy, KYC/KYB |
| Procurement | supplier discovery, RFQ, sourcing, vendor risk, purchase orders |
| Operations | SOPs, scheduling, workforce, QA, inventory, facilities, workflow |
| IT/Security | helpdesk, endpoint, SIEM, SOC, vulnerability, identity, incident response |
| Engineering | coding, code review, testing, CI/CD, SRE, architecture, documentation |
| Product | discovery, research, roadmap, specs, analytics, experimentation |
| Data/BI | ETL, warehouse, semantic layer, dashboards, forecasting, anomaly detection |
| Manufacturing | planning, quality, predictive maintenance, digital twin, robotics |
| Logistics | routing, fleet, warehouse, demand forecasting, supply chain |
| Real estate | property intelligence, valuation, lead management, document analysis |
| Education | tutoring, LMS, assessment, content, research, student support |
| Healthcare | imaging, clinical NLP, scheduling, research, drug discovery |
| Scientific | literature, simulation, chemistry, biology, materials, lab automation |
| Government | document processing, citizen support, procurement, public data, compliance |
| Media/creative | image, video, audio, 3D, avatars, localization, publishing |
| Accessibility | speech, OCR, vision assistance, translation, assistive interfaces |
| Localization | translation, transcription, dubbing, multilingual RAG/agents |
| Robotics | perception, planning, simulation, policies, control, fleet management |
| Edge/IoT | sensor AI, anomaly detection, local agents, privacy-preserving inference |

## 3. Nivy reuse record

Every discovered item should eventually be normalized into:

| Field | Required |
|---|---|
| ID | Yes |
| Technology family | Yes |
| Department / capability | Yes |
| System/project | Yes |
| Canonical URL | Yes |
| GitHub / source URL | If available |
| License | Verify |
| Open-source / source-available / SaaS | Yes |
| Self-hostable | Yes/No/Unknown |
| Model support | Yes |
| API / SDK | Yes |
| MCP / A2A | Yes/No/Unknown |
| Memory/RAG | Yes/No/Unknown |
| Multimodal | Yes/No/Unknown |
| Integrations | Yes |
| Deployment | Local/Docker/K8s/Cloud/etc. |
| Security/privacy | Verify |
| Maintenance/activity | Verify |
| Dependencies | Verify |
| Reuse method | Direct / Adapter / Fork / Inspired |
| Nivy target | V1/V2/Future |
| Verification date | Yes |
| Notes / limitations | Yes |

## 4. Current discovery signals

The 2026 ecosystem is broader than agent frameworks: current landscape work tracks model infrastructure, serving, training, data/compute, agent infrastructure, applications, memory/context, and safety/operations as separate layers. citeturn0search3turn0search12

The open-source AI stack is also expanding into retrieval, scientific models, compilers/model optimization, and storage/retrieval; one current map reports thousands of products across these categories. citeturn0search7

For enterprise reuse, interoperability, governance, identity, authorization, provenance and secure access are becoming explicit infrastructure requirements, not optional add-ons. citeturn0search1turn0search9

Physical AI/robotics, edge AI and smaller domain-specialized models are active technology lanes alongside general-purpose agent systems. citeturn0search4turn0search8

## 5. Important rule

Do **not** treat this catalog as complete. “All AI technology” is an expanding universe. The library should keep adding new categories whenever a technology family, business workflow, infrastructure layer, or emerging computing paradigm can materially contribute to Nivy.

The correct completion criterion is therefore:

**No known major technology family is intentionally omitted + every family has a discovery lane + reusable systems are continuously verified and added.**
