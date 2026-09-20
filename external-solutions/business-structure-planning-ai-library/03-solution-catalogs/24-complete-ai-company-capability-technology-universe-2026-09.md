# Complete AI-Native Company Capability & Technology Universe — 2026-09

**Purpose:** Expand the Nivy reuse library beyond JARVIS, creators, YouTube and marketing into the full capability stack required for an AI-native international company.

**Governing rule:** DISCOVER → DECOMPOSE → REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING.

> This is a capability map and reuse index, not a claim that every project is production-ready. Verify current maintenance, license, commercial rights, API/platform terms, security and regional availability before adoption.

## 1. Executive / JARVIS / proactive assistant

| Capability | Reuse candidates | Link |
|---|---|---|
| Desktop voice assistant | OpenDex/JARVIS | https://github.com/aviarytech/jarvis |
| Self-hosted voice assistant | PersonalJarvis | https://github.com/PersonalJarvis/PersonalJarvis |
| Local voice assistant | OpenJarvis | https://github.com/1nsaneeee/OpenJarvis |
| AI workspace | Open WebUI | https://github.com/open-webui/open-webui |
| Local AI runtime | Ollama | https://github.com/ollama/ollama |
| Desktop agent / computer use | OpenHands | https://github.com/All-Hands-AI/OpenHands |
| Computer interaction | Browser Use | https://github.com/browser-use/browser-use |
| Browser agent | Stagehand | https://github.com/browserbase/stagehand |

## 2. Real-time voice, phone and receptionist

| Capability | Reuse candidates | Link |
|---|---|---|
| Realtime voice agent infrastructure | LiveKit Agents | https://github.com/livekit/agents |
| Voice pipeline | Pipecat | https://github.com/pipecat-ai/pipecat |
| Voice agent framework | Vocode | https://github.com/vocodedev/vocode-core |
| Voice agent platform | Vapi | https://vapi.ai/ |
| Telephony/voice API | Telnyx | https://telnyx.com/ |
| Speech-to-text | Whisper | https://github.com/openai/whisper |
| Local STT | faster-whisper | https://github.com/SYSTRAN/faster-whisper |
| TTS | Piper | https://github.com/rhasspy/piper |
| TTS / voice generation | Coqui TTS | https://github.com/coqui-ai/TTS |
| Voice synthesis | ElevenLabs | https://elevenlabs.io/ |

LiveKit and Pipecat are important open-source building blocks for self-controlled realtime voice systems; voice vendors remain useful when managed telephony/deployment is preferred.

## 3. Agent frameworks and orchestration

| Capability | Reuse candidates | Link |
|---|---|---|
| Stateful agent graphs | LangGraph | https://github.com/langchain-ai/langgraph |
| Agent framework | CrewAI | https://github.com/crewAIInc/crewAI |
| Agent framework | Microsoft Agent Framework | https://github.com/microsoft/agent-framework |
| Agent/workflow platform | Dify | https://github.com/langgenius/dify |
| Agent framework | AutoGen | https://github.com/microsoft/autogen |
| Agent framework | Semantic Kernel | https://github.com/microsoft/semantic-kernel |
| Multi-agent framework | MetaGPT | https://github.com/FoundationAgents/MetaGPT |
| Agent runtime | LlamaIndex | https://github.com/run-llama/llama_index |

## 4. MCP / A2A / interoperability

| Capability | Resource | Link |
|---|---|---|
| Tool/data protocol | Model Context Protocol | https://modelcontextprotocol.io/ |
| MCP SDKs | MCP GitHub | https://github.com/modelcontextprotocol |
| Agent-to-agent protocol | A2A | https://a2a-protocol.org/ |
| A2A implementation | A2A GitHub | https://github.com/a2aproject/A2A |
| Agent communication | ACP | https://agentcommunicationprotocol.dev/ |

**Nivy principle:** MCP = agent → tool/data; A2A = agent → agent. Keep the two layers separate.

## 5. Workflow / automation / event orchestration

| Capability | Reuse candidates | Link |
|---|---|---|
| General automation | n8n | https://github.com/n8n-io/n8n |
| Workflow automation | Activepieces | https://github.com/activepieces/activepieces |
| Workflow engine | Temporal | https://github.com/temporalio/temporal |
| Workflow engine | Prefect | https://github.com/PrefectHQ/prefect |
| Data/ML workflows | Dagster | https://github.com/dagster-io/dagster |
| Event streaming | Apache Kafka | https://github.com/apache/kafka |
| Event streaming | Redpanda | https://github.com/redpanda-data/redpanda |

## 6. Company OS / ERP / CRM

| Capability | Reuse candidates | Link |
|---|---|---|
| ERP/CRM | Odoo | https://github.com/odoo/odoo |
| ERP | ERPNext | https://github.com/frappe/erpnext |
| ERP / AI ERP | Sentinel ERP | https://github.com/sentinel-erp |
| AI-native ERP/accounting | ERPClaw | https://github.com/erpclaw |
| CRM | Twenty | https://github.com/twentyhq/twenty |
| Agentic CRM | Comp AI CRM | https://github.com/trycompai/crm |
| CRM/data platform | NocoDB | https://github.com/nocodb/nocodb |
| Internal apps | Appsmith | https://github.com/appsmithorg/appsmith |

