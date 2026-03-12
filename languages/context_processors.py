def menu(request):
    menu_items = [
        {'title': 'Главная', 'url_name': 'lang'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Контакты', 'url_name': 'contact'},
    ]
    return {'menu': menu_items}