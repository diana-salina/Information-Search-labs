import os
from datetime import datetime

from flask import Flask, redirect, render_template, request, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:root@localhost:5432/university_db_salina",
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

with app.app_context():
    try:
        db.create_all()
    except Exception as exc:
        app.logger.error("Не удалось создать таблицы: %s", exc)


class University(db.Model):
    __tablename__ = "university"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    short_name = db.Column(db.String(50), nullable=False)
    foundation_date = db.Column(db.Date, nullable=False)
    students = db.relationship("Student", backref="university", cascade="all, delete-orphan")


class Student(db.Model):
    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey("university.id"), nullable=False)
    admission_year = db.Column(db.Integer, nullable=False)


class User(UserMixin, db.Model):
    __tablename__ = "auth_user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def parse_date(value: str):
    return datetime.strptime(value, "%Y-%m-%d").date()


@app.route("/")
def home():
    return render_template("main/home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if not username or not password:
            flash("Имя пользователя и пароль обязательны.", "danger")
            return redirect(url_for("register"))

        if User.query.filter_by(username=username).first():
            flash("Пользователь с таким именем уже существует.", "danger")
            return redirect(url_for("register"))

        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("Регистрация успешна. Войдите в систему.", "success")
        return redirect(url_for("login"))

    return render_template("auth/register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Вы вошли в систему.", "success")
            next_url = request.args.get("next")
            return redirect(next_url or url_for("home"))
        flash("Неверные учетные данные.", "danger")
    return render_template("auth/login.html")


@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("Вы вышли из системы.", "success")
    return redirect(url_for("home"))

@app.route("/universities")
def university_list():
    universities = University.query.order_by(University.short_name).all()
    return render_template("main/university_list.html", universities=universities)


@app.route("/universities/create", methods=["GET", "POST"])
@login_required
def university_create():
    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        short_name = request.form.get("short_name", "").strip()
        foundation_date = request.form.get("foundation_date")

        if not full_name or not short_name or not foundation_date:
            flash("Заполните все поля.", "danger")
            return redirect(url_for("university_create"))

        university = University(
            full_name=full_name,
            short_name=short_name,
            foundation_date=parse_date(foundation_date),
        )
        db.session.add(university)
        db.session.commit()
        flash("Университет создан.", "success")
        return redirect(url_for("university_list"))

    return render_template("main/university_form.html", university=None)


@app.route("/universities/<int:university_id>/edit", methods=["GET", "POST"])
@login_required
def university_update(university_id: int):
    university = University.query.get_or_404(university_id)

    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        short_name = request.form.get("short_name", "").strip()
        foundation_date = request.form.get("foundation_date")

        if not full_name or not short_name or not foundation_date:
            flash("Заполните все поля.", "danger")
            return redirect(url_for("university_update", university_id=university.id))

        university.full_name = full_name
        university.short_name = short_name
        university.foundation_date = parse_date(foundation_date)
        db.session.commit()
        flash("Университет обновлен.", "success")
        return redirect(url_for("university_list"))

    return render_template("main/university_form.html", university=university)


@app.route("/universities/<int:university_id>/delete", methods=["POST"])
@login_required
def university_delete(university_id: int):
    university = University.query.get_or_404(university_id)
    db.session.delete(university)
    db.session.commit()
    flash("Университет удален.", "success")
    return redirect(url_for("university_list"))

@app.route("/students")
def student_list():
    students = Student.query.order_by(Student.full_name).all()
    return render_template("main/student_list.html", students=students)


@app.route("/students/create", methods=["GET", "POST"])
@login_required
def student_create():
    universities = University.query.order_by(University.short_name).all()
    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        birth_date = request.form.get("birth_date")
        university_id = request.form.get("university_id")
        admission_year = request.form.get("admission_year")

        if not all([full_name, birth_date, university_id, admission_year]):
            flash("Заполните все поля.", "danger")
            return redirect(url_for("student_create"))

        student = Student(
            full_name=full_name,
            birth_date=parse_date(birth_date),
            university_id=int(university_id),
            admission_year=int(admission_year),
        )
        db.session.add(student)
        db.session.commit()
        flash("Студент добавлен.", "success")
        return redirect(url_for("student_list"))

    return render_template("main/student_form.html", student=None, universities=universities)


@app.route("/students/<int:student_id>/edit", methods=["GET", "POST"])
@login_required
def student_update(student_id: int):
    student = Student.query.get_or_404(student_id)
    universities = University.query.order_by(University.short_name).all()

    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        birth_date = request.form.get("birth_date")
        university_id = request.form.get("university_id")
        admission_year = request.form.get("admission_year")

        if not all([full_name, birth_date, university_id, admission_year]):
            flash("Заполните все поля.", "danger")
            return redirect(url_for("student_update", student_id=student.id))

        student.full_name = full_name
        student.birth_date = parse_date(birth_date)
        student.university_id = int(university_id)
        student.admission_year = int(admission_year)
        db.session.commit()
        flash("Данные студента обновлены.", "success")
        return redirect(url_for("student_list"))

    return render_template("main/student_form.html", student=student, universities=universities)


@app.route("/students/<int:student_id>/delete", methods=["POST"])
@login_required
def student_delete(student_id: int):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    flash("Студент удален.", "success")
    return redirect(url_for("student_list"))

@app.cli.command("init-db")
def init_db():
    """Создает таблицы в базе данных."""
    db.create_all()
    print("База данных готова.")


if __name__ == "__main__":
    app.run(debug=True)
