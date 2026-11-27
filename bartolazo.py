
from pathlib import Path
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Jamycha P. Bartolazo | Portfolio",
    page_icon="✳️",
    layout="wide"
)

# ---------------- IMAGE PATHS ----------------
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"


def show_image(filename, caption=None):
    image_path = IMAGE_DIR / filename

    if image_path.exists():
        st.image(str(image_path), caption=caption, use_container_width=True)
    else:
        st.markdown(
            f"""
            <div class="image-placeholder">
                <span>✳</span>
                <p>{filename}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --cream: #f5f0e6;
    --orange: #f15a32;
    --blue: #2546d2;
    --ink: #171717;
}

.stApp {
    background-color: var(--cream);
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}

header, footer {
    visibility: hidden;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--ink) !important;
}

p, li {
    color: var(--ink);
}

/* HEADER */
.brand {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid var(--ink);
    padding: 10px 0 18px 0;
    margin-bottom: 25px;
    gap: 12px;
}

.brand-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(20px, 3vw, 29px);
    font-weight: 800;
    letter-spacing: -1px;
}

.brand-tag {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    text-align: right;
}

/* NAVIGATION */
div[role="radiogroup"] {
    gap: 8px;
    flex-wrap: wrap;
}

div[role="radiogroup"] label {
    background: transparent !important;
    border: 1px solid #b8b1a5;
    border-radius: 30px;
    padding: 7px 17px;
    font-size: 12px;
    font-weight: 700;
}

div[role="radiogroup"] label:hover {
    border-color: var(--orange);
    color: var(--orange);
}

/* HERO */
.hero-label {
    color: var(--orange);
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 15px;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(48px, 8vw, 100px);
    line-height: .91;
    letter-spacing: -7px;
    font-weight: 800;
    margin: 0;
}

.hero-title span {
    color: var(--orange);
}

.hero-description {
    font-size: 16px;
    line-height: 1.8;
    max-width: 480px;
    color: #5e5a53;
    margin-top: 24px;
}

/* SECTION HEADINGS */
.section-kicker {
    color: var(--orange);
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.section-heading {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(34px, 5vw, 58px);
    line-height: 1;
    letter-spacing: -3px;
    font-weight: 800;
    margin-bottom: 18px;
}

.section-copy {
    color: #666158;
    font-size: 15px;
    line-height: 1.8;
}

/* CARDS */
.info-card {
    background: #fffaf1;
    border: 1px solid #ded6c8;
    padding: 25px;
    min-height: 170px;
    margin-bottom: 15px;
}

.info-card.blue {
    background: var(--blue);
    border-color: var(--blue);
    color: white;
}

.info-card.orange {
    background: var(--orange);
    border-color: var(--orange);
}

.card-number {
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
    opacity: .7;
}

.card-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 25px;
    font-weight: 800;
    margin-top: 25px;
    margin-bottom: 8px;
}

.card-description {
    font-size: 13px;
    line-height: 1.7;
}

/* IMAGE PLACEHOLDER */
.image-placeholder {
    background: #e8dfd0;
    border: 1px dashed #a79d8d;
    min-height: 220px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: #777;
}

.image-placeholder span {
    font-size: 45px;
    color: var(--orange);
}

.image-placeholder p {
    font-size: 12px;
    font-weight: 700;
}

/* DETAILS */
.detail-line {
    border-top: 1px solid #c9c0b2;
    padding: 15px 0;
}

.detail-label {
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 800;
    color: var(--orange);
}

.detail-value {
    font-size: 17px;
    font-weight: 700;
    margin-top: 5px;
}

/* FOOTER */
.footer {
    border-top: 2px solid var(--ink);
    margin-top: 65px;
    padding-top: 20px;
    display: flex;
    justify-content: space-between;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    color: #6d675e;
}

/* BUTTONS */
.stButton button {
    background: var(--orange);
    color: white;
    border: none;
    border-radius: 0;
    font-weight: 800;
    padding: 10px 24px;
}

.stButton button:hover {
    background: var(--blue);
    color: white;
    border: none;
}

@media(max-width: 700px) {
    .hero-title {
        letter-spacing: -3px;
    }

    .brand-tag {
        font-size: 9px;
    }

    .brand {
        align-items: flex-start;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown("""
<div class="brand">
    <div class="brand-name">
        Jamycha P. Bartolazo<span style="color:#f15a32">.</span>
    </div>
    <div class="brand-tag">Personal Portfolio / 2026</div>
</div>
""", unsafe_allow_html=True)


# ---------------- NAVIGATION ----------------
page = st.radio(
    "Navigation",
    [
        "Home",
        "About",
        "Education",
        "Music & Hobbies",
        "Songwriting",
        "Engineering"
    ],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("---")


# ---------------- HOME ----------------
if page == "Home":

    left, right = st.columns([1.25, 0.75], gap="large")

    with left:
        st.markdown(
            '<div class="hero-label">✳ HELLO, WELCOME TO MY WORLD</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class="hero-title">
            A LITTLE<br>
            BIT OF<br>
            <span>EVERYTHING.</span>
        </div>
        <div class="hero-description">
            Welcome to my personal space. A collection of the things
            I enjoy, the music I create, the experiences I value,
            and the things I continue to discover along the way.
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.markdown("**JAMYCHA P. BARTOLAZO**")
        st.caption("Student • Music Lover • Creative Explorer")

    with right:
        show_image("profile.jpg")

        st.markdown("""
        <div style="background:#2546d2;color:white;padding:20px;margin-top:10px;">
            <div style="font-size:11px;letter-spacing:3px;font-weight:800;">
                CURRENT CHAPTER
            </div>
            <div style="font-family:'Space Grotesk';font-size:27px;
                        font-weight:800;margin-top:10px;">
                Learning.<br>Creating.<br>Growing.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="section-kicker">A QUICK INTRODUCTION</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Things that make me, me.</div>',
                unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="info-card">
            <div class="card-number">01 / MUSIC</div>
            <div class="card-title">My Sound</div>
            <div class="card-description">
                Playing instruments, enjoying music, and creating
                melodies that express my personality.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="info-card orange">
            <div class="card-number">02 / CREATIVITY</div>
            <div class="card-title">My Ideas</div>
            <div class="card-description">
                Exploring new things, learning different skills,
                and expressing myself through creativity.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="info-card blue">
            <div class="card-number">03 / LIFE</div>
            <div class="card-title">My Little World</div>
            <div class="card-description" style="color:white;">
                Enjoying simple moments, spending time with my cats,
                and appreciating everyday experiences.
            </div>
        </div>
        """, unsafe_allow_html=True)


# ---------------- ABOUT ----------------
elif page == "About":

    st.markdown('<div class="section-kicker">01 / GET TO KNOW ME</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Behind the name.</div>',
                unsafe_allow_html=True)

    left, right = st.columns([0.85, 1.15], gap="large")

    with left:
        show_image("profile.jpg")

    with right:
        st.markdown("""
        I am **Jamycha P. Bartolazo**, a student who enjoys music,
        creativity, and discovering new things.

        I believe that learning does not happen only inside a classroom.
        It also comes from experiences, hobbies, challenges, and the
        people and things that make everyday life meaningful.

        Whether I am playing an instrument, writing songs, or spending
        time with my cats, I enjoy finding inspiration in the little
        things around me.
        """)

        st.write("")
        st.markdown("""
        <div class="detail-line">
            <div class="detail-label">Full Name</div>
            <div class="detail-value">Jamycha P. Bartolazo</div>
        </div>
        <div class="detail-line">
            <div class="detail-label">College</div>
            <div class="detail-value">North Eastern Mindanao State University</div>
        </div>
        <div class="detail-line">
            <div class="detail-label">Senior High School Strand</div>
            <div class="detail-value">Science, Technology, Engineering and Mathematics (STEM)</div>
        </div>
        """, unsafe_allow_html=True)


# ---------------- EDUCATION ----------------
elif page == "Education":

    st.markdown('<div class="section-kicker">02 / MY LEARNING JOURNEY</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Education is a journey.</div>',
                unsafe_allow_html=True)

    st.markdown("""
    Every stage of education has helped shape my knowledge,
    experiences, and personal growth.
    """)

    st.write("")

    st.markdown("""
    <div style="background:#2546d2;color:white;padding:30px;margin-bottom:15px;">
        <div style="font-size:12px;letter-spacing:3px;font-weight:800;">
            SENIOR HIGH SCHOOL
        </div>
        <div style="font-family:'Space Grotesk';font-size:32px;
                    font-weight:800;margin-top:12px;">
            Bislig City National High School
        </div>
        <div style="margin-top:12px;font-size:14px;color:#ffffff;">
            STEM — Science, Technology, Engineering and Mathematics
        </div>
    </div>
    <div style="background:#fffaf1;border:1px solid #ded6c8;
                padding:30px;">
        <div style="font-size:12px;letter-spacing:3px;
                    font-weight:800;color:#f15a32;">
            COLLEGE
        </div>
        <div style="font-family:'Space Grotesk';font-size:32px;
                    font-weight:800;margin-top:12px;">
            North Eastern Mindanao State University
        </div>
        <div style="margin-top:12px;font-size:14px;color:#666158;">
            Continuing my academic journey through higher education.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    show_image("engineering.jpg", "Learning, discovery, and the world of STEM.")


# ---------------- MUSIC & HOBBIES ----------------
elif page == "Music & Hobbies":

    st.markdown('<div class="section-kicker">03 / THE THINGS I ENJOY</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-heading">My world, in different notes.</div>',
                unsafe_allow_html=True)

    a, b = st.columns([1, 1], gap="large")

    with a:
        show_image("hobbies.jpg")
        st.markdown("### Playing the ukulele and guitar")
        st.markdown("""
        Music is one of the things I enjoy most. Playing the ukulele
        and guitar gives me a way to relax, have fun, and express myself
        through different sounds and melodies.
        """)

    with b:
        show_image("interest.jpg")
        st.markdown("### Learning and exploring")
        st.markdown("""
        I enjoy discovering new things and exploring different
        experiences. Every new skill or idea gives me an opportunity
        to learn something valuable.
        """)

    st.markdown("---")
    st.markdown("### A little time with my cats 🐈")
    st.markdown("""
    Spending time with my cats is another simple joy in my life.
    Playing with them and enjoying their company makes ordinary
    moments more memorable.
    """)


# ---------------- SONGWRITING ----------------
elif page == "Songwriting":

    st.markdown('<div class="section-kicker">04 / MY CREATIVE SIDE</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Turning thoughts into songs.</div>',
                unsafe_allow_html=True)

    left, right = st.columns([1.1, 0.9], gap="large")

    with left:
        show_image("interest.jpg")

    with right:
        st.markdown("""
        ### Composing my own songs

        Songwriting allows me to turn ideas, emotions, and imagination
        into something creative. It gives me the freedom to experiment
        with melodies, lyrics, and different musical styles.

        I enjoy the process of creating something from my own thoughts
        and giving it a sound of its own.
        """)

        st.markdown("""
        <div style="background:#f15a32;color:white;padding:22px;margin-top:20px;">
            <div style="font-size:11px;letter-spacing:3px;font-weight:800;">
                CREATIVE REMINDER
            </div>
            <div style="font-family:'Space Grotesk';font-size:25px;
                        font-weight:800;margin-top:10px;">
                Every song begins with an idea.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.markdown("### My creative process")

    x, y, z = st.columns(3)

    with x:
        st.markdown("**01 — Inspiration**")
        st.caption("Finding ideas from everyday experiences.")

    with y:
        st.markdown("**02 — Experimentation**")
        st.caption("Trying melodies, lyrics, and different sounds.")

    with z:
        st.markdown("**03 — Creation**")
        st.caption("Putting everything together into an original song.")


# ---------------- ENGINEERING ----------------
elif page == "Engineering":

    st.markdown('<div class="section-kicker">05 / STEM & INNOVATION</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Curiosity meets engineering.</div>',
                unsafe_allow_html=True)

    left, right = st.columns([1, 1], gap="large")

    with left:
        show_image("engineering.jpg")

    with right:
        st.markdown("""
        ### Exploring the world of Mechanical Engineering

        Engineering is a field that combines creativity, mathematics,
        science, and problem-solving to develop practical solutions.

        Mechanical Engineering focuses on machines, mechanisms,
        motion, energy, and the design of systems that help make
        everyday life easier.

        My STEM background provides a foundation for understanding
        scientific concepts and exploring how engineering ideas
        can be applied in the real world.
        """)

    st.write("")
    st.markdown("### What makes engineering interesting?")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="info-card">
            <div class="card-number">01</div>
            <div class="card-title">Design</div>
            <div class="card-description">
                Turning ideas into useful designs and structures.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="info-card orange">
            <div class="card-number">02</div>
            <div class="card-title">Innovation</div>
            <div class="card-description">
                Exploring new ways to improve existing systems.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="info-card blue">
            <div class="card-number">03</div>
            <div class="card-title">Problem Solving</div>
            <div class="card-description" style="color:white;">
                Using logic and creativity to find practical solutions.
            </div>
        </div>
        """, unsafe_allow_html=True)


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    <div>JAMYCHA P. BARTOLAZO</div>
    <div>MADE WITH CREATIVITY ✳ 2026</div>
</div>
""", unsafe_allow_html=True)
