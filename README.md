# 💍 Wedding Digital Invitation

<p align="center">
  <strong>کارت عروسی دیجیتال</strong>
</p>

<p align="center">
  A modern, elegant and fully responsive Persian digital wedding invitation built with Django.
</p>

---

## ✨ Overview

**Wedding Digital** is a web-based digital wedding invitation designed for creating a beautiful and interactive wedding experience for guests.

The project is built with **Django** and provides a customizable invitation page where wedding information, couple photos, ceremony events, gallery images, music, intro video and RSVP responses can be managed through the Django Admin panel.

The invitation is designed primarily for **Persian / RTL audiences** and includes Persian calendar support and Persian typography.

---

## 🌹 Features

### 💌 Interactive Invitation Opening

The invitation starts with an animated envelope experience.

* Animated wedding envelope
* Wax seal animation
* Opening transition
* Personalized couple initials
* Preloader
* Smooth transition into the main invitation

---

### 🎬 Intro Video

An optional introduction video can be displayed before the main invitation.

Supported media can be uploaded through the Django Admin panel.

Recommended format:

```text
MP4
```

---

### 👫 Couple Information

The invitation supports detailed information about the bride and groom:

* Bride name
* Groom name
* Bride photo
* Groom photo
* Bride's parents
* Groom's parents

---

### ⏳ Wedding Countdown

A live countdown section displays the remaining time until the wedding ceremony.

The wedding date and time are managed from the admin panel.

---

### 📖 Love Story

A dedicated section is available for displaying the couple's story or a personalized message.

The content can be changed directly from the admin panel.

---

### 📅 Wedding Events Timeline

Multiple events can be added to an invitation.

For example:

```text
عقد
حنابندان
مراسم عروسی
پذیرایی
```

Each event can contain:

* Event title
* Date and time
* Venue
* Display order

Events are automatically ordered by their configured order and date.

---

### 📸 Photo Gallery

The invitation includes a responsive photo gallery with:

* Multiple photos
* Captions
* Custom ordering
* Responsive grid
* Image hover effects
* Full-screen lightbox

Gallery images are managed through the Django Admin panel.

---

### 🗺️ Wedding Venue

The venue section supports:

* Venue name
* Full address
* Google Maps embed
* Venue information

The Google Maps iframe can be configured from the admin panel.

---

### 🎁 Scratch Card / Gift Message

The invitation includes an interactive scratch-card section that can reveal a personalized gift message.

The message can be configured through the admin panel.

---

### 🎵 Background Music

An optional background music file can be uploaded and played from the invitation.

Recommended format:

```text
MP3
```

The interface also includes a floating music control for controlling playback.

---

### 📝 RSVP

Guests can submit their attendance information directly from the invitation.

The RSVP system supports:

* Guest name
* Email
* Phone number
* Attendance status
* Number of accompanying guests
* Guest message
* Submission date

RSVP responses are stored in the database and can be reviewed from Django Admin.

There is also an AJAX-based RSVP endpoint:

```text
POST /rsvp/<invitation_id>/
```

The endpoint returns a JSON response after successfully storing the guest's response.

---

## 🎨 Design

The invitation uses a luxury wedding-inspired visual system.

### Main colors

```text
Wine       #6d2333
Deep Wine  #4a1622
Gold       #c9a227
Soft Gold  #e3c876
Ivory      #fbf3e6
Blush      #f1dad2
```

The interface uses:

* Persian RTL layout
* Elegant typography
* Glassmorphism elements
* Gold accents
* Smooth animations
* Responsive layouts
* Interactive UI components

The template uses **Vazirmatn**, **Noto Nastaliq Urdu**, and **Playfair Display** typography.

---

## 🛠️ Technology Stack

### Backend

* Python
* Django 5.2.16
* SQLite
* Django ORM
* Django Admin

### Frontend

* HTML5
* CSS3
* JavaScript
* Django Templates
* Bootstrap-based form styling
* AOS animations

