from resume_parser import extract_text_from_pdf, extract_text_from_txt
from skills_db import ROLE_SKILLS
from skill_matcher import match_skills

print("Resume Analyzer & Skill Gap Detector\n")

file_path = input("Enter resume file path: ")
role = input("Enter target role: ").title()

if file_path.endswith(".pdf"):
    resume_text = extract_text_from_pdf(file_path)
elif file_path.endswith(".txt"):
    resume_text = extract_text_from_txt(file_path)
else:
    print("Unsupported file format")
    exit()

required_skills = ROLE_SKILLS.get(role)

if not required_skills:
    print("Role not found")
    exit()

found, missing = match_skills(resume_text, required_skills)

print("\n Skills Found:")
for s in found:
    print("-", s)

print("\n Missing Skills:")
for s in missing:
    print("-", s)