## 7. Unified Nivy UI / employee workspace

| Capability | Reuse candidates | Link |
|---|---|---|
| React admin framework | Refine | https://github.com/refinedev/refine |
| UI components | shadcn/ui | https://github.com/shadcn-ui/ui |
| Dashboard UI | Tremor | https://github.com/tremorlabs/tremor |
| Internal tools | Appsmith | https://github.com/appsmithorg/appsmith |
| Low-code apps | ToolJet | https://github.com/ToolJet/ToolJet |
| Open-source workspace | AFFiNE | https://github.com/toeverything/AFFiNE |
| Knowledge workspace | AppFlowy | https://github.com/AppFlowy-IO/AppFlowy |

## 8. Identity / RBAC / authorization / secrets

| Capability | Reuse candidates | Link |
|---|---|---|
| IAM/SSO | Keycloak | https://github.com/keycloak/keycloak |
| Fine-grained authorization | OpenFGA | https://github.com/openfga/openfga |
| Policy engine | Open Policy Agent | https://github.com/open-policy-agent/opa |
| Identity provider | Authentik | https://github.com/goauthentik/authentik |
| Secrets | OpenBao | https://github.com/openbao/openbao |
| Secrets | Infisical | https://github.com/Infisical/infisical |

Nivy should combine identity + role + resource + action + approval policy rather than using simple UI hiding as authorization.

## 9. Memory / RAG / knowledge

| Capability | Reuse candidates | Link |
|---|---|---|
| RAG framework | LlamaIndex | https://github.com/run-llama/llama_index |
| RAG framework | Haystack | https://github.com/deepset-ai/haystack |
| LLM framework | LangChain | https://github.com/langchain-ai/langchain |
| Vector DB | Qdrant | https://github.com/qdrant/qdrant |
| Vector DB | Weaviate | https://github.com/weaviate/weaviate |
| Vector DB | Milvus | https://github.com/milvus-io/milvus |
| Vector DB | Chroma | https://github.com/chroma-core/chroma |
| Search engine | OpenSearch | https://github.com/opensearch-project/OpenSearch |
| Knowledge base | Outline | https://github.com/outline/outline |
| Documents | Paperless-ngx | https://github.com/paperless-ngx/paperless-ngx |
| Files | Nextcloud | https://github.com/nextcloud/server |

## 10. Deep research / OSINT / intelligence

| Capability | Reuse candidates | Link |
|---|---|---|
| Deep research | GPT Researcher | https://github.com/assafelovic/gpt-researcher |
| Deep research | STORM | https://github.com/stanford-oval/storm |
| Deep research | Deep Research agents catalog | https://github.com/tarun7r/deep-research-agent |
| Competitive intelligence | CompeteInsight | https://github.com/SHYTHU49/CompeteInsight |
| Web crawling | Crawl4AI | https://github.com/unclecode/crawl4ai |
| Web extraction | Firecrawl | https://github.com/mendableai/firecrawl |
| Scraping | Scrapy | https://github.com/scrapy/scrapy |
| Internet search | SearXNG | https://github.com/searxng/searxng |

## 11. Social listening / competitor / creator intelligence

| Capability | Reuse candidates | Link |
|---|---|---|
| Social agent | SamurAIGPT AI Social Agent | https://github.com/SamurAIGPT/open-ai-social-agent |
| Social automation | Social Agent AI | https://github.com/amanullahpy/social-media-agent-ai |
| Social browser agent | LocoAgent | https://github.com/LocoreMind/locoagent |
| Social agent benchmark | SoMe | https://github.com/LivXue/SoMe |
| Social publishing/ORM | Mesh Pilot AI Social Agent | https://github.com/Meshpilot-AGI/ai-social-agent |
| Social media scheduling | Postiz | https://github.com/gitroomhq/postiz |
| Social media management | Mixpost | https://github.com/inovector/mixpost |

## 12. SEO / AEO / GEO / AI visibility

| Capability | Reuse candidates | Link |
|---|---|---|
| AEO/SEO catalog | Awesome AEO SEO Tools | https://github.com/discoveredlabs/awesome-aeo-seo-tools |
| SEO/AEO/GEO catalog | awesome-seo-tools | https://github.com/XiaomingX/awesome-seo-tools |
| AI-search audit | foglift-scan | https://foglift.io/blog/open-source-geo-tools |
| SEO crawler | Ahrefs Webmaster Tools | https://ahrefs.com/webmaster-tools |
| Technical SEO crawler | Screaming Frog | https://www.screamingfrog.co.uk/seo-spider/ |
| Search console | Google Search Console | https://search.google.com/search-console/ |
| Structured data | Schema.org | https://schema.org/ |

## 13. Content / copy / editorial