### Media

* Pillow
* HTML5 Video
* HTML5 Audio
* Canvas-based interactions

### Static Files

* WhiteNoise

### Persian Date

* jdatetime
* Custom Django template filters for Shamsi dates

The project explicitly configures the Persian locale and `Asia/Tehran` timezone.

---

## 📁 Project Structure

```text
Wedding_Digital/
│
├── invitation/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── invitation/
│   │       └── home.html
│   │
│   ├── templatetags/
│   │   └── shamsi.py
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── wedding_invitation/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── media/
│   └── invitation/
│
├── staticfiles/
│
├── logs/
│
├── db.sqlite3
├── manage.py
├── passenger_wsgi.py
└── README.md
```

---

## 🗄️ Database Models

The application currently contains four main models.

### Invitation

Stores the main wedding information:

```text
Bride
Groom
Couple Photos
Parents
Wedding Date
Venue
Address
Google Maps
Love Story
Gift Message
Main Photo
Intro Video
Background Music
RSVP URL
```

### InvitationEvent

Stores individual ceremony events:

```text
Invitation
Title
Date & Time
Venue
Order
```

### GalleryPhoto

Stores wedding gallery photos:

```text
Invitation
Image
Caption
Order
```

### Rsvp

Stores guest attendance responses:

```text
Invitation
Name
Email
Phone
Attendance
Guests Count
Message
Created At
```

These relationships are implemented using Django foreign keys and related managers such as `invitation.events`, `invitation.gallery`, and `invitation.rsvps`.

---

## ⚙️ Admin Panel

The Django Admin panel is used as the main content-management system.

An administrator can manage:

* Bride and groom information
* Couple photos
* Parents
* Wedding date
* Venue
* Google Maps
* Love story
* Gift message
* Intro video
* Background music
* Ceremony timeline
* Gallery
* RSVP responses

The admin interface also includes:

* Inline event management
* Inline gallery management
* Inline RSVP viewing
* Image thumbnails
* Couple photo previews
* RSVP summaries
* Search and filtering
* Wedding date hierarchy

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Milad-mj22/Wedding_Digital.git
cd Wedding_Digital
```

---

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

Install the required packages:

```bash
pip install django pillow whitenoise jdatetime
```

If a `requirements.txt` file is added to the project, use:

```bash
pip install -r requirements.txt
```

---

### 4. Apply migrations

```bash
python manage.py migrate
```

---

### 5. Create an admin user

```bash
python manage.py createsuperuser
```

Enter your desired:

```text
Username
Email
Password
```

---

### 6. Collect static files

For production:

```bash
python manage.py collectstatic
```

---

### 7. Start the development server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

The Django project routes the root URL directly to the invitation application, while `/admin/` opens the administration panel.

---

## 🔐 Admin

Open:

```text
http://127.0.0.1:8000/admin/
```

After logging in, create an invitation and configure its:

1. Couple information
2. Photos
3. Wedding date
4. Venue
5. Events
6. Gallery
7. Music
8. Intro video
9. Gift message
10. RSVP settings

Once configured, the main invitation is available at:

```text
http://127.0.0.1:8000/
```

The current implementation displays the first `Invitation` object as the public invitation.

---

## 🇮🇷 Persian / Shamsi Date Support

The project contains custom Django template filters for converting Gregorian dates into Persian/Jalali dates.

Examples:

```django
{{ invitation.wedding_date|to_shamsi }}
```

or:

```django
{{ invitation.wedding_date|to_shamsi_short }}
```

There is also support for:

```django
{{ my_date|shamsi_date }}
```

and Persian number conversion:

```django
{{ value|to_persian_numbers }}
```

The conversion is implemented using `jdatetime`.

---

## 📱 Responsive Design

The invitation is designed for:

* 📱 Mobile
* 📱 Tablet
* 💻 Desktop
* 🖥️ Large displays

The frontend uses responsive CSS with viewport-based sizing, flexible grids and mobile-specific layouts.

---

## 🎯 User Experience

The intended guest flow is:

```text
┌───────────────────────┐
│   Digital Invitation  │
└───────────┬───────────┘
            │
            ▼
     ✉️ Open Envelope
            │
            ▼
       🎬 Intro Video
            │
            ▼
      💍 Wedding Hero
            │
            ▼
       ⏳ Countdown
            │
            ▼
        ❤️ Love Story
            │
            ▼
      📅 Event Timeline
            │
            ▼
       👰 Couple Info
            │
            ▼
       📸 Photo Gallery
            │
            ▼
        🗺️ Wedding Venue
            │
            ▼
       🎁 Gift Message
            │
            ▼
          📝 RSVP
            │
            ▼
        💕 Thank You
