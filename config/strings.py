home_url = "http://mediamarkt.pl"

driver_name = 'chrome'
window_width = 1920
window_height = 1080
timeout = 5

registration_url = "http://mediamarkt.pl/registration"
registration_data = {"first_name": "Janusz",
                      "last_name": "Autoamtyczny",
                      "email": "projektautomatyzacjitestowgr1@gmail.com",
                      "password": "321ewq#@!",
                      "phone": "501237742",
                      "zipcode": "54-438",
                      }

registration_data_invalid_firstname = ["a",
                                        "123",
                                        ]
registration_data_invalid_lastname = ["a",
                                       "123",
                                       ]
registration_data_invalid_email = ["a",
                                   "123",
                                   "mail_bez_malpy.com",
                                   "mail@bez_kropki_com",
                                   ]
registration_data_invalid_password = ["1234",
                                      ]
registration_data_invalid_phone = ["aaa",
                                   ]
registration_data_invalid_zipcode =["aa-bbb",
                                    ]

login_url = "https://mediamarkt.pl/login"
login_data = {"email": "projektautomatyzacjitestowgr1@gmail.com",
              "password": "321ewq#@!",
              "email1": "Kiedys.sie.uda@gmail.com",
              "email2": "@asdaad.com@",
              "password1": "AlboiNie",
              "password2": "a",
              }

search_data = {"a": "Monitor",
               "b": "123456789",
               "c": "java",
               "d": "!@#$%",
               }

resetting_url = "https://mediamarkt.pl/resetting"

resetting_data = {"email": "projektautomatyzacjitestowgr1@gmail.com",
                  "email2": "projektautomatyzacjitestowgr1gmail.com"
              }

changing_password_url = "https://mediamarkt.pl/reset/SHK7-jmFJ-51xEb1YS3Smry-KuzE95HkSBb-PmSxoHw"

changing_password_data = {"password": "1qwerty!@#",
                          "wrong_password": "1qwerty!@#$"
              }

bucket_product_url = "https://mediamarkt.pl/rtv-i-telewizory/telewizor-samsung-ue65ru7452u"

bucket_data = {"post_code": "55081",
               "post_code_wrong": "00-000"
              }

save_box_url = "https://mediamarkt.pl/agd-male/odkurzacz-workowy-electrolux-epf61rr"

address_list_url = "https://mediamarkt.pl/profile/address/list"

address_data = {"address_name": "Adres zapisany podczas testow",
                "email": "projektautomatyzacjitestowgr1@gmail.com",
                "first_name": "Janusz",
                "last_name": "Autoamtyczny",
                "street": "ulicaProjektowa",
                "street_number": "69",
                "zipcode": "54-438",
                "city": "Miasto",
                      }

address_data_invalid_street = ["a",
                                ]

address_data_invalid_street_number = []

address_data_invalid_email = ["a",
                                   "123",
                                   "mail_bez_malpy.com",
                                   "mail@bez_kropki_com",
                                   ]
address_data_invalid_zipcode =["aa-bbb",
                      ]

product_url = "https://mediamarkt.pl/agd-male/odkurzacz-workowy-electrolux-epf61rr"

product_availability_cities_list = ["Wrocław",
                                   "Wroclaw",
                                   "",
                                   "@$$%@",
                                   ]


discount_url = "https://mediamarkt.pl/koszyk/lista"
discount_data = {"a": "6998C4",
                 "b": "6998C5",
                 }