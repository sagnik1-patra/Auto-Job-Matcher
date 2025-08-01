def jaccard_similarity(set1, set2):
    return len(set1 & set2) / len(set1 | set2) if set1 | set2 else 0

def match_jobs(resume_skills, job_listings, threshold=0.3):
    matched = []
    for job in job_listings:
        job_words = set(job['summary'].lower().split())
        similarity = jaccard_similarity(set(resume_skills), job_words)
        if similarity >= threshold:
            job['match_score'] = round(similarity, 2)
            matched.append(job)
    return sorted(matched, key=lambda x: x['match_score'], reverse=True)