| Capability | Reuse candidates | Link |
|---|---|---|
| AI writing workspace | Open WebUI | https://github.com/open-webui/open-webui |
| Local LLM | Ollama | https://github.com/ollama/ollama |
| Prompt management | Promptfoo | https://github.com/promptfoo/promptfoo |
| Prompt/version testing | Langfuse | https://github.com/langfuse/langfuse |
| Editorial knowledge | Outline | https://github.com/outline/outline |

## 14. Image / design / creative factory

| Capability | Reuse candidates | Link |
|---|---|---|
| Generative workflow | ComfyUI | https://github.com/comfyanonymous/ComfyUI |
| Image generation | Stable Diffusion | https://github.com/Stability-AI/generative-models |
| Image generation UI | AUTOMATIC1111 | https://github.com/AUTOMATIC1111/stable-diffusion-webui |
| Design editor | Penpot | https://github.com/penpot/penpot |
| Graphics editor | Photopea | https://www.photopea.com/ |
| Image processing | ImageMagick | https://github.com/ImageMagick/ImageMagick |

## 15. Video / YouTube / podcast / UGC

| Capability | Reuse candidates | Link |
|---|---|---|
| YouTube automation | YouTube Automation Agent | https://github.com/Virendrabodele/youtube-automation-agent |
| YouTube autopilot | youtube-autopilot | https://github.com/khaoss85/youtube-autopilot |
| Podcast → Shorts | Podcast Shorts Factory | https://github.com/krakonjac300-pixel/podcast-shorts-factory |
| UGC ads | Open AI UGC | https://github.com/siriokun/ugc |
| AI ad studio | Atlas Marketing Studio | https://github.com/AtlasCloudAI/atlas-marketing-studio |
| Media processing | FFmpeg | https://github.com/FFmpeg/FFmpeg |
| Video editor | Shotcut | https://github.com/mltframework/shotcut |
| Video editor | Kdenlive | https://github.com/KDE/kdenlive |

## 16. Avatar / digital human / AI influencer

| Capability | Reuse candidates | Link |
|---|---|---|
| Talking portrait | SadTalker | https://github.com/OpenTalker/SadTalker |
| Lip sync | Wav2Lip | https://github.com/Rudrabha/Wav2Lip |
| Real-time lip sync | MuseTalk | https://github.com/TMElyralab/MuseTalk |
| Portrait animation | LivePortrait | https://github.com/KwaiVGI/LivePortrait |
| 3D avatar | Wav2Lip + 3D/Blender pipeline | https://www.blender.org/ |
| Avatar generation | HeyGen | https://www.heygen.com/ |
| Avatar video | Synthesia | https://www.synthesia.io/ |

## 17. Sales / lead generation / proposals

| Capability | Reuse candidates | Link |
|---|---|---|
| Agentic CRM | Comp AI CRM | https://github.com/trycompai/crm |
| CRM intelligence | AI-CRM | https://github.com/xragrawal/AI-CRM |
| Pre-sales/RFP | Pre-Sales Agent | https://github.com/Blazity/pre-sales-agent |
| Sales automation | n8n | https://github.com/n8n-io/n8n |
| CRM | Twenty | https://github.com/twentyhq/twenty |
| Sales CRM | Odoo CRM | https://github.com/odoo/odoo |

## 18. Customer support / success / helpdesk

| Capability | Reuse candidates | Link |
|---|---|---|
| Helpdesk | Zammad | https://github.com/zammad/zammad |
| Helpdesk | FreeScout | https://github.com/freescout-helpdesk/freescout |
| Customer support | Chatwoot | https://github.com/chatwoot/chatwoot |
| AI chat | Dify | https://github.com/langgenius/dify |
| Knowledge support | RAG/Haystack | https://github.com/deepset-ai/haystack |

## 19. HR / recruiting / employee operations

| Capability | Reuse candidates | Link |
|---|---|---|
| HRMS | OrangeHRM | https://github.com/orangehrm/orangehrm |
| HR/ERP | ERPNext HR | https://github.com/frappe/hrms |
| Recruiting | OpenCATS | https://github.com/opencats/OpenCATS |
| Recruiting / ATS | GoRecruit | https://github.com/gorecruit/gorecruit |
| Employee portal | Staff/HR portal patterns | https://github.com/frappe/hrms |

Use AI for sourcing, screening, interview scheduling, onboarding and knowledge assistance, but keep consequential employment decisions human-governed.

## 20. Finance / accounting / CFO

| Capability | Reuse candidates | Link |
|---|---|---|
| ERP accounting | Odoo | https://github.com/odoo/odoo |
| ERP accounting | ERPNext | https://github.com/frappe/erpnext |
| Accounting | Akaunting | https://github.com/akaunting/akaunting |
| Accounting | GnuCash | https://github.com/Gnucash/gnucash |
| AI accounting | ERPClaw | https://github.com/erpclaw |
| Finance OSS ecosystem | FINOS | https://github.com/finos |

## 21. Procurement / vendor management

| Capability | Reuse candidates | Link |
|---|---|---|
| ERP procurement | ERPNext | https://github.com/frappe/erpnext |
| ERP procurement | Odoo | https://github.com/odoo/odoo |
| Open procurement ecosystem | OpenProcurement | https://github.com/openprocurement |
| Supplier intelligence | Company research/deep research agents | https://github.com/assafelovic/gpt-researcher |

