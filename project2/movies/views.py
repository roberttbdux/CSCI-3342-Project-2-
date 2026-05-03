from django.shortcuts import render, redirect
from .forms import NewsletterForm
from .models import (
    Slider,
    Advertisement,
    SocialLink,
    Trailer,
    TrailerItem,
    Celebrity,
    News,
    Tweet,
    MovieTheater,
    MovieTV,
)


def home(request):
    sliders = Slider.objects.all()
    social_links = SocialLink.objects.all()

    theater_popular = MovieTheater.objects.filter(type="popular")
    theater_coming_soon = MovieTheater.objects.filter(type="coming soon")

    tv_popular = MovieTV.objects.filter(type="popular")
    tv_coming_soon = MovieTV.objects.filter(type="coming soon")

    sidebar_ad = Advertisement.objects.filter(section="sidebar").first()
    news_ad = Advertisement.objects.filter(section="news").first()

    celebrities = Celebrity.objects.all()

    trailers = Trailer.objects.all()
    trailer_items = TrailerItem.objects.all()

    main_news = News.objects.filter(section="main").first()
    more_news = News.objects.filter(section="more")

    tweets = Tweet.objects.all()

    newsletter_form = NewsletterForm()

    if request.method == "POST":
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            return redirect("home")

    context = {
        "sliders": sliders,
        "social_links": social_links,
        "theater_popular": theater_popular,
        "theater_coming_soon": theater_coming_soon,
        "tv_popular": tv_popular,
        "tv_coming_soon": tv_coming_soon,
        "sidebar_ad": sidebar_ad,
        "news_ad": news_ad,
        "celebrities": celebrities,
        "trailers": trailers,
        "trailer_items": trailer_items,
        "main_news": main_news,
        "more_news": more_news,
        "tweets": tweets,
        "newsletter_form": newsletter_form,
    }

    return render(request, "movies/home.html", context)