# D&D Character Sheet Manager

A Django web application for creating, managing, and tracking Dungeons & Dragons character sheets. Features an intuitive interface and comprehensive character customization.

---

## 🚀 Features

- **User Authentication:** Secure registration and login
- **Character Management:** Full CRUD for D&D characters
- **Character Attributes:**  
    - Basic info (name, description, level)  
    - Six ability scores: Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma  
    - Race, Background, Alignment selection  
    - Multi-class support  
    - Spell & item inventory  
    - Feat tracking
- **Dynamic Content:** Add custom spells and items
- **Responsive Design:** Bootstrap-powered, mobile-friendly
- **Admin Panel:** Django admin for data management

---

## 🛠️ Technology Stack

- **Backend:** Django 4.2.23
- **Database:** PostgreSQL (production) / SQLite (development)
- **Frontend:** Bootstrap 5.3.0, HTML5, CSS3
- **Authentication:** Django Allauth
- **Deployment:** Heroku-ready (Gunicorn)

---

## 🗂️ Database Design

**Entity Relationship Diagram (ERD):**  
Designed in Lucidchart, normalized for best practices.

- **User:** Django's built-in user model
- **Character:** Central entity (info & ability scores)
- **Race:** Racial traits & abilities
- **Background:** Skills & proficiencies
- **Alignment:** Moral/ethical alignment
- **Class:** D&D classes (Fighter, Wizard, etc.)
- **Spells:** Magic spells (school, level)
- **Items:** Equipment & inventory
- **Feats:** Special abilities & prerequisites

> Many-to-many relationships for flexible customization.

---

## ⚡ Installation & Setup

### Prerequisites

- Python 3.13+
- PostgreSQL (production)
- Git

### Local Development

1. **Clone the repository**
2. **Create & activate virtual environment**
3. **Install dependencies**
4. **Configure environment**
     - Copy `.env.example` to `.env`
     - Set `SECRET_KEY` and `DATABASE_URL`
5. **Database setup**
6. **Run development server**

Visit [http://localhost:8000](http://localhost:8000) to access the app.

---

## 📝 Usage

### Character Creation

1. Register or log in
2. Go to **My Characters**
3. Click **Create New Character**
4. Fill in details:
     - Basic info
     - Ability scores (1–20)
     - Race, background, alignment
     - Classes, spells, items
     - Add custom spells/items

### Character Management

- **View:** List all characters
- **Edit:** Update character info
- **Delete:** Remove characters (with confirmation)
- **Custom Content:** Add spells/items for all users

---

## 🎨 Wireframes & Design

- **Header Navigation:** Quick access
- **Tabbed Interface:** Organized forms
- **Responsive Layout:** Mobile-friendly
- **Form Validation:** Client/server-side
- **User Feedback:** Success/error messages

---

## 🤖 AI Assistance

Developed with help from **GitHub Copilot** for:

- Code completion & suggestions
- Django best practices
- Bootstrap integration
- Error debugging
- Documentation generation

---

## 🚢 Deployment

**Heroku-ready:**  
- Procfile (Gunicorn)
- `requirements.txt`
- Environment variables
- Static files (WhiteNoise)
- PostgreSQL integration

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch  
     `git checkout -b feature/new-feature`
3. Commit changes  
     `git commit -am 'Add new feature'`
4. Push branch  
     `git push origin feature/new-feature`
5. Create a Pull Request

---

## 🏆 Credits

- **Developer:** Jacob [Your Last Name]
- **Framework:** Django Software Foundation
- **UI:** Bootstrap Team
- **Database Design:** Lucidchart
- **Icons:** Font Awesome
- **AI Assistant:** GitHub Copilot
- **Inspiration:** Dungeons & Dragons by Wizards of the Coast

---

## 📄 License

Educational purposes only.  
D&D is a trademark of Wizards of the Coast.

---

## 🔮 Future Enhancements

- Character sheet PDF export
- Dice rolling simulator
- Campaign management
- Character sharing
- Advanced spell/item filtering
- Character portraits/images
- Mobile app version

---

**Live Application:** [Deploy URL when available]  
**Repository:** [GitHub Repository URL]