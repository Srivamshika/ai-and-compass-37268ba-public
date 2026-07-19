from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Ai And Compass', version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https://[a-z0-9-]+\.vercel\.app",
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)
PRODUCT = {"project_id": "37268bad-d9f3-436f-bff7-f7a4e99a6f9d", "product_name": "Ai And Compass", "idea": "Create AI and IoT-driven tools—such as affordable soil testing or precise weather monitoring—to help local farmers adapt to unpredictable monsoons and reduce water/pesticide usage", "problem": "Operations teams and domain specialists need a safer, faster way to turn scattered information into a reliable, measurable workflow decision. The opportunity should be tested through one repeatable decision workflow.", "elevator_pitch": "Ai And Compass helps operations teams and domain specialists turn scattered evidence into a human-approved next action and prove whether the workflow improves a measurable outcome.", "target_users": ["operations teams and domain specialists", "domain specialists", "an operations or business-unit leader"], "features": ["Structured case or workflow intake", "Evidence-backed recommendation with confidence and rationale", "Human approval and override with an audit trail", "Pilot dashboard for time, quality, and adoption outcomes"], "market_gap": "A narrow workflow innovation workflow that links evidence, a human approval, and a measurable outcome remains more defensible than another general AI chat surface."}

@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "generated-mvp-api"}

@app.get("/api/overview")
def overview() -> dict:
    return {
        "product_name": PRODUCT["product_name"],
        "pitch": PRODUCT["elevator_pitch"],
        "problem": PRODUCT["problem"],
        "target_users": PRODUCT["target_users"],
        "features": PRODUCT["features"],
        "demo_data": True,
    }
