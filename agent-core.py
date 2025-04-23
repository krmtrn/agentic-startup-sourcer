# Simplified agentic AI system for startup sourcing

class SourceAgent:
    def fetch_sources(self):
        return [
            {"title": "Pitch Istanbul", "type": "event", "url": "https://pitch.ist"},
            {"title": "500 Startups MENA", "type": "accelerator", "deadline": "2025-05-10"}
        ]

class AnalyzerAgent:
    def score(self, source):
        if "accelerator" in source["type"]:
            return {"score": 90}
        return {"score": 50}

if __name__ == "__main__":
    sa = SourceAgent()
    aa = AnalyzerAgent()
    sources = sa.fetch_sources()
    for s in sources:
        print(s["title"], aa.score(s))
