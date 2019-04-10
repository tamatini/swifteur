from django.shortcuts import render

posts = [
    {
        'author': 'Tamatini',
        'title': 'Post 1',
        'content': 'Haec igitur Epicuri non probo, inquam. De cetero vellem equidem aut ipse doctrinis fuisset '
                   'instructior est enim, quod tibi ita videri necesse est, non satis politus iis artibus, '
                   'quas qui tenent, eruditi appellantur aut ne deterruisset alios a studiis. '
                   'quamquam te quidem video minime esse deterritum.',
        'date_posted':'lundi 8 avril'
    },
    {
        'author': 'Tamatini',
        'title': 'Post 2',
        'content': 'Haec igitur Epicuri non probo, inquam. De cetero vellem equidem aut ipse doctrinis fuisset '
                   'instructior est enim, quod tibi ita videri necesse est, non satis politus iis artibus, '
                   'quas qui tenent, eruditi appellantur aut ne deterruisset alios a studiis. '
                   'quamquam te quidem video minime esse deterritum.',
        'date_posted':'lundi 8 avril'
    }
]

articles = [
    {
        'content': 'Ut enim quisque sibi plurimum confidit et ut quisque maxime virtute et sapientia sic munitus est, '
                   'ut nullo egeat suaque omnia in se ipso posita iudicet, ita in amicitiis expetendis colendisque '
                   'maxime excellit. Quid enim? Africanus indigens mei? Minime hercule! ac ne ego quidem illius; sed '
                   'ego admiratione quadam virtutis eius, ille vicissim opinione fortasse non nulla, quam de meis '
                   'moribus habebat, me dilexit; auxit benevolentiam consuetudo. Sed quamquam utilitates multae et '
                   'magnae consecutae sunt, non sunt tamen ab earum spe causae diligendi profectae.'
    }
]


def blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def article(request):
    context = {
        'articles': articles
    }
    return render(request, 'article.html', context)
