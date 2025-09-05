from django.shortcuts import render

def home(request):
    """Home page view with all portfolio sections"""
    context = {
        'name': 'Chelimalla Tejasai',
        'title': 'Computer Science Engineering Student',
        'email': 'tejasaiaa12@gmail.com',
        'education': [
            {
                'degree': 'B.Tech in Computer Science Engineering',
                'institution': 'SR University',
                'cgpa': '9.44/10',
                'status': 'Current'
            },
            {
                'degree': 'Higher Secondary',
                'institution': 'SR Junior College',
                'percentage': '91.6%',
                'status': 'Completed'
            }
        ],
        'skills': {
            'Programming': ['C', 'Python', 'Java'],
            'Web Development': ['HTML', 'CSS', 'Django'],
            'Database': ['MySQL'],
            'Tools': ['GitHub', 'VS Code', 'Figma', 'Git']
        },
        'experience': [
            {
                'title': 'Python Developer Intern',
                'company': 'Logic While',
                'duration': 'Jan 2025 – Present',
                'description': 'Developing Python applications and contributing to backend development projects.'
            },
            {
                'title': 'Web Developer Intern',
                'company': 'NIT Warangal',
                'duration': 'Jan 2024 – Mar 2024',
                'description': 'Built responsive web applications and collaborated on university web projects.'
            }
        ],
        'projects': [
            {
                'name': 'Pet Adoption & Care Portal',
                'description': 'A comprehensive web platform connecting pet adopters with shelters, featuring user profiles, pet listings, and adoption management.',
                'github': 'https://github.com/tejasai/pet-adoption-portal',
                'technologies': ['Django', 'Python', 'MySQL', 'HTML/CSS']
            },
            {
                'name': 'Machine Learning Movie Recommendation Engine',
                'description': 'An intelligent recommendation system using collaborative filtering and content-based algorithms to suggest movies based on user preferences.',
                'github': 'https://github.com/tejasai/movie-recommendation',
                'technologies': ['Python', 'Scikit-learn', 'Pandas', 'Flask']
            },
            {
                'name': 'Weather Forecasting App',
                'description': 'Real-time weather application with location-based forecasts, interactive maps, and weather alerts using external APIs.',
                'github': 'https://github.com/tejasai/weather-app',
                'technologies': ['Python', 'Django', 'Weather API', 'JavaScript']
            },
            {
                'name': 'Language Translator',
                'description': 'Multi-language translation tool with text and speech input/output capabilities, supporting over 50 languages.',
                'github': 'https://github.com/tejasai/language-translator',
                'technologies': ['Python', 'Google Translate API', 'Speech Recognition']
            }
        ],
        'achievements': [
            'Academic Excellence - Top 5% of class',
            'Microsoft Azure AI Fundamentals Certification',
            'Hackathon Finalist - University Tech Fest',
            'Cisco Cybersecurity Essentials Certification',
            'NPTEL Database Management Systems Elite Certificate',
            'Mentorship Impact Award - Peer Tutoring Program'
        ],
        'social_links': {
            'linkedin': 'https://linkedin.com/in/chelimalla-tejasai',
            'github': 'https://github.com/tejasai',
            'leetcode': 'https://leetcode.com/tejasai'
        }
    }
    return render(request, 'portfolio/index.html', context)