## 22. Legal / contracts / compliance

| Capability | Reuse candidates | Link |
|---|---|---|
| Legal agent organization | GLAW | https://github.com/rikitrader/glaw |
| Contract/document analysis | Haystack | https://github.com/deepset-ai/haystack |
| Document OCR | OCRmyPDF | https://github.com/ocrmypdf/OCRmyPDF |
| Document extraction | Unstructured | https://github.com/Unstructured-IO/unstructured |
| Compliance framework reference | NIST CSF | https://www.nist.gov/cyberframework |

Legal outputs should be treated as assisted work product and reviewed by qualified professionals where required.

## 23. IT / DevOps / SRE

| Capability | Reuse candidates | Link |
|---|---|---|
| AI coding agent | OpenHands | https://github.com/All-Hands-AI/OpenHands |
| Git platform | GitHub | https://github.com/ |
| CI/CD | GitHub Actions | https://github.com/features/actions |
| Containers | Docker | https://github.com/docker |
| Kubernetes | Kubernetes | https://github.com/kubernetes/kubernetes |
| GitOps | Argo CD | https://github.com/argoproj/argo-cd |
| Infrastructure as code | OpenTofu | https://github.com/opentofu/opentofu |
| Config automation | Ansible | https://github.com/ansible/ansible |

## 24. Cybersecurity / SOC / incident response

| Capability | Reuse candidates | Link |
|---|---|---|
| SIEM/XDR | Wazuh | https://github.com/wazuh/wazuh |
| Security monitoring | Security Onion | https://securityonionsolutions.org/ |
| Incident response | TheHive | https://github.com/TheHive-Project/TheHive |
| Threat intel | MISP | https://github.com/MISP/MISP |
| Network analysis | Zeek | https://github.com/zeek/zeek |
| IDS | Suricata | https://github.com/OISF/suricata |
| Vulnerability scanning | Greenbone/OpenVAS | https://github.com/greenbone/openvas-scanner |

## 25. Observability / agent tracing / evaluation

| Capability | Reuse candidates | Link |
|---|---|---|
| LLM observability/evaluation | Phoenix | https://github.com/Arize-ai/phoenix |
| LLM observability | Langfuse | https://github.com/langfuse/langfuse |
| LLM evaluation | Promptfoo | https://github.com/promptfoo/promptfoo |
| LLM evaluation | DeepEval | https://github.com/confident-ai/deepeval |
| General observability | OpenTelemetry | https://github.com/open-telemetry/opentelemetry-collector |
| Metrics | Prometheus | https://github.com/prometheus/prometheus |
| Dashboards | Grafana | https://github.com/grafana/grafana |

Every Nivy AI employee should have measurable success criteria, traceability, failure handling and cost visibility.

## 26. Data / databases / search / pipelines

| Capability | Reuse candidates | Link |
|---|---|---|
| Relational DB | PostgreSQL | https://github.com/postgres/postgres |
| Cache | Redis | https://github.com/redis/redis |
| Search | OpenSearch | https://github.com/opensearch-project/OpenSearch |
| Data transformation | dbt-core | https://github.com/dbt-labs/dbt-core |
| ETL | Airbyte | https://github.com/airbytehq/airbyte |
| Data integration | Meltano | https://github.com/meltano/meltano |
| Lakehouse | Apache Iceberg | https://github.com/apache/iceberg |
| OLAP | ClickHouse | https://github.com/ClickHouse/ClickHouse |

## 27. BI / analytics / decision intelligence

| Capability | Reuse candidates | Link |
|---|---|---|
| BI | Metabase | https://github.com/metabase/metabase |
| BI | Apache Superset | https://github.com/apache/superset |
| Observability dashboards | Grafana | https://github.com/grafana/grafana |
| Data notebooks | Jupyter | https://github.com/jupyter/notebook |
| Data science | pandas | https://github.com/pandas-dev/pandas |
| Forecasting | Nixtla | https://github.com/Nixtla/statsforecast |

## 28. Projects / tasks / OKRs

| Capability | Reuse candidates | Link |
|---|---|---|
| Project management | Plane | https://github.com/makeplane/plane |
| Project management | OpenProject | https://github.com/opf/openproject |
| Task/project | Taiga | https://github.com/taigaio/taiga-back |
| Goals/OKRs | Super Productivity + custom OKR layer | https://github.com/johannesjo/super-productivity |
| Team playbooks | Atlassian Team Playbook | https://www.atlassian.com/team-playbook |

## 29. Meetings / calendar / collaboration

| Capability | Reuse candidates | Link |
|---|---|---|
| Video meetings | Jitsi Meet | https://github.com/jitsi/jitsi-meet |
| Calendar | Cal.com | https://github.com/calcom/cal.com |
| Team chat | Mattermost | https://github.com/mattermost/mattermost |
| Team chat | Rocket.Chat | https://github.com/RocketChat/Rocket.Chat |
| Collaborative docs | Outline | https://github.com/outline/outline |