```

---

## 🏗️ Production Configuration

Before deploying to production, update the Django settings.

In particular:

```python
DEBUG = False
```

Configure:

```python
ALLOWED_HOSTS = [
    "your-domain.com",
    "www.your-domain.com",
]
```

Configure your production:

* Secret key
* Database
* Static files
* Media files
* HTTPS
* CSRF trusted origins
* Secure cookies
* Web server

The current repository contains development-oriented settings such as `DEBUG=True` and permissive `ALLOWED_HOSTS`, so these should be reviewed before production deployment.

---

## 🌐 Deployment

The project contains `passenger_wsgi.py`, making it suitable for deployment in environments supporting Passenger / WSGI.

For a production server, the typical architecture can be:

```text
                    ┌──────────────────┐
                    │      Browser     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Web Server /    │
                    │     Passenger    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │      Django      │
                    │ Wedding Digital  │
                    └───────┬──────────┘
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
          ┌─────────────┐       ┌─────────────┐
          │  Database   │       │    Media    │
          │   SQLite    │       │ Photos/Video│
          └─────────────┘       └─────────────┘
```

---

## 🔒 Security Notes

Before publishing the application publicly:

* Change the Django `SECRET_KEY`
* Disable `DEBUG`
* Restrict `ALLOWED_HOSTS`
* Configure HTTPS
* Configure `CSRF_TRUSTED_ORIGINS`
* Use secure session cookies
* Protect the admin URL
* Do not commit private credentials
* Consider moving production configuration to environment variables

---

## 📌 Current Architecture

The application currently follows a simple Django architecture:

```text
Django Project
│
├── wedding_invitation
│   ├── Settings
│   ├── URL Configuration
│   └── WSGI / ASGI
│
└── invitation
    ├── Models
    ├── Views
    ├── Admin
    ├── Templates
    ├── Static Assets
    └── Custom Template Tags
```

The public invitation is rendered through a Django template and populated dynamically from the `Invitation` model.

---

## 🚧 Future Improvements

Potential improvements for future versions:

* [ ] Multi-invitation support
* [ ] Unique invitation URLs
* [ ] Guest-specific personalized links
* [ ] QR code generation
* [ ] WhatsApp sharing
* [ ] RSVP dashboard and statistics
* [ ] Export RSVP list to Excel
* [ ] Multiple invitation themes
* [ ] Theme customization from admin
* [ ] PostgreSQL support
* [ ] Environment-based configuration
* [ ] Automatic image optimization
* [ ] CDN support for media
* [ ] Progressive Web App support
* [ ] Improved accessibility
* [ ] SEO metadata and Open Graph support
* [ ] Automatic calendar event generation
* [ ] Google Calendar integration

---

## 👨‍💻 Author

**Milad Moltaji**

GitHub:

https://github.com/Milad-mj22

---

## 📄 License

This project does not currently specify an open-source license.

If you intend to distribute the project publicly, consider adding an appropriate `LICENSE` file.

---

## ❤️ Project

**Wedding Digital**

> A beautiful digital way to invite people to one of life's most important celebrations.

💍 **Made with Django & ❤️**
