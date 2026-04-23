from jobspy import scrape_jobs
import json
from datetime import datetime

jobs = scrape_jobs(
    site_name=["linkedin", "indeed"],
    search_term="project manager OR operations director",
    location="worldwide",
    results_wanted=50,
    hours_old=48
)

filtered = []
for _, job in jobs.iterrows():
    filtered.append({
        "title": str(job.get("title", "—")),
        "company": str(job.get("company", "—")),
        "location": str(job.get("location", "—")),
        "salary": str(job.get("min_amount", "не указана")),
        "url": str(job.get("job_url", "—")),
        "date_found": datetime.now().strftime("%Y-%m-%d")
    })

with open("jobs.json", "w", encoding="utf-8") as f:
    json.dump(filtered, f, ensure_ascii=False, indent=2)

print(f"Найдено и сохранено: {len(filtered)} вакансий")