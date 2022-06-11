from flask.helpers import flash, url_for
from flask import render_template, redirect, request
from flask_login import login_user, logout_user, login_required
from calc.forms import FlyersCustomForm, FlyersFoldedForm, FlyersForm, LoginForm, PostersForm, VarChangerForm, BusinessCardsForm, RollUpForm, BannerForm, FoilForm, OwvForm, PostersSolForm, \
    PostersSolCustomForm, KarkuratorForm, BasicForm
from calc.models import User, Variable
from calc import app, db
from math import floor

""" Main file where calculations of each product become a real thing. """


@app.route("/")
def home_page():
    """ Simple template just to be here. 
        It can be used as an information page. """
    return render_template("home.html")


login_flash_message = "No, coś Ci nie wyszło - przypomnij sobie dane albo spadaj stąd."

@app.route("/login", methods=["GET", "POST"])
def login_page():
    """ Login require to access variables changer page.
        We don"t want to all users have possibility to change values.
        They should not be concerned about them. """
    form = LoginForm()

    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        attempted_password = User.query.filter_by(password_hash=form.password.data).first()
        if attempted_user and attempted_password:
            login_user(attempted_user)
            login_user(attempted_password)
            flash("Działaj śmiało!", category="success")
            return redirect(url_for("home_page"))
        else:
            flash(login_flash_message, category="danger")

    return render_template("variables/login.html",
                           form=form)


@app.route("/logout")
def logout_page():
    """ If login exists then there should be logout. Nothing special. """
    logout_user()
    flash("Nara, Szefuniu.", category="info")
    return redirect(url_for("home_page"))


@app.route("/changer", methods=["GET", "POST"])
@login_required
def var_changer():
    """ Page only for the chosen ones.
        They are able to change values of variables which are use to calculations. """
    var_changer_form = VarChangerForm()

    new_value = var_changer_form.new_value.data

    if request.method == "POST":
        """ Values changer in the database.
            Query by value"s name.
            Flash message about value change for confirmation. """
        var_to_change = request.form.get("changed_value")
        var_obj = Variable.query.filter_by(name=var_to_change).first()
        if var_obj:
            var_obj.value = new_value
            db.session.commit()
            flash(f"Wartość {var_obj.desc} została zmieniona na {var_obj.value}.", category="info")

    variables = Variable.query.all()

    return render_template("variables/var_changer.html",
                           variables=variables,
                           var_changer_form=var_changer_form)


""" Variables from DB use to calculations. """
sra3Ryza130g = Variable.query.filter_by(name="sra3Ryza130g").first().value
sra3Ryza150g = Variable.query.filter_by(name="sra3Ryza150g").first().value
sra3Ryza170g = Variable.query.filter_by(name="sra3Ryza170g").first().value
sra3Ryza200g = Variable.query.filter_by(name="sra3Ryza200g").first().value
sra3Ryza250g = Variable.query.filter_by(name="sra3Ryza250g").first().value
sra3Ryza300g = Variable.query.filter_by(name="sra3Ryza300g").first().value
sra3Ryza350g = Variable.query.filter_by(name="sra3Ryza350g").first().value
sra3RyzaOzdobny = Variable.query.filter_by(name="sra3RyzaOzdobny").first().value

iloscRyza125 = Variable.query.filter_by(name="iloscRyza125").first().value
iloscRyza250 = Variable.query.filter_by(name="iloscRyza250").first().value
iloscRyza500 = Variable.query.filter_by(name="iloscRyza500").first().value
iloscRyzaOzdobny = Variable.query.filter_by(name="iloscRyzaOzdobny").first().value

przelotSerwisowy = Variable.query.filter_by(name="przelotSerwisowy").first().value
ryczaltZaGilotyneNozMin = Variable.query.filter_by(name="ryczaltZaGilotyneNozMin").first().value
kosztWliczonyDoPrzelotu = Variable.query.filter_by(name="leasingMaszyny").first().value / 10000.0
stalyProcent = Variable.query.filter_by(name="stalyProcent").first().value
pakowanie = Variable.query.filter_by(name="pakowanie").first().value
iloscNaArkuszu = Variable.query.filter_by(name="iloscNaArkuszu").first().value

ciecieA3PracownikLokal = Variable.query.filter_by(name="ciecieA3PracownikLokal").first().value
ciecieA4PracownikLokal = Variable.query.filter_by(name="ciecieA4PracownikLokal").first().value
ciecieA5PracownikLokal = Variable.query.filter_by(name="ciecieA5PracownikLokal").first().value
ciecieA6PracownikLokal = Variable.query.filter_by(name="ciecieA6PracownikLokal").first().value
ciecieDlPracownikLokal = Variable.query.filter_by(name="ciecieDlPracownikLokal").first().value

ciecieKosztPracownika8MinutLokal = Variable.query.filter_by(name="ciecieKosztPracownika8MinutLokal").first().value
drukKosztPracownika1MinutaLokalZa1Pracownika = Variable.query.filter_by(name="drukKosztPracownika1MinutaLokalZa1Pracownika").first().value
cenaFoliiZaPrzelotSra310 = Variable.query.filter_by(name="cenaFoliiZaPrzelotSra310").first().value
ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3 = Variable.query.filter_by(name="ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3").first().value
foliaKosztPracownikaLokal = Variable.query.filter_by(name="foliaKosztPracownikaLokal").first().value
przygotowanieDoDrukuRozgrzanieMaszyny10Min = Variable.query.filter_by(name="przygotowanieDoDrukuRozgrzanieMaszyny10Min").first().value

cenaPapieruSra3130g = sra3Ryza130g / iloscRyza500
cenaPapieruSra3150g = sra3Ryza150g / iloscRyza500
cenaPapieruSra3170g = sra3Ryza170g / iloscRyza500
cenaPapieruSra3200g = sra3Ryza200g / iloscRyza250
cenaPapieruSra3250g = sra3Ryza250g / iloscRyza250
cenaPapieruSra3300g = sra3Ryza300g / iloscRyza250
cenaPapieruSra3350g = sra3Ryza350g / iloscRyza125
cenaPapieruSra3Ozdobny = sra3RyzaOzdobny / iloscRyzaOzdobny

drukKosztPracownikaLokal36Sra3NaMin = drukKosztPracownika1MinutaLokalZa1Pracownika / 30.0
drukKosztPracownikaLokal36Sra3NaMinWiz = drukKosztPracownika1MinutaLokalZa1Pracownika / 36.0
foliaKosztPracownikaLokal2PrzelotyNaMin = foliaKosztPracownikaLokal / 2.0