## 30. Documents / OCR / e-sign / records

| Capability | Reuse candidates | Link |
|---|---|---|
| Document management | Paperless-ngx | https://github.com/paperless-ngx/paperless-ngx |
| OCR | OCRmyPDF | https://github.com/ocrmypdf/OCRmyPDF |
| Document extraction | Unstructured | https://github.com/Unstructured-IO/unstructured |
| PDF tooling | PyMuPDF | https://github.com/pymupdf/PyMuPDF |
| E-signature | Documenso | https://github.com/documenso/documenso |
| Files/cloud | Nextcloud | https://github.com/nextcloud/server |

## 31. Product / engineering / QA

| Capability | Reuse candidates | Link |
|---|---|---|
| AI coding agent | OpenHands | https://github.com/All-Hands-AI/OpenHands |
| Code agent | SWE-agent | https://github.com/SWE-agent/SWE-agent |
| Software testing | Playwright | https://github.com/microsoft/playwright |
| Browser testing | Cypress | https://github.com/cypress-io/cypress |
| API testing | Hoppscotch | https://github.com/hoppscotch/hoppscotch |
| Feature flags | Flagsmith | https://github.com/Flagsmith/flagsmith |
| Product analytics | PostHog | https://github.com/PostHog/posthog |

## 32. Ecommerce / commerce agents

| Capability | Reuse candidates | Link |
|---|---|---|
| Ecommerce | Medusa | https://github.com/medusajs/medusa |
| Ecommerce | Saleor | https://github.com/saleor/saleor |
| Commerce | Vendure | https://github.com/vendure-ecommerce/vendure |
| Commerce | Smartstore | https://github.com/smartstore/Smartstore |
| Recommendation | OpenOneRec | https://github.com/ |
| AI commerce | KARTIQUE | https://github.com/ |

## 33. Marketing ads / creative optimization

| Capability | Reuse candidates | Link |
|---|---|---|
| Ad creative agent | Creative Ad Agent | https://github.com/DV0x/creative-ad-agent |
| AI ad studio | Atlas Marketing Studio | https://github.com/AtlasCloudAI/atlas-marketing-studio |
| UGC ads | Open AI UGC | https://github.com/siriokun/ugc |
| Workflow automation | n8n | https://github.com/n8n-io/n8n |
| Analytics | Metabase | https://github.com/metabase/metabase |

## 34. PR / newsroom / podcast / events

| Capability | Reuse candidates | Link |
|---|---|---|
| Podcast production | Podcast Shorts Factory | https://github.com/krakonjac300-pixel/podcast-shorts-factory |
| Video production | FFmpeg | https://github.com/FFmpeg/FFmpeg |
| Live streaming | Owncast | https://github.com/owncast/owncast |
| Webinar/video meetings | Jitsi | https://github.com/jitsi/jitsi-meet |
| Research/news monitoring | SearXNG | https://github.com/searxng/searxng |

## 35. Partner / affiliate / creator ecosystem

| Capability | Reuse candidates | Link |
|---|---|---|
| Creator discovery | AI Social Agent | https://github.com/SamurAIGPT/open-ai-social-agent |
| Affiliate/referral tracking | Solidus / commerce extensions | https://github.com/solidusio/solidus |
| Community platform | Discourse | https://github.com/discourse/discourse |
| Community chat | Mattermost | https://github.com/mattermost/mattermost |

## 36. Community / customer community

| Capability | Reuse candidates | Link |
|---|---|---|
| Community forum | Discourse | https://github.com/discourse/discourse |
| Community platform | Flarum | https://github.com/flarum/flarum |
| Chat community | Mattermost | https://github.com/mattermost/mattermost |
| Chat/community | Rocket.Chat | https://github.com/RocketChat/Rocket.Chat |

## 37. Notifications / messaging

| Capability | Reuse candidates | Link |
|---|---|---|
| Push notifications | Novu | https://github.com/novuhq/novu |
| Email infrastructure | Postal | https://github.com/postalserver/postal |
| Transactional email | Listmonk | https://github.com/knadh/listmonk |
| Customer messaging | Chatwoot | https://github.com/chatwoot/chatwoot |

## 38. Payments / billing / subscriptions

| Capability | Reuse candidates | Link |
|---|---|---|
| Billing | Lago | https://github.com/getlago/lago |
| Payments | Kill Bill | https://github.com/killbill/killbill |
| Payments | Stripe | https://stripe.com/ |
| India payments | Razorpay | https://razorpay.com/ |
| Open banking/payments reference | FINOS | https://github.com/finos |

## 39. Maps / location / field operations

| Capability | Reuse candidates | Link |
|---|---|---|
| Maps | OpenStreetMap | https://www.openstreetmap.org/ |
| Map rendering | MapLibre | https://github.com/maplibre/maplibre-gl-js |
| GIS | QGIS | https://github.com/qgis/QGIS |
| Routing | OSRM | https://github.com/Project-OSRM/osrm-backend |

## 40. IoT / edge / physical operations

