from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField
from wtforms.fields import IntegerField, SelectField
from wtforms.validators import DataRequired


# Login
class LoginForm(FlaskForm):
    username = StringField(
        label="Nazwa użytkownika",
        validators=[DataRequired()])

    password = PasswordField(
        label="Hasło",
        validators=[DataRequired()])

    submit = SubmitField(label="Wbijaj!")


# Changing values of the variables
class VarChangerForm(FlaskForm):
    new_value = FloatField(label="Nowa wartość: ")

    submit = SubmitField(label="Zmień")


# Business cards form
class BusinessCardsForm(FlaskForm):
    cards_patterns = IntegerField(
        label="Ilość wzorów: ",
        validators=[DataRequired()],
        default="1")

    cards_quantity = IntegerField(
        label="Ilość wizytówek: ",
        validators=[DataRequired()],
        default="100")

    cards_paper_weight = SelectField(
        label="Gramatura: ",
        choices=[
            ("350", "350"),
            ("fancy", "Ozdobny")],
        validators=[DataRequired()],
        default="350")

    cards_overprint = SelectField(
        label="Zadruk: ",
        choices=[
            ("40", "4+0"),
            ("44", "4+4")],
        validators=[DataRequired()],
        default="40")

    cards_foil = SelectField(
        label="Foliowanie: ",
        choices=[
            ("none", "Brak"),
            ("10", "1+0"),
            ("11", "1+1")],
        validators=[DataRequired()],
        default="none")

    cards_margin = IntegerField(
        label="Marża: ",
        default="75")

    submit = SubmitField(label="Oblicz")


# Posters
class PostersForm(FlaskForm):
    posters_patterns = IntegerField(
        label="Ilość wzorów: ",
        validators=[DataRequired()],
        default="1")

    posters_quantity = IntegerField(
        label="Ilość plakatów: ",
        validators=[DataRequired()],
        default="10")

    posters_size = SelectField(
        label="Wielkość: ",
        choices=[
            ("a4", "A4"),
            ("a3", "A3")],
        validators=[DataRequired()],
        default="a4")

    posters_paper_weight = SelectField(
        label="Gramatura: ",
        choices=[
            ("130", "130"),
            ("150", "150"),
            ("170", "170"),
            ("200", "200"),
            ("250", "250"),
            ("300", "300"),
            ("350", "350"),
            ("fancy", "Ozdobny")],
        validators=[DataRequired()],
        default="200")

    posters_overprint = SelectField(
        label="Zadruk: ",
        choices=[
            ("40", "4+0"),
            ("44", "4+4")],
        validators=[DataRequired()],
        default="40")

    posters_foil = SelectField(
        label="Foliowanie: ",
        choices=[
            ("none", "Brak"),
            ("10", "1+0"),
            ("11", "1+1")],
        validators=[DataRequired()],
        default="none")

    posters_margin = IntegerField(
        label="Marża: ",
        default="75")

    submit = SubmitField(label="Oblicz")


# Flyers
class FlyersForm(FlaskForm):
    flyers_patterns = IntegerField(
        label="Ilość wzorów: ",
        validators=[DataRequired()],
        default="1")

    flyers_quantity = IntegerField(
        label="Ilość ulotek: ",
        validators=[DataRequired()],
        default="100")

    flyers_size = SelectField(
        label="Wielkość: ",
        choices=[
            ("a4", "A4"),
            ("a5", "A5"),
            ("a6", "A6"),
            ("dl", "DL"),
            ("other", "14/14 14,5/14,5 15/15")],
        validators=[DataRequired()],
        default="a5")

    flyers_paper_weight = SelectField(
        label="Gramatura: ",
        choices=[
            ("130", "130"),
            ("150", "150"),
            ("170", "170"),
            ("200", "200"),
            ("250", "250"),
            ("300", "300"),
            ("350", "350"),
            ("fancy", "Ozdobny")],
        validators=[DataRequired()],
        default="130")

    flyers_overprint = SelectField(
        label="Zadruk: ",
        choices=[
            ("40", "4+0"),
            ("44", "4+4")],
        validators=[DataRequired()],
        default="40")

    flyers_foil = SelectField(
        label="Foliowanie: ",
        choices=[
            ("none", "Brak"),
            ("10", "1+0"),
            ("11", "1+1")],
        validators=[DataRequired()],
        default="none")

    flyers_margin = IntegerField(
        label="Marża: ",
        default="75")

    submit = SubmitField(label="Oblicz")


