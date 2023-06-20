#Django Movie Rental Management API

I've developed a Movie Rental Management API that enables the creation of movies and keeps track of which users have rented them.

With this API, users can sign up, log in, and update their details. The API also ensures that administrators have the permission to update and retrieve information of any user within the system.

Authentication is provided by the simplejwt library from Django REST framework, while authorization is handled by custom permissions, utilizing classes inherited from Django REST framework.

Each user can rent multiple movies, and this many-to-many relationship is facilitated by a custom pivot model that includes information about the movie, the user, and the rental order itself.
