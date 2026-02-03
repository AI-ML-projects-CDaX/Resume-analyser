def match_skills(resume_text, role_skills):
    found = []
    missing = []

    for skill in role_skills:
        if skill in resume_text:
            found.append(skill)
        else:
            missing.append(skill)

    return found, missing
