### Clustering and recommender system for career path

- For this project mostly the columns to use are those that provide insights into job profiles,technologies, and skills 

### Data 
- We used the 2023 Stack Overflow Annual Developer Survey. It can be found [here](https://cdn.stackoverflow.co/files/jo7n4k8s/production/49915bfd46d0902c3564fd9a06b509d08a20488c.zip/stack-overflow-developer-survey-2023.zip).

### Job profiles and roles 
- `DevType`: This column represents the type of developer or IT professional the respondent identifies as, which is crucial for understanding job profiles.

### Skills and Technologies
- `LanguageHaveWorkedWith`: Lists programming languages the respondent has experience with, which is key for matching job profiles to skills
- `DatabaseHaveWorkedWith`: Similar to programming languages, these columns focus on database technologies
- `PlatformHaveWorkedWith`: Platforms (e.g., cloud services) the respondent has experience with or is interested in.
- `ToolsTechHaveWorkedWith`: Tools and technologies used in professional work.
- `AISearchHaveWorkedWith`: AI search technologies the respondent has experience with or is interested in.
- `AIDevHaveWorkedWith`: AI development tools the respondent has used or wants to learn.

### Experience and Education
- `YearsCode`: Total years of coding experience, which helps in gauging expertise levels.
- `YearsCodePro`: Professional coding experience, important for understanding skill maturity.
- `EdLevel`: The respondent’s education level, which could correlate with job profiles and career paths.
- `LearnCodeCoursesCert`: Information on whether the respondent has taken courses or certifications, relevant for students seeking similar paths.


### Technology Adoption and Usage
- `ProfessionalTech`: Technologies used professionally, relevant for matching skills to job profiles.
- `Industry`: The industry the respondent works in, which might influence the type of technologies used and required skills.

### Clustering
`KMeans Clustering`: Job profiles are grouped into clusters based on their features.
`PCA Transformation`: Reduces the feature dimensions for better clustering performance.

### Usage

 - Job recommendations based on skills and experience:

```
student_skills = ['Python', 'SQL', 'AWS']
experience_years = 5
recommended_jobs = hybrid_recommend_jobs(student_skills, experience_years)
print(recommended_jobs)
```