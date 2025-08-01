from resume_parser import parse_resume
from job_scraper import scrape_jobs_indeed
from matcher import match_jobs
from notifier import send_email, send_telegram
import json

def main():
    with open('config.json') as f:
        config = json.load(f)

    resume_skills = parse_resume(config['resume_path'])
    job_listings = scrape_jobs_indeed(config['job_keyword'], config['location'])
    matched = match_jobs(resume_skills, job_listings)

    if matched:
        if config['notify']['email']:
            send_email(matched, config['notify']['receiver'], config['notify']['sender'], config['notify']['password'])

        if config['notify']['telegram']:
            send_telegram(matched, config['notify']['bot_token'], config['notify']['chat_id'])

if __name__ == "__main__":
    main()