skladanieMaszynowe = Variable.query.filter_by(name="skladanieMaszynowe").first().value
przygotowanieMaszynyDoSkladania = Variable.query.filter_by(name="przygotowanieMaszynyDoSkladania").first().value
ryczaltFalcerkaSkladarka = Variable.query.filter_by(name="ryczaltFalcerkaSkladarka").first().value
skladanieReczne = Variable.query.filter_by(name="skladanieReczne").first().value
bigowanie = Variable.query.filter_by(name="bigowanie").first().value
przygotowanieBigownicy = Variable.query.filter_by(name="przygotowanieBigownicy").first().value
ciecie = Variable.query.filter_by(name="ciecie").first().value

blockoutSico420gm = Variable.query.filter_by(name="blockoutSico420gm").first().value
blockoutSico530gm = Variable.query.filter_by(name="blockoutSico530gm").first().value
kosztAtramentM2 = Variable.query.filter_by(name="kosztAtramentM2").first().value
ryczaltMaszyna = Variable.query.filter_by(name="ryczaltMaszyna").first().value
kosztKaseta85 = Variable.query.filter_by(name="kosztKaseta85").first().value
kosztKaseta100 = Variable.query.filter_by(name="kosztKaseta100").first().value
kosztKaseta120 = Variable.query.filter_by(name="kosztKaseta120").first().value
kosztKaseta150 = Variable.query.filter_by(name="kosztKaseta150").first().value
plikMediaZaladowanieTestGlowicy = Variable.query.filter_by(name="plikMediaZaladowanieTestGlowicy").first().value
czasObsMasDrukStawkaPrac = Variable.query.filter_by(name="czasObsMasDrukStawkaPrac").first().value
kosztPracCiecie = Variable.query.filter_by(name="kosztPracCiecie").first().value
kosztPracCiecie150 = Variable.query.filter_by(name="kosztPracCiecie150").first().value
kosztPracMontazKaseta = Variable.query.filter_by(name="kosztPracMontazKaseta").first().value

""" Messages for bugs. """
flash_message = "No, coś nie wyszło. Dodatkowa kropka, przecinek, litera, dziwna liczba?"


@app.route("/karkurator", methods=["GET", "POST"])
def karkurator():
    """ Method which calculates how many target "things" will fit on the single sheet.
        "length" and "width" are values of the end product.
        "length_sheet" and "width_sheet" are values of the sheet which will be used for the product.
        
        Example of use - how many flyers 30x40 will fit on the sheet 145x215. """
    karkurator_form = KarkuratorForm()

    length = karkurator_form.length.data
    width = karkurator_form.width.data
    length_sheet = karkurator_form.length_sheet.data
    width_sheet = karkurator_form.width_sheet.data

    result = False
    customQuantityPerSheet = 0
    customQuantityPerSheet2 = 0

    if request.method == "POST":
        """ Two ways of fitting products on the sheet - horizontally and vertically. """
        if karkurator_form.validate_on_submit():
            customLengthQuantityPerSheet = floor((length_sheet - 13) / int(length))
            customWidthQuantityPerSheet = floor((width_sheet - 8) / int(width))
            customQuantityPerSheet = customLengthQuantityPerSheet * customWidthQuantityPerSheet

            customLengthQuantityPerSheet2 = floor((width_sheet - 13) / int(length))
            customWidthQuantityPerSheet2 = floor((length_sheet - 8) / int(width))
            customQuantityPerSheet2 = customLengthQuantityPerSheet2 * customWidthQuantityPerSheet2

            result = True
        else:
            flash("Nie używaj przecinków, bo nie wyjdzie. Na razie nie działamy z przecinkami. Machnij kropkę.", category="danger")

    return render_template("variables/karkurator.html",
                           result=result,
                           karkurator_form=karkurator_form,
                           customQuantityPerSheet=customQuantityPerSheet,
                           customQuantityPerSheet2=customQuantityPerSheet2)


@app.route("/basic", methods=["GET", "POST"])
def basic():
    """ Method which calculates the cost of usual, basic printing. """
    basic_form = BasicForm()

    """ Variables from the user. """
    basic_quantity_value = basic_form.basic_quantity.data
    basic_sides_value = basic_form.basic_sides.data
    basic_size_value = basic_form.basic_size.data

    result = False
    finalCost = 0
    finalCostMarginVAT = 0

    if request.method == "POST":
        if basic_form.validate_on_submit():
            cost = 0

            if basic_sides_value == "10":
                cost = 0.10 * basic_quantity_value
            elif basic_sides_value == "11":
                cost = 0.09 * basic_quantity_value
            else:
                cost = 0.50 * basic_quantity_value

            if basic_size_value == "a3" and basic_sides_value == "color" and basic_quantity_value > 30:
                cost = 0.80 * basic_quantity_value
            elif basic_size_value == "a3" and basic_sides_value == "color" and basic_quantity_value <= 30:
                cost = 0.90 * basic_quantity_value
            elif basic_size_value == "a3":
                cost *= 2

            finalCost = round(cost, 2)
            finalCostMarginVAT = round(finalCost * 1.23, 2)

            if finalCostMarginVAT < 10:
                finalCostMarginVAT = 10

            result = True
        else:
            flash(flash_message, category="danger")

    return render_template("cyfra/basic.html",
                           result=result,
                           basic_form=basic_form,
                           finalCostMarginVAT=finalCostMarginVAT,
                           finalCost=finalCost)


