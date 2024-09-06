### Clustering and recommender system for career path

- For this project mostly the columns to use are those that provide insights into job profiles,technologies, and skills 

### Job profiles and roles 
- `DevType`: This column represents the type of developer or IT professional the respondent identifies as, which is crucial for understanding job profiles.
- `Employment`: Provides information on the respondent's employment status, which can help differentiate between students, full-time employees, and others.
- `MainBranch`: Indicates the primary focus of the respondent's work (e.g., software development, data science), which is essential for categorizing job profiles.

### Skills and Technologies
- `LanguageHaveWorkedWith`: Lists programming languages the respondent has experience with, which is key for matching job profiles to skills.
- `LanguageWantToWorkWith`: Indicates programming languages the respondent is interested in learning, useful for career planning recommendations.
- `DatabaseHaveWorkedWith, DatabaseWantToWorkWith`: Similar to programming languages, these columns focus on database technologies.
- `PlatformHaveWorkedWith, PlatformWantToWorkWith`: Platforms (e.g., cloud services) the respondent has experience with or is interested in.
- `WebframeHaveWorkedWith, WebframeWantToWorkWith`: Web frameworks the respondent has worked with or wants to learn.
- `MiscTechHaveWorkedWith, MiscTechWantToWorkWith`: Miscellaneous technologies the respondent is familiar with or interested in.
- `ToolsTechHaveWorkedWith, ToolsTechWantToWorkWith`: Tools and technologies used in professional work.
- `AISearchHaveWorkedWith, AISearchWantToWorkWith`: AI search technologies the respondent has experience with or is interested in.
- `AIDevHaveWorkedWith, AIDevWantToWorkWith`: AI development tools the respondent has used or wants to learn.

### Experience and Education
- `YearsCode`: Total years of coding experience, which helps in gauging expertise levels.
- `YearsCodePro`: Professional coding experience, important for understanding skill maturity.
- `EdLevel`: The respondent’s education level, which could correlate with job profiles and career paths.
- `LearnCodeCoursesCert`: Information on whether the respondent has taken courses or certifications, relevant for students seeking similar paths.

### Work Environment and Preferences
- `OrgSize`: The size of the organization the respondent works for, which could influence the types of job profiles available.
- `RemoteWork`: Information on remote work, which can be a factor in career decisions.
- `WorkExp`: Overall work experience in the industry, crucial for understanding career progression.

### Compensation
- `CompTotal`: Total compensation, which can help students understand the financial prospects of different job profiles.
- `ConvertedCompYearly`: Annual compensation, which is useful for comparing salaries across roles.

### Technology Adoption and Usage
- `ProfessionalTech`: Technologies used professionally, relevant for matching skills to job profiles.
- `Industry`: The industry the respondent works in, which might influence the type of technologies used and required skills.

### deploy
Go to the directory and use ` streamlit run app/app.py`