| Capability | Reuse candidates | Link |
|---|---|---|
| IoT platform | ThingsBoard | https://github.com/thingsboard/thingsboard |
| MQTT | Eclipse Mosquitto | https://github.com/eclipse-mosquitto/mosquitto |
| Home/edge automation | Home Assistant | https://github.com/home-assistant/core |
| Edge AI | NVIDIA DeepStream | https://github.com/NVIDIA-AI-IOT/deepstream_reference_apps |

## 41. Computer vision / OCR / document intelligence

| Capability | Reuse candidates | Link |
|---|---|---|
| Computer vision | OpenCV | https://github.com/opencv/opencv |
| OCR | Tesseract | https://github.com/tesseract-ocr/tesseract |
| OCR/PDF | OCRmyPDF | https://github.com/ocrmypdf/OCRmyPDF |
| Document AI | DocTR | https://github.com/mindee/doctr |
| Document parsing | Unstructured | https://github.com/Unstructured-IO/unstructured |

## 42. Speech / translation / multilingual

| Capability | Reuse candidates | Link |
|---|---|---|
| STT | Whisper | https://github.com/openai/whisper |
| Fast STT | faster-whisper | https://github.com/SYSTRAN/faster-whisper |
| TTS | Piper | https://github.com/rhasspy/piper |
| Translation | LibreTranslate | https://github.com/LibreTranslate/LibreTranslate |
| Translation models | NLLB | https://huggingface.co/facebook/nllb-200-distilled-600M |

## 43. Model serving / inference / AI infrastructure

| Capability | Reuse candidates | Link |
|---|---|---|
| Local model runtime | Ollama | https://github.com/ollama/ollama |
| High-performance inference | vLLM | https://github.com/vllm-project/vllm |
| Inference server | NVIDIA Triton | https://github.com/triton-inference-server/server |
| Model serving | BentoML | https://github.com/bentoml/BentoML |
| Distributed compute | Ray | https://github.com/ray-project/ray |
| Model registry | MLflow | https://github.com/mlflow/mlflow |

## 44. Model discovery / open models

| Capability | Reuse candidates | Link |
|---|---|---|
| Model hub | Hugging Face | https://huggingface.co/ |
| Open model catalog | Ollama library | https://ollama.com/library |
| Model runtime | llama.cpp | https://github.com/ggml-org/llama.cpp |
| Quantized inference | llama.cpp | https://github.com/ggml-org/llama.cpp |

## 45. Guardrails / safety / policy enforcement

| Capability | Reuse candidates | Link |
|---|---|---|
| AI safety/guardrails | NeMo Guardrails | https://github.com/NVIDIA/NeMo-Guardrails |
| LLM security testing | Garak | https://github.com/NVIDIA/garak |
| Prompt testing | Promptfoo | https://github.com/promptfoo/promptfoo |
| Policy engine | OPA | https://github.com/open-policy-agent/opa |
| Secrets | OpenBao | https://github.com/openbao/openbao |

## 46. Agent security / permissions / audit

Nivy should implement:

**Identity → Agent identity → Tool permission → Data permission → Action policy → Risk classification → Approval → Execution → Audit → Rollback/compensation.**

Useful foundations:
- Keycloak — https://github.com/keycloak/keycloak
- OpenFGA — https://github.com/openfga/openfga
- OPA — https://github.com/open-policy-agent/opa
- OpenBao — https://github.com/openbao/openbao
- OpenTelemetry — https://github.com/open-telemetry/opentelemetry-collector

## 47. Agent memory / long-running work

| Capability | Reuse candidates | Link |
|---|---|---|
| Agent memory | Mem0 | https://github.com/mem0ai/mem0 |
| Knowledge graph | Neo4j | https://github.com/neo4j/neo4j |
| Graph database | Apache AGE | https://github.com/apache/age |
| Vector memory | Qdrant | https://github.com/qdrant/qdrant |
| RAG | LlamaIndex | https://github.com/run-llama/llama_index |

## 48. Knowledge graph / company digital twin

Recommended Nivy graph:

**Company → Brand → Country → Department → Role → Person → AI Employee → Skill → Tool → Workflow → Goal → KPI → Customer → Contact → Lead → Opportunity → Proposal → Contract → Project → Task → Product → Vendor → Invoice → Payment → Document → Knowledge → Risk → Approval → Audit Event.**

Reusable:
- Neo4j — https://github.com/neo4j/neo4j
- Apache AGE — https://github.com/apache/age
- Qdrant — https://github.com/qdrant/qdrant
- PostgreSQL — https://github.com/postgres/postgres

## 49. Digital twin / simulation / forecasting

| Capability | Reuse candidates | Link |
|---|---|---|
| Simulation platform | OpenModelica | https://github.com/OpenModelica/OpenModelica |
| Digital twin platform | Eclipse Ditto | https://github.com/eclipse-ditto/ditto |
| Forecasting | StatsForecast | https://github.com/Nixtla/statsforecast |
| ML | scikit-learn | https://github.com/scikit-learn/scikit-learn |

## 50. AI experimentation / A-B testing / optimization

