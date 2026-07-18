# 📄 Package Recommendation Logic

## Package Recommendation Logic

Use client answers from qualification to recommend the right package.

---

## Decision Framework

| Client Situation | Recommended Package |
| --- | --- |
| New business, small budget | Starter |
| Established, needs leads | Growth |
| Scaling, wants full system | Scale / Premium |

---

## Logic Flow

1. **Budget under $X?** → Recommend Starter
2. **Running ads already?** → Recommend Growth (optimize + expand)
3. **Needs full funnel + ads + content?** → Recommend Scale

---

*[Fill in exact package names and prices from Pricing System section]*