# Folded flyers
class FlyersFoldedForm(FlaskForm):
    flyers_folded_patterns = IntegerField(
        label="Ilość wzorów: ",
        validators=[DataRequired()],
        default="1")

    flyers_folded_quantity = IntegerField(
        label="Ilość ulotek: ",
        validators=[DataRequired()],
        default="100")

    flyers_folded_fold = SelectField(
        label="Składanie/bigowanie: ",
        choices=[
            ("big", "Tylko bigowanie"),
            ("fold_big", "Składanie i bigowanie")],
        validators=[DataRequired()],
        default="big")

    flyers_folded_size = SelectField(
        label="Wielkość: ",
        choices=[
            ("a3a4", "A3 do A4"),
            ("a4a5", "A4 do A5"),
            ("a5a6", "A5 do A6"),
            ("a6a7", "A6 do A7"),
            ("a4dl", "A4 do DL"),
            ("2xdldl", "2xDL do DL"),
            ("2814", "28 do 14"),
            ("halfs", "29 do 14,5, 30 do 15")],
        validators=[DataRequired()],
        default="a4a5")

    flyers_folded_paper_weight = SelectField(
        label="Gramatura: ",
        choices=[
            ("130", "130"),
            ("150", "150"),
            ("170", "170"),
            ("200", "200"),
            ("250", "250"),
            ("300", "300"),
            ("350", "350"),
            ("fancy", "Ozdobny")],
        validators=[DataRequired()],
        default="130")

    flyers_folded_overprint = SelectField(
        label="Zadruk: ",
        choices=[
            ("40", "4+0"),
            ("44", "4+4")],
        validators=[DataRequired()],
        default="44")

    flyers_folded_foil = SelectField(
        label="Foliowanie: ",
        choices=[
            ("none", "Brak"),
            ("10", "1+0"),
            ("11", "1+1")],
        validators=[DataRequired()],
        default="none")

    flyers_folded_margin = IntegerField(
        label="Marża: ",
        default="75")

    submit = SubmitField(label="Oblicz")


# Custom flyers
class FlyersCustomForm(FlaskForm):
    flyers_custom_length = FloatField(
        label="Długość [mm]: ",
        validators=[DataRequired()],
        default="10")

    flyers_custom_width = FloatField(
        label="Szerokość [mm]: ",
        validators=[DataRequired()],
        default="10")

    flyers_custom_quantity = IntegerField(
        label="Ilość ulotek: ",
        validators=[DataRequired()],
        default="100")

    flyers_custom_fold = SelectField(
        label="Składanie/bigowanie: ",
        choices=[
            ("none", "Brak"),
            ("big", "Tylko bigowanie"),
            ("fold_big", "Składanie i bigowanie")],
        validators=[DataRequired()],
        default="none")

    flyers_custom_paper_weight = SelectField(
        label="Gramatura: ",
        choices=[
            ("130", "130"),
            ("150", "150"),
            ("170", "170"),
            ("200", "200"),
            ("250", "250"),
            ("300", "300"),
            ("350", "350"),
            ("fancy", "Ozdobny")],
        validators=[DataRequired()],
        default="130")

    flyers_custom_overprint = SelectField(
        label="Zadruk: ",
        choices=[
            ("40", "4+0"),
            ("44", "4+4")],
        validators=[DataRequired()],
        default="40")

    flyers_custom_foil = SelectField(
        label="Foliowanie: ",
        choices=[
            ("none", "Brak"),
            ("10", "1+0"),
            ("11", "1+1")],
        validators=[DataRequired()],
        default="none")

    flyers_custom_margin = IntegerField(
        label="Marża: ",
        default="75")

    submit = SubmitField(label="Oblicz")


# Roll-Ups
class RollUpForm(FlaskForm):
    rollup_patterns = IntegerField(
        label="Ilość wzorów: ",
        validators=[DataRequired()],
        default="1")

    rollup_quantity = IntegerField(
        label="Ilość: ",
        validators=[DataRequired()],
        default="1")

    rollup_thickness = SelectField(
        label="Szerokość/grubość: ",
        choices=[
            ("85", "85"),
            ("100", "100"),
            ("120", "120"),
            ("150", "150")],
        validators=[DataRequired()],
        default="85")

    rollup_margin = IntegerField(
        label="Marża: ",
        default="75")

    submit = SubmitField(label="Oblicz")


# Banners
class BannerForm(FlaskForm):
    banner_length = FloatField(
        label="Długość [cm]: ",
        validators=[DataRequired()],
        default="200")

    banner_width = FloatField(
        label="Szerokość [cm]: ",
        validators=[DataRequired()],
        default="100")

    banner_quantity = IntegerField(
        label="Ilość: ",
        validators=[DataRequired()],
        default="1")

    banner_tape = SelectField(
        label="Taśma banerowa: ",
        choices=[
            ("tak", "Tak"),
            ("nie", "Nie")],
        validators=[DataRequired()],
        default="tak")

    banner_eyelet = SelectField(
        label="Oczka: ",
        choices=[
            ("none", "Brak"),
            ("25cm", "Co 25 cm"),
            ("50cm", "Co 50 cm"),
            ("corners", "Tylko rogi")],
        validators=[DataRequired()],
        default="50cm")

    banner_lamination = SelectField(
        label="Laminowanie płynem: ",
        choices=[
            ("tak", "Tak"),
            ("nie", "Nie")],
        validators=[DataRequired()],
        default="nie")

    banner_margin = IntegerField(
        label="Marża: ",
        default="75")

    submit = SubmitField(label="Oblicz")


