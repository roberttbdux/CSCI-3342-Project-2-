from django.core.management.base import BaseCommand
from movies.models import (
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


class Command(BaseCommand):
    help = "Seeds the database with initial movie website data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")

        Slider.objects.all().delete()
        Advertisement.objects.all().delete()
        SocialLink.objects.all().delete()
        Trailer.objects.all().delete()
        TrailerItem.objects.all().delete()
        Celebrity.objects.all().delete()
        News.objects.all().delete()
        Tweet.objects.all().delete()
        MovieTheater.objects.all().delete()
        MovieTV.objects.all().delete()

        self.stdout.write("Creating social links...")

        SocialLink.objects.create(
            name="Facebook",
            anchor_class="fb",
            icon_class="ion-social-facebook",
            url="#",
        )
        SocialLink.objects.create(
            name="Twitter",
            anchor_class="tw",
            icon_class="ion-social-twitter",
            url="#",
        )
        SocialLink.objects.create(
            name="Google Plus",
            anchor_class="gp",
            icon_class="ion-social-googleplus",
            url="#",
        )
        SocialLink.objects.create(
            name="YouTube",
            anchor_class="yt",
            icon_class="ion-social-youtube",
            url="#",
        )

        self.stdout.write("Creating slider records...")

        slider_data = [
            ("slider1.jpg", "Sci-fi", "Interstellar", "7.4", "10", "blue"),
            ("slider2.jpg", "Action", "The Revenant", "7.4", "10", "yell"),
            ("slider3.jpg", "Comedy", "Die Hard", "7.4", "10", "green"),
            ("slider4.jpg", "Adventure", "The Walk", "7.4", "10", "orange"),
        ]

        for image, genre, title, lower, upper, genre_class in slider_data:
            Slider.objects.create(
                image_src=image,
                image_width=285,
                image_height=437,
                anchor_url="#",
                movie_genre=genre,
                movie_title=title,
                lower_rating=lower,
                upper_rating=upper,
            )

        self.stdout.write("Creating advertisements...")

        Advertisement.objects.create(
            section="sidebar",
            img_src="ads1.png",
            img_width=336,
            img_height=296,
        )
        Advertisement.objects.create(
            section="news",
            img_src="ads2.png",
            img_width=728,
            img_height=106,
        )

        self.stdout.write("Creating celebrity records...")

        celebrity_data = [
            ("ava1.jpg", "Samuel N. Jack", "Actor"),
            ("ava2.jpg", "Benjamin Carroll", "Actor"),
            ("ava3.jpg", "Beverly Griffin", "Actor"),
            ("ava4.jpg", "Justin Weaver", "Actor"),
        ]

        for image, name, celebrity_type in celebrity_data:
            Celebrity.objects.create(
                anchor_url="#",
                img_width=70,
                img_height=70,
                celebrity_url="#",
                celebrity_name=name,
                celebrity_type=celebrity_type,
            )

        self.stdout.write("Creating movie theater records...")

        theater_movies = [
            ("popular", "mv-item1.jpg", "Interstellar", "Sci-fi", "7.4", "10"),
            ("popular", "mv-item2.jpg", "The Revenant", "Action", "7.4", "10"),
            ("popular", "mv-item3.jpg", "Die Hard", "Comedy", "7.4", "10"),
            ("popular", "mv-item4.jpg", "The Walk", "Adventure", "7.4", "10"),
            ("coming soon", "mv-item5.jpg", "Interstellar", "Sci-fi", "7.4", "10"),
            ("coming soon", "mv-item6.jpg", "The Revenant", "Action", "7.4", "10"),
            ("coming soon", "mv-item7.jpg", "Die Hard", "Comedy", "7.4", "10"),
            ("coming soon", "mv-item8.jpg", "The Walk", "Adventure", "7.4", "10"),
        ]

        for movie_type, image, title, genre, lower, upper in theater_movies:
            MovieTheater.objects.create(
                type=movie_type,
                img_src=image,
                img_width=185,
                img_height=284,
                anchor_url="moviesingle.html",
                movie_genre=genre,
                movie_title=title,
                lower_rating=lower,
                upper_rating=upper,
            )

        self.stdout.write("Creating movie TV records...")

        tv_movies = [
            ("popular", "mv-item1.jpg", "Interstellar", "Sci-fi", "7.4", "10"),
            ("popular", "mv-item2.jpg", "The Revenant", "Action", "7.4", "10"),
            ("popular", "mv-item3.jpg", "Die Hard", "Comedy", "7.4", "10"),
            ("popular", "mv-item4.jpg", "The Walk", "Adventure", "7.4", "10"),
            ("coming soon", "mv-item5.jpg", "Interstellar", "Sci-fi", "7.4", "10"),
            ("coming soon", "mv-item6.jpg", "The Revenant", "Action", "7.4", "10"),
            ("coming soon", "mv-item7.jpg", "Die Hard", "Comedy", "7.4", "10"),
            ("coming soon", "mv-item8.jpg", "The Walk", "Adventure", "7.4", "10"),
        ]

        for movie_type, image, title, genre, lower, upper in tv_movies:
            MovieTV.objects.create(
                type=movie_type,
                img_src=image,
                img_width=185,
                img_height=284,
                anchor_url="moviesingle.html",
                movie_genre=genre,
                movie_title=title,
                lower_rating=lower,
                upper_rating=upper,
            )

        self.stdout.write("Creating trailer records...")

        Trailer.objects.create(
            trailer_URL="https://www.youtube.com/embed/1Q8fG0TtVAY"
        )

        trailer_items = [
            ("trailer7.jpg", "photo by Barn Images", 4096, 2737, "Wonder Woman", "2:30"),
            ("trailer2.jpg", "photo by Barn Images", 350, 200, "Oblivion: Official Teaser Trailer", "2:37"),
            ("trailer6.jpg", "photo by Joshua Earle", 350, 200, "Exclusive Interview: Skull Island", "2:44"),
            ("trailer3.png", "photo by Alexander Dimitrov", 100, 56, "Logan: Director James Mangold Interview", "2:43"),
            ("trailer4.png", "photo by Wojciech Szaturski", 100, 56, "Beauty and the Beast: Official Teaser Trailer 2", "2:32"),
            ("trailer5.jpg", "photo by Wojciech Szaturski", 360, 189, "Fast&Furious 8", "3:11"),
        ]

        for image, alt, width, height, description, duration in trailer_items:
            TrailerItem.objects.create(
                img_src=image,
                img_alt=alt,
                img_width=width,
                img_height=height,
                description=description,
                duration=duration,
            )

        self.stdout.write("Creating news records...")

        News.objects.create(
            section="main",
            img_src="blog-it1.jpg",
            img_alt="Brie Larson",
            img_width=170,
            img_height=250,
            title="Brie Larson to play first female white house candidate Victoria Woodull in Amazon film",
            content="Exclusive: Amazon Studios has acquired Victoria Woodhull, with Oscar winning Room star Brie Larson poised to produce and play the first female candidate for the presidency of the United States.",
            time="13 hours ago",
        )

        more_news = [
            "Michael Shannon Frontrunner to play Cable in Deadpool 2",
            "French cannibal horror Raw inspires L.A. theater to hand out Barf Bags",
            "Laura Dern in talks to join Justin Kelly’s biopic JT Leroy",
            "China punishes more than 300 cinemas for box office cheating",
        ]

        for title in more_news:
            News.objects.create(
                section="more",
                img_src="blog-it1.jpg",
                img_alt="Movie news",
                img_width=170,
                img_height=250,
                title=title,
                content="More movie news content.",
                time="13 hours ago",
            )

        self.stdout.write("Creating tweet records...")

        Tweet.objects.create(
            content="Just watched Interstellar again 🚀🌌—still blown away by the visuals, the emotion, and that mind-bending journey through space and time. A true masterpiece that never gets old. ⭐️ #MovieNight #SciFi"
        )
        Tweet.objects.create(
            content="The latest movie trailers are looking amazing this week. Which one are you most excited to watch?"
        )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))