""" Digital Print - business cards, posters, flyers, folded flyers and custom flyers. """
@app.route("/businesscards", methods=["GET", "POST"])
def business_cards():
    """ Method which calculates the cost of business cards. """
    business_cards_form = BusinessCardsForm()

    """ Variables from user. """
    cards_patterns_value = business_cards_form.cards_patterns.data
    cards_quantity_value = business_cards_form.cards_quantity.data
    cards_margin_value = business_cards_form.cards_margin.data
    cards_overprint_value = business_cards_form.cards_overprint.data
    cards_foil_value = business_cards_form.cards_foil.data
    cards_paper_weight_value = business_cards_form.cards_paper_weight.data

    result = False
    finalCost = 0
    finalCostProfit = 0
    finalCostMargin = 0
    finalCostMarginVAT = 0

    if request.method == "POST":
        if business_cards_form.validate_on_submit():
            ciecie_wizytowek = (ciecieKosztPracownika8MinutLokal + ryczaltZaGilotyneNozMin) * cards_patterns_value

            cost1 = cards_patterns_value * cards_quantity_value / iloscNaArkuszu

            margin = round((cards_margin_value / 100), 3)

            cena_przelotu_pracownik = 0
            if cards_overprint_value == "40":
                cena_przelotu_pracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu + drukKosztPracownikaLokal36Sra3NaMinWiz))
            else:
                cena_przelotu_pracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu + drukKosztPracownikaLokal36Sra3NaMinWiz))

            foliowanie = cenaFoliiZaPrzelotSra310 + ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3 + foliaKosztPracownikaLokal2PrzelotyNaMin
            if cards_foil_value == "none":
                foliowanie = 0
            elif cards_foil_value == "10" and cards_overprint_value == "44":
                foliowanie = foliowanie * 2
            elif cards_foil_value == "11" and cards_overprint_value == "44":
                foliowanie = foliowanie * 4
            elif cards_foil_value == "10":
                foliowanie = foliowanie
            elif cards_foil_value == "11":
                foliowanie = foliowanie * 2
            else:
                foliowanie = float(foliowanie * 4)

            cost2 = cenaPapieruSra3350g + cena_przelotu_pracownik + foliowanie

            finalCost = round(((cost1 * cost2) + ciecie_wizytowek + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min), 2)

            if cards_paper_weight_value == "fancy":
                finalCost *= 1.3

            finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 2)
            finalCostMargin = round((finalCostProfit + (finalCostProfit * margin)), 2)
            finalCostMarginVAT = round(finalCostMargin * 1.23, 2)
            result = True
        else:
            flash(flash_message, category="danger")

    return render_template("cyfra/business_cards.html",
                           result=result,
                           business_cards_form=business_cards_form,
                           finalCostMarginVAT=finalCostMarginVAT,
                           finalCostMargin=finalCostMargin)


