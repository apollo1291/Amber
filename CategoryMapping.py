#constant
AMAZON_TO_API_CATEGORY = {
    'Sports & Outdoors': "Sporting and athletic goods",
    'Clothing, Shoes & Jewelry': "Clothing",
    'Home & Kitchen': "Home cooking appliances",
    'Baby Products': "Consumer goods and general rental centers",
    'Pet Supplies': "All other retail",
    'Arts, Crafts & Sewing': "Independent artists/writers and performers",
    'Electronics': "other miscellaneous electrical equipment and components",
    'Video Games': "Computer software and games",
    'Patio, Lawn & Garden': "Building material and garden equipment and supplies dealers",
    'Tools & Home Improvement': "Power tools",
    'Office Products': "Office supplies (not paper)",
    'Grocery & Gourmet Food': "Grocery and related product wholesalers",
    'Remote & App Controlled Vehicle Parts': "Sale/maintenance/repair/parts/accessories of motor vehicles/motorcycles",
    'Health & Household': "Health and personal care stores",
    'Industrial & Scientific': "Other commercial and service industry machinery",
    'Beauty & Personal Care': "Health and personal care stores",
    'Hobbies': "General merchandise stores",
    'Remote & App Controlled Vehicles & Parts': "Sale/maintenance/repair/parts/accessories of motor vehicles/motorcycles",
    'Automotive': "Automobiles",
    'Musical Instruments': "Gaskets/seals/musical instruments/fasteners/brooms/brushes/mop and other misc. goods",
    'Movies & TV': "Radio and television",
    'Cell Phones & Accessories': "Telephones",
    'Toys & Games': "Dolls/toys and games",
    'Appliances': "Small electrical appliances",
    'Books': "Books",
    'Mobility & Daily Living Aids': "All other retail",
    'Power & Hand Tools': "Power tools",
    'Medical Supplies & Equipment':  "Medical/precision and optical instruments/watches and clocks",
    'Kitchen & Dining': "Domestic appliances and disposables",
    'Motorcycle & Powersports': "Motorcycle/bicycle and parts",
    'CDs & Vinyl': "External hard drives/CDs/other storage media",
    'Small Appliance Parts & Accessories': "Small electrical appliances",
    'Office Electronics': "Office machinery and computers",
    'Instrument Accessories': "Gaskets/seals/musical instruments/fasteners/brooms/brushes/mop and other misc. goods"

}

API_CATEGORY_TO_ACTIVITY_ID = {
    "Sporting and athletic goods": "consumer_goods-type_sporting_athletic_goods",

    "Clothing": "consumer_goods-type_clothing",
    
    "Home cooking appliances": "electrical_equipment-type_home_cooking_appliances",

    "Consumer goods and general rental centers": "consumer_goods_rental-type_consumer_goods_general_rental_centers",
    
    "other miscellaneous electrical equipment and components": "electrical_equipment-type_other_miscellaneous_electrical_equipment_components",

    "Computer software and games": "consumer_goods-type_software",

    "Independent artists/writers and performers": "consumer_goods-type_independent_artists_writers_performers",

    "Health and personal care stores": "health_care-type_health_personal_care_stores",

    "Building material and garden equipment and supplies dealers": "equipment_gardening_diy-type_building_material_garden_equipment_supplies_dealers",

    "Power tools": "machinery-type_power_tools",

    "Office supplies (not paper)": "office_equipment-type_office_supplies_not_paper",

    "Grocery and related product wholesalers": "wholesale_trade-type_grocery_related_product_wholesalers",

    "Other commercial and service industry machinery": "machinery-type_other_commercial_service_industry_machinery",

    "Sale/maintenance/repair/parts/accessories of motor vehicles/motorcycles": "vehicle_manufacture-type_sale_maintenance_repair_parts_accessories_motor_vehicles_motorcycles",

    "General merchandise stores": "general_retail-type_general_merchandise_stores",

    "Automobiles": "passenger_vehicle-vehicle_type_automobiles-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",

    "Gaskets/seals/musical instruments/fasteners/brooms/brushes/mop and other misc. goods": "consumer_goods-type_gaskets_seals_musical_instruments_fasteners_brooms_brushes_mop_other_misc._goods",

    "Radio and television": "consumer_goods-type_radio_television",

    "Telephones": "electronics-type_telephones",

    "Dolls/toys and games": "consumer_goods-type_dolls_toys_games",

    "Small electrical appliances": "electrical_equipment-type_small_electrical_appliances",

    "Books": "consumer_goods-type_books",

    "All other retail": "general_retail-type_all_other_retail",

    "Medical/precision and optical instruments/watches and clocks": "electrical_equipment-type_medical_precision_optical_instruments_watches_clocks",

    "External hard drives/CDs/other storage media": "electronics-type_external_hard_drives_cds_other_storage_media",

    "Motorcycle/bicycle and parts": "passenger_vehicle-vehicle_type_motorcycle_bicycle_parts-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",

    "Office machinery and computers": "office_equipment-type_office_machinery_computers"





}

print(list(AMAZON_TO_API_CATEGORY.keys()))