| Capability | Reuse candidates | Link |
|---|---|---|
| Experiment tracking | MLflow | https://github.com/mlflow/mlflow |
| LLM experiments | Phoenix | https://github.com/Arize-ai/phoenix |
| Prompt experiments | Langfuse | https://github.com/langfuse/langfuse |
| LLM testing | Promptfoo | https://github.com/promptfoo/promptfoo |
| Product experimentation | GrowthBook | https://github.com/growthbook/growthbook |

## 51. Cost / FinOps / AI spend

| Capability | Reuse candidates | Link |
|---|---|---|
| Cloud cost management | OpenCost | https://github.com/opencost/opencost |
| FinOps | OpenCost | https://www.opencost.io/ |
| LLM observability/cost | Langfuse | https://github.com/langfuse/langfuse |
| LLM observability | Phoenix | https://github.com/Arize-ai/phoenix |

Nivy should track cost per agent, workflow, customer, department, task and revenue outcome.

## 52. Backup / disaster recovery / business continuity

| Capability | Reuse candidates | Link |
|---|---|---|
| Backup | Restic | https://github.com/restic/restic |
| Backup server | BorgBackup | https://github.com/borgbackup/borg |
| Database backup | pgBackRest | https://github.com/pgbackrest/pgbackrest |
| Monitoring | Uptime Kuma | https://github.com/louislam/uptime-kuma |

## 53. Monitoring / uptime / incident management

| Capability | Reuse candidates | Link |
|---|---|---|
| Monitoring | Prometheus | https://github.com/prometheus/prometheus |
| Dashboards | Grafana | https://github.com/grafana/grafana |
| Uptime | Uptime Kuma | https://github.com/louislam/uptime-kuma |
| Incident management | Grafana OnCall | https://github.com/grafana/mimir |

## 54. Search / discovery / internal universal search

| Capability | Reuse candidates | Link |
|---|---|---|
| Web search | SearXNG | https://github.com/searxng/searxng |
| Enterprise search | OpenSearch | https://github.com/opensearch-project/OpenSearch |
| Vector search | Qdrant | https://github.com/qdrant/qdrant |
| Hybrid retrieval | Weaviate | https://github.com/weaviate/weaviate |

Nivy search should search **people + work + CRM + documents + knowledge + agents + tasks + customers + research + audit**, not just files.

## 55. AI employee lifecycle

Required capabilities:

**Recruit AI employee → define role → assign manager → define goals/KPIs → attach skills → attach tools → define memory scope → define permissions → test → activate → monitor → evaluate → retrain/update → suspend → archive.**

Useful foundations:
- CompanyOS — https://github.com/rojenwai/CompanyOS
- AgentOS — https://github.com/SapienXai/AgentOS
- LangGraph — https://github.com/langchain-ai/langgraph
- MCP — https://modelcontextprotocol.io/
- A2A — https://a2a-protocol.org/

## 56. AI manager / department orchestration

Recommended hierarchy:

**CEO/Owner → Executive AI → Department Head AI → Manager AI → Specialist AI → Task Agent**

Managers should:
- distribute work
- check dependencies
- review outputs
- monitor KPIs
- escalate exceptions
- request human approval
- reassign failed tasks
- produce daily/weekly reports

Useful references:
- CompanyOS — https://github.com/rojenwai/CompanyOS
- Cyber AI Team — https://github.com/Hyper-AI-Lab/cyber-ai-team
- Bizbox — https://github.com/zesthq/bizbox
- CrewAI — https://github.com/crewAIInc/crewAI

## 57. Proactive intelligence / alerts

Nivy should continuously monitor:

**Sales ↓ → leads ↓ → website ↓ → ad performance ↓ → competitor change → social trend → customer complaint → overdue task → KPI miss → cash-flow risk → security alert → contract renewal → hiring need → opportunity.**

Building blocks:
- n8n — https://github.com/n8n-io/n8n
- Temporal — https://github.com/temporalio/temporal
- Prometheus — https://github.com/prometheus/prometheus
- Grafana — https://github.com/grafana/grafana
- OpenTelemetry — https://github.com/open-telemetry/opentelemetry-collector

## 58. Board / executive reporting

Required pipeline:

**Operational data → KPI computation → anomaly detection → causal/context research → executive summary → risks → opportunities → recommended actions → approval/tasks.**

Reuse:
- Metabase — https://github.com/metabase/metabase
- Superset — https://github.com/apache/superset
- Grafana — https://github.com/grafana/grafana
- Deep Research — https://github.com/assafelovic/gpt-researcher

## 59. Internationalization / multi-country operations

Nivy must model:

**Country → legal entity → currency → timezone → tax regime → payroll → banking/payment rails → language → local regulations → data residency → sales channel → market → customer segment.**

Useful systems:
- Odoo — https://github.com/odoo/odoo
- ERPNext — https://github.com/frappe/erpnext
- ERPClaw — https://github.com/erpclaw
- FINOS — https://github.com/finos

## 60. Complete Nivy AI operating loop

The target system is:

