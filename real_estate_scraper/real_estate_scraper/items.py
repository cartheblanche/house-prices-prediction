# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealEstateScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # GENEL BILGI

    url = scrapy.Field()
    ilan_no = scrapy.Field()
    ilan_durumu = scrapy.Field()
    son_guncelleme_tarihi = scrapy.Field()
    fiyat = scrapy.Field()
    oda_sayisi = scrapy.Field()
    salon_sayisi = scrapy.Field()
    banyo_sayisi = scrapy.Field()
    brut_m2 = scrapy.Field()
    net_m2 = scrapy.Field()
    isinma_tipi = scrapy.Field()
    bina_yasi = scrapy.Field()
    bulundugu_kat = scrapy.Field()
    kat_sayisi = scrapy.Field()
    krediye_uygunluk = scrapy.Field()
    konut_sekli = scrapy.Field()
    esya_durumu = scrapy.Field()
    yakit_tipi = scrapy.Field()
    yapi_tipi = scrapy.Field()
    yapinin_durumu = scrapy.Field()
    kullanim_durumu = scrapy.Field()
    aidat = scrapy.Field()
    takas = scrapy.Field()
    site_icerisinde = scrapy.Field()
    cephe = scrapy.Field()
    tapu_durumu = scrapy.Field()
    kira_getirisi = scrapy.Field()
    depozito = scrapy.Field()
    il = scrapy.Field()
    ilce = scrapy.Field()
    mahalle = scrapy.Field()
    adsl = scrapy.Field()# IC OZELLIKLER
    ahsap_dograma = scrapy.Field()
    alarm = scrapy.Field()
    ankastre_mutfak = scrapy.Field()
    balkon = scrapy.Field()
    barbeku = scrapy.Field()
    beyaz_esyali = scrapy.Field()
    camasir_odasi = scrapy.Field()
    celik_kapi = scrapy.Field()
    dusakabin = scrapy.Field()
    duvar_kagidi = scrapy.Field()
    ebeveyn_banyolu = scrapy.Field()
    giyinme_odasi = scrapy.Field()
    gomme_dolap = scrapy.Field()
    goruntulu_diafon = scrapy.Field()
    hali_kaplama = scrapy.Field()
    hazir_mutfak = scrapy.Field()
    hilton_banyo = scrapy.Field()
    isicam = scrapy.Field()
    jakuzi = scrapy.Field()
    kablo_tv_uydu = scrapy.Field()
    kapali_balkon = scrapy.Field()
    kartonpiyer = scrapy.Field()
    klima = scrapy.Field()
    laminant_mutfak = scrapy.Field()
    marley = scrapy.Field()
    mermer_zemin = scrapy.Field()
    mobilyali = scrapy.Field()
    mutfak_dogalgazi = scrapy.Field()
    panel_kapi = scrapy.Field()
    panjur = scrapy.Field()
    parke = scrapy.Field()
    parke___laminant = scrapy.Field()
    saten_alci = scrapy.Field()
    saten_boya = scrapy.Field()
    sauna = scrapy.Field()
    seramik_zemin = scrapy.Field()
    spot_isik = scrapy.Field()
    somine = scrapy.Field()
    teras = scrapy.Field()
    vestiyer = scrapy.Field()
    yerden_isitma = scrapy.Field()
    parke___lamine = scrapy.Field()
    asansor = scrapy.Field()# DIS OZELLIKLER
    bahceli = scrapy.Field()
    cam_mozaik_kaplama = scrapy.Field()
    fitness = scrapy.Field()
    guvenlik = scrapy.Field()
    hidrofor = scrapy.Field()
    isi_yalitim = scrapy.Field()
    jenerator = scrapy.Field()
    kapici = scrapy.Field()
    otopark___acik = scrapy.Field()
    otopark___kapali = scrapy.Field()
    oyun_parki = scrapy.Field()
    pvc_dograma = scrapy.Field()
    siding = scrapy.Field()
    site_icerisinde = scrapy.Field()
    su_deposu = scrapy.Field()
    tenis_kortu = scrapy.Field()
    yangin_merdiveni = scrapy.Field()
    yuzme_havuzu = scrapy.Field()
    ahsap_dograma = scrapy.Field()
    arka_cephe = scrapy.Field()# KONUM
    caddeye_yakin = scrapy.Field()
    denize_sifir = scrapy.Field()
    denize_yakin = scrapy.Field()
    havaalanina_yakin = scrapy.Field()
    manzara = scrapy.Field()
    manzara___bogaz = scrapy.Field()
    manzara___deniz = scrapy.Field()
    manzara___doga = scrapy.Field()
    manzara___gol = scrapy.Field()
    manzara___sehir = scrapy.Field()
    merkezde = scrapy.Field()
    metroya_yakin = scrapy.Field()
    otobana_yakin = scrapy.Field()
    on_cephe = scrapy.Field()
    toplu_ulasima_yakin = scrapy.Field()
    metrobuse_yakin = scrapy.Field()
    deniz_ulasimina_yakin = scrapy.Field()
    cadde_uzerinde = scrapy.Field()
    tramvaya_yakin = scrapy.Field()
    marmaraya_yakin = scrapy.Field()
    e_5_e_yakin = scrapy.Field()
    tem_e_yakin = scrapy.Field()
    minibus___dolmusa_yakin = scrapy.Field()
    avrasya_tuneli_ne_yakin = scrapy.Field()
    bogaz_koprulerine_yakin = scrapy.Field()

    # *****************
    """
    url = scrapy.Field()
    last_updated = scrapy.Field()
    room = scrapy.Field()
    living_room = scrapy.Field()
    bathroom = scrapy.Field()
    gross_area = scrapy.Field()
    net_area = scrapy.Field()
    heating_system = scrapy.Field()
    building_age = scrapy.Field()
    floor = scrapy.Field()
    number_of_floors_in_the_building = scrapy.Field()
    available_for_loan = scrapy.Field()
    furnished = scrapy.Field()
    fuel_type = scrapy.Field()
    building_type = scrapy.Field()
    building_status = scrapy.Field()
    usage_status = scrapy.Field()
    dues = scrapy.Field()
    with_in_buildings = scrapy.Field()
    north_facade = scrapy.Field()
    south_facade = scrapy.Field()
    east_facade = scrapy.Field()
    western_facade = scrapy.Field()
    title_deed_status = scrapy.Field()
    rental_income = scrapy.Field()
    latitude = scrapy.Field()
    address = scrapy.Field()

    # inside features

    adsl = scrapy.Field()
    woodwork = scrapy.Field()
    alarm = scrapy.Field()
    builtin_kitchen = scrapy.Field()
    balcony = scrapy.Field()
    barbecue = scrapy.Field()
    white_goods = scrapy.Field()
    steel_door = scrapy.Field()
    shower = scrapy.Field()
    wall_paper = scrapy.Field()
    parent_bathroom = scrapy.Field()
    dressing_room = scrapy.Field()
    builtin_wardrobe = scrapy.Field()
    video_intercom = scrapy.Field()
    carpeting = scrapy.Field()
    fitted_kitchen = scrapy.Field()
    vanity_unit = scrapy.Field()
    thermopane = scrapy.Field()
    jacuzzi = scrapy.Field()
    cable_tv_satellite = scrapy.Field()
    covered_balcony = scrapy.Field()
    plasterboard = scrapy.Field()
    air_conditioning = scrapy.Field()
    laminated_kitchen = scrapy.Field()
    marley_flooring = scrapy.Field()
    marble_floor = scrapy.Field()
    kitchen_natural_gas = scrapy.Field()
    panel_door = scrapy.Field()
    blinds = scrapy.Field()
    parquet = scrapy.Field()
    laminated_parquet = scrapy.Field()
    satin_plaster = scrapy.Field()
    sauna = scrapy.Field()
    ceramic_floor = scrapy.Field()
    spotlight = scrapy.Field()
    fireplace = scrapy.Field()
    terrace = scrapy.Field()
    cloakroom = scrapy.Field()
    underfloor_heating = scrapy.Field()
    Parquet_laminate = scrapy.Field()

    # outside features

    elevator = scrapy.Field()
    garden = scrapy.Field()
    glass_mosaic_pavement = scrapy.Field()
    fitness = scrapy.Field()
    security = scrapy.Field()
    booster = scrapy.Field()
    thermal_insulation = scrapy.Field()
    generator = scrapy.Field()
    doorman = scrapy.Field()
    parking_lot = scrapy.Field()
    parking_garage = scrapy.Field()
    playground = scrapy.Field()
    water_tank = scrapy.Field()
    tennis_court = scrapy.Field()
    fire_escape = scrapy.Field()
    swimming_pool = scrapy.Field()
    pvc = scrapy.Field()

    # location features

    rear_facade = scrapy.Field()
    frontage = scrapy.Field()
    on_the_street = scrapy.Field()
    close_to_street = scrapy.Field()
    next_to_sea = scrapy.Field()
    close_to_sea = scrapy.Field()
    view = scrapy.Field()
    bosporus_view = scrapy.Field()
    sea_view = scrapy.Field()
    landscape = scrapy.Field()
    lake_view = scrapy.Field()
    city_view = scrapy.Field()
    in_center = scrapy.Field()
    close_to_public_transportation = scrapy.Field()
    close_to_sea_transportation = scrapy.Field()
    close_to_subway = scrapy.Field()
    close_to_minibus = scrapy.Field()
    close_to_tram = scrapy.Field()
    close_to_marmaray = scrapy.Field()
    close_to_highway = scrapy.Field()
    close_to_e5 = scrapy.Field()
    close_to_tem = scrapy.Field()
    close_to_euraisa_tunnel = scrapy.Field()
    close_to_bosporus_bridges = scrapy.Field()
    """