@app.route("/posters", methods=["GET", "POST"])
def posters():
    """ Method which calculates the cost of posters. """
    posters_form = PostersForm()

    """ Variables from user. """
    posters_patterns_value = posters_form.posters_patterns.data
    posters_quantity_value = posters_form.posters_quantity.data
    posters_size_value = posters_form.posters_size.data
    posters_paper_weight_value = posters_form.posters_paper_weight.data
    posters_overprint_value = posters_form.posters_overprint.data
    posters_foil_value = posters_form.posters_foil.data
    posters_margin_value = posters_form.posters_margin.data

    result = False
    finalCost = 0
    finalCostProfit = 0
    finalCostMargin = 0
    finalCostMarginVAT = 0

    if request.method == "POST":
        if posters_form.validate_on_submit():
            margin = round((posters_margin_value / 100), 3)

            cost = 0
            if posters_size_value == "a4":
                cost = posters_patterns_value * posters_quantity_value / 2
            else:
                cost = posters_patterns_value * posters_quantity_value / 1

            cenaPrzelotuPracownik = 0
            if posters_overprint_value == "40":
                cenaPrzelotuPracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
            else:
                cenaPrzelotuPracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin

            foliowanie = cenaFoliiZaPrzelotSra310 + ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3 + foliaKosztPracownikaLokal2PrzelotyNaMin
            if posters_foil_value == "10":
                foliowanie = foliowanie
            elif posters_foil_value == "11":
                foliowanie = foliowanie * 2 + drukKosztPracownikaLokal36Sra3NaMin
            elif posters_paper_weight_value == "fancy":
                foliowanie = drukKosztPracownikaLokal36Sra3NaMin
            else:
                foliowanie = 0

            ciecie = 0
            if posters_size_value == "a4":
                ciecie = (ciecieA4PracownikLokal + ryczaltZaGilotyneNozMin) * posters_patterns_value
            else:
                ciecie = (ciecieA3PracownikLokal + ryczaltZaGilotyneNozMin) * posters_patterns_value

            finalCost = 0
            if posters_paper_weight_value == "130":
                finalCost = (cost * (cenaPapieruSra3130g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif posters_paper_weight_value == "150":
                finalCost = (cost * (cenaPapieruSra3150g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif posters_paper_weight_value == "170":
                finalCost = (cost * (cenaPapieruSra3170g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif posters_paper_weight_value == "200":
                finalCost = (cost * (cenaPapieruSra3200g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif posters_paper_weight_value == "250":
                finalCost = (cost * (cenaPapieruSra3250g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif posters_paper_weight_value == "300":
                finalCost = (cost * (cenaPapieruSra3300g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif posters_paper_weight_value == "350":
                finalCost = (cost * (cenaPapieruSra3350g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            else:
                finalCost = (cost * (cenaPapieruSra3Ozdobny + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)

            finalCost = round(finalCost, 2)
            finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 2)
            finalCostMargin = round((finalCostProfit + (finalCostProfit * margin)), 2)
            finalCostMarginVAT = round(finalCostMargin * 1.23, 2)
            result = True
        else:
            flash(flash_message, category="danger")

    return render_template("cyfra/posters.html",
                           result=result,
                           posters_form=posters_form,
                           finalCostMarginVAT=finalCostMarginVAT,
                           finalCostMargin=finalCostMargin)


@app.route("/flyers", methods=["GET", "POST"])
def flyers():
    """ Method which calculates the cost of flyers. """
    flyers_form = FlyersForm()

    """ Variables from user. """
    flyers_patterns_value = flyers_form.flyers_patterns.data
    flyers_quantity_value = flyers_form.flyers_quantity.data
    flyers_size_value = flyers_form.flyers_size.data
    flyers_paper_weight_value = flyers_form.flyers_paper_weight.data
    flyers_overprint_value = flyers_form.flyers_overprint.data
    flyers_foil_value = flyers_form.flyers_foil.data
    flyers_margin_value = flyers_form.flyers_margin.data

    result = False
    finalCost = 0
    finalCostProfit = 0
    finalCostMargin = 0
    finalCostMarginVAT = 0

    if request.method == "POST":
        if flyers_form.validate_on_submit():
            margin = round((flyers_margin_value / 100), 3)

            cost = 0
            if flyers_size_value == "a4":
                cost = flyers_patterns_value * flyers_quantity_value / 2
            elif flyers_size_value == "a5" or flyers_size_value == "other":
                cost = flyers_patterns_value * flyers_quantity_value / 4
            elif flyers_size_value == "a6":
                cost = flyers_patterns_value * flyers_quantity_value / 8
            else:
                cost = flyers_patterns_value * flyers_quantity_value / 6

            cenaPrzelotuPracownik = 0
            if flyers_overprint_value == "40":
                cenaPrzelotuPracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
            else:
                cenaPrzelotuPracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin

            foliowanie = cenaFoliiZaPrzelotSra310 + ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3 + foliaKosztPracownikaLokal2PrzelotyNaMin
            if flyers_foil_value == "10":
                foliowanie = foliowanie
            elif flyers_foil_value == "11":
                foliowanie = foliowanie * 2 + drukKosztPracownikaLokal36Sra3NaMin
            elif flyers_paper_weight_value == "fancy":
                foliowanie = drukKosztPracownikaLokal36Sra3NaMin
            else:
                foliowanie = 0

            ciecie = 0
            if flyers_size_value == "a4":
                ciecie = (ciecieA4PracownikLokal + ryczaltZaGilotyneNozMin) * flyers_patterns_value
            elif flyers_size_value == "a5" or flyers_size_value == "other":
                ciecie = (ciecieA5PracownikLokal + ryczaltZaGilotyneNozMin) * flyers_patterns_value
            elif flyers_size_value == "a6":
                ciecie = (ciecieA6PracownikLokal + ryczaltZaGilotyneNozMin) * flyers_patterns_value
            else:
                ciecie = (ciecieDlPracownikLokal + ryczaltZaGilotyneNozMin) * flyers_patterns_value

            finalCost = 0
            if flyers_paper_weight_value == "130":
                finalCost = (cost * (cenaPapieruSra3130g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_paper_weight_value == "150":
                finalCost = (cost * (cenaPapieruSra3150g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_paper_weight_value == "170":
                finalCost = (cost * (cenaPapieruSra3170g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_paper_weight_value == "200":
                finalCost = (cost * (cenaPapieruSra3200g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_paper_weight_value == "250":
                finalCost = (cost * (cenaPapieruSra3250g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_paper_weight_value == "300":
                finalCost = (cost * (cenaPapieruSra3300g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_paper_weight_value == "350":
                finalCost = (cost * (cenaPapieruSra3350g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            else:
                finalCost = (cost * (cenaPapieruSra3Ozdobny + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)

            finalCost = round(finalCost, 2)
            finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 2)
            finalCostMargin = round((finalCostProfit + (finalCostProfit * margin)), 2)
            finalCostMarginVAT = round(finalCostMargin * 1.23, 2)
            result = True
        else:
            flash(flash_message, category="danger")

    return render_template("cyfra/flyers.html",
                           result=result,
                           flyers_form=flyers_form,
                           finalCostMarginVAT=finalCostMarginVAT,
                           finalCostMargin=finalCostMargin)


@app.route("/flyersfolded", methods=["GET", "POST"])
def flyers_folded():
    """ Method which calculates the cost of folded flyers. """
    flyers_folded_form = FlyersFoldedForm()

    """ Variables from user. """
    flyers_folded_patterns_value = flyers_folded_form.flyers_folded_patterns.data
    flyers_folded_quantity_value = flyers_folded_form.flyers_folded_quantity.data
    flyers_folded_fold_value = flyers_folded_form.flyers_folded_fold.data
    flyers_folded_size_value = flyers_folded_form.flyers_folded_size.data
    flyers_folded_paper_weight_value = flyers_folded_form.flyers_folded_paper_weight.data
    flyers_folded_overprint_value = flyers_folded_form.flyers_folded_overprint.data
    flyers_folded_foil_value = flyers_folded_form.flyers_folded_foil.data
    flyers_folded_margin_value = flyers_folded_form.flyers_folded_margin.data

    result = False
    finalCost = 0
    finalCostProfit = 0
    finalCostProfitMargin = 0
    finalCostProfitMarginVAT = 0

    if request.method == "POST":
        if flyers_folded_form.validate_on_submit():
            margin = round((flyers_folded_margin_value / 100), 3)

            cenaPrzelotuPracownik = 0
            if flyers_folded_overprint_value == "40":
                cenaPrzelotuPracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
            elif flyers_folded_overprint_value == "40" and flyers_folded_foil_value == "10":
                cenaPrzelotuPracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + (2 * drukKosztPracownikaLokal36Sra3NaMin)
            elif flyers_folded_overprint_value == "44" and flyers_folded_foil_value == "11":
                cenaPrzelotuPracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + (2 * drukKosztPracownikaLokal36Sra3NaMin)
            else:
                cenaPrzelotuPracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin

            foliowanie = cenaFoliiZaPrzelotSra310 + ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3 + foliaKosztPracownikaLokal2PrzelotyNaMin
            if flyers_folded_foil_value == "10":
                foliowanie = foliowanie
            elif flyers_folded_foil_value == "11":
                foliowanie = foliowanie * 2
            else:
                foliowanie = 0

            ciecie = 0
            if flyers_folded_size_value == "a5a6":
                ciecie = (ciecieA5PracownikLokal + ryczaltZaGilotyneNozMin) * flyers_folded_patterns_value
            elif flyers_folded_size_value == "a6a7":
                ciecie = (ciecieA6PracownikLokal + ryczaltZaGilotyneNozMin) * flyers_folded_patterns_value
            else:
                ciecie = ((ciecieA4PracownikLokal + ryczaltZaGilotyneNozMin) * flyers_folded_patterns_value)

            foldMachineArm = round(ryczaltFalcerkaSkladarka + przygotowanieMaszynyDoSkladania + (skladanieMaszynowe * flyers_folded_quantity_value), 3)

            foldBig = 0
            if flyers_folded_fold_value == "big" and flyers_folded_size_value == "a4dl":
                foldBig = round(przygotowanieBigownicy + (bigowanie * flyers_folded_quantity_value * 2) + (skladanieReczne * flyers_folded_quantity_value * 0), 3)
            elif flyers_folded_fold_value == "fold_big" and flyers_folded_size_value == "a4dl":
                foldBig = round(przygotowanieBigownicy + (bigowanie * flyers_folded_quantity_value * 2) + (skladanieReczne * flyers_folded_quantity_value * 2), 3)
            elif flyers_folded_fold_value == "big":
                foldBig = round(przygotowanieBigownicy + (bigowanie * flyers_folded_quantity_value), 3)
            else:
                foldBig = round(przygotowanieBigownicy + (bigowanie * flyers_folded_quantity_value) + skladanieReczne * flyers_folded_quantity_value, 3)

            cost = 0
            if flyers_folded_size_value == "a3a4":
                cost = flyers_folded_patterns_value * flyers_folded_quantity_value
            elif flyers_folded_size_value == "a5a6":
                cost = flyers_folded_patterns_value * flyers_folded_quantity_value / 4
            elif flyers_folded_size_value == "a6a7":
                cost = flyers_folded_patterns_value * flyers_folded_quantity_value / 8
            elif flyers_folded_size_value == "2814":
                cost = flyers_folded_patterns_value * flyers_folded_quantity_value / 3
            else:
                cost = flyers_folded_patterns_value * flyers_folded_quantity_value / 2

            finalCost = 0
            if flyers_folded_paper_weight_value == "130":
                finalCost = (cost * (cenaPapieruSra3130g + cenaPrzelotuPracownik + foliowanie) + foldMachineArm + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_folded_paper_weight_value == "150":
                finalCost = (cost * (cenaPapieruSra3150g + cenaPrzelotuPracownik + foliowanie) + foldMachineArm + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_folded_paper_weight_value == "170":
                finalCost = (cost * (cenaPapieruSra3170g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_folded_paper_weight_value == "200":
                finalCost = (cost * (cenaPapieruSra3200g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_folded_paper_weight_value == "250":
                finalCost = (cost * (cenaPapieruSra3250g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_folded_paper_weight_value == "300":
                finalCost = (cost * (cenaPapieruSra3300g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_folded_paper_weight_value == "350":
                finalCost = (cost * (cenaPapieruSra3350g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            else:
                finalCost = (cost * (cenaPapieruSra3Ozdobny + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)

            finalCost = round(finalCost, 2)
            finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 2)
            finalCostProfitMargin = round((finalCostProfit + (finalCostProfit * margin)), 2)
            finalCostProfitMarginVAT = round(finalCostProfitMargin * 1.23, 2)
            result = True
        else:
            flash(flash_message, category="danger")

    return render_template("cyfra/flyers_folded.html",
                           result=result,
                           flyers_folded_form=flyers_folded_form,
                           finalCostMarginVAT=finalCostProfitMarginVAT,
                           finalCostProfitMargin=finalCostProfitMargin)


@app.route("/flyerscustom", methods=["GET", "POST"])
def flyers_custom():
    """ Method which calculates the cost of custom flyers. """
    flyers_custom_form = FlyersCustomForm()

    """ Variables from user. """
    flyers_custom_length_value = flyers_custom_form.flyers_custom_length.data
    flyers_custom_width_value = flyers_custom_form.flyers_custom_width.data
    flyers_custom_quantity_value = flyers_custom_form.flyers_custom_quantity.data
    flyers_custom_fold_value = flyers_custom_form.flyers_custom_fold.data
    flyers_custom_paper_weight_value = flyers_custom_form.flyers_custom_paper_weight.data
    flyers_custom_overprint_value = flyers_custom_form.flyers_custom_overprint.data
    flyers_custom_foil_value = flyers_custom_form.flyers_custom_foil.data
    flyers_custom_margin_value = flyers_custom_form.flyers_custom_margin.data

    result = False
    finalCost = 0
    finalCostProfit = 0
    finalCostProfitMargin = 0
    finalCostProfitMarginVAT = 0
    customQuantityPerSheet = 0
    customQuantityPerSheet2 = 0

    if request.method == "POST":
        if flyers_custom_form.validate_on_submit():
            margin = round((flyers_custom_margin_value / 100), 3)

            cenaPrzelotuPracownik = 0
            if flyers_custom_overprint_value == "40":
                cenaPrzelotuPracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
            elif flyers_custom_overprint_value == "40" and flyers_custom_foil_value == "10":
                cenaPrzelotuPracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + (2 * drukKosztPracownikaLokal36Sra3NaMin)
            elif flyers_custom_overprint_value == "44" and flyers_custom_foil_value == "11":
                cenaPrzelotuPracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + (2 * drukKosztPracownikaLokal36Sra3NaMin)
            else:
                cenaPrzelotuPracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin

            foliowanie = cenaFoliiZaPrzelotSra310 + ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3 + foliaKosztPracownikaLokal2PrzelotyNaMin
            if flyers_custom_foil_value == "10":
                foliowanie = foliowanie
            elif flyers_custom_foil_value == "11":
                foliowanie = foliowanie * 2
            else:
                foliowanie = 0

            foldMachineArm = round(ryczaltFalcerkaSkladarka + przygotowanieMaszynyDoSkladania + (skladanieMaszynowe * flyers_custom_quantity_value), 3)

            foldBig = 0
            if flyers_custom_fold_value == "big":
                foldBig = round(przygotowanieBigownicy + (bigowanie * flyers_custom_quantity_value * 2) + (skladanieReczne * flyers_custom_quantity_value * 0), 3)
            elif flyers_custom_fold_value == "fold_big":
                foldBig = round(przygotowanieBigownicy + (bigowanie * flyers_custom_quantity_value * 2) + (skladanieReczne * flyers_custom_quantity_value * 2), 3)
            else:
                foldBig = 0

            # Information about products fit on the single sheet.
            customLengthQuantityPerSheet = floor(309 / int(flyers_custom_length_value))
            customWidthQuantityPerSheet = floor(439 / int(flyers_custom_width_value))
            customQuantityPerSheet = customLengthQuantityPerSheet * customWidthQuantityPerSheet

            cost = flyers_custom_quantity_value / customQuantityPerSheet

            finalCost = 0
            if flyers_custom_paper_weight_value == "130":
                finalCost = (cost * (cenaPapieruSra3130g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_custom_paper_weight_value == "150":
                finalCost = (cost * (cenaPapieruSra3150g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_custom_paper_weight_value == "170":
                finalCost = (cost * (cenaPapieruSra3170g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_custom_paper_weight_value == "200":
                finalCost = (cost * (cenaPapieruSra3200g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_custom_paper_weight_value == "250":
                finalCost = (cost * (cenaPapieruSra3250g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_custom_paper_weight_value == "300":
                finalCost = (cost * (cenaPapieruSra3300g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            elif flyers_custom_paper_weight_value == "350":
                finalCost = (cost * (cenaPapieruSra3350g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
            else:
                finalCost = (cost * (cenaPapieruSra3Ozdobny + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)

            finalCost = round(finalCost, 2)
            finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 2)
            finalCostProfitMargin = round((finalCostProfit + (finalCostProfit * margin)), 2)
            finalCostProfitMarginVAT = round(finalCostProfitMargin * 1.23, 2)
            result = True

            # Second information about products fit on the single sheet.
            customLengthQuantityPerSheet2 = floor(309 / int(flyers_custom_width_value))
            customWidthQuantityPerSheet2 = floor(439 / int(flyers_custom_length_value))
            customQuantityPerSheet2 = customLengthQuantityPerSheet2 * customWidthQuantityPerSheet2
        else:
            flash(flash_message, category="danger")

    return render_template("cyfra/flyers_custom.html",
                           result=result,
                           flyers_custom_form=flyers_custom_form,
                           finalCostMarginVAT=finalCostProfitMarginVAT,
                           finalCostProfitMargin=finalCostProfitMargin,
                           customQuantityPerSheet=customQuantityPerSheet,
                           customQuantityPerSheet2=customQuantityPerSheet2)


""" Solvent Printing - rollups, banners, foils, owvs, posters. """


@app.route("/rollup", methods=["GET", "POST"])
def rollup():
    """ Method which calculates the cost of rollups. """
    rollup_form = RollUpForm()

    """ Variables from user. """
    rollup_patterns_value = rollup_form.rollup_patterns.data
    rollup_quantity_value = rollup_form.rollup_quantity.data
    rollup_thickness_value = rollup_form.rollup_thickness.data
    rollup_margin_value = rollup_form.rollup_margin.data

    # Additional variables for this product.
    cenaMaterial420gm = 2.5 * blockoutSico420gm
    cenaMaterial420gm120 = 2.5 * blockoutSico420gm * 1.2
    cenaMaterial530gm150 = 2.5 * blockoutSico530gm * 1.5
    cenaWydruk85M2 = 0.85 * kosztAtramentM2 * 2.1
    cenaWydruk100M2 = 1.0 * kosztAtramentM2 * 2.1
    cenaWydruk120M2 = 1.2 * kosztAtramentM2 * 2.1
    cenaWydruk150M2 = 1.5 * kosztAtramentM2 * 2.1
    ryczaltSerwis85M2 = ryczaltMaszyna * 0.85 * 2.1
    ryczaltSerwis100M2 = ryczaltMaszyna * 1.0 * 2.1
    ryczaltSerwis120M2 = ryczaltMaszyna * 1.2 * 2.1
    ryczaltSerwis150M2 = ryczaltMaszyna * 1.5 * 2.1
    kosztPracownik85 = czasObsMasDrukStawkaPrac * 0.85 * 2.1
    kosztPracownik100 = czasObsMasDrukStawkaPrac * 1.0 * 2.1
    kosztPracownik120 = czasObsMasDrukStawkaPrac * 1.2 * 2.1
    kosztPracownik150 = czasObsMasDrukStawkaPrac * 1.5 * 2.1

    result = False
    finalCost = 0
    finalCostProfit = 0
    finalCostProfitMargin = 0
    finalCostProfitMarginVAT = 0

    if request.method == "POST":
        if rollup_form.validate_on_submit():
            margin = round((rollup_margin_value / 100), 3)

            finalCost = 0
            if rollup_thickness_value == "85":
                finalCost = (plikMediaZaladowanieTestGlowicy + pakowanie + (cenaMaterial420gm + cenaWydruk85M2 + ryczaltSerwis85M2 + kosztKaseta85
                                                                            + kosztPracownik85 + kosztPracCiecie + kosztPracMontazKaseta) * rollup_quantity_value) * rollup_patterns_value
            elif rollup_thickness_value == "100":
                finalCost = (plikMediaZaladowanieTestGlowicy + pakowanie + (cenaMaterial420gm + cenaWydruk100M2 + ryczaltSerwis100M2 + kosztKaseta100
                                                                            + kosztPracownik100 + kosztPracCiecie + kosztPracMontazKaseta) * rollup_quantity_value) * rollup_patterns_value
            elif rollup_thickness_value == "120":
                finalCost = (plikMediaZaladowanieTestGlowicy + pakowanie + (cenaMaterial420gm120 + cenaWydruk120M2 + ryczaltSerwis120M2 + kosztKaseta120
                                                                            + kosztPracownik120 + kosztPracCiecie + kosztPracMontazKaseta) * rollup_quantity_value) * rollup_patterns_value
            elif rollup_thickness_value == "150":
                finalCost = (plikMediaZaladowanieTestGlowicy + pakowanie + (cenaMaterial530gm150 + cenaWydruk150M2 + ryczaltSerwis150M2 + kosztKaseta150
                                                                            + kosztPracownik150 + kosztPracCiecie150 + kosztPracMontazKaseta) * rollup_quantity_value) * rollup_patterns_value
            else:
                finalCost = 666.66

            finalCost = round(finalCost, 2)
            finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 2)
            finalCostProfitMargin = round((finalCostProfit + (finalCostProfit * margin)), 2)
            finalCostProfitMarginVAT = round(finalCostProfitMargin * 1.23, 2)
            result = True
        else:
            flash(flash_message, category="danger")

    return render_template("solwent/rollup.html",
                           result=result,
                           rollup_form=rollup_form,
                           finalCostProfitMarginVAT=finalCostProfitMarginVAT,
                           finalCostProfitMargin=finalCostProfitMargin)


@app.route("/banner", methods=["GET", "POST"])
def banner():
    """ Method which calculates the cost of banners. """
    banner_form = BannerForm()

    """ Variables from user. """
    banner_length_value = banner_form.banner_length.data
    banner_width_value = banner_form.banner_width.data
    banner_quantity_value = banner_form.banner_quantity.data
    banner_tape_value = banner_form.banner_tape.data
    banner_eyelet_value = banner_form.banner_eyelet.data
    banner_lamination_value = banner_form.banner_lamination.data
    banner_margin_value = banner_form.banner_margin.data

    result = False
    finalCost = 0
    finalCostProfit = 0
    finalCostProfitMargin = 0
    finalCostProfitMarginVAT = 0
    message = ""

    if request.method == "POST":
        if banner_form.validate_on_submit():
            margin = round((banner_margin_value / 100), 3)

            bannerCircuit = float(2 * (banner_length_value + banner_width_value))
            bannerArea = banner_length_value * banner_width_value

            if (banner_width_value >= 160):
                message = "Nie drukujemy tego u nas. Dzwoń do Krzysia lub Marty."

            bannerTapeCost = 0
            if banner_tape_value == "Tak":
                bannerTapeCost = float((bannerCircuit / 100) * 0.46)
            else:
                bannerTapeCost = 0

            bannerEyeletCost = 0
            bannerSingleEyeletCost = 0.09
            if banner_eyelet_value == "25cm":
                bannerEyeletCost = float(((bannerCircuit / 100) / 0.25) * bannerSingleEyeletCost)
            elif banner_eyelet_value == "50cm":
                bannerEyeletCost = float(((bannerCircuit / 100) / 0.50) * bannerSingleEyeletCost)
            elif banner_eyelet_value == "corners":
                bannerEyeletCost = 4 * bannerSingleEyeletCost
            else:
                bannerEyeletCost = 0

            bannerLaminationCost = 0
            if banner_lamination_value == "Tak":
                bannerLaminationCost = float((bannerArea / 10000) * 6.0)
                if bannerLaminationCost < 25.0:
                    bannerLaminationCost = 25.0
                else:
                    bannerLaminationCost = float((bannerArea / 10000) * 6.0)
            else:
                bannerLaminationCost = 0

            bannerCut = 5.0
            cenaJednostkowaMaterialBaner = 3.2

            bannerMaterialCost = float(cenaJednostkowaMaterialBaner * (bannerArea / 10000))
            bannerPrintCost = float(kosztAtramentM2 * (bannerArea / 10000))
            bannerRyczaltSerwis = float(ryczaltMaszyna * (bannerArea / 10000))
            kosztPracownikaBaner = 8.0

            finalCost = ((bannerMaterialCost + bannerPrintCost + bannerEyeletCost + bannerTapeCost + bannerLaminationCost + bannerRyczaltSerwis
                          + kosztPracownikaBaner + bannerCut) * banner_quantity_value) + plikMediaZaladowanieTestGlowicy + pakowanie

            finalCost = round(finalCost, 2)
            finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 2)
            finalCostProfitMargin = round((finalCostProfit + (finalCostProfit * margin)), 2)
            finalCostProfitMarginVAT = round(finalCostProfitMargin * 1.23, 2)
            result = True
        else:
            flash(flash_message, category="danger")

    return render_template("solwent/banner.html",
                           result=result,
                           banner_form=banner_form,
                           finalCostProfitMarginVAT=finalCostProfitMarginVAT,
                           finalCostProfitMargin=finalCostProfitMargin,
                           banner_length_value=banner_length_value,
                           banner_width_value=banner_width_value,
                           message=message)


@app.route("/foil", methods=["GET", "POST"])
def foil():
    """ Method which calculates the cost of foils. """
    foil_form = FoilForm()

    """ Variables from user. """
    foil_length_value = foil_form.foil_length.data
    foil_width_value = foil_form.foil_width.data
    foil_quantity_value = foil_form.foil_quantity.data
    foil_lamination_value = foil_form.foil_lamination.data
    foil_margin_value = foil_form.foil_margin.data

    result = False
    finalCost = 0
    finalCostProfit = 0
    finalCostProfitMargin = 0
    finalCostProfitMarginVAT = 0

    if request.method == "POST":
        if foil_form.validate_on_submit():
            margin = round((foil_margin_value / 100), 3)

            foilSingleMaterialCost = 4.65

            foilArea = (foil_length_value / 100) * (foil_width_value / 100)

            foilMaterialCost = foilSingleMaterialCost * foilArea

            foilPrintCost = foilArea * (kosztAtramentM2 + czasObsMasDrukStawkaPrac)

            foilRyczaltSerwis = (foilArea * foil_quantity_value) * ryczaltMaszyna

            przygotowanieDoDrukuRozgrzanieMaszyny = 10.0

            kosztPracownika = foilArea * czasObsMasDrukStawkaPrac

            kosztCiecie = 10.0

            foilLaminationCost = 0
            if foil_lamination_value == "liquid":
                foilLaminationCost = float(foilArea * 6.0)
                if foilLaminationCost < 25.0:
                    foilLaminationCost = 25.0
                else:
                    foilLaminationCost = float(foilArea * 6.0)
            elif foil_lamination_value == "foil":
                foilLaminationCost = float(foilArea * 8.0)
                if foilLaminationCost < 15.0:
                    foilLaminationCost = 15.0
            else:
                foilLaminationCost = 0

            finalCost = foilMaterialCost + ((foilPrintCost + foilRyczaltSerwis + kosztPracownika + kosztCiecie) * foilArea) + przygotowanieDoDrukuRozgrzanieMaszyny + foilLaminationCost + pakowanie

            finalCost = round(finalCost, 2)
            finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 2)
            finalCostProfitMargin = round((finalCostProfit + (finalCostProfit * margin)), 2)
            finalCostProfitMarginVAT = round(finalCostProfitMargin * 1.23, 2)
            result = True
        else:
            flash(flash_message, category="danger")

    return render_template("solwent/foil.html",
                           result=result, foil_form=foil_form,
                           finalCostProfitMarginVAT=finalCostProfitMarginVAT,
                           finalCostProfitMargin=finalCostProfitMargin)


@app.route("/owv", methods=["GET", "POST"])
def owv():
    """ Method which calculates the cost of owvs. """
    owv_form = OwvForm()

    """ Variables from user. """
    owv_length_value = owv_form.owv_length.data
    owv_width_value = owv_form.owv_width.data
    owv_quantity_value = owv_form.owv_quantity.data
    owv_lamination_value = owv_form.owv_lamination.data
    owv_margin_value = owv_form.owv_margin.data

    result = False
    finalCost = 0
    finalCostProfit = 0
    finalCostProfitMargin = 0
    finalCostProfitMarginVAT = 0

    if request.method == "POST":
        if owv_form.validate_on_submit():
            margin = round((owv_margin_value / 100), 3)

            owvArea = (owv_length_value * owv_width_value) / 10000

            owvSingleMaterialCost = 5.6
            owvMaterialCost = owvArea * owvSingleMaterialCost

            owvLaminationCost = 0
            if owv_lamination_value == "tak":
                owvLaminationCost = float(owvArea * 6.0)
                if owvLaminationCost < 25.0:
                    owvLaminationCost = 25.0
                else:
                    owvLaminationCost = float(owvArea * 6.0)
            else:
                owvLaminationCost = 0

            cenaWydrukuOwv = (owvArea * owv_quantity_value) * (kosztAtramentM2 + czasObsMasDrukStawkaPrac)

            ryczaltSerwisOwv = (owvArea * owv_quantity_value) * ryczaltMaszyna

            przygotowaniePlikowZalMedZalPlikowTestGlowicy = 10.0
            kosztPracCiecieM2Folii = 10.0
            kosztPracownikaOwvSolwent = owvArea * czasObsMasDrukStawkaPrac

            finalCost = owvMaterialCost + (
                        cenaWydrukuOwv + ryczaltSerwisOwv + kosztPracownikaOwvSolwent + kosztPracCiecieM2Folii) * owvArea + przygotowaniePlikowZalMedZalPlikowTestGlowicy + pakowanie + owvLaminationCost

            finalCost = round(finalCost, 2)
            finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 2)
            finalCostProfitMargin = round((finalCostProfit + (finalCostProfit * margin)), 2)
            finalCostProfitMarginVAT = round(finalCostProfitMargin * 1.23, 2)
            result = True
        else:
            flash(flash_message, category="danger")

    return render_template("solwent/owv.html",
                           result=result,
                           owv_form=owv_form,
                           finalCostProfitMarginVAT=finalCostProfitMarginVAT,
                           finalCostProfitMargin=finalCostProfitMargin)


@app.route("/posterssol", methods=["GET", "POST"])
def posters_sol():
    """ Method which calculates the cost of posters. """
    posters_sol_form = PostersSolForm()

    """ Variables from user. """
    posters_sol_quantity_value = posters_sol_form.posters_sol_quantity.data
    posters_sol_size_value = posters_sol_form.posters_sol_size.data
    posters_sol_paperweight_value = posters_sol_form.posters_sol_paperweight.data
    posters_sol_margin_value = posters_sol_form.posters_sol_margin.data

    result = False
    finalCost = 0
    finalCostProfit = 0
    finalCostProfitMargin = 0
    finalCostProfitMarginVAT = 0

    if request.method == "POST":
        if posters_sol_form.validate_on_submit():
            margin = round((posters_sol_margin_value / 100), 3)

            paperSize = 0
            if posters_sol_size_value == "a2":
                paperSize = 0.42 * 0.594
            elif posters_sol_size_value == "a1":
                paperSize = 0.594 * 0.841
            elif posters_sol_size_value == "a0":
                paperSize = 0.841 * 1.189
            elif posters_sol_size_value == "b2":
                paperSize = 0.5 * 0.7
            else:
                paperSize = 0.7 * 1.0

            paperMaterialCost = 0
            if posters_sol_paperweight_value == "150":
                paperMaterialCost = 2.0 * paperSize
            else:
                paperMaterialCost = 3.0 * paperSize

            paperCut = 1.0
            paperPrintCost = float(kosztAtramentM2 * paperSize)
            paperRyczaltCost = float(ryczaltMaszyna * paperSize)
            kosztPracownikaPlakat = 2.0

            finalCost = ((paperMaterialCost + paperPrintCost + paperRyczaltCost + kosztPracownikaPlakat + paperCut) * posters_sol_quantity_value) + plikMediaZaladowanieTestGlowicy + pakowanie

            finalCost = round(finalCost, 2)
            finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 2)
            finalCostProfitMargin = round((finalCostProfit + (finalCostProfit * margin)), 2)
            finalCostProfitMarginVAT = round(finalCostProfitMargin * 1.23, 2)
            result = True
        else:
            flash(flash_message, category="danger")

    return render_template("solwent/posters_sol.html",
                           result=result,
                           posters_sol_form=posters_sol_form,
                           finalCostProfitMarginVAT=finalCostProfitMarginVAT,
                           finalCostProfitMargin=finalCostProfitMargin)


@app.route("/postersolcustom", methods=["GET", "POST"])
def posters_sol_custom():
    """ Method which calculates the cost of custom posters. """
    posters_sol_custom_form = PostersSolCustomForm()

    """ Variables from user. """
    posters_sol_custom_quantity_value = posters_sol_custom_form.posters_sol_custom_quantity.data
    posters_sol_custom_length_value = posters_sol_custom_form.posters_sol_custom_length.data
    posters_sol_custom_width_value = posters_sol_custom_form.posters_sol_custom_width.data
    posters_sol_custom_paperweight_value = posters_sol_custom_form.posters_sol_custom_paperweight.data
    posters_sol_custom_margin_value = posters_sol_custom_form.posters_sol_custom_margin.data

    result = False
    finalCost = 0
    finalCostProfit = 0
    finalCostProfitMargin = 0
    finalCostProfitMarginVAT = 0
    message = ""

    if request.method == "POST":
        if posters_sol_custom_form.validate_on_submit():
            margin = round((posters_sol_custom_margin_value / 100), 3)

            paperSize = (posters_sol_custom_length_value * posters_sol_custom_width_value) / 10000

            if (posters_sol_custom_length_value >= 160) or (posters_sol_custom_width_value >= 160):
                flash("Nie drukujemy tego u nas. Dzwoń do Krzysia lub Marty.", category="info")

            paperMaterialCost = 0
            if posters_sol_custom_paperweight_value == "150":
                paperMaterialCost = 2.0 * paperSize
            else:
                paperMaterialCost = 3.0 * paperSize

            paperCut = 1.0
            paperPrintCost = float(kosztAtramentM2 * paperSize)
            paperRyczaltCost = float(ryczaltMaszyna * paperSize)
            kosztPracownikaPlakat = 2.0

            finalCost = ((paperMaterialCost + paperPrintCost + paperRyczaltCost + kosztPracownikaPlakat + paperCut) * posters_sol_custom_quantity_value) + plikMediaZaladowanieTestGlowicy + pakowanie

            finalCost = round(finalCost, 2)
            finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 2)
            finalCostProfitMargin = round((finalCostProfit + (finalCostProfit * margin)), 2)
            finalCostProfitMarginVAT = round(finalCostProfitMargin * 1.23, 2)
            result = True
        else:
            flash(flash_message, category="danger")

    return render_template("solwent/posters_sol_custom.html",
                           result=result,
                           posters_sol_custom_form=posters_sol_custom_form,
                           finalCostProfitMarginVAT=finalCostProfitMarginVAT,
                           finalCostProfitMargin=finalCostProfitMargin,
                           message=message,
                           posters_sol_custom_length_value=posters_sol_custom_length_value,
                           posters_sol_custom_width_value=posters_sol_custom_width_value)
