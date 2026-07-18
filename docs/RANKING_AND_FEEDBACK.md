# Ranking and Feedback

Ranking is rule-first and LLM-second.

The deterministic layer computes track relevance, project relevance, evidence,
credibility, actionability, authority signals, hype risk, topic drift risk, and
feedback score. LLM summaries may explain an item but cannot override negative
rules or primary-source requirements.

Feedback is local:

```bash
python feedback.py rate ITEM_ID highly_relevant
python feedback.py rate ITEM_ID irrelevant
python feedback.py follow-author AUTHOR_ID
python feedback.py mute-source SOURCE_ID
```

Positive feedback decays over time. Negative feedback is stronger. Muted sources
or topics are hard filters. No feedback file means cold-start profile ranking.
