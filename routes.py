"""
Routes and views for the bottle application.
"""

from bottle import route, view


@route('/')
@route('/home')
@view('Start')
def home():
    """Renders the home page."""
    return dict(
        title1='Данный сайт подготовлен для выполнения задания по учебной практике.',
        title2='Сайт предназначен для построения и нахождения кратчайших путей с помощью различных алгоритмов. Таких как алгоритм: Дейкстры, Флойда, Прима',
         title_enter = 'Ввод',
        title_main='Алгоритмы для нахождения кратчайшего пути.',
        title_size = 'Выберите размерность матрицы',
        text_main='Для нахождения кратчайшего пути в графах существуют различные алгоритмы.'+'\n'+ 
        ' Здесь представлены три алгоритма нахождения кратчайшего пути.',
        
        btn_text='Старт'
    )
@route('/Main')
@view('Main')



def home():
    """Renders the home page."""
    return dict(
        title_enter = 'Ввод',
        title_main='Алгоритмы для нахождения кратчайшего пути.',
        title_size = 'Выберите размерность матрицы',
        text_main='Для нахождения кратчайшего пути в графах существуют различные алгоритмы.'+'\n'+ 
        ' Здесь представлены три алгоритма нахождения кратчайшего пути.',
        title='Выберите алгоритм:',
        title1='Алгоритм Прима',
        title2='Алгоритм Дейкстра',
        title3='Алгоритм Флойда',
        text1='Алгоритм Прима - это алгоритм минимального остовного дерева, что принимает граф в качестве входных данных и находит подмножество ребер этого графа, который формирует дерево, включающее в себя каждую вершину, а также имеет минимальную сумму весов среди всех деревьев, которые могут быть сформированы из графа.',
        text2='Алгоритм Дейкстры позволяет найти кратчайший путь между двумя любыми вершинами графа (или кратчайший путь сети между заданным исходным и любым другим узлом). Граф — это совокупность двух множеств: точек (называются вершинами) и путей между ними (изображаются линиями и называются рёбрами).',
        text3='Алгоритм Флойда - Уоршелла — динамический алгоритм для нахождения кратчайших расстояний между всеми вершинами взвешенного ориентированного графа.',
        btn_text='Решить'
    )

@route('/Prima')
@view('Prima')
def contact():
    """Renders the contact page."""
    return dict(
        title='Алгоритм Прима',
         title_enter = 'Ввод',
        title_main='Алгоритмы для нахождения кратчайшего пути.',
        title_size = 'Выберите размерность матрицы',
        text_main='Для нахождения кратчайшего пути в графах существуют различные алгоритмы.'+'\n'+ 
        ' Здесь представлены три алгоритма нахождения кратчайшего пути.',

    )

@route('/Dextra')
@view('Dextra')
def about():
    """Renders the about page."""
    return dict(
        title='Алгоритм Дейкстра',
        title_mat1 = 'Матрица №1',
        title_mat2 = 'Матрица №2',
        btn_text='Ввод',
         title_enter = 'Ввод',
        title_main='Алгоритмы для нахождения кратчайшего пути.',
        title_size = 'Выберите размерность матрицы',
        text_main='Для нахождения кратчайшего пути в графах существуют различные алгоритмы.'+'\n'+ 
        ' Здесь представлены три алгоритма нахождения кратчайшего пути.',

    )
@route('/Floid')
@view('Floid')
def about():
    """Renders the about page."""
    return dict(
        title='Алгоритм Флойда',
        title_mat1 = 'Матрица №1',
        title_mat2 = 'Матрица №2',
        title_mat3 = 'Матрица №3',
         title_enter = 'Ввод',
        title_main='Алгоритмы для нахождения кратчайшего пути.',
        title_size = 'Выберите размерность матрицы',
        text_main='Для нахождения кратчайшего пути в графах существуют различные алгоритмы.'+'\n'+ 
        ' Здесь представлены три алгоритма нахождения кратчайшего пути.',

    )