# Foils
class FoilForm(FlaskForm):
    foil_length = FloatField(
        label="Długość [cm]: ",
        validators=[DataRequired()],
        default="100")

    foil_width = FloatField(
        label="Szerokość [cm]: ",
        validators=[DataRequired()],
        default="100")

    foil_quantity = IntegerField(
        label="Ilość: ",
        validators=[DataRequired()],
        default="1")

    foil_lamination = SelectField(
        label="Laminowanie: ",
        choices=[
            ("none", "Brak"),
            ("liquid", "Płynem"),
            ("foil", "Folią")],
        validators=[DataRequired()],
        default="none")

    foil_margin = IntegerField(
        label="Marża: ",
        default="75")

    submit = SubmitField(label="Oblicz")


# OWVs
class OwvForm(FlaskForm):
    owv_length = FloatField(
        label="Długość [cm]: ",
        validators=[DataRequired()],
        default="100")

    owv_width = FloatField(
        label="Szerokość [cm]: ",
        validators=[DataRequired()],
        default="100")

    owv_quantity = IntegerField(
        label="Ilość: ",
        validators=[DataRequired()],
        default="1")

    owv_lamination = SelectField(
        label="Laminowanie płynem: ",
        choices=[
            ("tak", "Tak"),
            ("nie", "Nie")],
        validators=[DataRequired()],
        default="nie")

    owv_margin = IntegerField(
        label="Marża: ",
        default="75")

    submit = SubmitField(label="Oblicz")


# Solvent posters
class PostersSolForm(FlaskForm):
    posters_sol_quantity = IntegerField(
        label="Ilość: ",
        validators=[DataRequired()],
        default="1")

    posters_sol_size = SelectField(
        label="Wielkość: ",
        choices=[
            ("a2", "A2"),
            ("a1", "A1"),
            ("a0", "A0"),
            ("b2", "B2"),
            ("b1", "B1")],
        validators=[DataRequired()],
        default="a2")

    posters_sol_paperweight = SelectField(
        label="Gramatura: ",
        choices=[
            ("150", "150"),
            ("200", "200")],
        validators=[DataRequired()],
        default="150")

    posters_sol_margin = IntegerField(
        label="Marża: ",
        default="75")

    submit = SubmitField(label="Oblicz")


# Custom solvent posters
class PostersSolCustomForm(FlaskForm):
    posters_sol_custom_quantity = IntegerField(
        label="Ilość: ",
        validators=[DataRequired()],
        default="1")

    posters_sol_custom_length = FloatField(
        label="Długość [cm]: ",
        validators=[DataRequired()],
        default="100")

    posters_sol_custom_width = FloatField(
        label="Szerokość [cm]: ",
        validators=[DataRequired()],
        default="100")

    posters_sol_custom_paperweight = SelectField(
        label="Gramatura: ",
        choices=[
            ("150", "150"),
            ("200", "200")],
        validators=[DataRequired()],
        default="150")

    posters_sol_custom_margin = IntegerField(
        label="Marża: ",
        default="75")

    submit = SubmitField(label="Oblicz")


# Field calc
class KarkuratorForm(FlaskForm):
    length = FloatField(
        label="Długość [cm]: ",
        validators=[DataRequired()],
        default="25")

    width = FloatField(
        label="Szerokość [cm]: ",
        validators=[DataRequired()],
        default="25")

    length_sheet = FloatField(
        label="Długość arkusza [cm]: ",
        validators=[DataRequired()],
        default="100")

    width_sheet = FloatField(
        label="Szerokość arkusza [cm]: ",
        validators=[DataRequired()],
        default="100")

    submit = SubmitField(label="Oblicz")


# Basic printing calc
class BasicForm(FlaskForm):
    basic_quantity = IntegerField(
        label="Ilość stron: ",
        validators=[DataRequired()],
        default="1")

    basic_sides = SelectField(
        label="Jednostronnie/dwustronnie/kolor",
        choices=[
            ("10", "1+0"),
            ("11", "1+1"),
            ("color", "Kolor")],
        validators=[DataRequired()],
        default="10")

    basic_size = SelectField(
        label="Rozmiar: ",
        choices=[
            ("a4", "A4"),
            ("a3", "A3")],
        validators=[DataRequired()],
        default="a4")
    
    submit = SubmitField(label="Oblicz")