**VOICE / CHAT / UI / API / EVENT**
→ Identity
→ Intent
→ Context
→ Memory
→ Company Digital Twin
→ Planner
→ AI Manager
→ AI Employee
→ Skills
→ MCP Tools
→ A2A Agents
→ Workflow
→ Risk Gate
→ Human Approval
→ Execution
→ Verification
→ Audit
→ KPI
→ Knowledge update
→ Proactive monitoring
→ Next action.

## 61. Nivy capability checklist

Before calling the Company OS complete, check:

- [ ] Executive/JARVIS
- [ ] Voice
- [ ] Phone/receptionist
- [ ] Computer use
- [ ] Browser automation
- [ ] Agent orchestration
- [ ] MCP
- [ ] A2A
- [ ] Workflow engine
- [ ] ERP
- [ ] CRM
- [ ] Unified UI
- [ ] Identity
- [ ] RBAC/ABAC
- [ ] Approval engine
- [ ] Audit
- [ ] Memory
- [ ] RAG
- [ ] Knowledge graph
- [ ] Digital twin
- [ ] Deep research
- [ ] OSINT
- [ ] Social intelligence
- [ ] SEO
- [ ] AEO/GEO
- [ ] Content
- [ ] Design
- [ ] Image
- [ ] Video
- [ ] YouTube
- [ ] Podcast
- [ ] UGC
- [ ] AI influencer/avatar
- [ ] Sales
- [ ] Lead generation
- [ ] Proposals/RFP
- [ ] Customer support
- [ ] Customer success
- [ ] Finance/accounting/CFO
- [ ] HR/recruiting
- [ ] Procurement
- [Legal/compliance]
- [ ] IT
- [ ] DevOps/SRE
- [ ] Cybersecurity/SOC
- [ ] Product
- [ ] Engineering
- [ ] QA
- [ ] Projects
- [ ] OKRs
- [ ] BI
- [ ] Decision intelligence
- [ ] Data pipelines
- [ ] Search
- [ ] Documents/OCR
- [ ] Ecommerce
- [ ] Ads
- [ ] PR/newsroom
- [ ] Events
- [ ] Community
- [ ] Messaging/notifications
- [ ] Payments/billing
- [ ] Maps/field operations
- [ ] IoT/edge
- [ ] Computer vision
- [ ] Speech/translation
- [ ] Model serving
- [ ] Model evaluation
- [ ] Guardrails
- [ ] Observability
- [ ] Cost/FinOps
- [ ] Backup/DR
- [ ] Monitoring
- [ ] Internationalization
- [ ] Executive/board reporting
- [ ] Proactive alerts
- [ ] AI employee lifecycle
- [ ] AI manager hierarchy

## 62. Important gaps that still require dedicated discovery

This catalog is broad but not exhaustive at implementation level. Dedicated deep discovery should still be run for:

1. Every department's detailed sub-functions and SOPs.
2. WhatsApp/Telegram/LinkedIn/Instagram/TikTok platform-specific connectors and policy constraints.
3. Indian + US + UK + Canada + Australia + UAE accounting/tax/payroll/legal systems.
4. Banking, payment reconciliation and treasury.
5. Insurance/risk management.
6. Physical logistics, fleet and warehouse operations.
7. Construction/field-service workflows.
8. Education/academy operations.
9. Healthcare-specific compliance if ever applicable.
10. Data residency and country-specific privacy.
11. AI governance, model risk and enterprise compliance.
12. Commercial licenses for every model, dataset, voice and media asset.
13. Disaster recovery and offline/local operation.
14. Human workforce + AI workforce joint operating model.
15. Nivy-specific universal data model and event schema.
16. Nivy-specific universal agent registry and skill registry.
17. Nivy-specific approval/risk policy engine.
18. Nivy-specific cross-system universal search.
19. Nivy-specific Digital Twin.
20. Nivy-specific executive proactive briefing engine.

## 63. Evidence / current research references

- A2A defines agent-to-agent interoperability and explicitly complements MCP: https://a2a-protocol.org/
- Phoenix provides open-source tracing, evaluation, datasets and experiments for LLM applications: https://github.com/Arize-ai/phoenix
- Open-source AEO/SEO resources are catalogued here: https://github.com/discoveredlabs/awesome-aeo-seo-tools
- Additional AIO/AEO/GEO tools are catalogued here: https://github.com/XiaomingX/awesome-seo-tools
- Current voice-agent ecosystem research identifies LiveKit and Pipecat as major open-source building blocks: https://www.cekura.ai/blogs/vapi-alternatives
- Current voice framework comparison: https://www.assemblyai.com/blog/vapi-vs-pipecat-vs-livekit

## 64. Reuse decision rule

For every capability:

1. Search Nivy library.
2. Search GitHub/open-source.
3. Search official vendor/product.
4. Inspect latest release/activity.
5. Inspect license.
6. Inspect commercial-use rights.
7. Inspect API/provider terms.
8. Test locally when practical.
9. Record evidence.
10. Reuse/adapt.
11. Build only the missing Nivy integration.
12. Register the reusable asset in this library.

**Do not build an agent merely because an agent sounds useful. First prove that no suitable existing system, workflow, skill, MCP server, API, model, template, dashboard, ERP/CRM module or open-source project can be reused.**
