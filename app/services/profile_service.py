class ProfileService:
    @staticmethod
    def get_profile():
        return {
            "name": "Istkhar Ali",
            "title": "Senior Full Stack Engineer",
            "location": "Meerut, Uttar Pradesh, India",
            "contact": {
                "phone": "+91 9319963296",
                "email": "istkharali1991@gmail.com",
                "linkedin": "https://linkedin.com/in/istkhar",
            },
            "summary": [
                "Senior Full Stack Engineer with 8+ years of experience building scalable web applications and backend systems.",
                "Strong in React.js, Next.js, Node.js, Laravel, Python, FastAPI, Flask, MySQL, PostgreSQL, and MongoDB.",
                "Experienced with REST APIs, JWT authentication, rate limiting, Redis caching, Docker, and AWS deployments.",
            ],
            "skills": {
                "languages": ["JavaScript", "PHP", "Python"],
                "frontend": ["React.js", "Next.js", "Redux"],
                "backend": ["Node.js", "Express.js", "Laravel", "FastAPI", "Flask"],
                "databases": ["MySQL", "PostgreSQL", "MongoDB"],
                "tools": ["Git", "Docker", "CI/CD", "AWS S3", "AWS EC2", "GitHub", "GitLab", "Jira"],
            },
            "experience": [
                {
                    "role": "Senior Full Stack Developer",
                    "company": "Q2AMedia",
                    "location": "Noida",
                    "duration": "March 2021 - Present",
                },
                {
                    "role": "Laravel Developer",
                    "company": "RNF Technologies",
                    "location": "Noida",
                    "duration": "December 2020 - March 2021",
                },
                {
                    "role": "Software Engineer",
                    "company": "Q2AMedia",
                    "location": "Noida",
                    "duration": "May 2019 - December 2020",
                },
                {
                    "role": "Software Engineer (PHP Developer)",
                    "company": "Chetu, Inc.",
                    "location": "Noida",
                    "duration": "November 2018 - May 2019",
                },
                {
                    "role": "Associate Software Developer",
                    "company": "Zvesta.com",
                    "location": "Gurugram",
                    "duration": "April 2018 - November 2018",
                },
            ],
            "projects": [
                {
                    "name": "LiFT Learning",
                    "links": ["https://teacher.mylift.io", "https://learner.mylift.io"],
                    "stack": ["React.js", "Node.js", "Python", "FastAPI", "Redis", "PostgreSQL", "MongoDB"],
                },
                {
                    "name": "Future Generation Hub",
                    "links": ["https://futuregenerationhub.com"],
                    "stack": ["React.js", "Laravel", "MySQL"],
                },
                {
                    "name": "QCode",
                    "links": ["https://qcode.qbslearning.com"],
                    "stack": ["React.js", "Laravel", "MySQL"],
                },
                {
                    "name": "LMS Platform",
                    "links": [],
                    "stack": ["Node.js", "MongoDB", "JWT"],
                },
            ],
            "education": [
                {
                    "degree": "Master of Computer Applications (MCA)",
                    "specialization": "Information Technology",
                    "college": "Radha Govind Engineering College, Meerut",
                    "duration": "2012 - 2015",
                },
                {
                    "degree": "Bachelor of Computer Applications (BCA)",
                    "specialization": "Information Technology",
                    "college": "BIMT College, Meerut",
                    "duration": "2009 - 2012",
                },
            ],
        }
